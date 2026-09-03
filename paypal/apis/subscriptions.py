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
from ..errors.activate_billing_plan_error import ActivateBillingPlanErrorBody, activate_billing_plan_error_mapper
from ..errors.activate_subscription_error import ActivateSubscriptionErrorBody, activate_subscription_error_mapper
from ..errors.cancel_subscription_error import CancelSubscriptionErrorBody, cancel_subscription_error_mapper
from ..errors.capture_subscription_error import CaptureSubscriptionErrorBody, capture_subscription_error_mapper
from ..errors.create_billing_plan_error import CreateBillingPlanErrorBody, create_billing_plan_error_mapper
from ..errors.create_subscription_error import CreateSubscriptionErrorBody, create_subscription_error_mapper
from ..errors.deactivate_billing_plan_error import DeactivateBillingPlanErrorBody, deactivate_billing_plan_error_mapper
from ..errors.get_billing_plan_error import GetBillingPlanErrorBody, get_billing_plan_error_mapper
from ..errors.get_subscription_error import GetSubscriptionErrorBody, get_subscription_error_mapper
from ..errors.list_billing_plans_error import ListBillingPlansErrorBody, list_billing_plans_error_mapper
from ..errors.list_subscription_transactions_error import (
    ListSubscriptionTransactionsErrorBody,
    list_subscription_transactions_error_mapper,
)
from ..errors.list_subscriptions_error import ListSubscriptionsErrorBody, list_subscriptions_error_mapper
from ..errors.patch_billing_plan_error import PatchBillingPlanErrorBody, patch_billing_plan_error_mapper
from ..errors.patch_subscription_error import PatchSubscriptionErrorBody, patch_subscription_error_mapper
from ..errors.revise_subscription_error import ReviseSubscriptionErrorBody, revise_subscription_error_mapper
from ..errors.suspend_subscription_error import SuspendSubscriptionErrorBody, suspend_subscription_error_mapper
from ..errors.update_billing_plan_pricing_schemes_error import (
    UpdateBillingPlanPricingSchemesErrorBody,
    update_billing_plan_pricing_schemes_error_mapper,
)
from ..models.activate_subscription_request import ActivateSubscriptionRequest, ActivateSubscriptionRequestDict
from ..models.billing_plan import BillingPlan
from ..models.cancel_subscription_request import CancelSubscriptionRequest, CancelSubscriptionRequestDict
from ..models.capture_subscription_request import CaptureSubscriptionRequest, CaptureSubscriptionRequestDict
from ..models.create_subscription_request import CreateSubscriptionRequest, CreateSubscriptionRequestDict
from ..models.modify_subscription_request import ModifySubscriptionRequest, ModifySubscriptionRequestDict
from ..models.modify_subscription_response import ModifySubscriptionResponse
from ..models.patch import Patch, PatchDict
from ..models.plan_collection import PlanCollection
from ..models.plan_request import PlanRequest, PlanRequestDict
from ..models.subscription import Subscription
from ..models.subscription_collection import SubscriptionCollection
from ..models.subscription_transaction_details import SubscriptionTransactionDetails
from ..models.suspend_subscription import SuspendSubscription, SuspendSubscriptionDict
from ..models.transactions_list import TransactionsList
from ..models.update_pricing_schemes_request import UpdatePricingSchemesRequest, UpdatePricingSchemesRequestDict
from ..server.server import Server


