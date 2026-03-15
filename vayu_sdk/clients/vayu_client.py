from openapi.api_client import ApiClient
from openapi.configuration import Configuration
from openapi.rest import RESTClientObject
from vayu_sdk.clients.authenticator import VayuAuthenticator


class VayuClient:
    def __init__(self, api_key: str, host: str = None):
        self._host = host
        self.auth = VayuAuthenticator(api_key, host)

    @property
    def access_token(self):
        return self.auth.access_token

    @property
    def is_logged_in(self):
        return self.auth.is_authenticated

    @property
    def client(self):
        configuration = Configuration(host=self._host)
        client = ApiClient(configuration)
        client.rest_client = AuthenticatedRESTClient(self.auth, configuration)
        return client

    def login(self):
        """Deprecated: Authentication is now handled automatically. You can remove this call."""
        self.auth.authenticate()

    def validate_logged_in(self):
        """Deprecated: Authentication is now handled automatically."""
        pass


class AuthenticatedRESTClient(RESTClientObject):
    """Thin REST client that delegates auth to VayuAuthenticator and retries on 401."""

    def __init__(self, authenticator: VayuAuthenticator, configuration: Configuration):
        super().__init__(configuration)
        self._auth = authenticator

    def request(self, method, url, headers=None, **kwargs):
        is_login_request = "/login" in url

        if not is_login_request:
            token = self._auth.ensure_valid_token()
            if headers is None:
                headers = {}
            headers["Authorization"] = f"Bearer {token}"

        response = super().request(method, url, headers=headers, **kwargs)

        # 401 retry: re-authenticate and retry once
        if not is_login_request and response.status == 401:
            self._auth.authenticate()
            headers["Authorization"] = f"Bearer {self._auth.access_token}"
            response = super().request(method, url, headers=headers, **kwargs)

        return response


__all__ = ["VayuClient"]
