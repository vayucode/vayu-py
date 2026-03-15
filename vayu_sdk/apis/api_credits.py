# vayu_sdk/apis/api_credits.py
from openapi.api.credits_api import CreditsApi
from vayu_sdk.clients.vayu_client import VayuClient
from openapi.models.deduct_credits_request import DeductCreditsRequest
from openapi.models.grant_credits_request import GrantCreditsRequest
from openapi.models.list_credit_ledger_entries_response import ListCreditLedgerEntriesResponse


class CreditsAPI:
    __client: CreditsApi = None

    def __init__(self, vayu_client: VayuClient):
        self.__client = CreditsApi(vayu_client.client)

    def deduct(self, request: DeductCreditsRequest):
        return self.__client.deduct_credits(deduct_credits_request=request)

    def grant(self, request: GrantCreditsRequest):
        return self.__client.grant_credits(grant_credits_request=request)

    def list_ledger_entries(self, customer_id: str, limit: int = None, cursor: str = None):
        return self.__client.list_credit_ledger_entries(
            customer_id=customer_id, limit=limit, cursor=cursor
        )
