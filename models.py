from typing import Optional, Union, Any, List, NamedTuple


class SignatureScheme:
    ED25519 = 'ED25519'
    Secp256k1 = 'Secp256k1'


class ExecuteType:
    ImmediateReturn = "ImmediateReturn"
    WaitForTxCert = "WaitForTxCert"
    WaitForEffectsCert = "WaitForEffectsCert"
    WaitForLocalExecution = "WaitForLocalExecution"


class WalletInfo(NamedTuple):
    mnemonic: str
    private_key: bytes
    public_key: bytes
    address: str


class WalletInfoParams:
    def __init__(
            self,
            mnemonic: str
    ):
        self.mnemonic = mnemonic


class GetPublicKeyAsb64StringParams:
    def __init__(
            self,
            public_key: bytes
    ):
        self.public_key = public_key


class DryRunTransactionParams:
    def __init__(
            self,
            tx_bytes: str
    ):
        self.tx_bytes = tx_bytes



class GetTransactionsIDParams:
    def __init__(
            self,
            response: dict
    ):
        self.response = response


class GetObjectsOwnedByAddressParams:
    def __init__(
            self,
            address: str
    ):
        self.address = address


class GetObjectsOwnedByObjectParams:
    def __init__(
            self,
            object_id: str
    ):
        self.object_id = object_id


class GetNormalizedMoveFunctionParams:
    def __init__(
            self,
            package: str,
            module_name: str,
            function_name: str
    ):
        self.package = package
        self.module_name = module_name
        self.function_name = function_name


class GetNormalizedMoveModuleParams:
    def __init__(
            self,
            package: str,
            module_name: str
    ):
        self.package = package
        self.module_name = module_name


class GetNormalizedMoveModulesByPackageParams:
    def __init__(
            self,
            package: str
    ):
        self.package = package


class GetNormalizedMoveStructParams:
    def __init__(
            self,
            package: str,
            module_name: str,
            struct_name: str
    ):
        self.package = package
        self.module_name = module_name
        self.struct_name = struct_name


class GetObjectParams:
    def __init__(
            self,
            object_id: str
    ):
        self.object_id = object_id


class MergeCoinsParams:
    def __init__(
            self,
            primary_coin: str,
            coin_to_merge: str,
            gas: str,
            gas_budget: int
    ):
        self.primary_coin = primary_coin
        self.coin_to_merge = coin_to_merge
        self.gas = gas
        self.gas_budget = gas_budget


class PayParams:
    def __init__(
            self,
            input_coins: List[str] or str,
            recipients: List[str] or str,
            amounts: List[int] or int,
            gas: str,
            gas_budget: int
    ):
        self.input_coins = input_coins
        self.recipients = recipients
        self.amounts = amounts
        self.gas = gas
        self.gas_budget = gas_budget


class PayAllParams:
    def __init__(
            self,
            input_coins: List[str] or str,
            recipient: str,
            gas_budget: int
    ):
        self.input_coins = input_coins
        self.recipient = recipient
        self.gas_budget = gas_budget


class PublishParams:
    def __init__(
            self,
            compiled_modules: str,
            gas: str,
            gas_budget: int
    ):
        self.compiled_modules = compiled_modules
        self.gas = gas,
        self.gas_budget = gas_budget


class SplitCoinParams:
    def __init__(
            self,
            coin_object_id: str,
            split_amounts: int,
            gas: str,
            gas_budget: int
    ):
        self.coin_object_id = coin_object_id
        self.split_amounts = split_amounts
        self.gas = gas,
        self.gas_budget = gas_budget


class SplitCoinEqualParams:
    def __init__(
            self,
            coin_object_id: str,
            split_count: int,
            gas: str,
            gas_budget: int
    ):
        self.coin_object_id = coin_object_id
        self.split_count = split_count
        self.gas = gas,
        self.gas_budget = gas_budget


class MoveCallParams:
    def __init__(
            self,
            package_object_id: str,
            module: str,
            function: str,
            type_arguments: Union[List[str], List[Any]],
            arguments: List[Union[bool, int, str, List[Any]]],
            gas_budget: int,
            gas_payment: Optional[str] = None
    ):
        self.package_object_id = package_object_id
        self.module = module
        self.function = function
        self.type_arguments = type_arguments
        self.arguments = arguments
        self.gas_budget = gas_budget
        self.gas_payment = gas_payment


class TransferObjectParams:
    def __init__(
            self,
            object_id: str,
            recipient: str,
            gas_budget: int,
            gas_payment: Optional[str] = None
    ):
        self.object_id = object_id
        self.gas_payment = gas_payment
        self.gas_budget = gas_budget
        self.recipient = recipient


class TransferSuiParams:
    def __init__(
            self,
            sui_object_id: str,
            recipient: str,
            gas_budget: int,
            amount: Optional[int] = None
    ):
        self.sui_object_id = sui_object_id
        self.recipient = recipient
        self.gas_budget = gas_budget
        self.amount = amount


class BatchTransactionParams:
    def __init__(
            self,
            single_transaction_params: list,
            gas: str,
            gas_budget: int
    ):
        self.single_transaction_params = single_transaction_params
        self.gas = gas
        self.gas_budget = gas_budget


class MoveFunctionArgTypesParams:
    def __init__(
            self,
            package: str,
            module: str,
            function: str
    ):
        self.package = package
        self.module = module
        self.function = function


class GetRawObjectParams:
    def __init__(
            self,
            object_id: str
    ):
        self.object_id = object_id


class GetTransactionsParams:
    def __init__(
            self,
            query: str,
            cursor: str,
            limit: int,
            descending_order: bool = False
    ):
        self.query = query
        self.cursor = cursor
        self.limit = limit
        self.descending_order = descending_order



class GetTransactionParams:
    def __init__(
            self,
            digest: str
    ):
        self.digest = digest



class GetEventsByTransactionParams:
    def __init__(
            self,
            query: str,
            cursor: str,
            limit: int
    ):
        self.query = query
        self.cursor = cursor
        self.limit = limit


class GetTotalTransactionsNumberInRangeParams:
    def __init__(
            self,
            start_of_range: int,
            end_of_range: int
    ):
        self.start_of_range = start_of_range
        self.end_of_range = end_of_range
