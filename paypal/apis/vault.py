from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    json_body,
    json_decoder,
    param,
)
from ..errors.create_payment_token_error import CreatePaymentTokenErrorBody, create_payment_token_error_mapper
from ..errors.create_setup_token_error import CreateSetupTokenErrorBody, create_setup_token_error_mapper
from ..errors.delete_payment_token_error import DeletePaymentTokenErrorBody, delete_payment_token_error_mapper
from ..errors.get_payment_token_error import GetPaymentTokenErrorBody, get_payment_token_error_mapper
from ..errors.get_setup_token_error import GetSetupTokenErrorBody, get_setup_token_error_mapper
from ..errors.list_customer_payment_tokens_error import (
    ListCustomerPaymentTokensErrorBody,
    list_customer_payment_tokens_error_mapper,
)
from ..models.customer_vault_payment_tokens_response import CustomerVaultPaymentTokensResponse
from ..models.payment_token_request import PaymentTokenRequest, PaymentTokenRequestDict
from ..models.payment_token_response import PaymentTokenResponse
from ..models.setup_token_request import SetupTokenRequest, SetupTokenRequestDict
from ..models.setup_token_response import SetupTokenResponse
from ..server.server import Server


class Vault:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VaultWithRawResponse(client, server, auth)

    def create_payment_token(
        self,
        body: PaymentTokenRequest | PaymentTokenRequestDict,
        *,
        pay_pal_request_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentTokenResponse:
        """Creates a Payment Token from the given payment source and adds it to the Vault of the associated customer.

        Args:
            body: Payment Token creation with a financial instrument and an optional customer_id.
            pay_pal_request_id: The server stores keys for 3 hours.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Idempotent response for a successful creation of payment token.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authorization failed due
                to insufficient permissions. Request contains reference to resources that do not exist. The requested
                action could not be performed, semantically incorrect, or failed business validation. An internal server
                error has occurred. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.create_payment_token(
            body, pay_pal_request_id=pay_pal_request_id, request_options=request_options
        ).unwrap()

    def create_setup_token(
        self,
        body: SetupTokenRequest | SetupTokenRequestDict,
        *,
        pay_pal_request_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SetupTokenResponse:
        """Creates a Setup Token from the given payment source and adds it to the Vault of the associated customer.

        Args:
            body: Setup Token creation with a instrument type optional financial instrument details and customer_id.
            pay_pal_request_id: The server stores keys for 3 hours.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Idempotent response for a successful creation of setup token.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authorization failed due
                to insufficient permissions. The requested action could not be performed, semantically incorrect, or
                failed business validation. An internal server error has occurred. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.create_setup_token(
            body, pay_pal_request_id=pay_pal_request_id, request_options=request_options
        ).unwrap()

    def delete_payment_token(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete the payment token associated with the payment token id.

        Args:
            id: ID of the payment token.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The server has successfully executed the method, but there is no entity body to return.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authorization failed due
                to insufficient permissions. An internal server error has occurred. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.delete_payment_token(id, request_options=request_options).unwrap()

    def get_payment_token(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PaymentTokenResponse:
        """Returns a readable representation of vaulted payment source associated with the payment token id.

        Args:
            id: ID of the payment token.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful execution.

        Raises:
            ApiError: Authorization failed due to insufficient permissions. The specified resource does not exist. The
                requested action could not be performed, semantically incorrect, or failed business validation. An
                internal server error has occurred. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_payment_token(id, request_options=request_options).unwrap()

    def get_setup_token(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> SetupTokenResponse:
        """Returns a readable representation of temporarily vaulted payment source associated with the setup token id.

        Args:
            id: ID of the setup token.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Found requested setup-token, returned a payment method associated with the token.

        Raises:
            ApiError: Authorization failed due to insufficient permissions. The specified resource does not exist. The
                requested action could not be performed, semantically incorrect, or failed business validation. An
                internal server error has occurred. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_setup_token(id, request_options=request_options).unwrap()

    def list_customer_payment_tokens(
        self,
        customer_id: str,
        *,
        page_size: int | None = 5,
        page: int | None = 1,
        total_required: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CustomerVaultPaymentTokensResponse:
        """Returns all payment tokens for a customer.

        Args:
            customer_id: A unique identifier representing a specific customer in merchant's/partner's system or records.
            page_size: A non-negative, non-zero integer indicating the maximum number of results to return at one time.
            page: A non-negative, non-zero integer representing the page of the results.
            total_required: A boolean indicating total number of items (total_items) and pages (total_pages) are
                expected to be returned in the response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful execution.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authorization failed due
                to insufficient permissions. An internal server error has occurred. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.list_customer_payment_tokens(
            customer_id, page_size=page_size, page=page, total_required=total_required, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VaultWithRawResponse:
        return self._with_raw_response


class AsyncVault:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVaultWithRawResponse(client, server, auth)

    async def create_payment_token(
        self,
        body: PaymentTokenRequest | PaymentTokenRequestDict,
        *,
        pay_pal_request_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentTokenResponse:
        """Creates a Payment Token from the given payment source and adds it to the Vault of the associated customer.

        Args:
            body: Payment Token creation with a financial instrument and an optional customer_id.
            pay_pal_request_id: The server stores keys for 3 hours.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Idempotent response for a successful creation of payment token.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authorization failed due
                to insufficient permissions. Request contains reference to resources that do not exist. The requested
                action could not be performed, semantically incorrect, or failed business validation. An internal server
                error has occurred. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.create_payment_token(
                body, pay_pal_request_id=pay_pal_request_id, request_options=request_options
            )
        ).unwrap()

    async def create_setup_token(
        self,
        body: SetupTokenRequest | SetupTokenRequestDict,
        *,
        pay_pal_request_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SetupTokenResponse:
        """Creates a Setup Token from the given payment source and adds it to the Vault of the associated customer.

        Args:
            body: Setup Token creation with a instrument type optional financial instrument details and customer_id.
            pay_pal_request_id: The server stores keys for 3 hours.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Idempotent response for a successful creation of setup token.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authorization failed due
                to insufficient permissions. The requested action could not be performed, semantically incorrect, or
                failed business validation. An internal server error has occurred. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.create_setup_token(
                body, pay_pal_request_id=pay_pal_request_id, request_options=request_options
            )
        ).unwrap()

    async def delete_payment_token(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Delete the payment token associated with the payment token id.

        Args:
            id: ID of the payment token.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The server has successfully executed the method, but there is no entity body to return.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authorization failed due
                to insufficient permissions. An internal server error has occurred. ``error`` is ``Error |
                RawError``."""
        return (await self._with_raw_response.delete_payment_token(id, request_options=request_options)).unwrap()

    async def get_payment_token(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PaymentTokenResponse:
        """Returns a readable representation of vaulted payment source associated with the payment token id.

        Args:
            id: ID of the payment token.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful execution.

        Raises:
            ApiError: Authorization failed due to insufficient permissions. The specified resource does not exist. The
                requested action could not be performed, semantically incorrect, or failed business validation. An
                internal server error has occurred. ``error`` is ``Error | RawError``."""
        return (await self._with_raw_response.get_payment_token(id, request_options=request_options)).unwrap()

    async def get_setup_token(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SetupTokenResponse:
        """Returns a readable representation of temporarily vaulted payment source associated with the setup token id.

        Args:
            id: ID of the setup token.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Found requested setup-token, returned a payment method associated with the token.

        Raises:
            ApiError: Authorization failed due to insufficient permissions. The specified resource does not exist. The
                requested action could not be performed, semantically incorrect, or failed business validation. An
                internal server error has occurred. ``error`` is ``Error | RawError``."""
        return (await self._with_raw_response.get_setup_token(id, request_options=request_options)).unwrap()

    async def list_customer_payment_tokens(
        self,
        customer_id: str,
        *,
        page_size: int | None = 5,
        page: int | None = 1,
        total_required: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CustomerVaultPaymentTokensResponse:
        """Returns all payment tokens for a customer.

        Args:
            customer_id: A unique identifier representing a specific customer in merchant's/partner's system or records.
            page_size: A non-negative, non-zero integer indicating the maximum number of results to return at one time.
            page: A non-negative, non-zero integer representing the page of the results.
            total_required: A boolean indicating total number of items (total_items) and pages (total_pages) are
                expected to be returned in the response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful execution.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authorization failed due
                to insufficient permissions. An internal server error has occurred. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.list_customer_payment_tokens(
                customer_id,
                page_size=page_size,
                page=page,
                total_required=total_required,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVaultWithRawResponse:
        return self._with_raw_response


class VaultWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_payment_token(
        self,
        body: PaymentTokenRequest | PaymentTokenRequestDict,
        *,
        pay_pal_request_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentTokenResponse, CreatePaymentTokenErrorBody]:
        """Creates a Payment Token from the given payment source and adds it to the Vault of the associated customer.

        Args:
            body: Payment Token creation with a financial instrument and an optional customer_id.
            pay_pal_request_id: The server stores keys for 3 hours.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/vault/payment-tokens"),
            headers=[
                param[str | None]("PayPal-Request-Id", pay_pal_request_id), param[UUID]("Idempotency-Key", uuid4())
            ],
            body=json_body[PaymentTokenRequest | PaymentTokenRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[PaymentTokenResponse],
            error_mapper=create_payment_token_error_mapper,
            request_options=request_options,
        )

    def create_setup_token(
        self,
        body: SetupTokenRequest | SetupTokenRequestDict,
        *,
        pay_pal_request_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SetupTokenResponse, CreateSetupTokenErrorBody]:
        """Creates a Setup Token from the given payment source and adds it to the Vault of the associated customer.

        Args:
            body: Setup Token creation with a instrument type optional financial instrument details and customer_id.
            pay_pal_request_id: The server stores keys for 3 hours.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/vault/setup-tokens"),
            headers=[
                param[str | None]("PayPal-Request-Id", pay_pal_request_id), param[UUID]("Idempotency-Key", uuid4())
            ],
            body=json_body[SetupTokenRequest | SetupTokenRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SetupTokenResponse],
            error_mapper=create_setup_token_error_mapper,
            request_options=request_options,
        )

    def delete_payment_token(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeletePaymentTokenErrorBody]:
        """Delete the payment token associated with the payment token id.

        Args:
            id: ID of the payment token.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v3/vault/payment-tokens/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=empty_response,
            error_mapper=delete_payment_token_error_mapper,
            request_options=request_options,
        )

    def get_payment_token(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PaymentTokenResponse, GetPaymentTokenErrorBody]:
        """Returns a readable representation of vaulted payment source associated with the payment token id.

        Args:
            id: ID of the payment token.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/vault/payment-tokens/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[PaymentTokenResponse],
            error_mapper=get_payment_token_error_mapper,
            request_options=request_options,
        )

    def get_setup_token(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SetupTokenResponse, GetSetupTokenErrorBody]:
        """Returns a readable representation of temporarily vaulted payment source associated with the setup token id.

        Args:
            id: ID of the setup token.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/vault/setup-tokens/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SetupTokenResponse],
            error_mapper=get_setup_token_error_mapper,
            request_options=request_options,
        )

    def list_customer_payment_tokens(
        self,
        customer_id: str,
        *,
        page_size: int | None = 5,
        page: int | None = 1,
        total_required: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CustomerVaultPaymentTokensResponse, ListCustomerPaymentTokensErrorBody]:
        """Returns all payment tokens for a customer.

        Args:
            customer_id: A unique identifier representing a specific customer in merchant's/partner's system or records.
            page_size: A non-negative, non-zero integer indicating the maximum number of results to return at one time.
            page: A non-negative, non-zero integer representing the page of the results.
            total_required: A boolean indicating total number of items (total_items) and pages (total_pages) are
                expected to be returned in the response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/vault/payment-tokens"),
            query_params=[
                param[str]("customer_id", customer_id),
                param[int | None]("page_size", page_size),
                param[int | None]("page", page),
                param[bool | None]("total_required", total_required),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CustomerVaultPaymentTokensResponse],
            error_mapper=list_customer_payment_tokens_error_mapper,
            request_options=request_options,
        )


class AsyncVaultWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_payment_token(
        self,
        body: PaymentTokenRequest | PaymentTokenRequestDict,
        *,
        pay_pal_request_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentTokenResponse, CreatePaymentTokenErrorBody]:
        """Creates a Payment Token from the given payment source and adds it to the Vault of the associated customer.

        Args:
            body: Payment Token creation with a financial instrument and an optional customer_id.
            pay_pal_request_id: The server stores keys for 3 hours.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/vault/payment-tokens"),
            headers=[
                param[str | None]("PayPal-Request-Id", pay_pal_request_id), param[UUID]("Idempotency-Key", uuid4())
            ],
            body=json_body[PaymentTokenRequest | PaymentTokenRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[PaymentTokenResponse],
            error_mapper=create_payment_token_error_mapper,
            request_options=request_options,
        )

    async def create_setup_token(
        self,
        body: SetupTokenRequest | SetupTokenRequestDict,
        *,
        pay_pal_request_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SetupTokenResponse, CreateSetupTokenErrorBody]:
        """Creates a Setup Token from the given payment source and adds it to the Vault of the associated customer.

        Args:
            body: Setup Token creation with a instrument type optional financial instrument details and customer_id.
            pay_pal_request_id: The server stores keys for 3 hours.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/vault/setup-tokens"),
            headers=[
                param[str | None]("PayPal-Request-Id", pay_pal_request_id), param[UUID]("Idempotency-Key", uuid4())
            ],
            body=json_body[SetupTokenRequest | SetupTokenRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SetupTokenResponse],
            error_mapper=create_setup_token_error_mapper,
            request_options=request_options,
        )

    async def delete_payment_token(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeletePaymentTokenErrorBody]:
        """Delete the payment token associated with the payment token id.

        Args:
            id: ID of the payment token.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v3/vault/payment-tokens/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=empty_response,
            error_mapper=delete_payment_token_error_mapper,
            request_options=request_options,
        )

    async def get_payment_token(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PaymentTokenResponse, GetPaymentTokenErrorBody]:
        """Returns a readable representation of vaulted payment source associated with the payment token id.

        Args:
            id: ID of the payment token.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/vault/payment-tokens/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[PaymentTokenResponse],
            error_mapper=get_payment_token_error_mapper,
            request_options=request_options,
        )

    async def get_setup_token(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SetupTokenResponse, GetSetupTokenErrorBody]:
        """Returns a readable representation of temporarily vaulted payment source associated with the setup token id.

        Args:
            id: ID of the setup token.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/vault/setup-tokens/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SetupTokenResponse],
            error_mapper=get_setup_token_error_mapper,
            request_options=request_options,
        )

    async def list_customer_payment_tokens(
        self,
        customer_id: str,
        *,
        page_size: int | None = 5,
        page: int | None = 1,
        total_required: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CustomerVaultPaymentTokensResponse, ListCustomerPaymentTokensErrorBody]:
        """Returns all payment tokens for a customer.

        Args:
            customer_id: A unique identifier representing a specific customer in merchant's/partner's system or records.
            page_size: A non-negative, non-zero integer indicating the maximum number of results to return at one time.
            page: A non-negative, non-zero integer representing the page of the results.
            total_required: A boolean indicating total number of items (total_items) and pages (total_pages) are
                expected to be returned in the response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/vault/payment-tokens"),
            query_params=[
                param[str]("customer_id", customer_id),
                param[int | None]("page_size", page_size),
                param[int | None]("page", page),
                param[bool | None]("total_required", total_required),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CustomerVaultPaymentTokensResponse],
            error_mapper=list_customer_payment_tokens_error_mapper,
            request_options=request_options,
        )
