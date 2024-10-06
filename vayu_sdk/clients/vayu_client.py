from datetime import datetime, timedelta
from openapi.api_client import ApiClient
from openapi.configuration import Configuration
from openapi.api.auth_api import AuthApi
from openapi.models.login_request import LoginRequest
from datetime import datetime, timedelta
from requests.adapters import HTTPAdapter
from requests.sessions import Session

class VayuClient:
    __access_token: str = None
    __expires_at: datetime = None
    __api_key: str = None
    __host: str = None
    __token_expiry_threshold = timedelta(minutes=5)

    def __init__(self, api_key: str, host: str = None):
        self.__access_token = None
        self.__host = host  
        self.__api_key = api_key
    
    @property
    def is_logged_in(self):
        return self.__access_token is not None

    @property
    def client(self):
        configuration = Configuration(host=self.__host, api_key=self.__access_token)
        session = self.__build_session()
        return ApiClient(
            configuration,
            header_name="Authorization",
            header_value=f"Bearer {self.__access_token}",
            session=session,
        )

    def __build_session(self) -> Session:
        session = Session()
        adapter = TokenRefreshAdapter(self)
        session.mount("https://", adapter)
        return session
    

    def login(self):
        configuration = Configuration(host=self.__host)
        client = ApiClient(configuration)
        api = AuthApi(client)
        login_request = LoginRequest(refreshToken=self.__api_key)
        refresh_response = api.login(login_request)

        self.__access_token = refresh_response.access_token

    def refresh_token(self):
        if self.__access_token is None or datetime.now(datetime.UTC) + self.__token_expiry_threshold > self.__expires_at:
            self.login()

    def validate_logged_in(self):
        if not self.is_logged_in:
            raise RuntimeError("vayu client is not logged in. please login before calling this method")

class TokenRefreshAdapter(HTTPAdapter):
    def __init__(self, client: VayuClient, *args, **kwargs):
        self.client = client
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        if request.path_url != "/login":
            self.client.refresh_token()
            request.headers["Authorization"] = f"Bearer {self.vayu_client._Vayu__access_token}"
        return super().send(request, **kwargs)

__all__ = ["VayuClient"]

