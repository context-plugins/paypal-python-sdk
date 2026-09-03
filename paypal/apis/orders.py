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
from ..errors.authorize_order_error import AuthorizeOrderErrorBody, authorize_order_error_mapper
from ..errors.capture_order_error import CaptureOrderErrorBody, capture_order_error_mapper
from ..errors.confirm_order_error import ConfirmOrderErrorBody, confirm_order_error_mapper
from ..errors.create_order_error import CreateOrderErrorBody, create_order_error_mapper
from ..errors.create_order_tracking_error import CreateOrderTrackingErrorBody, create_order_tracking_error_mapper
from ..errors.get_order_error import GetOrderErrorBody, get_order_error_mapper
from ..errors.patch_order_error import PatchOrderErrorBody, patch_order_error_mapper
from ..errors.update_order_tracking_error import UpdateOrderTrackingErrorBody, update_order_tracking_error_mapper
from ..models.confirm_order_request import ConfirmOrderRequest, ConfirmOrderRequestDict
from ..models.order import Order
from ..models.order_authorize_request import OrderAuthorizeRequest, OrderAuthorizeRequestDict
from ..models.order_authorize_response import OrderAuthorizeResponse
from ..models.order_capture_request import OrderCaptureRequest, OrderCaptureRequestDict
from ..models.order_request import OrderRequest, OrderRequestDict
from ..models.order_tracker_request import OrderTrackerRequest, OrderTrackerRequestDict
from ..models.patch import Patch, PatchDict
from ..server.server import Server


