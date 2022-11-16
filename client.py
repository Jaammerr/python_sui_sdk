import base64
import uuid
import bip_utils
import hashlib
import nacl
import requests
import pyuseragents

from typing import Optional
from mnemonic import Mnemonic
from .models import SignatureScheme, TransferSuiParams, TransferObjectParams, MoveCallParams, ExecuteType, \
    BatchTransactionParams, DryRunTransactionParams, MergeCoinsParams, PayParams, PayAllParams, PublishParams, \
    SplitCoinParams, SplitCoinEqualParams


mnemo = Mnemonic("english")


class Client:
    def __init__(self, faucet_url: str, rpc_url: str, mnemonic: str = True,
                 derivation_path="m/44'/784'/0'/0'/0'"):

        self.faucet_url = faucet_url
        self.rpc_url = rpc_url
        self.derivation_path = derivation_path

        self.session = requests.Session()
        self.headers = {
            'authority': 'fullnode.testnet.sui.io',
            'accept': '*/*',
            'accept-language': 'uk,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'origin': 'chrome-extension://opcgpfmipidbgpenhmajoajpbobppdil',
            'user-agent': pyuseragents.random(),
        }

        if mnemonic:

            self.mnemonic = mnemonic

            self.bip39_seed = bip_utils.Bip39SeedGenerator(self.mnemonic).Generate()
            self.bip32_ctx = bip_utils.Bip32Slip10Ed25519.FromSeed(self.bip39_seed)
            self.bip32_der_ctx = self.bip32_ctx.DerivePath(derivation_path)

            self.private_key: bytes = self.bip32_der_ctx.PrivateKey().Raw().ToBytes()
            self.public_key: bytes = self.bip32_der_ctx.PublicKey().RawCompressed().ToBytes()


    def get_address(self) -> Optional[str]:
        return "0x" + hashlib.sha3_256(self.bip32_der_ctx.PublicKey().RawCompressed().ToBytes()).digest().hex()[:40]

    def get_public_key_as_b64_string(self) -> Optional[str]:
        return base64.b64encode(self.public_key[1:]).decode()


    def batch_transaction(self, tx: BatchTransactionParams):
        return self.send_request_to_rpc(
            method="sui_batchTransaction",
            params=[
                self.get_address(),
                tx.single_transaction_params,
                tx.gas_budget,
                tx.gas,
                tx.gas_budget
            ])


    def dryrun_transaction(self, tx: DryRunTransactionParams):
        return self.send_request_to_rpc(
            method='sui_dryRunTransaction',
            params=[
                tx.tx_bytes
            ]
        )


    def mint_example_nft(self) -> Optional[dict]:
        response = self.send_request_to_rpc(
            method='sui_moveCall',
            params=[
                self.get_address()[2:],
                '0x2',
                'devnet_nft',
                'mint',
                [],
                ["Example NFT", "An NFT created by Sui Wallet",
                 "ipfs://QmZPWWy5Si54R3d26toaqRiqvCH7HkGdXkxwUgCm2oKKM2?filename=img-sq-01.png"],
                None,
                10000,
            ])

        tx_bytes = base64.b64decode(str(response['result']['txBytes']))
        return self.sign_and_execute_transaction(tx_bytes)

    def mint_wizard_nft(self) -> Optional[dict]:
        response = self.send_request_to_rpc(
            method='sui_moveCall',
            params=[
                self.get_address()[2:],
                '0x2',
                'devnet_nft',
                'mint',
                [],
                ["Wizard Land", "Expanding The Magic Land",
                 "https://gateway.pinata.cloud/ipfs/QmYfw8RbtdjPAF3LrC6S3wGVwWgn6QKq4LGS4HFS55adU2?w=800&h=450&c=crop"],
                None,
                10000,
            ])

        tx_bytes = base64.b64decode(str(response['result']['txBytes']))
        return self.sign_and_execute_transaction(tx_bytes)


    def move_call(self, tx: MoveCallParams):
        return self.send_request_to_rpc(
            method="sui_moveCall",
            params=[
                self.get_address(),
                tx.package_object_id,
                tx.module,
                tx.function,
                tx.type_arguments,
                tx.arguments,
                tx.gas_payment,
                tx.gas_budget,
            ])


    def transfer_object(self, tx: TransferObjectParams):
        return self.send_request_to_rpc(
            method="sui_transferObject",
            params=[
                self.get_address(),
                tx.object_id,
                tx.gas_payment,
                tx.gas_budget,
                tx.recipient
            ])


    def transfer_sui(self, tx: TransferSuiParams):
        return self.send_request_to_rpc(
            method="sui_transferObject",
            params=[
                self.get_address(),
                tx.sui_object_id,
                tx.gas_budget,
                tx.recipient,
                tx.amount
            ])


    def merge_coins(self, tx: MergeCoinsParams):
        return self.send_request_to_rpc(
            method='sui_mergeCoins',
            params=[
                self.get_address(),
                tx.primary_coin,
                tx.coin_to_merge,
                tx.gas,
                tx.gas_budget
            ]
        )

    def pay_sui(self, tx: PayParams):
        return self.send_request_to_rpc(
            method='sui_pay',
            params=[
                self.get_address(),
                tx.input_coins,
                tx.recipients,
                tx.amounts,
                tx.gas,
                tx.gas_budget
            ]
        )


    def pay_all_sui(self, tx: PayAllParams):
        return self.send_request_to_rpc(
            method='sui_payAllSui',
            params=[
                self.get_address(),
                tx.input_coins,
                tx.recipient,
                tx.gas_budget
            ]
        )

    def publish(self, tx: PublishParams):
        return self.send_request_to_rpc(
            method='sui_publish',
            params=[
                self.get_address(),
                tx.compiled_modules,
                tx.gas,
                tx.gas_budget
            ]
        )

    def split_coin(self, tx: SplitCoinParams):
        return self.send_request_to_rpc(
            method='sui_splitCoin',
            params=[
                self.get_address(),
                tx.coin_object_id,
                tx.split_amounts,
                tx.gas,
                tx.gas_budget
            ]
        )

    def split_coin_equal(self, tx: SplitCoinEqualParams):
        return self.send_request_to_rpc(
            method='sui_splitCoinEqual',
            params=[
                self.get_address(),
                tx.coin_object_id,
                tx.split_count,
                tx.gas,
                tx.gas_budget
            ]
        )


    def sign_data(self, data: bytes) -> Optional[bytes]:
        return nacl.signing.SigningKey(self.private_key).sign(data)[:64]


    def sign_and_execute_transaction(self, tx_bytes: bytes) -> Optional[dict]:
        signature_bytes = self.sign_data(tx_bytes)

        x_bytes_b64_encoded = base64.b64encode(tx_bytes).decode()
        signature_b64_encoded = base64.b64encode(signature_bytes).decode()
        pubkey_b64_encoded = self.get_public_key_as_b64_string()
        signature_scheme = SignatureScheme.ED25519
        execute_type = ExecuteType.WaitForLocalExecution

        return self.send_request_to_rpc(method='sui_executeTransaction', params=[
            x_bytes_b64_encoded,
            signature_scheme,
            signature_b64_encoded,
            pubkey_b64_encoded,
            execute_type
        ])


    def send_request_to_rpc(
            self,
            method: str,
            params: list = None,
            request_id: str = None
    ) -> Optional[dict]:

        response = requests.post(
            self.rpc_url, json={
                "jsonrpc": "2.0",
                "method": method,
                "params": params or [],
                "id": request_id or str(uuid.uuid4()),
            })

        if response.status_code <= 201:
            return response.json()
        else:
            raise Exception(
                f'Failed to send transaction | Response status: {response.status_code} | Details: {response.text}')
