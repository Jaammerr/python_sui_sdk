import base64
import hashlib
import bip_utils

from typing import Optional
from .client import Client
from .errors import SuiError
from .models import WalletInfo, WalletInfoParams


class Wallet(Client):

    def generate_wallet(self) -> WalletInfo:
        mnemonic = bip_utils.Bip39MnemonicGenerator().FromWordsNumber(bip_utils.Bip39WordsNum.WORDS_NUM_12).ToStr()

        bip39_seed = bip_utils.Bip39SeedGenerator(mnemonic).Generate()
        bip32_ctx = bip_utils.Bip32Slip10Ed25519.FromSeed(bip39_seed)
        bip32_der_ctx = bip32_ctx.DerivePath(self.derivation_path)

        private_key: bytes = bip32_der_ctx.PrivateKey().Raw().ToBytes()
        public_key: bytes = bip32_der_ctx.PublicKey().RawCompressed().ToBytes()
        address: str = "0x" + hashlib.sha3_256(bip32_der_ctx.PublicKey().RawCompressed().ToBytes()).digest().hex()[:40]

        return WalletInfo(mnemonic, private_key, public_key, address)


    def get_wallet_info(self) -> WalletInfo:
        return WalletInfo(self.mnemonic, self.private_key, self.public_key, self.get_address())


    def get_another_wallet_info(self, tx: WalletInfoParams) -> WalletInfo:
        bip39_seed = bip_utils.Bip39SeedGenerator(tx.mnemonic).Generate()
        bip32_ctx = bip_utils.Bip32Slip10Ed25519.FromSeed(bip39_seed)
        bip32_der_ctx = bip32_ctx.DerivePath(self.derivation_path)

        private_key: bytes = bip32_der_ctx.PrivateKey().Raw().ToBytes()
        public_key: bytes = bip32_der_ctx.PublicKey().RawCompressed().ToBytes()
        address: str = "0x" + hashlib.sha3_256(bip32_der_ctx.PublicKey().RawCompressed().ToBytes()).digest().hex()[:40]

        return WalletInfo(tx.mnemonic, private_key, public_key, address)



    def get_address(self) -> Optional[str]:
        return "0x" + hashlib.sha3_256(self.bip32_der_ctx.PublicKey().RawCompressed().ToBytes()).digest().hex()[:40]


    def get_balance(self, balance=0) -> Optional[float]:

        response = self.send_request_to_rpc(
            method='sui_getObjectsOwnedByAddress',
            params=[
                self.get_address()
            ])

        for el in response['result']:
            object_id = el['objectId']

            object_data = self.send_request_to_rpc(
                method='sui_getObject',
                params=[
                    str(object_id)
                ])

            try:
                balance += int(object_data['result']['details']['data']['fields']['balance'])
            except KeyError:
                continue

        else:
            return balance / 1000000000


    def request_tokens_from_faucet(self) -> Optional[dict]:
        response = self.session.post(
            self.faucet_url,
            json={
                "FixedAmountRequest": {"recipient": self.get_address()}
            })

        if response.status_code <= 201:
            return response.json()
        else:
            raise Exception(f'Failed to get tokens | Response status: {response.status_code} | Details: {response.text}')


    def get_public_key_as_b64_string(self) -> Optional[str]:
        return base64.b64encode(self.public_key[1:]).decode()

