from openapi.api.customers_api import CustomersApi
from vayu_sdk.clients.vayu_client import VayuClient
from openapi.models.create_customer_request import CreateCustomerRequest
from openapi.models.update_customer_request import UpdateCustomerRequest

from openapi.models.create_customer_response_customer import (
    CreateCustomerResponseCustomer,
)
from openapi.models.list_customers_response import ListCustomersResponse
from openapi.models.get_customer_response import GetCustomerResponse
from openapi.models.create_customer_response import CreateCustomerResponse
from openapi.models.update_customer_response import UpdateCustomerResponse
from openapi.models.delete_customer_response import DeleteCustomerResponse


Customer = CreateCustomerResponseCustomer


class CustomersAPI:
    __client: CustomersApi = None

    def __init__(self, vayu_client: VayuClient):
        vayu_client.validate_logged_in()
        self.__client = CustomersApi(vayu_client.client)

    def list(self, cursor: str = None, limit: int = None):
        return self.__client.list_customers(limit=limit, cursor=cursor)

    def get(self, customer_id: str):
        response = self.__client.get_customer(customer_id)

        return response

    def create(self, name: str, alias: str):
        request = CreateCustomerRequest(name=name, alias=alias)
        response = self.__client.create_customer(
            request
        )

        return response

    def update(self, id: str, name: str = None, alias: str = None):
        request = UpdateCustomerRequest(name=name, alias=alias)
        response = self.__client.update_customer(
            id, request
        )

        return response

    def delete(self, id: str):
        response = self.__client.delete_customer(id)

        return response


__all__ = [
    "CustomersAPI",
    "Customer",
    "ListCustomersResponse",
    "GetCustomerResponse",
    "CreateCustomerResponse",
    "UpdateCustomerResponse",
    "DeleteCustomerResponse",
]