class Subscriptions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SubscriptionsWithRawResponse(client, server, auth)

    def activate_billing_plan(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Activates a plan, by ID.

        Args:
            id: The ID of the plan.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``204 No Content`` status code with no JSON response body.

        Raises:
            ApiError: Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The specified resource does not exist. The
                requested action could not be performed, semantically incorrect, or failed business validation. An
                internal server error has occurred. ``error`` is ``SubscriptionError | RawError``."""
        return self._with_raw_response.activate_billing_plan(id, request_options=request_options).unwrap()

    def activate_subscription(
        self,
        id: str,
        *,
        body: ActivateSubscriptionRequest | ActivateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Activates the subscription.

        Args:
            id: The ID of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``204 No Content`` status code with no JSON response body.

        Raises:
            ApiError: Bad Request. Request is not well-formed, syntactically incorrect, or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The specified resource does not exist. The
                requested action could not be performed, semantically incorrect, or failed business validation. An
                internal server error has occurred. ``error`` is ``SubscriptionError | RawError``."""
        return self._with_raw_response.activate_subscription(id, body=body, request_options=request_options).unwrap()

    def cancel_subscription(
        self,
        id: str,
        *,
        body: CancelSubscriptionRequest | CancelSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Cancels the subscription.

        Args:
            id: The ID of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``204 No Content`` status code with no JSON response body.

        Raises:
            ApiError: Bad Request. Request is not well-formed, syntactically incorrect, or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The specified resource does not exist. The
                requested action could not be performed, semantically incorrect, or failed business validation. An
                internal server error has occurred. ``error`` is ``SubscriptionError | RawError``."""
        return self._with_raw_response.cancel_subscription(id, body=body, request_options=request_options).unwrap()

    def capture_subscription(
        self,
        id: str,
        *,
        pay_pal_request_id: str | None = None,
        body: CaptureSubscriptionRequest | CaptureSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionTransactionDetails:
        """Captures an authorized payment from the subscriber on the subscription.

        Args:
            id: The ID of the subscription.
            pay_pal_request_id: The server stores keys for 72 hours.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that shows
            subscription details.

        Raises:
            ApiError: Bad Request. Request is not well-formed, syntactically incorrect, or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The specified resource does not exist. The
                requested action could not be performed, semantically incorrect, or failed business validation. An
                internal server error has occurred. ``error`` is ``SubscriptionError | RawError``."""
        return self._with_raw_response.capture_subscription(
            id, pay_pal_request_id=pay_pal_request_id, body=body, request_options=request_options
        ).unwrap()

    def create_billing_plan(
        self,
        *,
        prefer: str | None = "return=minimal",
        pay_pal_request_id: str | None = None,
        body: PlanRequest | PlanRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BillingPlan:
        """Creates a plan that defines pricing and billing cycle details for subscriptions.

        Args:
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_request_id: The server stores keys for 72 hours.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that shows billing
            plan details.

        Raises:
            ApiError: Bad Request. Request is not well-formed, syntactically incorrect, or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The requested action could not be performed,
                semantically incorrect, or failed business validation. An internal server error has occurred. ``error``
                is ``SubscriptionError | RawError``."""
        return self._with_raw_response.create_billing_plan(
            prefer=prefer, pay_pal_request_id=pay_pal_request_id, body=body, request_options=request_options
        ).unwrap()

    def create_subscription(
        self,
        *,
        prefer: str | None = "return=minimal",
        pay_pal_request_id: str | None = None,
        pay_pal_client_metadata_id: str | None = None,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Subscription:
        """Creates a subscription.

        Args:
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_request_id: The server stores keys for 72 hours.
            pay_pal_client_metadata_id: The PayPal Client Metadata Id(CMID) is used to provide device-specific
                information to PayPal's risk engine. This is crucial for transactions that require device-specific risk
                assessments. Merchants typically use the Paypal SDK that automatically submits the CMID or they use
                tools like Fraudnet JS for web or Magnes JS for mobile to generate the CMID on the frontend and then
                pass it to the API as part of the request headers.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that shows
            subscription details.

        Raises:
            ApiError: Bad Request. Request is not well-formed, syntactically incorrect, or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The requested action could not be performed,
                semantically incorrect, or failed business validation. An internal server error has occurred. ``error``
                is ``SubscriptionError | RawError``."""
        return self._with_raw_response.create_subscription(
            prefer=prefer,
            pay_pal_request_id=pay_pal_request_id,
            pay_pal_client_metadata_id=pay_pal_client_metadata_id,
            body=body,
            request_options=request_options,
        ).unwrap()

    def deactivate_billing_plan(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Deactivates a plan, by ID.

        Args:
            id: The ID of the plan.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``204 No Content`` status code with no JSON response body.

        Raises:
            ApiError: Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The specified resource does not exist. The
                requested action could not be performed, semantically incorrect, or failed business validation. An
                internal server error has occurred. ``error`` is ``SubscriptionError | RawError``."""
        return self._with_raw_response.deactivate_billing_plan(id, request_options=request_options).unwrap()

    def get_billing_plan(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> BillingPlan:
        """Shows details for a plan, by ID.

        Args:
            id: The ID of the plan.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that shows plan
            details.

        Raises:
            ApiError: Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The specified resource does not exist. An internal
                server error has occurred. ``error`` is ``SubscriptionError | RawError``."""
        return self._with_raw_response.get_billing_plan(id, request_options=request_options).unwrap()

    def get_subscription(
        self, id: str, *, fields: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Subscription:
        """Shows details for a subscription, by ID.

        Args:
            id: The ID of the subscription.
            fields: List of fields that are to be returned in the response. Possible value for fields are
                last_failed_payment and plan.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that shows
            subscription details.

        Raises:
            ApiError: Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The specified resource does not exist. An internal
                server error has occurred. ``error`` is ``SubscriptionError | RawError``."""
        return self._with_raw_response.get_subscription(id, fields=fields, request_options=request_options).unwrap()

    def list_billing_plans(
        self,
        *,
        product_id: str | None = None,
        page_size: int | None = 10,
        page: int | None = 1,
        total_required: bool | None = False,
        prefer: str | None = "return=minimal",
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlanCollection:
        """Lists billing plans.

        Args:
            product_id: Filters the response by a Product ID.
            page_size: The number of items to return in the response.
            page: A non-zero integer which is the start index of the entire list of items to return in the response. The
                combination of ``page=1`` and ``page_size=20`` returns the first 20 items. The combination of ``page=2``
                and ``page_size=20`` returns the next 20 items.
            total_required: Indicates whether to show the total count in the response.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, name, description and HATEOAS links. return=representation. The server
                returns a complete resource representation, including the current state of the resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that lists billing
            plans.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authentication failed due
                to missing authorization header, or invalid authentication credentials. Authorization failed due to
                insufficient permissions. The specified resource does not exist. An internal server error has occurred.
                ``error`` is ``SubscriptionError | RawError``."""
        return self._with_raw_response.list_billing_plans(
            product_id=product_id,
            page_size=page_size,
            page=page,
            total_required=total_required,
            prefer=prefer,
            request_options=request_options,
        ).unwrap()

    def list_subscription_transactions(
        self, id: str, start_time: str, end_time: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransactionsList:
        """Lists transactions for a subscription.

        Args:
            id: The ID of the subscription.
            start_time: The start time of the range of transactions to list.
            end_time: The end time of the range of transactions to list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that shows
            subscription details.

        Raises:
            ApiError: Bad Request. Request is not well-formed, syntactically incorrect, or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The specified resource does not exist. An internal
                server error has occurred. ``error`` is ``SubscriptionError | RawError``."""
        return self._with_raw_response.list_subscription_transactions(
            id, start_time, end_time, request_options=request_options
        ).unwrap()

    def list_subscriptions(
        self,
        *,
        plan_ids: str | None = None,
        statuses: str | None = None,
        created_after: str | None = None,
        created_before: str | None = None,
        status_updated_before: str | None = None,
        status_updated_after: str | None = None,
        filter: str | None = None,
        page_size: int | None = 10,
        page: int | None = 1,
        customer_ids: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionCollection:
        """List all subscriptions for merchant account.

        Args:
            plan_ids: Filters the response by list of plan IDs. Filter supports upto 70 plan IDs. URLs should not exceed
                a length of 2000 characters.
            statuses: Filters the response by list of subscription statuses.
            created_after: Filters the response by subscription creation start time for a range of subscriptions.
            created_before: Filters the response by subscription creation end time for a range of subscriptions.
            status_updated_before: Filters the response by status update start time for a range of subscriptions.
            status_updated_after: Filters the response by status update end time for a range of subscriptions.
            filter: Filter the response using complex expressions that could use comparison operators like ge, gt, le,
                lt and logical operators such as 'and' and 'or'.
            page_size: The number of items to return in the response.
            page: A non-zero integer which is the start index of the entire list of items to return in the response. The
                combination of ``page=1`` and ``page_size=20`` returns the first 20 items. The combination of ``page=2``
                and ``page_size=20`` returns the next 20 items.
            customer_ids: Filters the response by comma separated vault customer IDs (FSS subscriptions only).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that lists the
            subscriptions.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authentication failed due
                to missing authorization header, or invalid authentication credentials. Authorization failed due to
                insufficient permissions. An internal server error has occurred. ``error`` is ``SubscriptionError |
                RawError``."""
        return self._with_raw_response.list_subscriptions(
            plan_ids=plan_ids,
            statuses=statuses,
            created_after=created_after,
            created_before=created_before,
            status_updated_before=status_updated_before,
            status_updated_after=status_updated_after,
            filter=filter,
            page_size=page_size,
            page=page,
            customer_ids=customer_ids,
            request_options=request_options,
        ).unwrap()

    def patch_billing_plan(
        self,
        id: str,
        *,
        body: list[Patch | PatchDict] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Updates a plan with the ``CREATED`` or ``ACTIVE`` status. For an ``INACTIVE`` plan, you can make only status
        updates. You can patch these attributes and objects: Attribute or object Operations description replace
        payment_preferences.auto_bill_outstanding replace taxes.percentage replace
        payment_preferences.payment_failure_threshold replace payment_preferences.setup_fee replace
        payment_preferences.setup_fee_failure_action replace name replace

        Args:
            id: The ID of the plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``204 No Content`` status code with no JSON response body.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authentication failed due
                to missing authorization header, or invalid authentication credentials. Authorization failed due to
                insufficient permissions. The specified resource does not exist. The requested action could not be
                performed, semantically incorrect, or failed business validation. An internal server error has occurred.
                ``error`` is ``SubscriptionError | RawError``."""
        return self._with_raw_response.patch_billing_plan(id, body=body, request_options=request_options).unwrap()

    def patch_subscription(
        self,
        id: str,
        *,
        body: list[Patch | PatchDict] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Updates a subscription which could be in ACTIVE or SUSPENDED status. You can override plan level default
        attributes by providing customised values for plan path in the patch request. You cannot update attributes that
        have already completed (Example - trial cycles can’t be updated if completed). Once overridden, changes to plan
        resource will not impact subscription. Any price update will not impact billing cycles within next 10 days
        (Applicable only for subscriptions funded by PayPal account). Following are the fields eligible for patch.
        Attribute or object Operations billing_info.outstanding_balance replace custom_id add,replace
        plan.billing_cycles[@sequence==n]. pricing_scheme.fixed_price add,replace plan.billing_cycles[@sequence==n].
        pricing_scheme.tiers replace plan.billing_cycles[@sequence==n]. total_cycles replace plan.payment_preferences.
        auto_bill_outstanding replace plan.payment_preferences. payment_failure_threshold replace plan.taxes.inclusive
        add,replace plan.taxes.percentage add,replace shipping_amount add,replace start_time replace
        subscriber.shipping_address add,replace subscriber.payment_source (for subscriptions funded by card payments)
        replace

        Args:
            id: The ID for the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``204 No Content`` status code with no JSON response body.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authentication failed due
                to missing authorization header, or invalid authentication credentials. Authorization failed due to
                insufficient permissions. The specified resource does not exist. The requested action could not be
                performed, semantically incorrect, or failed business validation. An internal server error has occurred.
                ``error`` is ``SubscriptionError | RawError``."""
        return self._with_raw_response.patch_subscription(id, body=body, request_options=request_options).unwrap()

    def revise_subscription(
        self,
        id: str,
        *,
        body: ModifySubscriptionRequest | ModifySubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ModifySubscriptionResponse:
        """Updates the quantity of the product or service in a subscription. You can also use this method to switch the
        plan and update the ``shipping_amount``, ``shipping_address`` values for the subscription. This type of update
        requires the buyer's consent.

        Args:
            id: The ID of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that shows
            subscription details.

        Raises:
            ApiError: Bad Request. Request is not well-formed, syntactically incorrect, or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The specified resource does not exist. The
                requested action could not be performed, semantically incorrect, or failed business validation. An
                internal server error has occurred. ``error`` is ``SubscriptionError | RawError``."""
        return self._with_raw_response.revise_subscription(id, body=body, request_options=request_options).unwrap()

    def suspend_subscription(
        self,
        id: str,
        *,
        body: SuspendSubscription | SuspendSubscriptionDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Suspends the subscription.

        Args:
            id: The ID of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``204 No Content`` status code with no JSON response body.

        Raises:
            ApiError: Bad Request. Request is not well-formed, syntactically incorrect, or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The specified resource does not exist. The
                requested action could not be performed, semantically incorrect, or failed business validation. An
                internal server error has occurred. ``error`` is ``SubscriptionError | RawError``."""
        return self._with_raw_response.suspend_subscription(id, body=body, request_options=request_options).unwrap()

    def update_billing_plan_pricing_schemes(
        self,
        id: str,
        *,
        body: UpdatePricingSchemesRequest | UpdatePricingSchemesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Updates pricing for a plan. For example, you can update a regular billing cycle from $5 per month to $7 per
        month.

        Args:
            id: The ID for the plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``204 No Content`` status code with no JSON response body.

        Raises:
            ApiError: Bad Request. Request is not well-formed, syntactically incorrect, or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The specified resource does not exist. The
                requested action could not be performed, semantically incorrect, or failed business validation. An
                internal server error has occurred. ``error`` is ``SubscriptionError | RawError``."""
        return self._with_raw_response.update_billing_plan_pricing_schemes(
            id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SubscriptionsWithRawResponse:
        return self._with_raw_response


class AsyncSubscriptions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSubscriptionsWithRawResponse(client, server, auth)

    async def activate_billing_plan(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Activates a plan, by ID.

        Args:
            id: The ID of the plan.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``204 No Content`` status code with no JSON response body.

        Raises:
            ApiError: Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The specified resource does not exist. The
                requested action could not be performed, semantically incorrect, or failed business validation. An
                internal server error has occurred. ``error`` is ``SubscriptionError | RawError``."""
        return (await self._with_raw_response.activate_billing_plan(id, request_options=request_options)).unwrap()

    async def activate_subscription(
        self,
        id: str,
        *,
        body: ActivateSubscriptionRequest | ActivateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Activates the subscription.

        Args:
            id: The ID of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``204 No Content`` status code with no JSON response body.

        Raises:
            ApiError: Bad Request. Request is not well-formed, syntactically incorrect, or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The specified resource does not exist. The
                requested action could not be performed, semantically incorrect, or failed business validation. An
                internal server error has occurred. ``error`` is ``SubscriptionError | RawError``."""
        return (
            await self._with_raw_response.activate_subscription(id, body=body, request_options=request_options)
        ).unwrap()

    async def cancel_subscription(
        self,
        id: str,
        *,
        body: CancelSubscriptionRequest | CancelSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Cancels the subscription.

        Args:
            id: The ID of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``204 No Content`` status code with no JSON response body.

        Raises:
            ApiError: Bad Request. Request is not well-formed, syntactically incorrect, or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The specified resource does not exist. The
                requested action could not be performed, semantically incorrect, or failed business validation. An
                internal server error has occurred. ``error`` is ``SubscriptionError | RawError``."""
        return (
            await self._with_raw_response.cancel_subscription(id, body=body, request_options=request_options)
        ).unwrap()

    async def capture_subscription(
        self,
        id: str,
        *,
        pay_pal_request_id: str | None = None,
        body: CaptureSubscriptionRequest | CaptureSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionTransactionDetails:
        """Captures an authorized payment from the subscriber on the subscription.

        Args:
            id: The ID of the subscription.
            pay_pal_request_id: The server stores keys for 72 hours.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that shows
            subscription details.

        Raises:
            ApiError: Bad Request. Request is not well-formed, syntactically incorrect, or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The specified resource does not exist. The
                requested action could not be performed, semantically incorrect, or failed business validation. An
                internal server error has occurred. ``error`` is ``SubscriptionError | RawError``."""
        return (
            await self._with_raw_response.capture_subscription(
                id, pay_pal_request_id=pay_pal_request_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def create_billing_plan(
        self,
        *,
        prefer: str | None = "return=minimal",
        pay_pal_request_id: str | None = None,
        body: PlanRequest | PlanRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BillingPlan:
        """Creates a plan that defines pricing and billing cycle details for subscriptions.

        Args:
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_request_id: The server stores keys for 72 hours.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that shows billing
            plan details.

        Raises:
            ApiError: Bad Request. Request is not well-formed, syntactically incorrect, or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The requested action could not be performed,
                semantically incorrect, or failed business validation. An internal server error has occurred. ``error``
                is ``SubscriptionError | RawError``."""
        return (
            await self._with_raw_response.create_billing_plan(
                prefer=prefer, pay_pal_request_id=pay_pal_request_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def create_subscription(
        self,
        *,
        prefer: str | None = "return=minimal",
        pay_pal_request_id: str | None = None,
        pay_pal_client_metadata_id: str | None = None,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Subscription:
        """Creates a subscription.

        Args:
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_request_id: The server stores keys for 72 hours.
            pay_pal_client_metadata_id: The PayPal Client Metadata Id(CMID) is used to provide device-specific
                information to PayPal's risk engine. This is crucial for transactions that require device-specific risk
                assessments. Merchants typically use the Paypal SDK that automatically submits the CMID or they use
                tools like Fraudnet JS for web or Magnes JS for mobile to generate the CMID on the frontend and then
                pass it to the API as part of the request headers.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that shows
            subscription details.

        Raises:
            ApiError: Bad Request. Request is not well-formed, syntactically incorrect, or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The requested action could not be performed,
                semantically incorrect, or failed business validation. An internal server error has occurred. ``error``
                is ``SubscriptionError | RawError``."""
        return (
            await self._with_raw_response.create_subscription(
                prefer=prefer,
                pay_pal_request_id=pay_pal_request_id,
                pay_pal_client_metadata_id=pay_pal_client_metadata_id,
                body=body,
                request_options=request_options,
            )
        ).unwrap()

    async def deactivate_billing_plan(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Deactivates a plan, by ID.

        Args:
            id: The ID of the plan.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``204 No Content`` status code with no JSON response body.

        Raises:
            ApiError: Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The specified resource does not exist. The
                requested action could not be performed, semantically incorrect, or failed business validation. An
                internal server error has occurred. ``error`` is ``SubscriptionError | RawError``."""
        return (await self._with_raw_response.deactivate_billing_plan(id, request_options=request_options)).unwrap()

    async def get_billing_plan(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> BillingPlan:
        """Shows details for a plan, by ID.

        Args:
            id: The ID of the plan.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that shows plan
            details.

        Raises:
            ApiError: Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The specified resource does not exist. An internal
                server error has occurred. ``error`` is ``SubscriptionError | RawError``."""
        return (await self._with_raw_response.get_billing_plan(id, request_options=request_options)).unwrap()

    async def get_subscription(
        self, id: str, *, fields: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> Subscription:
        """Shows details for a subscription, by ID.

        Args:
            id: The ID of the subscription.
            fields: List of fields that are to be returned in the response. Possible value for fields are
                last_failed_payment and plan.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that shows
            subscription details.

        Raises:
            ApiError: Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The specified resource does not exist. An internal
                server error has occurred. ``error`` is ``SubscriptionError | RawError``."""
        return (
            await self._with_raw_response.get_subscription(id, fields=fields, request_options=request_options)
        ).unwrap()

    async def list_billing_plans(
        self,
        *,
        product_id: str | None = None,
        page_size: int | None = 10,
        page: int | None = 1,
        total_required: bool | None = False,
        prefer: str | None = "return=minimal",
        request_options: RequestOptionsOrDict | None = None,
    ) -> PlanCollection:
        """Lists billing plans.

        Args:
            product_id: Filters the response by a Product ID.
            page_size: The number of items to return in the response.
            page: A non-zero integer which is the start index of the entire list of items to return in the response. The
                combination of ``page=1`` and ``page_size=20`` returns the first 20 items. The combination of ``page=2``
                and ``page_size=20`` returns the next 20 items.
            total_required: Indicates whether to show the total count in the response.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, name, description and HATEOAS links. return=representation. The server
                returns a complete resource representation, including the current state of the resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that lists billing
            plans.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authentication failed due
                to missing authorization header, or invalid authentication credentials. Authorization failed due to
                insufficient permissions. The specified resource does not exist. An internal server error has occurred.
                ``error`` is ``SubscriptionError | RawError``."""
        return (
            await self._with_raw_response.list_billing_plans(
                product_id=product_id,
                page_size=page_size,
                page=page,
                total_required=total_required,
                prefer=prefer,
                request_options=request_options,
            )
        ).unwrap()

    async def list_subscription_transactions(
        self, id: str, start_time: str, end_time: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransactionsList:
        """Lists transactions for a subscription.

        Args:
            id: The ID of the subscription.
            start_time: The start time of the range of transactions to list.
            end_time: The end time of the range of transactions to list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that shows
            subscription details.

        Raises:
            ApiError: Bad Request. Request is not well-formed, syntactically incorrect, or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The specified resource does not exist. An internal
                server error has occurred. ``error`` is ``SubscriptionError | RawError``."""
        return (
            await self._with_raw_response.list_subscription_transactions(
                id, start_time, end_time, request_options=request_options
            )
        ).unwrap()

    async def list_subscriptions(
        self,
        *,
        plan_ids: str | None = None,
        statuses: str | None = None,
        created_after: str | None = None,
        created_before: str | None = None,
        status_updated_before: str | None = None,
        status_updated_after: str | None = None,
        filter: str | None = None,
        page_size: int | None = 10,
        page: int | None = 1,
        customer_ids: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionCollection:
        """List all subscriptions for merchant account.

        Args:
            plan_ids: Filters the response by list of plan IDs. Filter supports upto 70 plan IDs. URLs should not exceed
                a length of 2000 characters.
            statuses: Filters the response by list of subscription statuses.
            created_after: Filters the response by subscription creation start time for a range of subscriptions.
            created_before: Filters the response by subscription creation end time for a range of subscriptions.
            status_updated_before: Filters the response by status update start time for a range of subscriptions.
            status_updated_after: Filters the response by status update end time for a range of subscriptions.
            filter: Filter the response using complex expressions that could use comparison operators like ge, gt, le,
                lt and logical operators such as 'and' and 'or'.
            page_size: The number of items to return in the response.
            page: A non-zero integer which is the start index of the entire list of items to return in the response. The
                combination of ``page=1`` and ``page_size=20`` returns the first 20 items. The combination of ``page=2``
                and ``page_size=20`` returns the next 20 items.
            customer_ids: Filters the response by comma separated vault customer IDs (FSS subscriptions only).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that lists the
            subscriptions.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authentication failed due
                to missing authorization header, or invalid authentication credentials. Authorization failed due to
                insufficient permissions. An internal server error has occurred. ``error`` is ``SubscriptionError |
                RawError``."""
        return (
            await self._with_raw_response.list_subscriptions(
                plan_ids=plan_ids,
                statuses=statuses,
                created_after=created_after,
                created_before=created_before,
                status_updated_before=status_updated_before,
                status_updated_after=status_updated_after,
                filter=filter,
                page_size=page_size,
                page=page,
                customer_ids=customer_ids,
                request_options=request_options,
            )
        ).unwrap()

    async def patch_billing_plan(
        self,
        id: str,
        *,
        body: list[Patch | PatchDict] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Updates a plan with the ``CREATED`` or ``ACTIVE`` status. For an ``INACTIVE`` plan, you can make only status
        updates. You can patch these attributes and objects: Attribute or object Operations description replace
        payment_preferences.auto_bill_outstanding replace taxes.percentage replace
        payment_preferences.payment_failure_threshold replace payment_preferences.setup_fee replace
        payment_preferences.setup_fee_failure_action replace name replace

        Args:
            id: The ID of the plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``204 No Content`` status code with no JSON response body.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authentication failed due
                to missing authorization header, or invalid authentication credentials. Authorization failed due to
                insufficient permissions. The specified resource does not exist. The requested action could not be
                performed, semantically incorrect, or failed business validation. An internal server error has occurred.
                ``error`` is ``SubscriptionError | RawError``."""
        return (
            await self._with_raw_response.patch_billing_plan(id, body=body, request_options=request_options)
        ).unwrap()

    async def patch_subscription(
        self,
        id: str,
        *,
        body: list[Patch | PatchDict] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Updates a subscription which could be in ACTIVE or SUSPENDED status. You can override plan level default
        attributes by providing customised values for plan path in the patch request. You cannot update attributes that
        have already completed (Example - trial cycles can’t be updated if completed). Once overridden, changes to plan
        resource will not impact subscription. Any price update will not impact billing cycles within next 10 days
        (Applicable only for subscriptions funded by PayPal account). Following are the fields eligible for patch.
        Attribute or object Operations billing_info.outstanding_balance replace custom_id add,replace
        plan.billing_cycles[@sequence==n]. pricing_scheme.fixed_price add,replace plan.billing_cycles[@sequence==n].
        pricing_scheme.tiers replace plan.billing_cycles[@sequence==n]. total_cycles replace plan.payment_preferences.
        auto_bill_outstanding replace plan.payment_preferences. payment_failure_threshold replace plan.taxes.inclusive
        add,replace plan.taxes.percentage add,replace shipping_amount add,replace start_time replace
        subscriber.shipping_address add,replace subscriber.payment_source (for subscriptions funded by card payments)
        replace

        Args:
            id: The ID for the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``204 No Content`` status code with no JSON response body.

        Raises:
            ApiError: Request is not well-formed, syntactically incorrect, or violates schema. Authentication failed due
                to missing authorization header, or invalid authentication credentials. Authorization failed due to
                insufficient permissions. The specified resource does not exist. The requested action could not be
                performed, semantically incorrect, or failed business validation. An internal server error has occurred.
                ``error`` is ``SubscriptionError | RawError``."""
        return (
            await self._with_raw_response.patch_subscription(id, body=body, request_options=request_options)
        ).unwrap()

    async def revise_subscription(
        self,
        id: str,
        *,
        body: ModifySubscriptionRequest | ModifySubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ModifySubscriptionResponse:
        """Updates the quantity of the product or service in a subscription. You can also use this method to switch the
        plan and update the ``shipping_amount``, ``shipping_address`` values for the subscription. This type of update
        requires the buyer's consent.

        Args:
            id: The ID of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that shows
            subscription details.

        Raises:
            ApiError: Bad Request. Request is not well-formed, syntactically incorrect, or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The specified resource does not exist. The
                requested action could not be performed, semantically incorrect, or failed business validation. An
                internal server error has occurred. ``error`` is ``SubscriptionError | RawError``."""
        return (
            await self._with_raw_response.revise_subscription(id, body=body, request_options=request_options)
        ).unwrap()

    async def suspend_subscription(
        self,
        id: str,
        *,
        body: SuspendSubscription | SuspendSubscriptionDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Suspends the subscription.

        Args:
            id: The ID of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``204 No Content`` status code with no JSON response body.

        Raises:
            ApiError: Bad Request. Request is not well-formed, syntactically incorrect, or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The specified resource does not exist. The
                requested action could not be performed, semantically incorrect, or failed business validation. An
                internal server error has occurred. ``error`` is ``SubscriptionError | RawError``."""
        return (
            await self._with_raw_response.suspend_subscription(id, body=body, request_options=request_options)
        ).unwrap()

    async def update_billing_plan_pricing_schemes(
        self,
        id: str,
        *,
        body: UpdatePricingSchemesRequest | UpdatePricingSchemesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Updates pricing for a plan. For example, you can update a regular billing cycle from $5 per month to $7 per
        month.

        Args:
            id: The ID for the plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``204 No Content`` status code with no JSON response body.

        Raises:
            ApiError: Bad Request. Request is not well-formed, syntactically incorrect, or violates schema.
                Authentication failed due to missing authorization header, or invalid authentication credentials.
                Authorization failed due to insufficient permissions. The specified resource does not exist. The
                requested action could not be performed, semantically incorrect, or failed business validation. An
                internal server error has occurred. ``error`` is ``SubscriptionError | RawError``."""
        return (
            await self._with_raw_response.update_billing_plan_pricing_schemes(
                id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSubscriptionsWithRawResponse:
        return self._with_raw_response


class SubscriptionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def activate_billing_plan(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, ActivateBillingPlanErrorBody]:
        """Activates a plan, by ID.

        Args:
            id: The ID of the plan.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/billing/plans/{id}/activate"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=empty_response,
            error_mapper=activate_billing_plan_error_mapper,
            request_options=request_options,
        )

    def activate_subscription(
        self,
        id: str,
        *,
        body: ActivateSubscriptionRequest | ActivateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, ActivateSubscriptionErrorBody]:
        """Activates the subscription.

        Args:
            id: The ID of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/billing/subscriptions/{id}/activate"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ActivateSubscriptionRequest | ActivateSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=empty_response,
            error_mapper=activate_subscription_error_mapper,
            request_options=request_options,
        )

    def cancel_subscription(
        self,
        id: str,
        *,
        body: CancelSubscriptionRequest | CancelSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, CancelSubscriptionErrorBody]:
        """Cancels the subscription.

        Args:
            id: The ID of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/billing/subscriptions/{id}/cancel"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancelSubscriptionRequest | CancelSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=empty_response,
            error_mapper=cancel_subscription_error_mapper,
            request_options=request_options,
        )

    def capture_subscription(
        self,
        id: str,
        *,
        pay_pal_request_id: str | None = None,
        body: CaptureSubscriptionRequest | CaptureSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionTransactionDetails, CaptureSubscriptionErrorBody]:
        """Captures an authorized payment from the subscriber on the subscription.

        Args:
            id: The ID of the subscription.
            pay_pal_request_id: The server stores keys for 72 hours.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/billing/subscriptions/{id}/capture"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str | None]("PayPal-Request-Id", pay_pal_request_id), param[UUID]("Idempotency-Key", uuid4())
            ],
            body=json_body[CaptureSubscriptionRequest | CaptureSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SubscriptionTransactionDetails],
            error_mapper=capture_subscription_error_mapper,
            request_options=request_options,
        )

    def create_billing_plan(
        self,
        *,
        prefer: str | None = "return=minimal",
        pay_pal_request_id: str | None = None,
        body: PlanRequest | PlanRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BillingPlan, CreateBillingPlanErrorBody]:
        """Creates a plan that defines pricing and billing cycle details for subscriptions.

        Args:
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_request_id: The server stores keys for 72 hours.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/billing/plans"),
            headers=[
                param[str | None]("Prefer", prefer),
                param[str | None]("PayPal-Request-Id", pay_pal_request_id),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[PlanRequest | PlanRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BillingPlan],
            error_mapper=create_billing_plan_error_mapper,
            request_options=request_options,
        )

    def create_subscription(
        self,
        *,
        prefer: str | None = "return=minimal",
        pay_pal_request_id: str | None = None,
        pay_pal_client_metadata_id: str | None = None,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Subscription, CreateSubscriptionErrorBody]:
        """Creates a subscription.

        Args:
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_request_id: The server stores keys for 72 hours.
            pay_pal_client_metadata_id: The PayPal Client Metadata Id(CMID) is used to provide device-specific
                information to PayPal's risk engine. This is crucial for transactions that require device-specific risk
                assessments. Merchants typically use the Paypal SDK that automatically submits the CMID or they use
                tools like Fraudnet JS for web or Magnes JS for mobile to generate the CMID on the frontend and then
                pass it to the API as part of the request headers.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/billing/subscriptions"),
            headers=[
                param[str | None]("Prefer", prefer),
                param[str | None]("PayPal-Request-Id", pay_pal_request_id),
                param[str | None]("PayPal-Client-Metadata-Id", pay_pal_client_metadata_id),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[CreateSubscriptionRequest | CreateSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[Subscription],
            error_mapper=create_subscription_error_mapper,
            request_options=request_options,
        )

    def deactivate_billing_plan(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeactivateBillingPlanErrorBody]:
        """Deactivates a plan, by ID.

        Args:
            id: The ID of the plan.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/billing/plans/{id}/deactivate"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=empty_response,
            error_mapper=deactivate_billing_plan_error_mapper,
            request_options=request_options,
        )

    def get_billing_plan(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BillingPlan, GetBillingPlanErrorBody]:
        """Shows details for a plan, by ID.

        Args:
            id: The ID of the plan.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/billing/plans/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BillingPlan],
            error_mapper=get_billing_plan_error_mapper,
            request_options=request_options,
        )

    def get_subscription(
        self, id: str, *, fields: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Subscription, GetSubscriptionErrorBody]:
        """Shows details for a subscription, by ID.

        Args:
            id: The ID of the subscription.
            fields: List of fields that are to be returned in the response. Possible value for fields are
                last_failed_payment and plan.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/billing/subscriptions/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str | None]("fields", fields)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[Subscription],
            error_mapper=get_subscription_error_mapper,
            request_options=request_options,
        )

    def list_billing_plans(
        self,
        *,
        product_id: str | None = None,
        page_size: int | None = 10,
        page: int | None = 1,
        total_required: bool | None = False,
        prefer: str | None = "return=minimal",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlanCollection, ListBillingPlansErrorBody]:
        """Lists billing plans.

        Args:
            product_id: Filters the response by a Product ID.
            page_size: The number of items to return in the response.
            page: A non-zero integer which is the start index of the entire list of items to return in the response. The
                combination of ``page=1`` and ``page_size=20`` returns the first 20 items. The combination of ``page=2``
                and ``page_size=20`` returns the next 20 items.
            total_required: Indicates whether to show the total count in the response.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, name, description and HATEOAS links. return=representation. The server
                returns a complete resource representation, including the current state of the resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/billing/plans"),
            query_params=[
                param[str | None]("product_id", product_id),
                param[int | None]("page_size", page_size),
                param[int | None]("page", page),
                param[bool | None]("total_required", total_required),
            ],
            headers=[param[str | None]("Prefer", prefer)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[PlanCollection],
            error_mapper=list_billing_plans_error_mapper,
            request_options=request_options,
        )

    def list_subscription_transactions(
        self, id: str, start_time: str, end_time: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransactionsList, ListSubscriptionTransactionsErrorBody]:
        """Lists transactions for a subscription.

        Args:
            id: The ID of the subscription.
            start_time: The start time of the range of transactions to list.
            end_time: The end time of the range of transactions to list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/billing/subscriptions/{id}/transactions"),
            path_params=[param[str]("id", id)],
            query_params=[param[str]("start_time", start_time), param[str]("end_time", end_time)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[TransactionsList],
            error_mapper=list_subscription_transactions_error_mapper,
            request_options=request_options,
        )

    def list_subscriptions(
        self,
        *,
        plan_ids: str | None = None,
        statuses: str | None = None,
        created_after: str | None = None,
        created_before: str | None = None,
        status_updated_before: str | None = None,
        status_updated_after: str | None = None,
        filter: str | None = None,
        page_size: int | None = 10,
        page: int | None = 1,
        customer_ids: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionCollection, ListSubscriptionsErrorBody]:
        """List all subscriptions for merchant account.

        Args:
            plan_ids: Filters the response by list of plan IDs. Filter supports upto 70 plan IDs. URLs should not exceed
                a length of 2000 characters.
            statuses: Filters the response by list of subscription statuses.
            created_after: Filters the response by subscription creation start time for a range of subscriptions.
            created_before: Filters the response by subscription creation end time for a range of subscriptions.
            status_updated_before: Filters the response by status update start time for a range of subscriptions.
            status_updated_after: Filters the response by status update end time for a range of subscriptions.
            filter: Filter the response using complex expressions that could use comparison operators like ge, gt, le,
                lt and logical operators such as 'and' and 'or'.
            page_size: The number of items to return in the response.
            page: A non-zero integer which is the start index of the entire list of items to return in the response. The
                combination of ``page=1`` and ``page_size=20`` returns the first 20 items. The combination of ``page=2``
                and ``page_size=20`` returns the next 20 items.
            customer_ids: Filters the response by comma separated vault customer IDs (FSS subscriptions only).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/billing/subscriptions"),
            query_params=[
                param[str | None]("plan_ids", plan_ids),
                param[str | None]("statuses", statuses),
                param[str | None]("created_after", created_after),
                param[str | None]("created_before", created_before),
                param[str | None]("status_updated_before", status_updated_before),
                param[str | None]("status_updated_after", status_updated_after),
                param[str | None]("filter", filter),
                param[int | None]("page_size", page_size),
                param[int | None]("page", page),
                param[list[str] | None]("customer_ids", customer_ids),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SubscriptionCollection],
            error_mapper=list_subscriptions_error_mapper,
            request_options=request_options,
        )

    def patch_billing_plan(
        self,
        id: str,
        *,
        body: list[Patch | PatchDict] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PatchBillingPlanErrorBody]:
        """Updates a plan with the ``CREATED`` or ``ACTIVE`` status. For an ``INACTIVE`` plan, you can make only status
        updates. You can patch these attributes and objects: Attribute or object Operations description replace
        payment_preferences.auto_bill_outstanding replace taxes.percentage replace
        payment_preferences.payment_failure_threshold replace payment_preferences.setup_fee replace
        payment_preferences.setup_fee_failure_action replace name replace

        Args:
            id: The ID of the plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/billing/plans/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[list[Patch | PatchDict] | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=empty_response,
            error_mapper=patch_billing_plan_error_mapper,
            request_options=request_options,
        )

    def patch_subscription(
        self,
        id: str,
        *,
        body: list[Patch | PatchDict] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PatchSubscriptionErrorBody]:
        """Updates a subscription which could be in ACTIVE or SUSPENDED status. You can override plan level default
        attributes by providing customised values for plan path in the patch request. You cannot update attributes that
        have already completed (Example - trial cycles can’t be updated if completed). Once overridden, changes to plan
        resource will not impact subscription. Any price update will not impact billing cycles within next 10 days
        (Applicable only for subscriptions funded by PayPal account). Following are the fields eligible for patch.
        Attribute or object Operations billing_info.outstanding_balance replace custom_id add,replace
        plan.billing_cycles[@sequence==n]. pricing_scheme.fixed_price add,replace plan.billing_cycles[@sequence==n].
        pricing_scheme.tiers replace plan.billing_cycles[@sequence==n]. total_cycles replace plan.payment_preferences.
        auto_bill_outstanding replace plan.payment_preferences. payment_failure_threshold replace plan.taxes.inclusive
        add,replace plan.taxes.percentage add,replace shipping_amount add,replace start_time replace
        subscriber.shipping_address add,replace subscriber.payment_source (for subscriptions funded by card payments)
        replace

        Args:
            id: The ID for the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/billing/subscriptions/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[list[Patch | PatchDict] | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=empty_response,
            error_mapper=patch_subscription_error_mapper,
            request_options=request_options,
        )

    def revise_subscription(
        self,
        id: str,
        *,
        body: ModifySubscriptionRequest | ModifySubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ModifySubscriptionResponse, ReviseSubscriptionErrorBody]:
        """Updates the quantity of the product or service in a subscription. You can also use this method to switch the
        plan and update the ``shipping_amount``, ``shipping_address`` values for the subscription. This type of update
        requires the buyer's consent.

        Args:
            id: The ID of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/billing/subscriptions/{id}/revise"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ModifySubscriptionRequest | ModifySubscriptionRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ModifySubscriptionResponse],
            error_mapper=revise_subscription_error_mapper,
            request_options=request_options,
        )

    def suspend_subscription(
        self,
        id: str,
        *,
        body: SuspendSubscription | SuspendSubscriptionDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SuspendSubscriptionErrorBody]:
        """Suspends the subscription.

        Args:
            id: The ID of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/billing/subscriptions/{id}/suspend"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SuspendSubscription | SuspendSubscriptionDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=empty_response,
            error_mapper=suspend_subscription_error_mapper,
            request_options=request_options,
        )

    def update_billing_plan_pricing_schemes(
        self,
        id: str,
        *,
        body: UpdatePricingSchemesRequest | UpdatePricingSchemesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UpdateBillingPlanPricingSchemesErrorBody]:
        """Updates pricing for a plan. For example, you can update a regular billing cycle from $5 per month to $7 per
        month.

        Args:
            id: The ID for the plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/billing/plans/{id}/update-pricing-schemes"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdatePricingSchemesRequest | UpdatePricingSchemesRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=empty_response,
            error_mapper=update_billing_plan_pricing_schemes_error_mapper,
            request_options=request_options,
        )


class AsyncSubscriptionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def activate_billing_plan(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, ActivateBillingPlanErrorBody]:
        """Activates a plan, by ID.

        Args:
            id: The ID of the plan.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/billing/plans/{id}/activate"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=empty_response,
            error_mapper=activate_billing_plan_error_mapper,
            request_options=request_options,
        )

    async def activate_subscription(
        self,
        id: str,
        *,
        body: ActivateSubscriptionRequest | ActivateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, ActivateSubscriptionErrorBody]:
        """Activates the subscription.

        Args:
            id: The ID of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/billing/subscriptions/{id}/activate"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ActivateSubscriptionRequest | ActivateSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=empty_response,
            error_mapper=activate_subscription_error_mapper,
            request_options=request_options,
        )

    async def cancel_subscription(
        self,
        id: str,
        *,
        body: CancelSubscriptionRequest | CancelSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, CancelSubscriptionErrorBody]:
        """Cancels the subscription.

        Args:
            id: The ID of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/billing/subscriptions/{id}/cancel"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancelSubscriptionRequest | CancelSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=empty_response,
            error_mapper=cancel_subscription_error_mapper,
            request_options=request_options,
        )

    async def capture_subscription(
        self,
        id: str,
        *,
        pay_pal_request_id: str | None = None,
        body: CaptureSubscriptionRequest | CaptureSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionTransactionDetails, CaptureSubscriptionErrorBody]:
        """Captures an authorized payment from the subscriber on the subscription.

        Args:
            id: The ID of the subscription.
            pay_pal_request_id: The server stores keys for 72 hours.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/billing/subscriptions/{id}/capture"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str | None]("PayPal-Request-Id", pay_pal_request_id), param[UUID]("Idempotency-Key", uuid4())
            ],
            body=json_body[CaptureSubscriptionRequest | CaptureSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SubscriptionTransactionDetails],
            error_mapper=capture_subscription_error_mapper,
            request_options=request_options,
        )

    async def create_billing_plan(
        self,
        *,
        prefer: str | None = "return=minimal",
        pay_pal_request_id: str | None = None,
        body: PlanRequest | PlanRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BillingPlan, CreateBillingPlanErrorBody]:
        """Creates a plan that defines pricing and billing cycle details for subscriptions.

        Args:
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_request_id: The server stores keys for 72 hours.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/billing/plans"),
            headers=[
                param[str | None]("Prefer", prefer),
                param[str | None]("PayPal-Request-Id", pay_pal_request_id),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[PlanRequest | PlanRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BillingPlan],
            error_mapper=create_billing_plan_error_mapper,
            request_options=request_options,
        )

    async def create_subscription(
        self,
        *,
        prefer: str | None = "return=minimal",
        pay_pal_request_id: str | None = None,
        pay_pal_client_metadata_id: str | None = None,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Subscription, CreateSubscriptionErrorBody]:
        """Creates a subscription.

        Args:
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, status and HATEOAS links. return=representation. The server returns a
                complete resource representation, including the current state of the resource.
            pay_pal_request_id: The server stores keys for 72 hours.
            pay_pal_client_metadata_id: The PayPal Client Metadata Id(CMID) is used to provide device-specific
                information to PayPal's risk engine. This is crucial for transactions that require device-specific risk
                assessments. Merchants typically use the Paypal SDK that automatically submits the CMID or they use
                tools like Fraudnet JS for web or Magnes JS for mobile to generate the CMID on the frontend and then
                pass it to the API as part of the request headers.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/billing/subscriptions"),
            headers=[
                param[str | None]("Prefer", prefer),
                param[str | None]("PayPal-Request-Id", pay_pal_request_id),
                param[str | None]("PayPal-Client-Metadata-Id", pay_pal_client_metadata_id),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[CreateSubscriptionRequest | CreateSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[Subscription],
            error_mapper=create_subscription_error_mapper,
            request_options=request_options,
        )

    async def deactivate_billing_plan(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeactivateBillingPlanErrorBody]:
        """Deactivates a plan, by ID.

        Args:
            id: The ID of the plan.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/billing/plans/{id}/deactivate"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=empty_response,
            error_mapper=deactivate_billing_plan_error_mapper,
            request_options=request_options,
        )

    async def get_billing_plan(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BillingPlan, GetBillingPlanErrorBody]:
        """Shows details for a plan, by ID.

        Args:
            id: The ID of the plan.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/billing/plans/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BillingPlan],
            error_mapper=get_billing_plan_error_mapper,
            request_options=request_options,
        )

    async def get_subscription(
        self, id: str, *, fields: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Subscription, GetSubscriptionErrorBody]:
        """Shows details for a subscription, by ID.

        Args:
            id: The ID of the subscription.
            fields: List of fields that are to be returned in the response. Possible value for fields are
                last_failed_payment and plan.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/billing/subscriptions/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str | None]("fields", fields)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[Subscription],
            error_mapper=get_subscription_error_mapper,
            request_options=request_options,
        )

    async def list_billing_plans(
        self,
        *,
        product_id: str | None = None,
        page_size: int | None = 10,
        page: int | None = 1,
        total_required: bool | None = False,
        prefer: str | None = "return=minimal",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PlanCollection, ListBillingPlansErrorBody]:
        """Lists billing plans.

        Args:
            product_id: Filters the response by a Product ID.
            page_size: The number of items to return in the response.
            page: A non-zero integer which is the start index of the entire list of items to return in the response. The
                combination of ``page=1`` and ``page_size=20`` returns the first 20 items. The combination of ``page=2``
                and ``page_size=20`` returns the next 20 items.
            total_required: Indicates whether to show the total count in the response.
            prefer: The preferred server response upon successful completion of the request. Value is: return=minimal.
                The server returns a minimal response to optimize communication between the API caller and the server. A
                minimal response includes the id, name, description and HATEOAS links. return=representation. The server
                returns a complete resource representation, including the current state of the resource.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/billing/plans"),
            query_params=[
                param[str | None]("product_id", product_id),
                param[int | None]("page_size", page_size),
                param[int | None]("page", page),
                param[bool | None]("total_required", total_required),
            ],
            headers=[param[str | None]("Prefer", prefer)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[PlanCollection],
            error_mapper=list_billing_plans_error_mapper,
            request_options=request_options,
        )

    async def list_subscription_transactions(
        self, id: str, start_time: str, end_time: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransactionsList, ListSubscriptionTransactionsErrorBody]:
        """Lists transactions for a subscription.

        Args:
            id: The ID of the subscription.
            start_time: The start time of the range of transactions to list.
            end_time: The end time of the range of transactions to list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/billing/subscriptions/{id}/transactions"),
            path_params=[param[str]("id", id)],
            query_params=[param[str]("start_time", start_time), param[str]("end_time", end_time)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[TransactionsList],
            error_mapper=list_subscription_transactions_error_mapper,
            request_options=request_options,
        )

    async def list_subscriptions(
        self,
        *,
        plan_ids: str | None = None,
        statuses: str | None = None,
        created_after: str | None = None,
        created_before: str | None = None,
        status_updated_before: str | None = None,
        status_updated_after: str | None = None,
        filter: str | None = None,
        page_size: int | None = 10,
        page: int | None = 1,
        customer_ids: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionCollection, ListSubscriptionsErrorBody]:
        """List all subscriptions for merchant account.

        Args:
            plan_ids: Filters the response by list of plan IDs. Filter supports upto 70 plan IDs. URLs should not exceed
                a length of 2000 characters.
            statuses: Filters the response by list of subscription statuses.
            created_after: Filters the response by subscription creation start time for a range of subscriptions.
            created_before: Filters the response by subscription creation end time for a range of subscriptions.
            status_updated_before: Filters the response by status update start time for a range of subscriptions.
            status_updated_after: Filters the response by status update end time for a range of subscriptions.
            filter: Filter the response using complex expressions that could use comparison operators like ge, gt, le,
                lt and logical operators such as 'and' and 'or'.
            page_size: The number of items to return in the response.
            page: A non-zero integer which is the start index of the entire list of items to return in the response. The
                combination of ``page=1`` and ``page_size=20`` returns the first 20 items. The combination of ``page=2``
                and ``page_size=20`` returns the next 20 items.
            customer_ids: Filters the response by comma separated vault customer IDs (FSS subscriptions only).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/billing/subscriptions"),
            query_params=[
                param[str | None]("plan_ids", plan_ids),
                param[str | None]("statuses", statuses),
                param[str | None]("created_after", created_after),
                param[str | None]("created_before", created_before),
                param[str | None]("status_updated_before", status_updated_before),
                param[str | None]("status_updated_after", status_updated_after),
                param[str | None]("filter", filter),
                param[int | None]("page_size", page_size),
                param[int | None]("page", page),
                param[list[str] | None]("customer_ids", customer_ids),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SubscriptionCollection],
            error_mapper=list_subscriptions_error_mapper,
            request_options=request_options,
        )

    async def patch_billing_plan(
        self,
        id: str,
        *,
        body: list[Patch | PatchDict] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PatchBillingPlanErrorBody]:
        """Updates a plan with the ``CREATED`` or ``ACTIVE`` status. For an ``INACTIVE`` plan, you can make only status
        updates. You can patch these attributes and objects: Attribute or object Operations description replace
        payment_preferences.auto_bill_outstanding replace taxes.percentage replace
        payment_preferences.payment_failure_threshold replace payment_preferences.setup_fee replace
        payment_preferences.setup_fee_failure_action replace name replace

        Args:
            id: The ID of the plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/billing/plans/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[list[Patch | PatchDict] | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=empty_response,
            error_mapper=patch_billing_plan_error_mapper,
            request_options=request_options,
        )

    async def patch_subscription(
        self,
        id: str,
        *,
        body: list[Patch | PatchDict] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PatchSubscriptionErrorBody]:
        """Updates a subscription which could be in ACTIVE or SUSPENDED status. You can override plan level default
        attributes by providing customised values for plan path in the patch request. You cannot update attributes that
        have already completed (Example - trial cycles can’t be updated if completed). Once overridden, changes to plan
        resource will not impact subscription. Any price update will not impact billing cycles within next 10 days
        (Applicable only for subscriptions funded by PayPal account). Following are the fields eligible for patch.
        Attribute or object Operations billing_info.outstanding_balance replace custom_id add,replace
        plan.billing_cycles[@sequence==n]. pricing_scheme.fixed_price add,replace plan.billing_cycles[@sequence==n].
        pricing_scheme.tiers replace plan.billing_cycles[@sequence==n]. total_cycles replace plan.payment_preferences.
        auto_bill_outstanding replace plan.payment_preferences. payment_failure_threshold replace plan.taxes.inclusive
        add,replace plan.taxes.percentage add,replace shipping_amount add,replace start_time replace
        subscriber.shipping_address add,replace subscriber.payment_source (for subscriptions funded by card payments)
        replace

        Args:
            id: The ID for the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/billing/subscriptions/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[list[Patch | PatchDict] | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=empty_response,
            error_mapper=patch_subscription_error_mapper,
            request_options=request_options,
        )

    async def revise_subscription(
        self,
        id: str,
        *,
        body: ModifySubscriptionRequest | ModifySubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ModifySubscriptionResponse, ReviseSubscriptionErrorBody]:
        """Updates the quantity of the product or service in a subscription. You can also use this method to switch the
        plan and update the ``shipping_amount``, ``shipping_address`` values for the subscription. This type of update
        requires the buyer's consent.

        Args:
            id: The ID of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/billing/subscriptions/{id}/revise"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ModifySubscriptionRequest | ModifySubscriptionRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ModifySubscriptionResponse],
            error_mapper=revise_subscription_error_mapper,
            request_options=request_options,
        )

    async def suspend_subscription(
        self,
        id: str,
        *,
        body: SuspendSubscription | SuspendSubscriptionDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SuspendSubscriptionErrorBody]:
        """Suspends the subscription.

        Args:
            id: The ID of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/billing/subscriptions/{id}/suspend"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SuspendSubscription | SuspendSubscriptionDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=empty_response,
            error_mapper=suspend_subscription_error_mapper,
            request_options=request_options,
        )

    async def update_billing_plan_pricing_schemes(
        self,
        id: str,
        *,
        body: UpdatePricingSchemesRequest | UpdatePricingSchemesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UpdateBillingPlanPricingSchemesErrorBody]:
        """Updates pricing for a plan. For example, you can update a regular billing cycle from $5 per month to $7 per
        month.

        Args:
            id: The ID for the plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/billing/plans/{id}/update-pricing-schemes"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdatePricingSchemesRequest | UpdatePricingSchemesRequestDict | None](body),
            auth_scheme=self._auth.oauth2,
            decoder=empty_response,
            error_mapper=update_billing_plan_pricing_schemes_error_mapper,
            request_options=request_options,
        )
