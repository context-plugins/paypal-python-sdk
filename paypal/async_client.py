from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.orders import AsyncOrders
from .apis.payments import AsyncPayments
from .apis.subscriptions import AsyncSubscriptions
from .apis.transaction_search import AsyncTransactionSearch
from .apis.vault import AsyncVault
from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BasePaypalClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    AsyncClientCredentialsTokenSource,
    AsyncHttpClient,
    AsyncHttpxClient,
    AsyncOAuth2Scheme,
    AsyncRawClient,
    AsyncTokenSource,
    ClientCredentials,
    ClientCredentialsOrDict,
    client_secret_basic,
    no_auth,
    param,
)


class AsyncPaypalClient(BasePaypalClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_async_http_client: AsyncHttpClient | None = None,
        oauth2: ClientCredentialsOrDict | None = None,
        oauth2_token_source: AsyncTokenSource[ClientCredentials] | None = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpxClient(timeout=timeout)
            ),
            global_headers=[
                param[str]("User-Agent", "PaypalClient/2.29 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "2.29"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(
            oauth2=(
                AsyncOAuth2Scheme(
                    credentials=ClientCredentials.coerce(oauth2),
                    source=(
                        oauth2_token_source
                        if oauth2_token_source is not None
                        else AsyncClientCredentialsTokenSource(
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
    def orders(self) -> AsyncOrders:
        return AsyncOrders(self._raw_client, self._server, self._auth)

    @cached_property
    def payments(self) -> AsyncPayments:
        return AsyncPayments(self._raw_client, self._server, self._auth)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptions:
        return AsyncSubscriptions(self._raw_client, self._server, self._auth)

    @cached_property
    def transaction_search(self) -> AsyncTransactionSearch:
        return AsyncTransactionSearch(self._raw_client, self._server, self._auth)

    @cached_property
    def vault(self) -> AsyncVault:
        return AsyncVault(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncPaypalClient
