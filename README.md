# Python SDK for SUI

This SDK is in alpha version, so there are possible errors.
All functions can be viewed here: https://docs.sui.io/sui-jsonrpc

## Author's additions:

- Function to get the balance
- Function for mint a NFT (example/wizard)
- Function to generate a random wallet
- Function to request test tokens from a faucet
- Function to get public key as b64 string
- Function to get transaction ID

## Installation

Requires `Python 3.10-3.11`

```
pip install pysdk-sui
```



## Example usage
```
from pysdk_sui import Client, Wallet, RpcDetails, WalletInfoParams, MoveCallParams, TransferObjectParams, GetTransactionsIDParams, MoveFunctionArgTypesParams

faucet_url_ = 'https://faucet.testnet.sui.io/gas'
rpc_url_ = 'https://fullnode.testnet.sui.io/'
test_mnemonic = 'trip offer end cloth patrol core pioneer debate cigar swarm patch tattoo'


client = Client(rpc_url=rpc_url_, faucet_url=faucet_url_, mnemonic=test_mnemonic)
wallet = Wallet(rpc_url=rpc_url_, faucet_url=faucet_url_, mnemonic=test_mnemonic)
rpc = RpcDetails(rpc_url=rpc_url_, faucet_url=faucet_url_, mnemonic=test_mnemonic)


def example_wallet():
    # get balance
    balance = wallet.get_balance()

    # generate wallet (return NamedTuple with mnemonic, private key, public key and address)
    wallet_data = wallet.generate_wallet()

    # get my wallet info (return NamedTuple with mnemonic, private key, public key and address)
    my_wallet_info = wallet.get_wallet_info()

    # get another wallet info (return NamedTuple with mnemonic, private key, public key and address)
    another_wallet_info = wallet.get_another_wallet_info(
        WalletInfoParams(
            'params'
        ))

    # request test tokens from faucet
    response_data = wallet.request_tokens_from_faucet()

    # get public key as b64 string
    public_b64_key = wallet.get_public_key_as_b64_string()

    '''ANOTHER FUNCTION USING SAME'''


def example_client():
    # get example NFT
    response_data = client.mint_example_nft()

    # move call
    response_data = client.move_call(
        MoveCallParams(
            'params'
    ))

    # transfer object
    response_data = client.transfer_object(
        TransferObjectParams(
            'params'
        ))

    '''ANOTHER FUNCTION USING SAME'''


def example_rpc():
    # get transaction ID (digest)
    transaction_id = rpc.get_transaction_id(
        GetTransactionsIDParams(
            params
        ))

    # get move function arg types
    data = rpc.get_move_function_arg_types(
        MoveFunctionArgTypesParams(
            params
        ))

    '''ANOTHER FUNCTION USING SAME'''


```

>GOOD LUCK :D

