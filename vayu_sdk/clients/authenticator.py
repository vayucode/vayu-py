from openapi.api_client import ApiClient
from openapi.configuration import Configuration
from openapi.api.auth_api import AuthApi
from openapi.models.login_request import LoginRequest
import jwt
from datetime import datetime, timedelta


class VayuAuthenticator:
    _TOKEN_EXPIRY_THRESHOLD = timedelta(minutes=5)

    def __init__(self, api_key: str, host: str = None):
        self._api_key = api_key
        self._host = host
        self._access_token: str = None
        self._expires_at: datetime = datetime.min

    @property
    def is_authenticated(self) -> bool:
        return self._access_token is not None

    @property
    def access_token(self) -> str:
        return self._access_token

    @property
    def needs_refresh(self) -> bool:
        return (
            self._access_token is None
            or datetime.now() + self._TOKEN_EXPIRY_THRESHOLD > self._expires_at
        )

    def ensure_valid_token(self) -> str:
        """Return a valid access token, logging in or refreshing as needed."""
        if self.needs_refresh:
            self.authenticate()

        return self._access_token

    def authenticate(self):
        """Exchange the refresh token for a new access token."""
        configuration = Configuration(host=self._host)
        client = ApiClient(configuration)
        api = AuthApi(client)
        login_request = LoginRequest(refreshToken=self._api_key)
        response = api.login(login_request)

        self._access_token = response.access_token

        decoded_token = jwt.decode(
            self._access_token, options={"verify_signature": False}
        )
        self._expires_at = datetime.fromtimestamp(decoded_token["exp"])


__all__ = ["VayuAuthenticator"]
