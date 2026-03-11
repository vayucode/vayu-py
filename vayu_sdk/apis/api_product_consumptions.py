# vayu_sdk/apis/api_product_consumptions.py
from openapi.api.product_consumptions_api import ProductConsumptionsApi
from vayu_sdk.clients.vayu_client import VayuClient
from openapi.models.get_product_consumption_response import GetProductConsumptionResponse


class ProductConsumptionsAPI:
    __client: ProductConsumptionsApi = None

    def __init__(self, vayu_client: VayuClient):
        self.__client = ProductConsumptionsApi(vayu_client.client)

    def get(self, product_id: str):
        return self.__client.get_product_consumption(product_id=product_id)
