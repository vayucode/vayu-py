# vayu_sdk/apis/api_catalog_products.py
from openapi.api.catalog_products_api import CatalogProductsApi
from vayu_sdk.clients.vayu_client import VayuClient
from openapi.models.create_catalog_product_request import CreateCatalogProductRequest
from openapi.models.create_catalog_product_response import CreateCatalogProductResponse
from openapi.models.delete_catalog_product_response import DeleteCatalogProductResponse
from openapi.models.get_catalog_product_response import GetCatalogProductResponse
from openapi.models.list_catalog_products_response import ListCatalogProductsResponse
from openapi.models.update_catalog_product_request import UpdateCatalogProductRequest
from openapi.models.update_catalog_product_response import UpdateCatalogProductResponse


class CatalogProductsAPI:
    __client: CatalogProductsApi = None

    def __init__(self, vayu_client: VayuClient):
        self.__client = CatalogProductsApi(vayu_client.client)

    def create(self, request: CreateCatalogProductRequest):
        return self.__client.create_catalog_product(create_catalog_product_request=request)

    def delete(self, id: str):
        return self.__client.delete_catalog_product(catalog_product_id=id)

    def get(self, id: str):
        return self.__client.get_catalog_product(catalog_product_id=id)

    def list(self, limit: int = None, cursor: str = None):
        return self.__client.list_catalog_products(limit=limit, cursor=cursor)

    def update(self, id: str, request: UpdateCatalogProductRequest):
        return self.__client.update_catalog_product(
            update_catalog_product_request=request, catalog_product_id=id
        )
