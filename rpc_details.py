from .client import Client
from .models import MoveFunctionArgTypesParams, GetTransactionsParams, GetTransactionsIDParams, \
    GetObjectsOwnedByAddressParams, GetObjectsOwnedByObjectParams, GetObjectParams, GetTransactionParams, \
    GetEventsByTransactionParams, GetTotalTransactionsNumberInRangeParams, GetNormalizedMoveFunctionParams, \
    GetNormalizedMoveModuleParams, GetNormalizedMoveModulesByPackageParams, GetNormalizedMoveStructParams, \
    GetRawObjectParams





class RpcDetails(Client):

    @staticmethod
    def get_transaction_id(tx: GetTransactionsIDParams) -> str:
        return tx.response['result']['EffectsCert']['certificate']['transactionDigest']

    def get_rpc_version(self):
        return self.send_request_to_rpc(
            method="rpc.discover"
        )


    def get_move_function_arg_types(self, tx: MoveFunctionArgTypesParams):
        return self.send_request_to_rpc(
            method="sui_getMoveFunctionArgTypes",
            params=[
                tx.package,
                tx.module,
                tx.function
            ])

    def get_normalized_move_function(self, tx: GetNormalizedMoveFunctionParams):
        return self.send_request_to_rpc(
            method='sui_getNormalizedMoveFunction',
            params=[
                tx.package,
                tx.module_name,
                tx.function_name
            ]
        )

    def get_normalized_move_module(self, tx: GetNormalizedMoveModuleParams):
        return self.send_request_to_rpc(
            method='sui_getNormalizedMoveModule',
            params=[
                tx.package,
                tx.module_name
            ]
        )


    def get_normalized_move_modules_by_package(self, tx: GetNormalizedMoveModulesByPackageParams):
        return self.send_request_to_rpc(
            method='sui_getNormalizedMoveModulesByPackage',
            params=[
                tx.package
            ]
        )

    def get_normalized_move_struct(self, tx: GetNormalizedMoveStructParams):
        return self.send_request_to_rpc(
            method='sui_getNormalizedMoveStruct',
            params=[
                tx.package,
                tx.module_name,
                tx.struct_name
            ]
        )

    def get_object(self, tx: GetObjectParams) -> dict:
        return self.send_request_to_rpc(
            method="sui_getObject",
            params=[
                tx.object_id
            ])

    def get_objects_owned_by_address(self, tx: GetObjectsOwnedByAddressParams) -> dict:
        return self.send_request_to_rpc(
            method="sui_getObjectsOwnedByAddress",
            params=[
                tx.address
            ])

    def get_objects_owned_by_object(self, tx: GetObjectsOwnedByObjectParams) -> dict:
        return self.send_request_to_rpc(
            method="sui_getObjectsOwnedByObject",
            params=[
                tx.object_id
            ])

    def get_raw_object(self, tx: GetRawObjectParams):
        return self.send_request_to_rpc(
            method='sui_getRawObject',
            params=[
                tx.object_id
            ]
        )


    def get_transactions(self, tx: GetTransactionsParams) -> dict:
        return self.send_request_to_rpc(
            method="sui_getTransactions",
            params=[
                tx.query,
                tx.cursor,
                tx.limit,
                tx.descending_order
            ])


    def get_transaction(self, tx: GetTransactionParams) -> dict:
        return self.send_request_to_rpc(
            method="sui_getTransaction",
            params=[
                tx.digest
            ])

    def get_events_by_transaction(self, tx: GetEventsByTransactionParams):
        return self.send_request_to_rpc(
            method="sui_getEventsByTransaction",
            params=[
                tx.query,
                tx.cursor,
                tx.limit
            ])

    def get_total_transaction_number(self) -> dict:
        return self.send_request_to_rpc(
            method="sui_getTotalTransactionNumber"
        )

    def get_total_transaction_in_range(self, tx: GetTotalTransactionsNumberInRangeParams) -> dict:
        return self.send_request_to_rpc(
            method="sui_getTransactionsInRange",
            params=[
                tx.start_of_range,
                tx.end_of_range
            ])
