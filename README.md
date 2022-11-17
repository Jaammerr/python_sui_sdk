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


class Example(Client):
    def __init__(self, faucet_url: str, rpc_url: str, mnemonic: str = True):  # mnemonic can be False
        super().__init__(faucet_url, rpc_url, mnemonic)
        self.wallet = Wallet(faucet_url, rpc_url, mnemonic)
        self.rpc = RpcDetails(faucet_url, rpc_url, mnemonic)

    def example_wallet(self):
        # get balance
        balance = self.wallet.get_balance()

        # generate wallet (return NamedTuple with mnemonic, private key, public key and address)
        wallet_data = self.wallet.generate_wallet()

        # get my wallet info (return NamedTuple with mnemonic, private key, public key and address)
        my_wallet_info = self.wallet.get_wallet_info()

        # get another wallet info (return NamedTuple with mnemonic, private key, public key and address)
        another_wallet_info = self.wallet.get_another_wallet_info(self, WalletInfoParams(params))
        
        # request test tokens from faucet
        response_data = self.wallet.request_tokens_from_faucet()
        
        # get public key as b64 string
        public_b64_key = self.wallet.get_public_key_as_b64_string()
        
        
    def example_client(self):
        # get example NFT
        response_data = self.mint_example_nft()
        
        # move call
        response_data = self.move_call(self, MoveCallParams(params))
        
        # transfer object
        response_data = self.transfer_object(self, TransferObjectParams(params))
        
        '''ANOTHER FUNCTION USING SAME'''
        
    
    def example_rpc(self):
        # get transaction ID (digest)
        transaction_id = self.rpc.get_transaction_id(self, GetTransactionsIDParams(params))
        
        # get move function arg types
        data = self.rpc.get_move_function_arg_types(self, MoveFunctionArgTypesParams(params))

        '''ANOTHER FUNCTION USING SAME'''
```

>GOOD LUCK :D