class Orders:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = OrdersWithRawResponse(client, server, auth)

    def authorize_order(
        self,
        id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_client_metadata_id: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        body: OrderAuthorizeRequest | OrderAuthorizeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OrderAuthorizeResponse:
        """Authorizes payment for an order. To successfully authorize payment for an order, the buyer must first approve
        the order or a valid payment_source must be provided in the request. A buyer can approve the order upon being
        redirected to the rel:approve URL that was returned in the HATEOAS links in the create order response. Note: For
        error handling and troubleshooting, see Orders v2 errors.

        Args:
            id: The ID of the order for which to authorize.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_request_id: The server stores keys for 6 hours. The API callers can request the times to up to 72
                hours by speaking to their Account Manager. It is mandatory for all single-step create order calls (E.g.
                Create Order Request with payment source information like Card, PayPal.vault_id,
                PayPal.billing_agreement_id, etc).
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_client_metadata_id: Value sent with the request.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful response to an idempotent request returns the HTTP ``200 OK`` status code with a JSON response
            body that shows authorized payment details.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authentication failed due
                to missing authorization header, or invalid authentication credentials. The authorized payment failed
                due to insufficient permissions. The specified resource does not exist. The requested action could not
                be performed, semantically incorrect, or failed business validation. An internal server error has
                occurred. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.authorize_order(
            id,
            pay_pal_mock_response=pay_pal_mock_response,
            pay_pal_request_id=pay_pal_request_id,
            prefer=prefer,
            pay_pal_client_metadata_id=pay_pal_client_metadata_id,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
            body=body,
            request_options=request_options,
        ).unwrap()

    def capture_order(
        self,
        id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_client_metadata_id: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        body: OrderCaptureRequest | OrderCaptureRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Order:
        """Captures payment for an order. To successfully capture payment for an order, the buyer must first approve the
        order or a valid payment_source must be provided in the request. A buyer can approve the order upon being
        redirected to the rel:approve URL that was returned in the HATEOAS links in the create order response. Note: For
        error handling and troubleshooting, see Orders v2 errors.

        Args:
            id: The ID of the order for which to capture a payment.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_request_id: The server stores keys for 6 hours. The API callers can request the times to up to 72
                hours by speaking to their Account Manager. It is mandatory for all single-step create order calls (E.g.
                Create Order Request with payment source information like Card, PayPal.vault_id,
                PayPal.billing_agreement_id, etc).
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_client_metadata_id: Value sent with the request.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful response to an idempotent request returns the HTTP ``200 OK`` status code with a JSON response
            body that shows captured payment details.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authentication failed due
                to missing authorization header, or invalid authentication credentials. The authorized payment failed
                due to insufficient permissions. The specified resource does not exist. The requested action could not
                be performed, semantically incorrect, or failed business validation. An internal server error has
                occurred. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.capture_order(
            id,
            pay_pal_mock_response=pay_pal_mock_response,
            pay_pal_request_id=pay_pal_request_id,
            prefer=prefer,
            pay_pal_client_metadata_id=pay_pal_client_metadata_id,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
            body=body,
            request_options=request_options,
        ).unwrap()

    def confirm_order(
        self,
        id: str,
        *,
        pay_pal_client_metadata_id: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        prefer: str | None = "return=minimal",
        body: ConfirmOrderRequest | ConfirmOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Order:
        """Payer confirms their intent to pay for the the Order with the given payment source.

        Args:
            id: The ID of the order for which the payer confirms their intent to pay.
            pay_pal_client_metadata_id: Value sent with the request.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request indicates that the payment source was added to the Order. A successful request returns
            the HTTP ``200 OK`` status code with a JSON response body that shows order details.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authorization failed due
                to insufficient permissions. The requested action could not be performed, semantically incorrect, or
                failed business validation. An internal server error has occurred. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.confirm_order(
            id,
            pay_pal_client_metadata_id=pay_pal_client_metadata_id,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
            prefer=prefer,
            body=body,
            request_options=request_options,
        ).unwrap()

    def create_order(
        self,
        body: OrderRequest | OrderRequestDict,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_request_id: str | None = None,
        pay_pal_partner_attribution_id: str | None = None,
        pay_pal_client_metadata_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_auth_assertion: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Order:
        """Creates an order. Merchants and partners can add Level 2 and 3 data to payments to reduce risk and payment
        processing costs. For more information about processing payments, see checkout or multiparty checkout. Note: For
        error handling and troubleshooting, see Orders v2 errors.

        Args:
            body: The request body.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_request_id: The server stores keys for 6 hours. The API callers can request the times to up to 72
                hours by speaking to their Account Manager. It is mandatory for all single-step create order calls (E.g.
                Create Order Request with payment source information like Card, PayPal.vault_id,
                PayPal.billing_agreement_id, etc).
            pay_pal_partner_attribution_id: Value sent with the request.
            pay_pal_client_metadata_id: Value sent with the request.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful response to an idempotent request returns the HTTP ``200 OK`` status code with a JSON response
            body that shows order details.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authentication failed due
                to missing authorization header, or invalid authentication credentials. The requested action could not
                be performed, semantically incorrect, or failed business validation. ``error`` is ``Error |
                RawError``."""
        return self._with_raw_response.create_order(
            body,
            pay_pal_mock_response=pay_pal_mock_response,
            pay_pal_request_id=pay_pal_request_id,
            pay_pal_partner_attribution_id=pay_pal_partner_attribution_id,
            pay_pal_client_metadata_id=pay_pal_client_metadata_id,
            prefer=prefer,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
            request_options=request_options,
        ).unwrap()

    def create_order_tracking(
        self,
        id: str,
        body: OrderTrackerRequest | OrderTrackerRequestDict,
        *,
        pay_pal_auth_assertion: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Order:
        """Adds tracking information for an Order.

        Args:
            id: The ID of the order that the tracking information is associated with.
            body: The request body.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful response to an idempotent request returns the HTTP ``200 OK`` status code with a JSON response
            body that shows tracker details.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authorization failed due
                to insufficient permissions. The specified resource does not exist. The requested action could not be
                performed, semantically incorrect, or failed business validation. An internal server error has occurred.
                ``error`` is ``Error | RawError``."""
        return self._with_raw_response.create_order_tracking(
            id, body, pay_pal_auth_assertion=pay_pal_auth_assertion, request_options=request_options
        ).unwrap()

    def get_order(
        self,
        id: str,
        *,
        fields: str | None = None,
        pay_pal_mock_response: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Order:
        """Shows details for an order, by ID. Note: For error handling and troubleshooting, see Orders v2 errors.

        Args:
            id: The ID of the order for which to show details.
            fields: A comma-separated list of fields that should be returned for the order. Valid filter field is
                ``payment_source``.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that shows order
            details.

        Raises:
            ApiError: Authentication failed due to missing authorization header, or invalid authentication credentials.
                The specified resource does not exist. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_order(
            id,
            fields=fields,
            pay_pal_mock_response=pay_pal_mock_response,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
            request_options=request_options,
        ).unwrap()

    def patch_order(
        self,
        id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        body: list[Patch | PatchDict] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        r"""Updates an order with a ``CREATED`` or ``APPROVED`` status. You cannot update an order with the
        ``COMPLETED`` status.<br/><br/>To make an update, you must provide a ``reference_id``. If you omit this value
        with an order that contains only one purchase unit, PayPal sets the value to ``default`` which enables you to
        use the path: <code>\"/purchase_units/@reference_id=='default'/{attribute-or-object}\"</code>. Merchants and
        partners can add Level 2 and 3 data to payments to reduce risk and payment processing costs. For more
        information about processing payments, see <a
        href="https://developer.paypal.com/docs/checkout/advanced/processing/">checkout</a> or <a
        href="https://developer.paypal.com/docs/multiparty/checkout/advanced/processing/">multiparty
        checkout</a>.<blockquote><strong>Note:</strong> For error handling and troubleshooting, see <a
        href="https://developer.paypal.com/api/rest/reference/orders/v2/errors/#patch-order">Orders v2
        errors</a>.</blockquote>Patchable attributes or
        objects:<br/><br/><table><thead><th>Attribute</th><th>Op</th><th>Notes</th></thead><tbody><tr><td><code>intent</code></td><td>replace</td><td></td></tr><tr><td><code>payer</code></td><td>replace,
        add</td><td>Using replace op for <code>payer</code> will replace the whole <code>payer</code> object with the
        value sent in request.</td></tr><tr><td><code>purchase_units</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].custom_id</code></td><td>replace, add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].description</code></td><td>replace, add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].payee.email</code></td><td>replace</td><td></td></tr><tr><td><code>purchase_units[].shipping.name</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.email_address</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.phone_number</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.options</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.address</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.type</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].soft_descriptor</code></td><td>replace,
        remove</td><td></td></tr><tr><td><code>purchase_units[].amount</code></td><td>replace</td><td></td></tr><tr><td><code>purchase_units[].items</code></td><td>replace,
        add, remove</td><td></td></tr><tr><td><code>purchase_units[].invoice_id</code></td><td>replace, add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].payment_instruction</code></td><td>replace</td><td></td></tr><tr><td><code>purchase_units[].payment_instruction.disbursement_mode</code></td><td>replace</td><td>By
        default, <code>disbursement_mode</code> is
        <code>INSTANT</code>.</td></tr><tr><td><code>purchase_units[].payment_instruction.payee_receivable_fx_rate_id</code></td><td>replace,
        add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].payment_instruction.platform_fees</code></td><td>replace,
        add, remove</td><td></td></tr><tr><td><code>purchase_units[].supplementary_data.airline</code></td><td>replace,
        add, remove</td><td></td></tr><tr><td><code>purchase_units[].supplementary_data.card</code></td><td>replace,
        add, remove</td><td></td></tr><tr><td><code>application_context.client_configuration</code></td><td>replace,
        add</td><td></td></tr></tbody></table>

        Args:
            id: The ID of the order to update.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``204 No Content`` status code with an empty object in the JSON
            response body.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authentication failed due
                to missing authorization header, or invalid authentication credentials. The specified resource does not
                exist. The requested action could not be performed, semantically incorrect, or failed business
                validation. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.patch_order(
            id,
            pay_pal_mock_response=pay_pal_mock_response,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
            body=body,
            request_options=request_options,
        ).unwrap()

    def update_order_tracking(
        self,
        id: str,
        tracker_id: str,
        *,
        pay_pal_auth_assertion: str | None = None,
        body: list[Patch | PatchDict] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Updates or cancels the tracking information for a PayPal order, by ID. Updatable attributes or objects:
        Attribute Op Notes items replace Using replace op for items will replace the entire items object with the value
        sent in request. notify_payer replace, add status replace Only patching status to CANCELLED is currently
        supported.

        Args:
            id: The ID of the order that the tracking information is associated with.
            tracker_id: The order tracking ID.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``204 No Content`` status code with an empty object in the JSON
            response body.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authorization failed due
                to insufficient permissions. The specified resource does not exist. The requested action could not be
                performed, semantically incorrect, or failed business validation. An internal server error has occurred.
                ``error`` is ``Error | RawError``."""
        return self._with_raw_response.update_order_tracking(
            id, tracker_id, pay_pal_auth_assertion=pay_pal_auth_assertion, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> OrdersWithRawResponse:
        return self._with_raw_response


class AsyncOrders:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncOrdersWithRawResponse(client, server, auth)

    async def authorize_order(
        self,
        id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_client_metadata_id: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        body: OrderAuthorizeRequest | OrderAuthorizeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OrderAuthorizeResponse:
        """Authorizes payment for an order. To successfully authorize payment for an order, the buyer must first approve
        the order or a valid payment_source must be provided in the request. A buyer can approve the order upon being
        redirected to the rel:approve URL that was returned in the HATEOAS links in the create order response. Note: For
        error handling and troubleshooting, see Orders v2 errors.

        Args:
            id: The ID of the order for which to authorize.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_request_id: The server stores keys for 6 hours. The API callers can request the times to up to 72
                hours by speaking to their Account Manager. It is mandatory for all single-step create order calls (E.g.
                Create Order Request with payment source information like Card, PayPal.vault_id,
                PayPal.billing_agreement_id, etc).
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_client_metadata_id: Value sent with the request.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful response to an idempotent request returns the HTTP ``200 OK`` status code with a JSON response
            body that shows authorized payment details.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authentication failed due
                to missing authorization header, or invalid authentication credentials. The authorized payment failed
                due to insufficient permissions. The specified resource does not exist. The requested action could not
                be performed, semantically incorrect, or failed business validation. An internal server error has
                occurred. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.authorize_order(
                id,
                pay_pal_mock_response=pay_pal_mock_response,
                pay_pal_request_id=pay_pal_request_id,
                prefer=prefer,
                pay_pal_client_metadata_id=pay_pal_client_metadata_id,
                pay_pal_auth_assertion=pay_pal_auth_assertion,
                body=body,
                request_options=request_options,
            )
        ).unwrap()

    async def capture_order(
        self,
        id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_client_metadata_id: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        body: OrderCaptureRequest | OrderCaptureRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Order:
        """Captures payment for an order. To successfully capture payment for an order, the buyer must first approve the
        order or a valid payment_source must be provided in the request. A buyer can approve the order upon being
        redirected to the rel:approve URL that was returned in the HATEOAS links in the create order response. Note: For
        error handling and troubleshooting, see Orders v2 errors.

        Args:
            id: The ID of the order for which to capture a payment.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_request_id: The server stores keys for 6 hours. The API callers can request the times to up to 72
                hours by speaking to their Account Manager. It is mandatory for all single-step create order calls (E.g.
                Create Order Request with payment source information like Card, PayPal.vault_id,
                PayPal.billing_agreement_id, etc).
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_client_metadata_id: Value sent with the request.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful response to an idempotent request returns the HTTP ``200 OK`` status code with a JSON response
            body that shows captured payment details.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authentication failed due
                to missing authorization header, or invalid authentication credentials. The authorized payment failed
                due to insufficient permissions. The specified resource does not exist. The requested action could not
                be performed, semantically incorrect, or failed business validation. An internal server error has
                occurred. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.capture_order(
                id,
                pay_pal_mock_response=pay_pal_mock_response,
                pay_pal_request_id=pay_pal_request_id,
                prefer=prefer,
                pay_pal_client_metadata_id=pay_pal_client_metadata_id,
                pay_pal_auth_assertion=pay_pal_auth_assertion,
                body=body,
                request_options=request_options,
            )
        ).unwrap()

    async def confirm_order(
        self,
        id: str,
        *,
        pay_pal_client_metadata_id: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        prefer: str | None = "return=minimal",
        body: ConfirmOrderRequest | ConfirmOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Order:
        """Payer confirms their intent to pay for the the Order with the given payment source.

        Args:
            id: The ID of the order for which the payer confirms their intent to pay.
            pay_pal_client_metadata_id: Value sent with the request.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request indicates that the payment source was added to the Order. A successful request returns
            the HTTP ``200 OK`` status code with a JSON response body that shows order details.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authorization failed due
                to insufficient permissions. The requested action could not be performed, semantically incorrect, or
                failed business validation. An internal server error has occurred. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.confirm_order(
                id,
                pay_pal_client_metadata_id=pay_pal_client_metadata_id,
                pay_pal_auth_assertion=pay_pal_auth_assertion,
                prefer=prefer,
                body=body,
                request_options=request_options,
            )
        ).unwrap()

    async def create_order(
        self,
        body: OrderRequest | OrderRequestDict,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_request_id: str | None = None,
        pay_pal_partner_attribution_id: str | None = None,
        pay_pal_client_metadata_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_auth_assertion: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Order:
        """Creates an order. Merchants and partners can add Level 2 and 3 data to payments to reduce risk and payment
        processing costs. For more information about processing payments, see checkout or multiparty checkout. Note: For
        error handling and troubleshooting, see Orders v2 errors.

        Args:
            body: The request body.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_request_id: The server stores keys for 6 hours. The API callers can request the times to up to 72
                hours by speaking to their Account Manager. It is mandatory for all single-step create order calls (E.g.
                Create Order Request with payment source information like Card, PayPal.vault_id,
                PayPal.billing_agreement_id, etc).
            pay_pal_partner_attribution_id: Value sent with the request.
            pay_pal_client_metadata_id: Value sent with the request.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful response to an idempotent request returns the HTTP ``200 OK`` status code with a JSON response
            body that shows order details.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authentication failed due
                to missing authorization header, or invalid authentication credentials. The requested action could not
                be performed, semantically incorrect, or failed business validation. ``error`` is ``Error |
                RawError``."""
        return (
            await self._with_raw_response.create_order(
                body,
                pay_pal_mock_response=pay_pal_mock_response,
                pay_pal_request_id=pay_pal_request_id,
                pay_pal_partner_attribution_id=pay_pal_partner_attribution_id,
                pay_pal_client_metadata_id=pay_pal_client_metadata_id,
                prefer=prefer,
                pay_pal_auth_assertion=pay_pal_auth_assertion,
                request_options=request_options,
            )
        ).unwrap()

    async def create_order_tracking(
        self,
        id: str,
        body: OrderTrackerRequest | OrderTrackerRequestDict,
        *,
        pay_pal_auth_assertion: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Order:
        """Adds tracking information for an Order.

        Args:
            id: The ID of the order that the tracking information is associated with.
            body: The request body.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful response to an idempotent request returns the HTTP ``200 OK`` status code with a JSON response
            body that shows tracker details.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authorization failed due
                to insufficient permissions. The specified resource does not exist. The requested action could not be
                performed, semantically incorrect, or failed business validation. An internal server error has occurred.
                ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.create_order_tracking(
                id, body, pay_pal_auth_assertion=pay_pal_auth_assertion, request_options=request_options
            )
        ).unwrap()

    async def get_order(
        self,
        id: str,
        *,
        fields: str | None = None,
        pay_pal_mock_response: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Order:
        """Shows details for an order, by ID. Note: For error handling and troubleshooting, see Orders v2 errors.

        Args:
            id: The ID of the order for which to show details.
            fields: A comma-separated list of fields that should be returned for the order. Valid filter field is
                ``payment_source``.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that shows order
            details.

        Raises:
            ApiError: Authentication failed due to missing authorization header, or invalid authentication credentials.
                The specified resource does not exist. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.get_order(
                id,
                fields=fields,
                pay_pal_mock_response=pay_pal_mock_response,
                pay_pal_auth_assertion=pay_pal_auth_assertion,
                request_options=request_options,
            )
        ).unwrap()

    async def patch_order(
        self,
        id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        body: list[Patch | PatchDict] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        r"""Updates an order with a ``CREATED`` or ``APPROVED`` status. You cannot update an order with the
        ``COMPLETED`` status.<br/><br/>To make an update, you must provide a ``reference_id``. If you omit this value
        with an order that contains only one purchase unit, PayPal sets the value to ``default`` which enables you to
        use the path: <code>\"/purchase_units/@reference_id=='default'/{attribute-or-object}\"</code>. Merchants and
        partners can add Level 2 and 3 data to payments to reduce risk and payment processing costs. For more
        information about processing payments, see <a
        href="https://developer.paypal.com/docs/checkout/advanced/processing/">checkout</a> or <a
        href="https://developer.paypal.com/docs/multiparty/checkout/advanced/processing/">multiparty
        checkout</a>.<blockquote><strong>Note:</strong> For error handling and troubleshooting, see <a
        href="https://developer.paypal.com/api/rest/reference/orders/v2/errors/#patch-order">Orders v2
        errors</a>.</blockquote>Patchable attributes or
        objects:<br/><br/><table><thead><th>Attribute</th><th>Op</th><th>Notes</th></thead><tbody><tr><td><code>intent</code></td><td>replace</td><td></td></tr><tr><td><code>payer</code></td><td>replace,
        add</td><td>Using replace op for <code>payer</code> will replace the whole <code>payer</code> object with the
        value sent in request.</td></tr><tr><td><code>purchase_units</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].custom_id</code></td><td>replace, add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].description</code></td><td>replace, add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].payee.email</code></td><td>replace</td><td></td></tr><tr><td><code>purchase_units[].shipping.name</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.email_address</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.phone_number</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.options</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.address</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.type</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].soft_descriptor</code></td><td>replace,
        remove</td><td></td></tr><tr><td><code>purchase_units[].amount</code></td><td>replace</td><td></td></tr><tr><td><code>purchase_units[].items</code></td><td>replace,
        add, remove</td><td></td></tr><tr><td><code>purchase_units[].invoice_id</code></td><td>replace, add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].payment_instruction</code></td><td>replace</td><td></td></tr><tr><td><code>purchase_units[].payment_instruction.disbursement_mode</code></td><td>replace</td><td>By
        default, <code>disbursement_mode</code> is
        <code>INSTANT</code>.</td></tr><tr><td><code>purchase_units[].payment_instruction.payee_receivable_fx_rate_id</code></td><td>replace,
        add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].payment_instruction.platform_fees</code></td><td>replace,
        add, remove</td><td></td></tr><tr><td><code>purchase_units[].supplementary_data.airline</code></td><td>replace,
        add, remove</td><td></td></tr><tr><td><code>purchase_units[].supplementary_data.card</code></td><td>replace,
        add, remove</td><td></td></tr><tr><td><code>application_context.client_configuration</code></td><td>replace,
        add</td><td></td></tr></tbody></table>

        Args:
            id: The ID of the order to update.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``204 No Content`` status code with an empty object in the JSON
            response body.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authentication failed due
                to missing authorization header, or invalid authentication credentials. The specified resource does not
                exist. The requested action could not be performed, semantically incorrect, or failed business
                validation. ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.patch_order(
                id,
                pay_pal_mock_response=pay_pal_mock_response,
                pay_pal_auth_assertion=pay_pal_auth_assertion,
                body=body,
                request_options=request_options,
            )
        ).unwrap()

    async def update_order_tracking(
        self,
        id: str,
        tracker_id: str,
        *,
        pay_pal_auth_assertion: str | None = None,
        body: list[Patch | PatchDict] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Updates or cancels the tracking information for a PayPal order, by ID. Updatable attributes or objects:
        Attribute Op Notes items replace Using replace op for items will replace the entire items object with the value
        sent in request. notify_payer replace, add status replace Only patching status to CANCELLED is currently
        supported.

        Args:
            id: The ID of the order that the tracking information is associated with.
            tracker_id: The order tracking ID.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``204 No Content`` status code with an empty object in the JSON
            response body.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authorization failed due
                to insufficient permissions. The specified resource does not exist. The requested action could not be
                performed, semantically incorrect, or failed business validation. An internal server error has occurred.
                ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.update_order_tracking(
                id,
                tracker_id,
                pay_pal_auth_assertion=pay_pal_auth_assertion,
                body=body,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncOrdersWithRawResponse:
        return self._with_raw_response


class OrdersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def authorize_order(
        self,
        id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_client_metadata_id: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        body: OrderAuthorizeRequest | OrderAuthorizeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OrderAuthorizeResponse, AuthorizeOrderErrorBody]:
        """Authorizes payment for an order. To successfully authorize payment for an order, the buyer must first approve
        the order or a valid payment_source must be provided in the request. A buyer can approve the order upon being
        redirected to the rel:approve URL that was returned in the HATEOAS links in the create order response. Note: For
        error handling and troubleshooting, see Orders v2 errors.

        Args:
            id: The ID of the order for which to authorize.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_request_id: The server stores keys for 6 hours. The API callers can request the times to up to 72
                hours by speaking to their Account Manager. It is mandatory for all single-step create order calls (E.g.
                Create Order Request with payment source information like Card, PayPal.vault_id,
                PayPal.billing_agreement_id, etc).
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_client_metadata_id: Value sent with the request.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/checkout/orders/{id}/authorize"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str | None]("PayPal-Mock-Response", pay_pal_mock_response),
                param[str | None]("PayPal-Request-Id", pay_pal_request_id),
                param[str | None]("Prefer", prefer),
                param[str | None]("PayPal-Client-Metadata-Id", pay_pal_client_metadata_id),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[OrderAuthorizeRequest | OrderAuthorizeRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[OrderAuthorizeResponse],
            error_mapper=authorize_order_error_mapper,
            request_options=request_options,
        )

    def capture_order(
        self,
        id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_client_metadata_id: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        body: OrderCaptureRequest | OrderCaptureRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Order, CaptureOrderErrorBody]:
        """Captures payment for an order. To successfully capture payment for an order, the buyer must first approve the
        order or a valid payment_source must be provided in the request. A buyer can approve the order upon being
        redirected to the rel:approve URL that was returned in the HATEOAS links in the create order response. Note: For
        error handling and troubleshooting, see Orders v2 errors.

        Args:
            id: The ID of the order for which to capture a payment.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_request_id: The server stores keys for 6 hours. The API callers can request the times to up to 72
                hours by speaking to their Account Manager. It is mandatory for all single-step create order calls (E.g.
                Create Order Request with payment source information like Card, PayPal.vault_id,
                PayPal.billing_agreement_id, etc).
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_client_metadata_id: Value sent with the request.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/checkout/orders/{id}/capture"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str | None]("PayPal-Mock-Response", pay_pal_mock_response),
                param[str | None]("PayPal-Request-Id", pay_pal_request_id),
                param[str | None]("Prefer", prefer),
                param[str | None]("PayPal-Client-Metadata-Id", pay_pal_client_metadata_id),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[OrderCaptureRequest | OrderCaptureRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[Order],
            error_mapper=capture_order_error_mapper,
            request_options=request_options,
        )

    def confirm_order(
        self,
        id: str,
        *,
        pay_pal_client_metadata_id: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        prefer: str | None = "return=minimal",
        body: ConfirmOrderRequest | ConfirmOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Order, ConfirmOrderErrorBody]:
        """Payer confirms their intent to pay for the the Order with the given payment source.

        Args:
            id: The ID of the order for which the payer confirms their intent to pay.
            pay_pal_client_metadata_id: Value sent with the request.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/checkout/orders/{id}/confirm-payment-source"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str | None]("PayPal-Client-Metadata-Id", pay_pal_client_metadata_id),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
                param[str | None]("Prefer", prefer),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[ConfirmOrderRequest | ConfirmOrderRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[Order],
            error_mapper=confirm_order_error_mapper,
            request_options=request_options,
        )

    def create_order(
        self,
        body: OrderRequest | OrderRequestDict,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_request_id: str | None = None,
        pay_pal_partner_attribution_id: str | None = None,
        pay_pal_client_metadata_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_auth_assertion: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Order, CreateOrderErrorBody]:
        """Creates an order. Merchants and partners can add Level 2 and 3 data to payments to reduce risk and payment
        processing costs. For more information about processing payments, see checkout or multiparty checkout. Note: For
        error handling and troubleshooting, see Orders v2 errors.

        Args:
            body: The request body.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_request_id: The server stores keys for 6 hours. The API callers can request the times to up to 72
                hours by speaking to their Account Manager. It is mandatory for all single-step create order calls (E.g.
                Create Order Request with payment source information like Card, PayPal.vault_id,
                PayPal.billing_agreement_id, etc).
            pay_pal_partner_attribution_id: Value sent with the request.
            pay_pal_client_metadata_id: Value sent with the request.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/checkout/orders"),
            headers=[
                param[str | None]("PayPal-Mock-Response", pay_pal_mock_response),
                param[str | None]("PayPal-Request-Id", pay_pal_request_id),
                param[str | None]("PayPal-Partner-Attribution-Id", pay_pal_partner_attribution_id),
                param[str | None]("PayPal-Client-Metadata-Id", pay_pal_client_metadata_id),
                param[str | None]("Prefer", prefer),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[OrderRequest | OrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[Order],
            error_mapper=create_order_error_mapper,
            request_options=request_options,
        )

    def create_order_tracking(
        self,
        id: str,
        body: OrderTrackerRequest | OrderTrackerRequestDict,
        *,
        pay_pal_auth_assertion: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Order, CreateOrderTrackingErrorBody]:
        """Adds tracking information for an Order.

        Args:
            id: The ID of the order that the tracking information is associated with.
            body: The request body.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/checkout/orders/{id}/track"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[OrderTrackerRequest | OrderTrackerRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[Order],
            error_mapper=create_order_tracking_error_mapper,
            request_options=request_options,
        )

    def get_order(
        self,
        id: str,
        *,
        fields: str | None = None,
        pay_pal_mock_response: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Order, GetOrderErrorBody]:
        """Shows details for an order, by ID. Note: For error handling and troubleshooting, see Orders v2 errors.

        Args:
            id: The ID of the order for which to show details.
            fields: A comma-separated list of fields that should be returned for the order. Valid filter field is
                ``payment_source``.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/checkout/orders/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str | None]("fields", fields)],
            headers=[
                param[str | None]("PayPal-Mock-Response", pay_pal_mock_response),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[Order],
            error_mapper=get_order_error_mapper,
            request_options=request_options,
        )

    def patch_order(
        self,
        id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        body: list[Patch | PatchDict] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PatchOrderErrorBody]:
        r"""Updates an order with a ``CREATED`` or ``APPROVED`` status. You cannot update an order with the
        ``COMPLETED`` status.<br/><br/>To make an update, you must provide a ``reference_id``. If you omit this value
        with an order that contains only one purchase unit, PayPal sets the value to ``default`` which enables you to
        use the path: <code>\"/purchase_units/@reference_id=='default'/{attribute-or-object}\"</code>. Merchants and
        partners can add Level 2 and 3 data to payments to reduce risk and payment processing costs. For more
        information about processing payments, see <a
        href="https://developer.paypal.com/docs/checkout/advanced/processing/">checkout</a> or <a
        href="https://developer.paypal.com/docs/multiparty/checkout/advanced/processing/">multiparty
        checkout</a>.<blockquote><strong>Note:</strong> For error handling and troubleshooting, see <a
        href="https://developer.paypal.com/api/rest/reference/orders/v2/errors/#patch-order">Orders v2
        errors</a>.</blockquote>Patchable attributes or
        objects:<br/><br/><table><thead><th>Attribute</th><th>Op</th><th>Notes</th></thead><tbody><tr><td><code>intent</code></td><td>replace</td><td></td></tr><tr><td><code>payer</code></td><td>replace,
        add</td><td>Using replace op for <code>payer</code> will replace the whole <code>payer</code> object with the
        value sent in request.</td></tr><tr><td><code>purchase_units</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].custom_id</code></td><td>replace, add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].description</code></td><td>replace, add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].payee.email</code></td><td>replace</td><td></td></tr><tr><td><code>purchase_units[].shipping.name</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.email_address</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.phone_number</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.options</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.address</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.type</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].soft_descriptor</code></td><td>replace,
        remove</td><td></td></tr><tr><td><code>purchase_units[].amount</code></td><td>replace</td><td></td></tr><tr><td><code>purchase_units[].items</code></td><td>replace,
        add, remove</td><td></td></tr><tr><td><code>purchase_units[].invoice_id</code></td><td>replace, add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].payment_instruction</code></td><td>replace</td><td></td></tr><tr><td><code>purchase_units[].payment_instruction.disbursement_mode</code></td><td>replace</td><td>By
        default, <code>disbursement_mode</code> is
        <code>INSTANT</code>.</td></tr><tr><td><code>purchase_units[].payment_instruction.payee_receivable_fx_rate_id</code></td><td>replace,
        add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].payment_instruction.platform_fees</code></td><td>replace,
        add, remove</td><td></td></tr><tr><td><code>purchase_units[].supplementary_data.airline</code></td><td>replace,
        add, remove</td><td></td></tr><tr><td><code>purchase_units[].supplementary_data.card</code></td><td>replace,
        add, remove</td><td></td></tr><tr><td><code>application_context.client_configuration</code></td><td>replace,
        add</td><td></td></tr></tbody></table>

        Args:
            id: The ID of the order to update.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v2/checkout/orders/{id}"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str | None]("PayPal-Mock-Response", pay_pal_mock_response),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[list[Patch | PatchDict] | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=empty_response,
            error_mapper=patch_order_error_mapper,
            request_options=request_options,
        )

    def update_order_tracking(
        self,
        id: str,
        tracker_id: str,
        *,
        pay_pal_auth_assertion: str | None = None,
        body: list[Patch | PatchDict] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UpdateOrderTrackingErrorBody]:
        """Updates or cancels the tracking information for a PayPal order, by ID. Updatable attributes or objects:
        Attribute Op Notes items replace Using replace op for items will replace the entire items object with the value
        sent in request. notify_payer replace, add status replace Only patching status to CANCELLED is currently
        supported.

        Args:
            id: The ID of the order that the tracking information is associated with.
            tracker_id: The order tracking ID.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v2/checkout/orders/{id}/trackers/{tracker_id}"),
            path_params=[param[str]("id", id), param[str]("tracker_id", tracker_id)],
            headers=[
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[list[Patch | PatchDict] | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=empty_response,
            error_mapper=update_order_tracking_error_mapper,
            request_options=request_options,
        )


class AsyncOrdersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def authorize_order(
        self,
        id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_client_metadata_id: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        body: OrderAuthorizeRequest | OrderAuthorizeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OrderAuthorizeResponse, AuthorizeOrderErrorBody]:
        """Authorizes payment for an order. To successfully authorize payment for an order, the buyer must first approve
        the order or a valid payment_source must be provided in the request. A buyer can approve the order upon being
        redirected to the rel:approve URL that was returned in the HATEOAS links in the create order response. Note: For
        error handling and troubleshooting, see Orders v2 errors.

        Args:
            id: The ID of the order for which to authorize.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_request_id: The server stores keys for 6 hours. The API callers can request the times to up to 72
                hours by speaking to their Account Manager. It is mandatory for all single-step create order calls (E.g.
                Create Order Request with payment source information like Card, PayPal.vault_id,
                PayPal.billing_agreement_id, etc).
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_client_metadata_id: Value sent with the request.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/checkout/orders/{id}/authorize"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str | None]("PayPal-Mock-Response", pay_pal_mock_response),
                param[str | None]("PayPal-Request-Id", pay_pal_request_id),
                param[str | None]("Prefer", prefer),
                param[str | None]("PayPal-Client-Metadata-Id", pay_pal_client_metadata_id),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[OrderAuthorizeRequest | OrderAuthorizeRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[OrderAuthorizeResponse],
            error_mapper=authorize_order_error_mapper,
            request_options=request_options,
        )

    async def capture_order(
        self,
        id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_request_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_client_metadata_id: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        body: OrderCaptureRequest | OrderCaptureRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Order, CaptureOrderErrorBody]:
        """Captures payment for an order. To successfully capture payment for an order, the buyer must first approve the
        order or a valid payment_source must be provided in the request. A buyer can approve the order upon being
        redirected to the rel:approve URL that was returned in the HATEOAS links in the create order response. Note: For
        error handling and troubleshooting, see Orders v2 errors.

        Args:
            id: The ID of the order for which to capture a payment.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_request_id: The server stores keys for 6 hours. The API callers can request the times to up to 72
                hours by speaking to their Account Manager. It is mandatory for all single-step create order calls (E.g.
                Create Order Request with payment source information like Card, PayPal.vault_id,
                PayPal.billing_agreement_id, etc).
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_client_metadata_id: Value sent with the request.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/checkout/orders/{id}/capture"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str | None]("PayPal-Mock-Response", pay_pal_mock_response),
                param[str | None]("PayPal-Request-Id", pay_pal_request_id),
                param[str | None]("Prefer", prefer),
                param[str | None]("PayPal-Client-Metadata-Id", pay_pal_client_metadata_id),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[OrderCaptureRequest | OrderCaptureRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[Order],
            error_mapper=capture_order_error_mapper,
            request_options=request_options,
        )

    async def confirm_order(
        self,
        id: str,
        *,
        pay_pal_client_metadata_id: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        prefer: str | None = "return=minimal",
        body: ConfirmOrderRequest | ConfirmOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Order, ConfirmOrderErrorBody]:
        """Payer confirms their intent to pay for the the Order with the given payment source.

        Args:
            id: The ID of the order for which the payer confirms their intent to pay.
            pay_pal_client_metadata_id: Value sent with the request.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/checkout/orders/{id}/confirm-payment-source"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str | None]("PayPal-Client-Metadata-Id", pay_pal_client_metadata_id),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
                param[str | None]("Prefer", prefer),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[ConfirmOrderRequest | ConfirmOrderRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[Order],
            error_mapper=confirm_order_error_mapper,
            request_options=request_options,
        )

    async def create_order(
        self,
        body: OrderRequest | OrderRequestDict,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_request_id: str | None = None,
        pay_pal_partner_attribution_id: str | None = None,
        pay_pal_client_metadata_id: str | None = None,
        prefer: str | None = "return=minimal",
        pay_pal_auth_assertion: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Order, CreateOrderErrorBody]:
        """Creates an order. Merchants and partners can add Level 2 and 3 data to payments to reduce risk and payment
        processing costs. For more information about processing payments, see checkout or multiparty checkout. Note: For
        error handling and troubleshooting, see Orders v2 errors.

        Args:
            body: The request body.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_request_id: The server stores keys for 6 hours. The API callers can request the times to up to 72
                hours by speaking to their Account Manager. It is mandatory for all single-step create order calls (E.g.
                Create Order Request with payment source information like Card, PayPal.vault_id,
                PayPal.billing_agreement_id, etc).
            pay_pal_partner_attribution_id: Value sent with the request.
            pay_pal_client_metadata_id: Value sent with the request.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/checkout/orders"),
            headers=[
                param[str | None]("PayPal-Mock-Response", pay_pal_mock_response),
                param[str | None]("PayPal-Request-Id", pay_pal_request_id),
                param[str | None]("PayPal-Partner-Attribution-Id", pay_pal_partner_attribution_id),
                param[str | None]("PayPal-Client-Metadata-Id", pay_pal_client_metadata_id),
                param[str | None]("Prefer", prefer),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[OrderRequest | OrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[Order],
            error_mapper=create_order_error_mapper,
            request_options=request_options,
        )

    async def create_order_tracking(
        self,
        id: str,
        body: OrderTrackerRequest | OrderTrackerRequestDict,
        *,
        pay_pal_auth_assertion: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Order, CreateOrderTrackingErrorBody]:
        """Adds tracking information for an Order.

        Args:
            id: The ID of the order that the tracking information is associated with.
            body: The request body.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/checkout/orders/{id}/track"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[OrderTrackerRequest | OrderTrackerRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[Order],
            error_mapper=create_order_tracking_error_mapper,
            request_options=request_options,
        )

    async def get_order(
        self,
        id: str,
        *,
        fields: str | None = None,
        pay_pal_mock_response: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Order, GetOrderErrorBody]:
        """Shows details for an order, by ID. Note: For error handling and troubleshooting, see Orders v2 errors.

        Args:
            id: The ID of the order for which to show details.
            fields: A comma-separated list of fields that should be returned for the order. Valid filter field is
                ``payment_source``.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/checkout/orders/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str | None]("fields", fields)],
            headers=[
                param[str | None]("PayPal-Mock-Response", pay_pal_mock_response),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[Order],
            error_mapper=get_order_error_mapper,
            request_options=request_options,
        )

    async def patch_order(
        self,
        id: str,
        *,
        pay_pal_mock_response: str | None = None,
        pay_pal_auth_assertion: str | None = None,
        body: list[Patch | PatchDict] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PatchOrderErrorBody]:
        r"""Updates an order with a ``CREATED`` or ``APPROVED`` status. You cannot update an order with the
        ``COMPLETED`` status.<br/><br/>To make an update, you must provide a ``reference_id``. If you omit this value
        with an order that contains only one purchase unit, PayPal sets the value to ``default`` which enables you to
        use the path: <code>\"/purchase_units/@reference_id=='default'/{attribute-or-object}\"</code>. Merchants and
        partners can add Level 2 and 3 data to payments to reduce risk and payment processing costs. For more
        information about processing payments, see <a
        href="https://developer.paypal.com/docs/checkout/advanced/processing/">checkout</a> or <a
        href="https://developer.paypal.com/docs/multiparty/checkout/advanced/processing/">multiparty
        checkout</a>.<blockquote><strong>Note:</strong> For error handling and troubleshooting, see <a
        href="https://developer.paypal.com/api/rest/reference/orders/v2/errors/#patch-order">Orders v2
        errors</a>.</blockquote>Patchable attributes or
        objects:<br/><br/><table><thead><th>Attribute</th><th>Op</th><th>Notes</th></thead><tbody><tr><td><code>intent</code></td><td>replace</td><td></td></tr><tr><td><code>payer</code></td><td>replace,
        add</td><td>Using replace op for <code>payer</code> will replace the whole <code>payer</code> object with the
        value sent in request.</td></tr><tr><td><code>purchase_units</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].custom_id</code></td><td>replace, add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].description</code></td><td>replace, add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].payee.email</code></td><td>replace</td><td></td></tr><tr><td><code>purchase_units[].shipping.name</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.email_address</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.phone_number</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.options</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.address</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].shipping.type</code></td><td>replace,
        add</td><td></td></tr><tr><td><code>purchase_units[].soft_descriptor</code></td><td>replace,
        remove</td><td></td></tr><tr><td><code>purchase_units[].amount</code></td><td>replace</td><td></td></tr><tr><td><code>purchase_units[].items</code></td><td>replace,
        add, remove</td><td></td></tr><tr><td><code>purchase_units[].invoice_id</code></td><td>replace, add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].payment_instruction</code></td><td>replace</td><td></td></tr><tr><td><code>purchase_units[].payment_instruction.disbursement_mode</code></td><td>replace</td><td>By
        default, <code>disbursement_mode</code> is
        <code>INSTANT</code>.</td></tr><tr><td><code>purchase_units[].payment_instruction.payee_receivable_fx_rate_id</code></td><td>replace,
        add,
        remove</td><td></td></tr><tr><td><code>purchase_units[].payment_instruction.platform_fees</code></td><td>replace,
        add, remove</td><td></td></tr><tr><td><code>purchase_units[].supplementary_data.airline</code></td><td>replace,
        add, remove</td><td></td></tr><tr><td><code>purchase_units[].supplementary_data.card</code></td><td>replace,
        add, remove</td><td></td></tr><tr><td><code>application_context.client_configuration</code></td><td>replace,
        add</td><td></td></tr></tbody></table>

        Args:
            id: The ID of the order to update.
            pay_pal_mock_response: PayPal's REST API uses a request header to invoke negative testing in the sandbox.
                This header configures the sandbox into a negative testing state for transactions that include the
                merchant.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v2/checkout/orders/{id}"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str | None]("PayPal-Mock-Response", pay_pal_mock_response),
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[list[Patch | PatchDict] | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=empty_response,
            error_mapper=patch_order_error_mapper,
            request_options=request_options,
        )

    async def update_order_tracking(
        self,
        id: str,
        tracker_id: str,
        *,
        pay_pal_auth_assertion: str | None = None,
        body: list[Patch | PatchDict] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UpdateOrderTrackingErrorBody]:
        """Updates or cancels the tracking information for a PayPal order, by ID. Updatable attributes or objects:
        Attribute Op Notes items replace Using replace op for items will replace the entire items object with the value
        sent in request. notify_payer replace, add status replace Only patching status to CANCELLED is currently
        supported.

        Args:
            id: The ID of the order that the tracking information is associated with.
            tracker_id: The order tracking ID.
            pay_pal_auth_assertion: An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant.
                For details, see PayPal-Auth-Assertion.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v2/checkout/orders/{id}/trackers/{tracker_id}"),
            path_params=[param[str]("id", id), param[str]("tracker_id", tracker_id)],
            headers=[
                param[str | None]("PayPal-Auth-Assertion", pay_pal_auth_assertion),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[list[Patch | PatchDict] | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=empty_response,
            error_mapper=update_order_tracking_error_mapper,
            request_options=request_options,
        )
