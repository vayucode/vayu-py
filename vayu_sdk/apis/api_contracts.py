from openapi.api.contracts_api import ContractsApi
from vayu_sdk.clients.vayu_client import VayuClient
from openapi.models.create_contract_request import CreateContractRequest
from datetime import datetime

from openapi.models.get_contract_response_contract import GetContractResponseContract
from openapi.models.list_contracts_response import ListContractsResponse
from openapi.models.get_contract_response import GetContractResponse
from openapi.models.create_contract_response import CreateContractResponse
from openapi.models.delete_contract_response import DeleteContractResponse

Contract = GetContractResponseContract


class ContractsAPI:
    __client: ContractsApi = None

    def __init__(self, vayu_client: VayuClient):
        vayu_client.validate_logged_in()
        self.__client = ContractsApi(vayu_client.client)

    def list(self, limit: int = None, cursor: int = None):
        return self.__client.list_contracts(limit=limit, cursor=cursor)

    def get(self, contract_id: str):
        response = self.__client.get_contract(contract_id)

        return response

    def create(
        self, start_date: datetime, end_date: datetime | None, customer_id: str, plan_id: str
    ):
        request = CreateContractRequest(
            start_date=start_date,
            end_date=end_date,
            customer_id=customer_id,
            plan_id=plan_id,
        )

        response = self.__client.create_contract(
            request
        )

        return response

    def delete(self, id: str):
        response = self.__client.delete_contract(id)

        return response


__all__ = [
    "ContractsAPI",
    "Contract",
    "ListContractsResponse",
    "GetContractResponse",
    "CreateContractResponse",
    "DeleteContractResponse",
]
