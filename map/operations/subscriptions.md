<!-- Generated file — do not edit; regenerated with the SDK. -->

# Subscriptions — operations

Accessor: `client.subscriptions` · Source: `paypal/apis/subscriptions.py` · 17 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.subscriptions.activate_billing_plan

- **Route**: `POST /v1/billing/plans/{id}/activate`
- **Auth**: `oauth2`
- **Signature**: `def activate_billing_plan(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, ActivateBillingPlanErrorBody]`
- **Error**: `ActivateBillingPlanErrorBody` — **Case A (typed)**
- **Error arms**: `SubscriptionError` [401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ActivateBillingPlanErrorBody` | `paypal/errors/activate_billing_plan_error.py` |
| `SubscriptionError` | `paypal/models/subscription_error.py` |

### client.subscriptions.activate_subscription

- **Route**: `POST /v1/billing/subscriptions/{id}/activate`
- **Auth**: `oauth2`
- **Signature**: `def activate_subscription(id: str, *, body: ActivateSubscriptionRequest | ActivateSubscriptionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, ActivateSubscriptionErrorBody]`
- **Error**: `ActivateSubscriptionErrorBody` — **Case A (typed)**
- **Error arms**: `SubscriptionError` [400, 401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ActivateSubscriptionRequest` | `paypal/models/activate_subscription_request.py` |
| `ActivateSubscriptionRequestDict` | `paypal/models/activate_subscription_request.py` |
| `ActivateSubscriptionErrorBody` | `paypal/errors/activate_subscription_error.py` |
| `SubscriptionError` | `paypal/models/subscription_error.py` |

### client.subscriptions.cancel_subscription

- **Route**: `POST /v1/billing/subscriptions/{id}/cancel`
- **Auth**: `oauth2`
- **Signature**: `def cancel_subscription(id: str, *, body: CancelSubscriptionRequest | CancelSubscriptionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, CancelSubscriptionErrorBody]`
- **Error**: `CancelSubscriptionErrorBody` — **Case A (typed)**
- **Error arms**: `SubscriptionError` [400, 401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelSubscriptionRequest` | `paypal/models/cancel_subscription_request.py` |
| `CancelSubscriptionRequestDict` | `paypal/models/cancel_subscription_request.py` |
| `CancelSubscriptionErrorBody` | `paypal/errors/cancel_subscription_error.py` |
| `SubscriptionError` | `paypal/models/subscription_error.py` |

### client.subscriptions.capture_subscription

- **Route**: `POST /v1/billing/subscriptions/{id}/capture`
- **Auth**: `oauth2`
- **Signature**: `def capture_subscription(id: str, *, pay_pal_request_id: str | None = None, body: CaptureSubscriptionRequest | CaptureSubscriptionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `pay_pal_request_id` — header `PayPal-Request-Id` · `body` — JSON body
- **Returns (parsed)**: `SubscriptionTransactionDetails`
- **Returns (raw)**: `ApiResult[SubscriptionTransactionDetails, CaptureSubscriptionErrorBody]`
- **Error**: `CaptureSubscriptionErrorBody` — **Case A (typed)**
- **Error arms**: `SubscriptionError` [400, 401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CaptureSubscriptionRequest` | `paypal/models/capture_subscription_request.py` |
| `CaptureSubscriptionRequestDict` | `paypal/models/capture_subscription_request.py` |
| `SubscriptionTransactionDetails` | `paypal/models/subscription_transaction_details.py` |
| `CaptureSubscriptionErrorBody` | `paypal/errors/capture_subscription_error.py` |
| `SubscriptionError` | `paypal/models/subscription_error.py` |

### client.subscriptions.create_billing_plan

- **Route**: `POST /v1/billing/plans`
- **Auth**: `oauth2`
- **Signature**: `def create_billing_plan(*, prefer: str | None = "return=minimal", pay_pal_request_id: str | None = None, body: PlanRequest | PlanRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `prefer` — header `Prefer` · `pay_pal_request_id` — header `PayPal-Request-Id` · `body` — JSON body
- **Returns (parsed)**: `BillingPlan`
- **Returns (raw)**: `ApiResult[BillingPlan, CreateBillingPlanErrorBody]`
- **Error**: `CreateBillingPlanErrorBody` — **Case A (typed)**
- **Error arms**: `SubscriptionError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PlanRequest` | `paypal/models/plan_request.py` |
| `PlanRequestDict` | `paypal/models/plan_request.py` |
| `BillingPlan` | `paypal/models/billing_plan.py` |
| `CreateBillingPlanErrorBody` | `paypal/errors/create_billing_plan_error.py` |
| `SubscriptionError` | `paypal/models/subscription_error.py` |

### client.subscriptions.create_subscription

- **Route**: `POST /v1/billing/subscriptions`
- **Auth**: `oauth2`
- **Signature**: `def create_subscription(*, prefer: str | None = "return=minimal", pay_pal_request_id: str | None = None, pay_pal_client_metadata_id: str | None = None, body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `prefer` — header `Prefer` · `pay_pal_request_id` — header `PayPal-Request-Id` · `pay_pal_client_metadata_id` — header `PayPal-Client-Metadata-Id` · `body` — JSON body
- **Returns (parsed)**: `Subscription`
- **Returns (raw)**: `ApiResult[Subscription, CreateSubscriptionErrorBody]`
- **Error**: `CreateSubscriptionErrorBody` — **Case A (typed)**
- **Error arms**: `SubscriptionError` [400, 401, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateSubscriptionRequest` | `paypal/models/create_subscription_request.py` |
| `CreateSubscriptionRequestDict` | `paypal/models/create_subscription_request.py` |
| `Subscription` | `paypal/models/subscription.py` |
| `CreateSubscriptionErrorBody` | `paypal/errors/create_subscription_error.py` |
| `SubscriptionError` | `paypal/models/subscription_error.py` |

### client.subscriptions.deactivate_billing_plan

- **Route**: `POST /v1/billing/plans/{id}/deactivate`
- **Auth**: `oauth2`
- **Signature**: `def deactivate_billing_plan(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeactivateBillingPlanErrorBody]`
- **Error**: `DeactivateBillingPlanErrorBody` — **Case A (typed)**
- **Error arms**: `SubscriptionError` [401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeactivateBillingPlanErrorBody` | `paypal/errors/deactivate_billing_plan_error.py` |
| `SubscriptionError` | `paypal/models/subscription_error.py` |

### client.subscriptions.get_billing_plan

- **Route**: `GET /v1/billing/plans/{id}`
- **Auth**: `oauth2`
- **Signature**: `def get_billing_plan(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `BillingPlan`
- **Returns (raw)**: `ApiResult[BillingPlan, GetBillingPlanErrorBody]`
- **Error**: `GetBillingPlanErrorBody` — **Case A (typed)**
- **Error arms**: `SubscriptionError` [401, 403, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BillingPlan` | `paypal/models/billing_plan.py` |
| `GetBillingPlanErrorBody` | `paypal/errors/get_billing_plan_error.py` |
| `SubscriptionError` | `paypal/models/subscription_error.py` |

### client.subscriptions.get_subscription

- **Route**: `GET /v1/billing/subscriptions/{id}`
- **Auth**: `oauth2`
- **Signature**: `def get_subscription(id: str, *, fields: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `fields` — query
- **Returns (parsed)**: `Subscription`
- **Returns (raw)**: `ApiResult[Subscription, GetSubscriptionErrorBody]`
- **Error**: `GetSubscriptionErrorBody` — **Case A (typed)**
- **Error arms**: `SubscriptionError` [401, 403, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Subscription` | `paypal/models/subscription.py` |
| `GetSubscriptionErrorBody` | `paypal/errors/get_subscription_error.py` |
| `SubscriptionError` | `paypal/models/subscription_error.py` |

### client.subscriptions.list_billing_plans

- **Route**: `GET /v1/billing/plans`
- **Auth**: `oauth2`
- **Signature**: `def list_billing_plans(*, product_id: str | None = None, page_size: int | None = 10, page: int | None = 1, total_required: bool | None = False, prefer: str | None = "return=minimal", request_options: RequestOptionsOrDict | None = None)`
- **Params**: `product_id` — query · `page_size` — query · `page` — query · `total_required` — query · `prefer` — header `Prefer`
- **Returns (parsed)**: `PlanCollection`
- **Returns (raw)**: `ApiResult[PlanCollection, ListBillingPlansErrorBody]`
- **Error**: `ListBillingPlansErrorBody` — **Case A (typed)**
- **Error arms**: `SubscriptionError` [400, 401, 403, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PlanCollection` | `paypal/models/plan_collection.py` |
| `ListBillingPlansErrorBody` | `paypal/errors/list_billing_plans_error.py` |
| `SubscriptionError` | `paypal/models/subscription_error.py` |

### client.subscriptions.list_subscription_transactions

- **Route**: `GET /v1/billing/subscriptions/{id}/transactions`
- **Auth**: `oauth2`
- **Signature**: `def list_subscription_transactions(id: str, start_time: str, end_time: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `start_time`, `end_time`
- **Params**: `id` — path · `start_time` — query · `end_time` — query
- **Returns (parsed)**: `TransactionsList`
- **Returns (raw)**: `ApiResult[TransactionsList, ListSubscriptionTransactionsErrorBody]`
- **Error**: `ListSubscriptionTransactionsErrorBody` — **Case A (typed)**
- **Error arms**: `SubscriptionError` [400, 401, 403, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TransactionsList` | `paypal/models/transactions_list.py` |
| `ListSubscriptionTransactionsErrorBody` | `paypal/errors/list_subscription_transactions_error.py` |
| `SubscriptionError` | `paypal/models/subscription_error.py` |

### client.subscriptions.list_subscriptions

- **Route**: `GET /v1/billing/subscriptions`
- **Auth**: `oauth2`
- **Signature**: `def list_subscriptions(*, plan_ids: str | None = None, statuses: str | None = None, created_after: str | None = None, created_before: str | None = None, status_updated_before: str | None = None, status_updated_after: str | None = None, filter: str | None = None, page_size: int | None = 10, page: int | None = 1, customer_ids: list[str] | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `plan_ids` — query · `statuses` — query · `created_after` — query · `created_before` — query · `status_updated_before` — query · `status_updated_after` — query · `filter` — query · `page_size` — query · `page` — query · `customer_ids` — query
- **Returns (parsed)**: `SubscriptionCollection`
- **Returns (raw)**: `ApiResult[SubscriptionCollection, ListSubscriptionsErrorBody]`
- **Error**: `ListSubscriptionsErrorBody` — **Case A (typed)**
- **Error arms**: `SubscriptionError` [400, 401, 403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubscriptionCollection` | `paypal/models/subscription_collection.py` |
| `ListSubscriptionsErrorBody` | `paypal/errors/list_subscriptions_error.py` |
| `SubscriptionError` | `paypal/models/subscription_error.py` |

### client.subscriptions.patch_billing_plan

- **Route**: `PATCH /v1/billing/plans/{id}`
- **Auth**: `oauth2`
- **Signature**: `def patch_billing_plan(id: str, *, body: list[Patch | PatchDict] | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, PatchBillingPlanErrorBody]`
- **Error**: `PatchBillingPlanErrorBody` — **Case A (typed)**
- **Error arms**: `SubscriptionError` [400, 401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Patch` | `paypal/models/patch.py` |
| `PatchDict` | `paypal/models/patch.py` |
| `PatchBillingPlanErrorBody` | `paypal/errors/patch_billing_plan_error.py` |
| `SubscriptionError` | `paypal/models/subscription_error.py` |

### client.subscriptions.patch_subscription

- **Route**: `PATCH /v1/billing/subscriptions/{id}`
- **Auth**: `oauth2`
- **Signature**: `def patch_subscription(id: str, *, body: list[Patch | PatchDict] | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, PatchSubscriptionErrorBody]`
- **Error**: `PatchSubscriptionErrorBody` — **Case A (typed)**
- **Error arms**: `SubscriptionError` [400, 401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Patch` | `paypal/models/patch.py` |
| `PatchDict` | `paypal/models/patch.py` |
| `PatchSubscriptionErrorBody` | `paypal/errors/patch_subscription_error.py` |
| `SubscriptionError` | `paypal/models/subscription_error.py` |

### client.subscriptions.revise_subscription

- **Route**: `POST /v1/billing/subscriptions/{id}/revise`
- **Auth**: `oauth2`
- **Signature**: `def revise_subscription(id: str, *, body: ModifySubscriptionRequest | ModifySubscriptionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `ModifySubscriptionResponse`
- **Returns (raw)**: `ApiResult[ModifySubscriptionResponse, ReviseSubscriptionErrorBody]`
- **Error**: `ReviseSubscriptionErrorBody` — **Case A (typed)**
- **Error arms**: `SubscriptionError` [400, 401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ModifySubscriptionRequest` | `paypal/models/modify_subscription_request.py` |
| `ModifySubscriptionRequestDict` | `paypal/models/modify_subscription_request.py` |
| `ModifySubscriptionResponse` | `paypal/models/modify_subscription_response.py` |
| `ReviseSubscriptionErrorBody` | `paypal/errors/revise_subscription_error.py` |
| `SubscriptionError` | `paypal/models/subscription_error.py` |

### client.subscriptions.suspend_subscription

- **Route**: `POST /v1/billing/subscriptions/{id}/suspend`
- **Auth**: `oauth2`
- **Signature**: `def suspend_subscription(id: str, *, body: SuspendSubscription | SuspendSubscriptionDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SuspendSubscriptionErrorBody]`
- **Error**: `SuspendSubscriptionErrorBody` — **Case A (typed)**
- **Error arms**: `SubscriptionError` [400, 401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SuspendSubscription` | `paypal/models/suspend_subscription.py` |
| `SuspendSubscriptionDict` | `paypal/models/suspend_subscription.py` |
| `SuspendSubscriptionErrorBody` | `paypal/errors/suspend_subscription_error.py` |
| `SubscriptionError` | `paypal/models/subscription_error.py` |

### client.subscriptions.update_billing_plan_pricing_schemes

- **Route**: `POST /v1/billing/plans/{id}/update-pricing-schemes`
- **Auth**: `oauth2`
- **Signature**: `def update_billing_plan_pricing_schemes(id: str, *, body: UpdatePricingSchemesRequest | UpdatePricingSchemesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, UpdateBillingPlanPricingSchemesErrorBody]`
- **Error**: `UpdateBillingPlanPricingSchemesErrorBody` — **Case A (typed)**
- **Error arms**: `SubscriptionError` [400, 401, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdatePricingSchemesRequest` | `paypal/models/update_pricing_schemes_request.py` |
| `UpdatePricingSchemesRequestDict` | `paypal/models/update_pricing_schemes_request.py` |
| `UpdateBillingPlanPricingSchemesErrorBody` | `paypal/errors/update_billing_plan_pricing_schemes_error.py` |
| `SubscriptionError` | `paypal/models/subscription_error.py` |

