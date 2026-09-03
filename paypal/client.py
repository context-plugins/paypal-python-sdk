from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.orders import Orders
from .apis.payments import Payments
from .apis.subscriptions import Subscriptions
from .apis.transaction_search import TransactionSearch
from .apis.vault import Vault
from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BasePaypalClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ClientCredentials,
    ClientCredentialsOrDict,
    ClientCredentialsTokenSource,
    HttpClient,
    HttpxClient,
    OAuth2Scheme,
    RawClient,
    TokenSource,
    client_secret_basic,
    no_auth,
    param,
)


class PaypalClient(BasePaypalClient[RawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_http_client: HttpClient | None = None,
        oauth2: ClientCredentialsOrDict | None = None,
        oauth2_token_source: TokenSource[ClientCredentials] | None = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout),
            global_headers=[
                param[str]("User-Agent", "PaypalClient/2.29 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "2.29"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AuthSchemes(
            oauth2=(
                OAuth2Scheme(
                    credentials=ClientCredentials.coerce(oauth2),
                    source=(
                        oauth2_token_source
                        if oauth2_token_source is not None
                        else ClientCredentialsTokenSource(
                            client=self._raw_client,
                            token_url=self._server.default("/v1/oauth2/token"),
                            placement=client_secret_basic,
                        )
                    ),
                )
                if oauth2 is not None
                else no_auth
            ),
        )

    @cached_property
    def orders(self) -> Orders:
        return Orders(self._raw_client, self._server, self._auth)

    @cached_property
    def payments(self) -> Payments:
        return Payments(self._raw_client, self._server, self._auth)

    @cached_property
    def subscriptions(self) -> Subscriptions:
        return Subscriptions(self._raw_client, self._server, self._auth)

    @cached_property
    def transaction_search(self) -> TransactionSearch:
        return TransactionSearch(self._raw_client, self._server, self._auth)

    @cached_property
    def vault(self) -> Vault:
        return Vault(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = PaypalClient
