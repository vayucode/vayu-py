from .apis import *
from .clients import VayuClient


class Vayu:
    __api_key: str = None
    __host: str = None
    __client: VayuClient = None

    def __init__(self, api_key: str, host: str = None):
        self.__host = host
        self.__api_key = api_key
        self.__client = VayuClient(self.__api_key, self.__host)

    @property
    def contracts(self) -> ContractsAPI:
        return ContractsAPI(self.__client)

    @property
    def customers(self) -> CustomersAPI:
        return CustomersAPI(self.__client)

    @property
    def events(self) -> EventsAPI:
        return EventsAPI(self.__client)

    @property
    def invoices(self) -> InvoicesAPI:
        return InvoicesAPI(self.__client)

    @property
    def meters(self) -> MetersAPI:
        return MetersAPI(self.__client)

    @property
    def webhooks(self) -> WebhooksAPI:
        return WebhooksAPI(self.__client)

    @property
    def credits(self) -> CreditsAPI:
        return CreditsAPI(self.__client)

    @property
    def measurements(self) -> MeasurementsAPI:
        return MeasurementsAPI(self.__client)

    @property
    def catalog_products(self) -> CatalogProductsAPI:
        return CatalogProductsAPI(self.__client)

    @property
    def product_consumptions(self) -> ProductConsumptionsAPI:
        return ProductConsumptionsAPI(self.__client)

    def login(self):
        """Deprecated: Authentication is now handled automatically. You can remove this call."""
        self.__client.login()
