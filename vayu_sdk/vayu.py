from vayu_sdk.apis.api_webhooks import WebhooksAPI, Webhook, GetWebhookResponse, QueryWebhooksResponse, CreateWebhookResponse, UpdateWebhookResponse, DeleteWebhookResponse
from .clients.vayu_client import VayuClient, VayuClient
from .apis.api_contracts import ContractsAPI, Contract, GetContractResponse, QueryContractsResponse, CreateContractResponse, UpdateContractResponse, DeleteContractResponse
from .apis.api_customers import CustomersAPI, Customer, GetCustomerResponse, QueryCustomersResponse, CreateCustomerResponse, UpdateCustomerResponse, DeleteCustomerResponse
from .apis.api_events import EventsAPI, Event, GetEventResponse, DeleteEventResponse, QueryEventsResponse, SendEventsResponse, EventsDryRunResponse
from .apis.api_invoices import InvoicesAPI, Invoice, GetInvoiceResponse, QueryInvoicesResponse, CreateInvoiceResponse, UpdateInvoiceResponse, DeleteInvoiceResponse
from .apis.api_meters import MetersAPI, Meter, GetMeterResponse, QueryMetersResponse, CreateMeterResponse, UpdateMeterResponse, DeleteMeterResponse
from .apis.api_plans import PlansAPI, Plan, GetPlanResponse, QueryPlansResponse, CreatePlanResponse, UpdatePlanResponse, DeletePlanResponse

class Vayu:
    __api_key: str = None
    __host: str = None
    __client: VayuClient = None

    def __init__(self, api_key: str, host: str = None):
        self.__client = None
        self.__host = host
        self.__api_key = api_key

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
    def plans(self) -> PlansAPI:
        return PlansAPI(self.__client)
    
    @property
    def webhooks(self) -> WebhooksAPI:
        return WebhooksAPI(self.__client)
    
    def login(self):
        self.__client = VayuClient(self.__api_key, self.__host)
        self.__client.login()

__all__ = [
    "Vayu",
    "Event",
    "EventsAPI",
    "EventsDryRunResponse",
    "GetEventResponse",
    "DeleteEventResponse",
    "QueryEventsResponse",
    "SendEventsResponse",
    "Contract",
    "ContractsAPI",
    "CreateContractResponse",
    "DeleteContractResponse",
    "GetContractResponse",
    "QueryContractsResponse",
    "Customer",
    "CustomersAPI",
    "CreateCustomerResponse",
    "DeleteCustomerResponse",
    "GetCustomerResponse",
    "QueryCustomersResponse",
    "Invoice",
    "InvoicesAPI",
    "CreateInvoiceResponse",
    "DeleteInvoiceResponse",
    "GetInvoiceResponse",
    "QueryInvoicesResponse",
    "Meter",
    "MetersAPI",
    "CreateMeterResponse",
    "DeleteMeterResponse",
    "GetMeterResponse",
    "QueryMetersResponse",
    "Plan",
    "PlansAPI",
    "CreatePlanResponse",
    "DeletePlanResponse",
    "GetPlanResponse",
    "QueryPlansResponse",
    "Webhook",
    "WebhooksAPI",
    "CreateWebhookResponse",
    "DeleteWebhookResponse",
    "GetWebhookResponse",
    "QueryWebhooksResponse",
]
