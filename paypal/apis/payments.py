from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
)
from ..errors.capture_authorized_payment_error import (
    CaptureAuthorizedPaymentErrorBody,
    capture_authorized_payment_error_mapper,
)
from ..errors.get_authorized_payment_error import GetAuthorizedPaymentErrorBody, get_authorized_payment_error_mapper
from ..errors.get_captured_payment_error import GetCapturedPaymentErrorBody, get_captured_payment_error_mapper
from ..errors.get_refund_error import GetRefundErrorBody, get_refund_error_mapper
from ..errors.reauthorize_payment_error import ReauthorizePaymentErrorBody, reauthorize_payment_error_mapper
from ..errors.refund_captured_payment_error import RefundCapturedPaymentErrorBody, refund_captured_payment_error_mapper
from ..errors.void_payment_error import VoidPaymentErrorBody, void_payment_error_mapper
from ..models.capture_request import CaptureRequest, CaptureRequestDict
from ..models.captured_payment import CapturedPayment
from ..models.payment_authorization import PaymentAuthorization
from ..models.reauthorize_request import ReauthorizeRequest, ReauthorizeRequestDict
from ..models.refund import Refund
from ..models.refund_request import RefundRequest, RefundRequestDict
from ..server.server import Server


class Payments:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PaymentsWithRawResponse(client, server, auth)

    def capture_authorized_payment(
        self,
        authorization_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_auth_assertion: str | None = None,
        body: CaptureRequest | CaptureRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CapturedPayment:
        """Captures an authorized payment, by ID.

        Args:
            authorization_id: The PayPal-generated ID for the authorized payment to capture.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_request_id: The server stores keys for 45 days.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP 200 OK status code and a JSON response body that shows captured
            payment details.

        Raises:
            ApiError: The request failed because it is not well-formed or is syntactically incorrect or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials. The
                request failed because the caller has insufficient permissions. The request failed because the resource
                does not exist. The server has detected a conflict while processing this request. The request failed
                because it is semantically incorrect or failed business validation. The request failed because an
                internal server error occurred. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.capture_authorized_payment(
            authorization_id,
            pay_pal_mock_response=pay_pal_mock_response,
            pay_pal_request_id=pay_pal_request_id,
            prefer=prefer,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
            body=body,
            request_options=request_options,
        ).unwrap()

    def get_authorized_payment(
        self,
        authorization_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentAuthorization:
        """Shows details for an authorized payment, by ID.

        Args:
            authorization_id: The ID of the authorized payment for which to show details.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP 200 OK status code and a JSON response body that shows authorization
            details.

        Raises:
            ApiError: Authentication failed due to missing authorization header, or invalid authentication credentials.
                The request failed because the caller has insufficient permissions. The request failed because the
                resource does not exist. The request failed because an internal server error occurred. ``error`` is
                ``Error | RawError``."""
        return self._with_raw_response.get_authorized_payment(
            authorization_id,
            pay_pal_mock_response=pay_pal_mock_response,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
            request_options=request_options,
        ).unwrap()

    def get_captured_payment(
        self,
        capture_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CapturedPayment:
        """Shows details for a captured payment, by ID.

        Args:
            capture_id: The PayPal-generated ID for the captured payment for which to show details.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP 200 OK status code and a JSON response body that shows captured
            payment details.

        Raises:
            ApiError: Authentication failed due to missing authorization header, or invalid authentication credentials.
                The request failed because the caller has insufficient permissions. The request failed because the
                resource does not exist. The request failed because an internal server error occurred. ``error`` is
                ``Error | RawError``."""
        return self._with_raw_response.get_captured_payment(
            capture_id, pay_pal_mock_response=pay_pal_mock_response, request_options=request_options
        ).unwrap()

    def get_refund(
        self,
        refund_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Refund:
        """Shows details for a refund, by ID.

        Args:
            refund_id: The PayPal-generated ID for the refund for which to show details.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP 200 OK status code and a JSON response body that shows refund details.

        Raises:
            ApiError: Authentication failed due to missing authorization header, or invalid authentication credentials.
                The request failed because the caller has insufficient permissions. The request failed because the
                resource does not exist. The request failed because an internal server error occurred. ``error`` is
                ``Error | RawError``."""
        return self._with_raw_response.get_refund(
            refund_id,
            pay_pal_mock_response=pay_pal_mock_response,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
            request_options=request_options,
        ).unwrap()

    def reauthorize_payment(
        self,
        authorization_id: str,
        *,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_auth_assertion: str | None = None,
        body: ReauthorizeRequest | ReauthorizeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentAuthorization:
        """Reauthorizes an authorized PayPal account payment, by ID. To ensure that funds are still available,
        reauthorize a payment after its initial three-day honor period expires. Within the 29-day authorization period,
        you can issue multiple re-authorizations after the honor period expires. If 30 days have transpired since the
        date of the original authorization, you must create an authorized payment instead of reauthorizing the original
        authorized payment. A reauthorized payment itself has a new honor period of three days. You can reauthorize an
        authorized payment from 4 to 29 days after the 3-day honor period. The allowed amount depends on context and
        geography, for example in US it is up to 115% of the original authorized amount, not to exceed an increase of
        $75 USD. Supports only the ``amount`` request parameter.

        Args:
            authorization_id: The PayPal-generated ID for the authorized payment to reauthorize.
            pay_pal_request_id: The server stores keys for 45 days.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP 200 OK status code and a JSON response body that shows the
            reauthorized payment details.

        Raises:
            ApiError: The request failed because it is not well-formed or is syntactically incorrect or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials. The
                request failed because the caller has insufficient permissions. The request failed because the resource
                does not exist. The request failed because it either is semantically incorrect or failed business
                validation. The request failed because an internal server error occurred. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.reauthorize_payment(
            authorization_id,
            pay_pal_request_id=pay_pal_request_id,
            prefer=prefer,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
            body=body,
            request_options=request_options,
        ).unwrap()

    def refund_captured_payment(
        self,
        capture_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_auth_assertion: str | None = None,
        body: RefundRequest | RefundRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Refund:
        """Refunds a captured payment, by ID. For a full refund, include an empty payload in the JSON request body. For
        a partial refund, include an amount object in the JSON request body.

        Args:
            capture_id: The PayPal-generated ID for the captured payment to refund.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_request_id: The server stores keys for 45 days.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP 200 OK status code and a JSON response body that shows refund details.

        Raises:
            ApiError: The request failed because it is not well-formed or is syntactically incorrect or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials. The
                request failed because the caller has insufficient permissions. The request failed because the resource
                does not exist. The request failed because a previous call for the given resource is in progress. The
                request failed because it either is semantically incorrect or failed business validation. The request
                failed because an internal server error occurred. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.refund_captured_payment(
            capture_id,
            pay_pal_mock_response=pay_pal_mock_response,
            pay_pal_request_id=pay_pal_request_id,
            prefer=prefer,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
            body=body,
            request_options=request_options,
        ).unwrap()

    def void_payment(
        self,
        authorization_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentAuthorization:
        """Voids, or cancels, an authorized payment, by ID. You cannot void an authorized payment that has been fully
        captured.

        Args:
            authorization_id: The PayPal-generated ID for the authorized payment to void.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            pay_pal_request_id: The server stores keys for 45 days.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP 200 OK status code and a JSON response body that shows authorization
            details. This response is returned when the Prefer header is set to return=representation.

        Raises:
            ApiError: Authentication failed due to missing authorization header, or invalid authentication credentials.
                The request failed because the caller has insufficient permissions. The request failed because the
                resource does not exist. The request failed because a previous call for the given resource is in
                progress. The request failed because it either is semantically incorrect or failed business validation.
                The request failed because an internal server error occurred. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.void_payment(
            authorization_id,
            pay_pal_mock_response=pay_pal_mock_response,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
            pay_pal_request_id=pay_pal_request_id,
            prefer=prefer,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> PaymentsWithRawResponse:
        return self._with_raw_response


class AsyncPayments:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPaymentsWithRawResponse(client, server, auth)

    async def capture_authorized_payment(
        self,
        authorization_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_auth_assertion: str | None = None,
        body: CaptureRequest | CaptureRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CapturedPayment:
        """Captures an authorized payment, by ID.

        Args:
            authorization_id: The PayPal-generated ID for the authorized payment to capture.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_request_id: The server stores keys for 45 days.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP 200 OK status code and a JSON response body that shows captured
            payment details.

        Raises:
            ApiError: The request failed because it is not well-formed or is syntactically incorrect or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials. The
                request failed because the caller has insufficient permissions. The request failed because the resource
                does not exist. The server has detected a conflict while processing this request. The request failed
                because it is semantically incorrect or failed business validation. The request failed because an
                internal server error occurred. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.capture_authorized_payment(
                authorization_id,
                pay_pal_mock_response=pay_pal_mock_response,
                pay_pal_request_id=pay_pal_request_id,
                prefer=prefer,
                pay_pal_auth_assertion=pay_pal_auth_assertion,
                body=body,
                request_options=request_options,
            )
        ).unwrap()

    async def get_authorized_payment(
        self,
        authorization_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentAuthorization:
        """Shows details for an authorized payment, by ID.

        Args:
            authorization_id: The ID of the authorized payment for which to show details.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP 200 OK status code and a JSON response body that shows authorization
            details.

        Raises:
            ApiError: Authentication failed due to missing authorization header, or invalid authentication credentials.
                The request failed because the caller has insufficient permissions. The request failed because the
                resource does not exist. The request failed because an internal server error occurred. ``error`` is
                ``Error | RawError``."""
        return (
            await self._with_raw_response.get_authorized_payment(
                authorization_id,
                pay_pal_mock_response=pay_pal_mock_response,
                pay_pal_auth_assertion=pay_pal_auth_assertion,
                request_options=request_options,
            )
        ).unwrap()

    async def get_captured_payment(
        self,
        capture_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CapturedPayment:
        """Shows details for a captured payment, by ID.

        Args:
            capture_id: The PayPal-generated ID for the captured payment for which to show details.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP 200 OK status code and a JSON response body that shows captured
            payment details.

        Raises:
            ApiError: Authentication failed due to missing authorization header, or invalid authentication credentials.
                The request failed because the caller has insufficient permissions. The request failed because the
                resource does not exist. The request failed because an internal server error occurred. ``error`` is
                ``Error | RawError``."""
        return (
            await self._with_raw_response.get_captured_payment(
                capture_id, pay_pal_mock_response=pay_pal_mock_response, request_options=request_options
            )
        ).unwrap()

    async def get_refund(
        self,
        refund_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Refund:
        """Shows details for a refund, by ID.

        Args:
            refund_id: The PayPal-generated ID for the refund for which to show details.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP 200 OK status code and a JSON response body that shows refund details.

        Raises:
            ApiError: Authentication failed due to missing authorization header, or invalid authentication credentials.
                The request failed because the caller has insufficient permissions. The request failed because the
                resource does not exist. The request failed because an internal server error occurred. ``error`` is
                ``Error | RawError``."""
        return (
            await self._with_raw_response.get_refund(
                refund_id,
                pay_pal_mock_response=pay_pal_mock_response,
                pay_pal_auth_assertion=pay_pal_auth_assertion,
                request_options=request_options,
            )
        ).unwrap()

    async def reauthorize_payment(
        self,
        authorization_id: str,
        *,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_auth_assertion: str | None = None,
        body: ReauthorizeRequest | ReauthorizeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentAuthorization:
        """Reauthorizes an authorized PayPal account payment, by ID. To ensure that funds are still available,
        reauthorize a payment after its initial three-day honor period expires. Within the 29-day authorization period,
        you can issue multiple re-authorizations after the honor period expires. If 30 days have transpired since the
        date of the original authorization, you must create an authorized payment instead of reauthorizing the original
        authorized payment. A reauthorized payment itself has a new honor period of three days. You can reauthorize an
        authorized payment from 4 to 29 days after the 3-day honor period. The allowed amount depends on context and
        geography, for example in US it is up to 115% of the original authorized amount, not to exceed an increase of
        $75 USD. Supports only the ``amount`` request parameter.

        Args:
            authorization_id: The PayPal-generated ID for the authorized payment to reauthorize.
            pay_pal_request_id: The server stores keys for 45 days.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP 200 OK status code and a JSON response body that shows the
            reauthorized payment details.

        Raises:
            ApiError: The request failed because it is not well-formed or is syntactically incorrect or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials. The
                request failed because the caller has insufficient permissions. The request failed because the resource
                does not exist. The request failed because it either is semantically incorrect or failed business
                validation. The request failed because an internal server error occurred. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.reauthorize_payment(
                authorization_id,
                pay_pal_request_id=pay_pal_request_id,
                prefer=prefer,
                pay_pal_auth_assertion=pay_pal_auth_assertion,
                body=body,
                request_options=request_options,
            )
        ).unwrap()

    async def refund_captured_payment(
        self,
        capture_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_auth_assertion: str | None = None,
        body: RefundRequest | RefundRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Refund:
        """Refunds a captured payment, by ID. For a full refund, include an empty payload in the JSON request body. For
        a partial refund, include an amount object in the JSON request body.

        Args:
            capture_id: The PayPal-generated ID for the captured payment to refund.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_request_id: The server stores keys for 45 days.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP 200 OK status code and a JSON response body that shows refund details.

        Raises:
            ApiError: The request failed because it is not well-formed or is syntactically incorrect or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials. The
                request failed because the caller has insufficient permissions. The request failed because the resource
                does not exist. The request failed because a previous call for the given resource is in progress. The
                request failed because it either is semantically incorrect or failed business validation. The request
                failed because an internal server error occurred. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.refund_captured_payment(
                capture_id,
                pay_pal_mock_response=pay_pal_mock_response,
                pay_pal_request_id=pay_pal_request_id,
                prefer=prefer,
                pay_pal_auth_assertion=pay_pal_auth_assertion,
                body=body,
                request_options=request_options,
            )
        ).unwrap()

    async def void_payment(
        self,
        authorization_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentAuthorization:
        """Voids, or cancels, an authorized payment, by ID. You cannot void an authorized payment that has been fully
        captured.

        Args:
            authorization_id: The PayPal-generated ID for the authorized payment to void.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            pay_pal_request_id: The server stores keys for 45 days.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP 200 OK status code and a JSON response body that shows authorization
            details. This response is returned when the Prefer header is set to return=representation.

        Raises:
            ApiError: Authentication failed due to missing authorization header, or invalid authentication credentials.
                The request failed because the caller has insufficient permissions. The request failed because the
                resource does not exist. The request failed because a previous call for the given resource is in
                progress. The request failed because it either is semantically incorrect or failed business validation.
                The request failed because an internal server error occurred. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.void_payment(
                authorization_id,
                pay_pal_mock_response=pay_pal_mock_response,
                pay_pal_auth_assertion=pay_pal_auth_assertion,
                pay_pal_request_id=pay_pal_request_id,
                prefer=prefer,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPaymentsWithRawResponse:
        return self._with_raw_response


class PaymentsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def capture_authorized_payment(
        self,
        authorization_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_auth_assertion: str | None = None,
        body: CaptureRequest | CaptureRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CapturedPayment, CaptureAuthorizedPaymentErrorBody]:
        """Captures an authorized payment, by ID.

        Args:
            authorization_id: The PayPal-generated ID for the authorized payment to capture.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_request_id: The server stores keys for 45 days.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/payments/authorizations/{authorization_id}/capture"),
            path_params=[param[str]("authorization_id", authorization_id)],
            headers=[
                param[str | None]("PayPal-Mock-Response", pay_pal_mock_response),
                param[str | None]("PayPal-Request-Id", pay_pal_request_id),
                param[str | None]("Prefer", prefer),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[CaptureRequest | CaptureRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CapturedPayment],
            error_mapper=capture_authorized_payment_error_mapper,
            request_options=request_options,
        )

    def get_authorized_payment(
        self,
        authorization_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentAuthorization, GetAuthorizedPaymentErrorBody]:
        """Shows details for an authorized payment, by ID.

        Args:
            authorization_id: The ID of the authorized payment for which to show details.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/payments/authorizations/{authorization_id}"),
            path_params=[param[str]("authorization_id", authorization_id)],
            headers=[
                param[str | None]("PayPal-Mock-Response", pay_pal_mock_response),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[PaymentAuthorization],
            error_mapper=get_authorized_payment_error_mapper,
            request_options=request_options,
        )

    def get_captured_payment(
        self,
        capture_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CapturedPayment, GetCapturedPaymentErrorBody]:
        """Shows details for a captured payment, by ID.

        Args:
            capture_id: The PayPal-generated ID for the captured payment for which to show details.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/payments/captures/{capture_id}"),
            path_params=[param[str]("capture_id", capture_id)],
            headers=[param[str | None]("PayPal-Mock-Response", pay_pal_mock_response)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CapturedPayment],
            error_mapper=get_captured_payment_error_mapper,
            request_options=request_options,
        )

    def get_refund(
        self,
        refund_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Refund, GetRefundErrorBody]:
        """Shows details for a refund, by ID.

        Args:
            refund_id: The PayPal-generated ID for the refund for which to show details.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/payments/refunds/{refund_id}"),
            path_params=[param[str]("refund_id", refund_id)],
            headers=[
                param[str | None]("PayPal-Mock-Response", pay_pal_mock_response),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[Refund],
            error_mapper=get_refund_error_mapper,
            request_options=request_options,
        )

    def reauthorize_payment(
        self,
        authorization_id: str,
        *,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_auth_assertion: str | None = None,
        body: ReauthorizeRequest | ReauthorizeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentAuthorization, ReauthorizePaymentErrorBody]:
        """Reauthorizes an authorized PayPal account payment, by ID. To ensure that funds are still available,
        reauthorize a payment after its initial three-day honor period expires. Within the 29-day authorization period,
        you can issue multiple re-authorizations after the honor period expires. If 30 days have transpired since the
        date of the original authorization, you must create an authorized payment instead of reauthorizing the original
        authorized payment. A reauthorized payment itself has a new honor period of three days. You can reauthorize an
        authorized payment from 4 to 29 days after the 3-day honor period. The allowed amount depends on context and
        geography, for example in US it is up to 115% of the original authorized amount, not to exceed an increase of
        $75 USD. Supports only the ``amount`` request parameter.

        Args:
            authorization_id: The PayPal-generated ID for the authorized payment to reauthorize.
            pay_pal_request_id: The server stores keys for 45 days.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/payments/authorizations/{authorization_id}/reauthorize"),
            path_params=[param[str]("authorization_id", authorization_id)],
            headers=[
                param[str | None]("PayPal-Request-Id", pay_pal_request_id),
                param[str | None]("Prefer", prefer),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[ReauthorizeRequest | ReauthorizeRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[PaymentAuthorization],
            error_mapper=reauthorize_payment_error_mapper,
            request_options=request_options,
        )

    def refund_captured_payment(
        self,
        capture_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_auth_assertion: str | None = None,
        body: RefundRequest | RefundRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Refund, RefundCapturedPaymentErrorBody]:
        """Refunds a captured payment, by ID. For a full refund, include an empty payload in the JSON request body. For
        a partial refund, include an amount object in the JSON request body.

        Args:
            capture_id: The PayPal-generated ID for the captured payment to refund.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_request_id: The server stores keys for 45 days.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/payments/captures/{capture_id}/refund"),
            path_params=[param[str]("capture_id", capture_id)],
            headers=[
                param[str | None]("PayPal-Mock-Response", pay_pal_mock_response),
                param[str | None]("PayPal-Request-Id", pay_pal_request_id),
                param[str | None]("Prefer", prefer),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[RefundRequest | RefundRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[Refund],
            error_mapper=refund_captured_payment_error_mapper,
            request_options=request_options,
        )

    def void_payment(
        self,
        authorization_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentAuthorization, VoidPaymentErrorBody]:
        """Voids, or cancels, an authorized payment, by ID. You cannot void an authorized payment that has been fully
        captured.

        Args:
            authorization_id: The PayPal-generated ID for the authorized payment to void.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            pay_pal_request_id: The server stores keys for 45 days.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/payments/authorizations/{authorization_id}/void"),
            path_params=[param[str]("authorization_id", authorization_id)],
            headers=[
                param[str | None]("PayPal-Mock-Response", pay_pal_mock_response),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
                param[str | None]("PayPal-Request-Id", pay_pal_request_id),
                param[str | None]("Prefer", prefer),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[PaymentAuthorization],
            error_mapper=void_payment_error_mapper,
            request_options=request_options,
        )


class AsyncPaymentsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def capture_authorized_payment(
        self,
        authorization_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_auth_assertion: str | None = None,
        body: CaptureRequest | CaptureRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CapturedPayment, CaptureAuthorizedPaymentErrorBody]:
        """Captures an authorized payment, by ID.

        Args:
            authorization_id: The PayPal-generated ID for the authorized payment to capture.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_request_id: The server stores keys for 45 days.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/payments/authorizations/{authorization_id}/capture"),
            path_params=[param[str]("authorization_id", authorization_id)],
            headers=[
                param[str | None]("PayPal-Mock-Response", pay_pal_mock_response),
                param[str | None]("PayPal-Request-Id", pay_pal_request_id),
                param[str | None]("Prefer", prefer),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[CaptureRequest | CaptureRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CapturedPayment],
            error_mapper=capture_authorized_payment_error_mapper,
            request_options=request_options,
        )

    async def get_authorized_payment(
        self,
        authorization_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentAuthorization, GetAuthorizedPaymentErrorBody]:
        """Shows details for an authorized payment, by ID.

        Args:
            authorization_id: The ID of the authorized payment for which to show details.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/payments/authorizations/{authorization_id}"),
            path_params=[param[str]("authorization_id", authorization_id)],
            headers=[
                param[str | None]("PayPal-Mock-Response", pay_pal_mock_response),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[PaymentAuthorization],
            error_mapper=get_authorized_payment_error_mapper,
            request_options=request_options,
        )

    async def get_captured_payment(
        self,
        capture_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CapturedPayment, GetCapturedPaymentErrorBody]:
        """Shows details for a captured payment, by ID.

        Args:
            capture_id: The PayPal-generated ID for the captured payment for which to show details.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/payments/captures/{capture_id}"),
            path_params=[param[str]("capture_id", capture_id)],
            headers=[param[str | None]("PayPal-Mock-Response", pay_pal_mock_response)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CapturedPayment],
            error_mapper=get_captured_payment_error_mapper,
            request_options=request_options,
        )

    async def get_refund(
        self,
        refund_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Refund, GetRefundErrorBody]:
        """Shows details for a refund, by ID.

        Args:
            refund_id: The PayPal-generated ID for the refund for which to show details.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/payments/refunds/{refund_id}"),
            path_params=[param[str]("refund_id", refund_id)],
            headers=[
                param[str | None]("PayPal-Mock-Response", pay_pal_mock_response),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[Refund],
            error_mapper=get_refund_error_mapper,
            request_options=request_options,
        )

    async def reauthorize_payment(
        self,
        authorization_id: str,
        *,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_auth_assertion: str | None = None,
        body: ReauthorizeRequest | ReauthorizeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentAuthorization, ReauthorizePaymentErrorBody]:
        """Reauthorizes an authorized PayPal account payment, by ID. To ensure that funds are still available,
        reauthorize a payment after its initial three-day honor period expires. Within the 29-day authorization period,
        you can issue multiple re-authorizations after the honor period expires. If 30 days have transpired since the
        date of the original authorization, you must create an authorized payment instead of reauthorizing the original
        authorized payment. A reauthorized payment itself has a new honor period of three days. You can reauthorize an
        authorized payment from 4 to 29 days after the 3-day honor period. The allowed amount depends on context and
        geography, for example in US it is up to 115% of the original authorized amount, not to exceed an increase of
        $75 USD. Supports only the ``amount`` request parameter.

        Args:
            authorization_id: The PayPal-generated ID for the authorized payment to reauthorize.
            pay_pal_request_id: The server stores keys for 45 days.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/payments/authorizations/{authorization_id}/reauthorize"),
            path_params=[param[str]("authorization_id", authorization_id)],
            headers=[
                param[str | None]("PayPal-Request-Id", pay_pal_request_id),
                param[str | None]("Prefer", prefer),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[ReauthorizeRequest | ReauthorizeRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[PaymentAuthorization],
            error_mapper=reauthorize_payment_error_mapper,
            request_options=request_options,
        )

    async def refund_captured_payment(
        self,
        capture_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_auth_assertion: str | None = None,
        body: RefundRequest | RefundRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Refund, RefundCapturedPaymentErrorBody]:
        """Refunds a captured payment, by ID. For a full refund, include an empty payload in the JSON request body. For
        a partial refund, include an amount object in the JSON request body.

        Args:
            capture_id: The PayPal-generated ID for the captured payment to refund.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_request_id: The server stores keys for 45 days.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/payments/captures/{capture_id}/refund"),
            path_params=[param[str]("capture_id", capture_id)],
            headers=[
                param[str | None]("PayPal-Mock-Response", pay_pal_mock_response),
                param[str | None]("PayPal-Request-Id", pay_pal_request_id),
                param[str | None]("Prefer", prefer),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[RefundRequest | RefundRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[Refund],
            error_mapper=refund_captured_payment_error_mapper,
            request_options=request_options,
        )

    async def void_payment(
        self,
        authorization_id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentAuthorization, VoidPaymentErrorBody]:
        """Voids, or cancels, an authorized payment, by ID. You cannot void an authorized payment that has been fully
        captured.

        Args:
            authorization_id: The PayPal-generated ID for the authorized payment to void.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see `PayPal-Auth-Assertion </docs/api/reference/api-requests/#paypal-auth-assertion>`__.
                Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant,
                the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token
                with target_subject.
            pay_pal_request_id: The server stores keys for 45 days.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/payments/authorizations/{authorization_id}/void"),
            path_params=[param[str]("authorization_id", authorization_id)],
            headers=[
                param[str | None]("PayPal-Mock-Response", pay_pal_mock_response),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
                param[str | None]("PayPal-Request-Id", pay_pal_request_id),
                param[str | None]("Prefer", prefer),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[PaymentAuthorization],
            error_mapper=void_payment_error_mapper,
            request_options=request_options,
        )
