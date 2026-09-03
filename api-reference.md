# Reference

**Parsed** endpoints return the typed payload and raise `ApiError` on a documented non-2xx. For the raw endpoints, see [Raw API Reference](raw-api-reference.md).

> Source: [PaypalClient](paypal/client.py)

## Orders

> Source: [Orders](paypal/apis/orders.py)

<details>
<summary><code>def authorize_order(id: str, *, pay_pal_mock_response: str | None = None, pay_pal_request_id: str | None = None, prefer: str | None = "return=minimal", pay_pal_client_metadata_id: str | None = None, pay_pal_auth_assertion: str | None = None, body: OrderAuthorizeRequest | OrderAuthorizeRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> OrderAuthorizeResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Authorizes payment for an order. To successfully authorize payment for an order, the buyer must first approve the order or a valid payment_source must be provided in the request. A buyer can approve the order upon being redirected to the rel:approve URL that was returned in the HATEOAS links in the create order response. Note: For error handling and troubleshooting, see Orders v2 errors.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.orders.authorize_order(id)
    # TODO: Handle 'response' of type OrderAuthorizeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AuthorizeOrderErrorBody
```

**Async**

```python
try:
    response = await async_client.orders.authorize_order(id)
    # TODO: Handle 'response' of type OrderAuthorizeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AuthorizeOrderErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the order for which to authorize. |
| <code>pay_pal_mock_response</code> | <code>str \| None</code> | PayPal's REST API uses a request header to invoke negative testing in the sandbox. This header configures the sandbox into a negative testing state for transactions that include the merchant.<br>**Default**: <code>None</code> |
| <code>pay_pal_request_id</code> | <code>str \| None</code> | The server stores keys for 6 hours. The API callers can request the times to up to 72 hours by speaking to their Account Manager. It is mandatory for all single-step create order calls (E.g. Create Order Request with payment source information like Card, PayPal.vault_id, PayPal.billing_agreement_id, etc).<br>**Default**: <code>None</code> |
| <code>prefer</code> | <code>str \| None</code> | The preferred server response upon successful completion of the request. Value is: return=minimal. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the id, status and HATEOAS links. return=representation. The server returns a complete resource representation, including the current state of the resource.<br>**Default**: <code>"return=minimal"</code> |
| <code>pay_pal_client_metadata_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pay_pal_auth_assertion</code> | <code>str \| None</code> | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see PayPal-Auth-Assertion.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[OrderAuthorizeRequest](paypal/models/order_authorize_request.py) \| [OrderAuthorizeRequestDict](paypal/models/order_authorize_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[OrderAuthorizeResponse](paypal/models/order_authorize_response.py)</code> -- A successful response to an idempotent request returns the HTTP `200 OK` status code with a JSON response body that shows authorized payment details.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[AuthorizeOrderErrorBody](paypal/errors/authorize_order_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 422, 500 | <code>[Error](paypal/models/error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def capture_order(id: str, *, pay_pal_mock_response: str | None = None, pay_pal_request_id: str | None = None, prefer: str | None = "return=minimal", pay_pal_client_metadata_id: str | None = None, pay_pal_auth_assertion: str | None = None, body: OrderCaptureRequest | OrderCaptureRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> Order</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Captures payment for an order. To successfully capture payment for an order, the buyer must first approve the order or a valid payment_source must be provided in the request. A buyer can approve the order upon being redirected to the rel:approve URL that was returned in the HATEOAS links in the create order response. Note: For error handling and troubleshooting, see Orders v2 errors.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.orders.capture_order(id)
    # TODO: Handle 'response' of type Order
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CaptureOrderErrorBody
```

**Async**

```python
try:
    response = await async_client.orders.capture_order(id)
    # TODO: Handle 'response' of type Order
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CaptureOrderErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the order for which to capture a payment. |
| <code>pay_pal_mock_response</code> | <code>str \| None</code> | PayPal's REST API uses a request header to invoke negative testing in the sandbox. This header configures the sandbox into a negative testing state for transactions that include the merchant.<br>**Default**: <code>None</code> |
| <code>pay_pal_request_id</code> | <code>str \| None</code> | The server stores keys for 6 hours. The API callers can request the times to up to 72 hours by speaking to their Account Manager. It is mandatory for all single-step create order calls (E.g. Create Order Request with payment source information like Card, PayPal.vault_id, PayPal.billing_agreement_id, etc).<br>**Default**: <code>None</code> |
| <code>prefer</code> | <code>str \| None</code> | The preferred server response upon successful completion of the request. Value is: return=minimal. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the id, status and HATEOAS links. return=representation. The server returns a complete resource representation, including the current state of the resource.<br>**Default**: <code>"return=minimal"</code> |
| <code>pay_pal_client_metadata_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pay_pal_auth_assertion</code> | <code>str \| None</code> | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see PayPal-Auth-Assertion.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[OrderCaptureRequest](paypal/models/order_capture_request.py) \| [OrderCaptureRequestDict](paypal/models/order_capture_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Order](paypal/models/order.py)</code> -- A successful response to an idempotent request returns the HTTP `200 OK` status code with a JSON response body that shows captured payment details.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[CaptureOrderErrorBody](paypal/errors/capture_order_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 422, 500 | <code>[Error](paypal/models/error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def confirm_order(id: str, *, pay_pal_client_metadata_id: str | None = None, pay_pal_auth_assertion: str | None = None, prefer: str | None = "return=minimal", body: ConfirmOrderRequest | ConfirmOrderRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> Order</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Payer confirms their intent to pay for the the Order with the given payment source.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.orders.confirm_order(id)
    # TODO: Handle 'response' of type Order
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConfirmOrderErrorBody
```

**Async**

```python
try:
    response = await async_client.orders.confirm_order(id)
    # TODO: Handle 'response' of type Order
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConfirmOrderErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the order for which the payer confirms their intent to pay. |
| <code>pay_pal_client_metadata_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pay_pal_auth_assertion</code> | <code>str \| None</code> | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see PayPal-Auth-Assertion.<br>**Default**: <code>None</code> |
| <code>prefer</code> | <code>str \| None</code> | The preferred server response upon successful completion of the request. Value is: return=minimal. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the id, status and HATEOAS links. return=representation. The server returns a complete resource representation, including the current state of the resource.<br>**Default**: <code>"return=minimal"</code> |
| <code>body</code> | <code>[ConfirmOrderRequest](paypal/models/confirm_order_request.py) \| [ConfirmOrderRequestDict](paypal/models/confirm_order_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Order](paypal/models/order.py)</code> -- A successful request indicates that the payment source was added to the Order. A successful request returns the HTTP `200 OK` status code with a JSON response body that shows order details.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[ConfirmOrderErrorBody](paypal/errors/confirm_order_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 422, 500 | <code>[Error](paypal/models/error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_order(body: OrderRequest | OrderRequestDict, *, pay_pal_mock_response: str | None = None, pay_pal_request_id: str | None = None, pay_pal_partner_attribution_id: str | None = None, pay_pal_client_metadata_id: str | None = None, prefer: str | None = "return=minimal", pay_pal_auth_assertion: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Order</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates an order. Merchants and partners can add Level 2 and 3 data to payments to reduce risk and payment processing costs. For more information about processing payments, see checkout or multiparty checkout. Note: For error handling and troubleshooting, see Orders v2 errors.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.orders.create_order(body)
    # TODO: Handle 'response' of type Order
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateOrderErrorBody
```

**Async**

```python
try:
    response = await async_client.orders.create_order(body)
    # TODO: Handle 'response' of type Order
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateOrderErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[OrderRequest](paypal/models/order_request.py) \| [OrderRequestDict](paypal/models/order_request.py)</code> | The request body. |
| <code>pay_pal_mock_response</code> | <code>str \| None</code> | PayPal's REST API uses a request header to invoke negative testing in the sandbox. This header configures the sandbox into a negative testing state for transactions that include the merchant.<br>**Default**: <code>None</code> |
| <code>pay_pal_request_id</code> | <code>str \| None</code> | The server stores keys for 6 hours. The API callers can request the times to up to 72 hours by speaking to their Account Manager. It is mandatory for all single-step create order calls (E.g. Create Order Request with payment source information like Card, PayPal.vault_id, PayPal.billing_agreement_id, etc).<br>**Default**: <code>None</code> |
| <code>pay_pal_partner_attribution_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pay_pal_client_metadata_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>prefer</code> | <code>str \| None</code> | The preferred server response upon successful completion of the request. Value is: return=minimal. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the id, status and HATEOAS links. return=representation. The server returns a complete resource representation, including the current state of the resource.<br>**Default**: <code>"return=minimal"</code> |
| <code>pay_pal_auth_assertion</code> | <code>str \| None</code> | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see PayPal-Auth-Assertion.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Order](paypal/models/order.py)</code> -- A successful response to an idempotent request returns the HTTP `200 OK` status code with a JSON response body that shows order details.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[CreateOrderErrorBody](paypal/errors/create_order_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 422 | <code>[Error](paypal/models/error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_order_tracking(id: str, body: OrderTrackerRequest | OrderTrackerRequestDict, *, pay_pal_auth_assertion: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Order</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Adds tracking information for an Order.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.orders.create_order_tracking(id, body)
    # TODO: Handle 'response' of type Order
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateOrderTrackingErrorBody
```

**Async**

```python
try:
    response = await async_client.orders.create_order_tracking(id, body)
    # TODO: Handle 'response' of type Order
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateOrderTrackingErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the order that the tracking information is associated with. |
| <code>body</code> | <code>[OrderTrackerRequest](paypal/models/order_tracker_request.py) \| [OrderTrackerRequestDict](paypal/models/order_tracker_request.py)</code> | The request body. |
| <code>pay_pal_auth_assertion</code> | <code>str \| None</code> | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see PayPal-Auth-Assertion.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Order](paypal/models/order.py)</code> -- A successful response to an idempotent request returns the HTTP `200 OK` status code with a JSON response body that shows tracker details.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[CreateOrderTrackingErrorBody](paypal/errors/create_order_tracking_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 422, 500 | <code>[Error](paypal/models/error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_order(id: str, *, fields: str | None = None, pay_pal_mock_response: str | None = None, pay_pal_auth_assertion: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Order</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Shows details for an order, by ID. Note: For error handling and troubleshooting, see Orders v2 errors.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.orders.get_order(id)
    # TODO: Handle 'response' of type Order
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetOrderErrorBody
```

**Async**

```python
try:
    response = await async_client.orders.get_order(id)
    # TODO: Handle 'response' of type Order
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetOrderErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the order for which to show details. |
| <code>fields</code> | <code>str \| None</code> | A comma-separated list of fields that should be returned for the order. Valid filter field is `payment_source`.<br>**Default**: <code>None</code> |
| <code>pay_pal_mock_response</code> | <code>str \| None</code> | PayPal's REST API uses a request header to invoke negative testing in the sandbox. This header configures the sandbox into a negative testing state for transactions that include the merchant.<br>**Default**: <code>None</code> |
| <code>pay_pal_auth_assertion</code> | <code>str \| None</code> | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see PayPal-Auth-Assertion.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Order](paypal/models/order.py)</code> -- A successful request returns the HTTP `200 OK` status code and a JSON response body that shows order details.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[GetOrderErrorBody](paypal/errors/get_order_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 404 | <code>[Error](paypal/models/error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def patch_order(id: str, *, pay_pal_mock_response: str | None = None, pay_pal_auth_assertion: str | None = None, body: list[Patch | PatchDict] | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates an order with a `CREATED` or `APPROVED` status. You cannot update an order with the `COMPLETED` status.<br/><br/>To make an update, you must provide a `reference_id`. If you omit this value with an order that contains only one purchase unit, PayPal sets the value to `default` which enables you to use the path: <code>\"/purchase_units/@reference_id=='default'/{attribute-or-object}\"</code>. Merchants and partners can add Level 2 and 3 data to payments to reduce risk and payment processing costs. For more information about processing payments, see <a href="https://developer.paypal.com/docs/checkout/advanced/processing/">checkout</a> or <a href="https://developer.paypal.com/docs/multiparty/checkout/advanced/processing/">multiparty checkout</a>.<blockquote><strong>Note:</strong> For error handling and troubleshooting, see <a href="https://developer.paypal.com/api/rest/reference/orders/v2/errors/#patch-order">Orders v2 errors</a>.</blockquote>Patchable attributes or objects:<br/><br/><table><thead><th>Attribute</th><th>Op</th><th>Notes</th></thead><tbody><tr><td><code>intent</code></td><td>replace</td><td></td></tr><tr><td><code>payer</code></td><td>replace, add</td><td>Using replace op for <code>payer</code> will replace the whole <code>payer</code> object with the value sent in request.</td></tr><tr><td><code>purchase_units</code></td><td>replace, add</td><td></td></tr><tr><td><code>purchase_units[].custom_id</code></td><td>replace, add, remove</td><td></td></tr><tr><td><code>purchase_units[].description</code></td><td>replace, add, remove</td><td></td></tr><tr><td><code>purchase_units[].payee.email</code></td><td>replace</td><td></td></tr><tr><td><code>purchase_units[].shipping.name</code></td><td>replace, add</td><td></td></tr><tr><td><code>purchase_units[].shipping.email_address</code></td><td>replace, add</td><td></td></tr><tr><td><code>purchase_units[].shipping.phone_number</code></td><td>replace, add</td><td></td></tr><tr><td><code>purchase_units[].shipping.options</code></td><td>replace, add</td><td></td></tr><tr><td><code>purchase_units[].shipping.address</code></td><td>replace, add</td><td></td></tr><tr><td><code>purchase_units[].shipping.type</code></td><td>replace, add</td><td></td></tr><tr><td><code>purchase_units[].soft_descriptor</code></td><td>replace, remove</td><td></td></tr><tr><td><code>purchase_units[].amount</code></td><td>replace</td><td></td></tr><tr><td><code>purchase_units[].items</code></td><td>replace, add, remove</td><td></td></tr><tr><td><code>purchase_units[].invoice_id</code></td><td>replace, add, remove</td><td></td></tr><tr><td><code>purchase_units[].payment_instruction</code></td><td>replace</td><td></td></tr><tr><td><code>purchase_units[].payment_instruction.disbursement_mode</code></td><td>replace</td><td>By default, <code>disbursement_mode</code> is <code>INSTANT</code>.</td></tr><tr><td><code>purchase_units[].payment_instruction.payee_receivable_fx_rate_id</code></td><td>replace, add, remove</td><td></td></tr><tr><td><code>purchase_units[].payment_instruction.platform_fees</code></td><td>replace, add, remove</td><td></td></tr><tr><td><code>purchase_units[].supplementary_data.airline</code></td><td>replace, add, remove</td><td></td></tr><tr><td><code>purchase_units[].supplementary_data.card</code></td><td>replace, add, remove</td><td></td></tr><tr><td><code>application_context.client_configuration</code></td><td>replace, add</td><td></td></tr></tbody></table>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.orders.patch_order(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PatchOrderErrorBody
```

**Async**

```python
try:
    await async_client.orders.patch_order(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PatchOrderErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the order to update. |
| <code>pay_pal_mock_response</code> | <code>str \| None</code> | PayPal's REST API uses a request header to invoke negative testing in the sandbox. This header configures the sandbox into a negative testing state for transactions that include the merchant.<br>**Default**: <code>None</code> |
| <code>pay_pal_auth_assertion</code> | <code>str \| None</code> | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see PayPal-Auth-Assertion.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>list&#91;[Patch](paypal/models/patch.py) \| [PatchDict](paypal/models/patch.py)&#93; \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[PatchOrderErrorBody](paypal/errors/patch_order_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 404, 422 | <code>[Error](paypal/models/error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_order_tracking(id: str, tracker_id: str, *, pay_pal_auth_assertion: str | None = None, body: list[Patch | PatchDict] | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates or cancels the tracking information for a PayPal order, by ID. Updatable attributes or objects: Attribute Op Notes items replace Using replace op for items will replace the entire items object with the value sent in request. notify_payer replace, add status replace Only patching status to CANCELLED is currently supported.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.orders.update_order_tracking(id, tracker_id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateOrderTrackingErrorBody
```

**Async**

```python
try:
    await async_client.orders.update_order_tracking(id, tracker_id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateOrderTrackingErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the order that the tracking information is associated with. |
| <code>tracker_id</code> | <code>str</code> | The order tracking ID. |
| <code>pay_pal_auth_assertion</code> | <code>str \| None</code> | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see PayPal-Auth-Assertion.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>list&#91;[Patch](paypal/models/patch.py) \| [PatchDict](paypal/models/patch.py)&#93; \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[UpdateOrderTrackingErrorBody](paypal/errors/update_order_tracking_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 422, 500 | <code>[Error](paypal/models/error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Payments

> Source: [Payments](paypal/apis/payments.py)

<details>
<summary><code>def capture_authorized_payment(authorization_id: str, *, pay_pal_mock_response: str | None = None, pay_pal_request_id: str | None = None, prefer: str | None = "return=minimal", pay_pal_auth_assertion: str | None = None, body: CaptureRequest | CaptureRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> CapturedPayment</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Captures an authorized payment, by ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payments.capture_authorized_payment(authorization_id)
    # TODO: Handle 'response' of type CapturedPayment
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CaptureAuthorizedPaymentErrorBody
```

**Async**

```python
try:
    response = await async_client.payments.capture_authorized_payment(authorization_id)
    # TODO: Handle 'response' of type CapturedPayment
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CaptureAuthorizedPaymentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>authorization_id</code> | <code>str</code> | The PayPal-generated ID for the authorized payment to capture. |
| <code>pay_pal_mock_response</code> | <code>str \| None</code> | PayPal's REST API uses a request header to invoke negative testing in the sandbox. This header configures the sandbox into a negative testing state for transactions that include the merchant.<br>**Default**: <code>None</code> |
| <code>pay_pal_request_id</code> | <code>str \| None</code> | The server stores keys for 45 days.<br>**Default**: <code>None</code> |
| <code>prefer</code> | <code>str \| None</code> | The preferred server response upon successful completion of the request. Value is: return=minimal. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the id, status and HATEOAS links. return=representation. The server returns a complete resource representation, including the current state of the resource.<br>**Default**: <code>"return=minimal"</code> |
| <code>pay_pal_auth_assertion</code> | <code>str \| None</code> | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see [PayPal-Auth-Assertion](/docs/api/reference/api-requests/#paypal-auth-assertion). Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant, the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token with target_subject.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[CaptureRequest](paypal/models/capture_request.py) \| [CaptureRequestDict](paypal/models/capture_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CapturedPayment](paypal/models/captured_payment.py)</code> -- A successful request returns the HTTP 200 OK status code and a JSON response body that shows captured payment details.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[CaptureAuthorizedPaymentErrorBody](paypal/errors/capture_authorized_payment_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 409, 422 | <code>[Error](paypal/models/error.py)</code> |
| 500 | <code>[RawError](paypal/core/results.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_authorized_payment(authorization_id: str, *, pay_pal_mock_response: str | None = None, pay_pal_auth_assertion: str | None = None, request_options: RequestOptionsOrDict | None = None) -> PaymentAuthorization</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Shows details for an authorized payment, by ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payments.get_authorized_payment(authorization_id)
    # TODO: Handle 'response' of type PaymentAuthorization
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAuthorizedPaymentErrorBody
```

**Async**

```python
try:
    response = await async_client.payments.get_authorized_payment(authorization_id)
    # TODO: Handle 'response' of type PaymentAuthorization
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAuthorizedPaymentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>authorization_id</code> | <code>str</code> | The ID of the authorized payment for which to show details. |
| <code>pay_pal_mock_response</code> | <code>str \| None</code> | PayPal's REST API uses a request header to invoke negative testing in the sandbox. This header configures the sandbox into a negative testing state for transactions that include the merchant.<br>**Default**: <code>None</code> |
| <code>pay_pal_auth_assertion</code> | <code>str \| None</code> | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see [PayPal-Auth-Assertion](/docs/api/reference/api-requests/#paypal-auth-assertion). Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant, the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token with target_subject.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PaymentAuthorization](paypal/models/payment_authorization.py)</code> -- A successful request returns the HTTP 200 OK status code and a JSON response body that shows authorization details.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[GetAuthorizedPaymentErrorBody](paypal/errors/get_authorized_payment_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 403, 404 | <code>[Error](paypal/models/error.py)</code> |
| 500 | <code>[RawError](paypal/core/results.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_captured_payment(capture_id: str, *, pay_pal_mock_response: str | None = None, request_options: RequestOptionsOrDict | None = None) -> CapturedPayment</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Shows details for a captured payment, by ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payments.get_captured_payment(capture_id)
    # TODO: Handle 'response' of type CapturedPayment
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCapturedPaymentErrorBody
```

**Async**

```python
try:
    response = await async_client.payments.get_captured_payment(capture_id)
    # TODO: Handle 'response' of type CapturedPayment
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCapturedPaymentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>capture_id</code> | <code>str</code> | The PayPal-generated ID for the captured payment for which to show details. |
| <code>pay_pal_mock_response</code> | <code>str \| None</code> | PayPal's REST API uses a request header to invoke negative testing in the sandbox. This header configures the sandbox into a negative testing state for transactions that include the merchant.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CapturedPayment](paypal/models/captured_payment.py)</code> -- A successful request returns the HTTP 200 OK status code and a JSON response body that shows captured payment details.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[GetCapturedPaymentErrorBody](paypal/errors/get_captured_payment_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 403, 404 | <code>[Error](paypal/models/error.py)</code> |
| 500 | <code>[RawError](paypal/core/results.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_refund(refund_id: str, *, pay_pal_mock_response: str | None = None, pay_pal_auth_assertion: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Refund</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Shows details for a refund, by ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payments.get_refund(refund_id)
    # TODO: Handle 'response' of type Refund
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetRefundErrorBody
```

**Async**

```python
try:
    response = await async_client.payments.get_refund(refund_id)
    # TODO: Handle 'response' of type Refund
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetRefundErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>refund_id</code> | <code>str</code> | The PayPal-generated ID for the refund for which to show details. |
| <code>pay_pal_mock_response</code> | <code>str \| None</code> | PayPal's REST API uses a request header to invoke negative testing in the sandbox. This header configures the sandbox into a negative testing state for transactions that include the merchant.<br>**Default**: <code>None</code> |
| <code>pay_pal_auth_assertion</code> | <code>str \| None</code> | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see [PayPal-Auth-Assertion](/docs/api/reference/api-requests/#paypal-auth-assertion). Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant, the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token with target_subject.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Refund](paypal/models/refund.py)</code> -- A successful request returns the HTTP 200 OK status code and a JSON response body that shows refund details.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[GetRefundErrorBody](paypal/errors/get_refund_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 403, 404 | <code>[Error](paypal/models/error.py)</code> |
| 500 | <code>[RawError](paypal/core/results.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def reauthorize_payment(authorization_id: str, *, pay_pal_request_id: str | None = None, prefer: str | None = "return=minimal", pay_pal_auth_assertion: str | None = None, body: ReauthorizeRequest | ReauthorizeRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> PaymentAuthorization</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Reauthorizes an authorized PayPal account payment, by ID. To ensure that funds are still available, reauthorize a payment after its initial three-day honor period expires. Within the 29-day authorization period, you can issue multiple re-authorizations after the honor period expires. If 30 days have transpired since the date of the original authorization, you must create an authorized payment instead of reauthorizing the original authorized payment. A reauthorized payment itself has a new honor period of three days. You can reauthorize an authorized payment from 4 to 29 days after the 3-day honor period. The allowed amount depends on context and geography, for example in US it is up to 115% of the original authorized amount, not to exceed an increase of $75 USD. Supports only the `amount` request parameter.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payments.reauthorize_payment(authorization_id)
    # TODO: Handle 'response' of type PaymentAuthorization
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReauthorizePaymentErrorBody
```

**Async**

```python
try:
    response = await async_client.payments.reauthorize_payment(authorization_id)
    # TODO: Handle 'response' of type PaymentAuthorization
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReauthorizePaymentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>authorization_id</code> | <code>str</code> | The PayPal-generated ID for the authorized payment to reauthorize. |
| <code>pay_pal_request_id</code> | <code>str \| None</code> | The server stores keys for 45 days.<br>**Default**: <code>None</code> |
| <code>prefer</code> | <code>str \| None</code> | The preferred server response upon successful completion of the request. Value is: return=minimal. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the id, status and HATEOAS links. return=representation. The server returns a complete resource representation, including the current state of the resource.<br>**Default**: <code>"return=minimal"</code> |
| <code>pay_pal_auth_assertion</code> | <code>str \| None</code> | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see [PayPal-Auth-Assertion](/docs/api/reference/api-requests/#paypal-auth-assertion). Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant, the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token with target_subject.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[ReauthorizeRequest](paypal/models/reauthorize_request.py) \| [ReauthorizeRequestDict](paypal/models/reauthorize_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PaymentAuthorization](paypal/models/payment_authorization.py)</code> -- A successful request returns the HTTP 200 OK status code and a JSON response body that shows the reauthorized payment details.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[ReauthorizePaymentErrorBody](paypal/errors/reauthorize_payment_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 422 | <code>[Error](paypal/models/error.py)</code> |
| 500 | <code>[RawError](paypal/core/results.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def refund_captured_payment(capture_id: str, *, pay_pal_mock_response: str | None = None, pay_pal_request_id: str | None = None, prefer: str | None = "return=minimal", pay_pal_auth_assertion: str | None = None, body: RefundRequest | RefundRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> Refund</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Refunds a captured payment, by ID. For a full refund, include an empty payload in the JSON request body. For a partial refund, include an amount object in the JSON request body.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payments.refund_captured_payment(capture_id)
    # TODO: Handle 'response' of type Refund
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RefundCapturedPaymentErrorBody
```

**Async**

```python
try:
    response = await async_client.payments.refund_captured_payment(capture_id)
    # TODO: Handle 'response' of type Refund
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RefundCapturedPaymentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>capture_id</code> | <code>str</code> | The PayPal-generated ID for the captured payment to refund. |
| <code>pay_pal_mock_response</code> | <code>str \| None</code> | PayPal's REST API uses a request header to invoke negative testing in the sandbox. This header configures the sandbox into a negative testing state for transactions that include the merchant.<br>**Default**: <code>None</code> |
| <code>pay_pal_request_id</code> | <code>str \| None</code> | The server stores keys for 45 days.<br>**Default**: <code>None</code> |
| <code>prefer</code> | <code>str \| None</code> | The preferred server response upon successful completion of the request. Value is: return=minimal. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the id, status and HATEOAS links. return=representation. The server returns a complete resource representation, including the current state of the resource.<br>**Default**: <code>"return=minimal"</code> |
| <code>pay_pal_auth_assertion</code> | <code>str \| None</code> | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see [PayPal-Auth-Assertion](/docs/api/reference/api-requests/#paypal-auth-assertion). Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant, the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token with target_subject.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[RefundRequest](paypal/models/refund_request.py) \| [RefundRequestDict](paypal/models/refund_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Refund](paypal/models/refund.py)</code> -- A successful request returns the HTTP 200 OK status code and a JSON response body that shows refund details.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[RefundCapturedPaymentErrorBody](paypal/errors/refund_captured_payment_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 409, 422 | <code>[Error](paypal/models/error.py)</code> |
| 500 | <code>[RawError](paypal/core/results.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def void_payment(authorization_id: str, *, pay_pal_mock_response: str | None = None, pay_pal_auth_assertion: str | None = None, pay_pal_request_id: str | None = None, prefer: str | None = "return=minimal", request_options: RequestOptionsOrDict | None = None) -> PaymentAuthorization</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Voids, or cancels, an authorized payment, by ID. You cannot void an authorized payment that has been fully captured.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payments.void_payment(authorization_id)
    # TODO: Handle 'response' of type PaymentAuthorization
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type VoidPaymentErrorBody
```

**Async**

```python
try:
    response = await async_client.payments.void_payment(authorization_id)
    # TODO: Handle 'response' of type PaymentAuthorization
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type VoidPaymentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>authorization_id</code> | <code>str</code> | The PayPal-generated ID for the authorized payment to void. |
| <code>pay_pal_mock_response</code> | <code>str \| None</code> | PayPal's REST API uses a request header to invoke negative testing in the sandbox. This header configures the sandbox into a negative testing state for transactions that include the merchant.<br>**Default**: <code>None</code> |
| <code>pay_pal_auth_assertion</code> | <code>str \| None</code> | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see [PayPal-Auth-Assertion](/docs/api/reference/api-requests/#paypal-auth-assertion). Note:For three party transactions in which a partner is managing the API calls on behalf of a merchant, the partner must identify the merchant using either a PayPal-Auth-Assertion header or an access token with target_subject.<br>**Default**: <code>None</code> |
| <code>pay_pal_request_id</code> | <code>str \| None</code> | The server stores keys for 45 days.<br>**Default**: <code>None</code> |
| <code>prefer</code> | <code>str \| None</code> | The preferred server response upon successful completion of the request. Value is: return=minimal. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the id, status and HATEOAS links. return=representation. The server returns a complete resource representation, including the current state of the resource.<br>**Default**: <code>"return=minimal"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PaymentAuthorization](paypal/models/payment_authorization.py)</code> -- A successful request returns the HTTP 200 OK status code and a JSON response body that shows authorization details. This response is returned when the Prefer header is set to return=representation.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[VoidPaymentErrorBody](paypal/errors/void_payment_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 403, 404, 409, 422 | <code>[Error](paypal/models/error.py)</code> |
| 500 | <code>[RawError](paypal/core/results.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Subscriptions

> Source: [Subscriptions](paypal/apis/subscriptions.py)

<details>
<summary><code>def activate_billing_plan(id: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Activates a plan, by ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.subscriptions.activate_billing_plan(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ActivateBillingPlanErrorBody
```

**Async**

```python
try:
    await async_client.subscriptions.activate_billing_plan(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ActivateBillingPlanErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the plan. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[ActivateBillingPlanErrorBody](paypal/errors/activate_billing_plan_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 403, 404, 422, 500 | <code>[SubscriptionError](paypal/models/subscription_error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def activate_subscription(id: str, *, body: ActivateSubscriptionRequest | ActivateSubscriptionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Activates the subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.subscriptions.activate_subscription(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ActivateSubscriptionErrorBody
```

**Async**

```python
try:
    await async_client.subscriptions.activate_subscription(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ActivateSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the subscription. |
| <code>body</code> | <code>[ActivateSubscriptionRequest](paypal/models/activate_subscription_request.py) \| [ActivateSubscriptionRequestDict](paypal/models/activate_subscription_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[ActivateSubscriptionErrorBody](paypal/errors/activate_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 422, 500 | <code>[SubscriptionError](paypal/models/subscription_error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cancel_subscription(id: str, *, body: CancelSubscriptionRequest | CancelSubscriptionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancels the subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.subscriptions.cancel_subscription(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelSubscriptionErrorBody
```

**Async**

```python
try:
    await async_client.subscriptions.cancel_subscription(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the subscription. |
| <code>body</code> | <code>[CancelSubscriptionRequest](paypal/models/cancel_subscription_request.py) \| [CancelSubscriptionRequestDict](paypal/models/cancel_subscription_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[CancelSubscriptionErrorBody](paypal/errors/cancel_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 422, 500 | <code>[SubscriptionError](paypal/models/subscription_error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def capture_subscription(id: str, *, pay_pal_request_id: str | None = None, body: CaptureSubscriptionRequest | CaptureSubscriptionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionTransactionDetails</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Captures an authorized payment from the subscriber on the subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscriptions.capture_subscription(id)
    # TODO: Handle 'response' of type SubscriptionTransactionDetails
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CaptureSubscriptionErrorBody
```

**Async**

```python
try:
    response = await async_client.subscriptions.capture_subscription(id)
    # TODO: Handle 'response' of type SubscriptionTransactionDetails
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CaptureSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the subscription. |
| <code>pay_pal_request_id</code> | <code>str \| None</code> | The server stores keys for 72 hours.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[CaptureSubscriptionRequest](paypal/models/capture_subscription_request.py) \| [CaptureSubscriptionRequestDict](paypal/models/capture_subscription_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionTransactionDetails](paypal/models/subscription_transaction_details.py)</code> -- A successful request returns the HTTP `200 OK` status code and a JSON response body that shows subscription details.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[CaptureSubscriptionErrorBody](paypal/errors/capture_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 422, 500 | <code>[SubscriptionError](paypal/models/subscription_error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_billing_plan(*, prefer: str | None = "return=minimal", pay_pal_request_id: str | None = None, body: PlanRequest | PlanRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> BillingPlan</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a plan that defines pricing and billing cycle details for subscriptions.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscriptions.create_billing_plan()
    # TODO: Handle 'response' of type BillingPlan
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateBillingPlanErrorBody
```

**Async**

```python
try:
    response = await async_client.subscriptions.create_billing_plan()
    # TODO: Handle 'response' of type BillingPlan
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateBillingPlanErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>prefer</code> | <code>str \| None</code> | The preferred server response upon successful completion of the request. Value is: return=minimal. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the id, status and HATEOAS links. return=representation. The server returns a complete resource representation, including the current state of the resource.<br>**Default**: <code>"return=minimal"</code> |
| <code>pay_pal_request_id</code> | <code>str \| None</code> | The server stores keys for 72 hours.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[PlanRequest](paypal/models/plan_request.py) \| [PlanRequestDict](paypal/models/plan_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BillingPlan](paypal/models/billing_plan.py)</code> -- A successful request returns the HTTP `200 OK` status code and a JSON response body that shows billing plan details.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[CreateBillingPlanErrorBody](paypal/errors/create_billing_plan_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 422, 500 | <code>[SubscriptionError](paypal/models/subscription_error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_subscription(*, prefer: str | None = "return=minimal", pay_pal_request_id: str | None = None, pay_pal_client_metadata_id: str | None = None, body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> Subscription</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscriptions.create_subscription()
    # TODO: Handle 'response' of type Subscription
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateSubscriptionErrorBody
```

**Async**

```python
try:
    response = await async_client.subscriptions.create_subscription()
    # TODO: Handle 'response' of type Subscription
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>prefer</code> | <code>str \| None</code> | The preferred server response upon successful completion of the request. Value is: return=minimal. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the id, status and HATEOAS links. return=representation. The server returns a complete resource representation, including the current state of the resource.<br>**Default**: <code>"return=minimal"</code> |
| <code>pay_pal_request_id</code> | <code>str \| None</code> | The server stores keys for 72 hours.<br>**Default**: <code>None</code> |
| <code>pay_pal_client_metadata_id</code> | <code>str \| None</code> | The PayPal Client Metadata Id(CMID) is used to provide device-specific information to PayPal's risk engine. This is crucial for transactions that require device-specific risk assessments. Merchants typically use the Paypal SDK that automatically submits the CMID or they use tools like Fraudnet JS for web or Magnes JS for mobile to generate the CMID on the frontend and then pass it to the API as part of the request headers.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[CreateSubscriptionRequest](paypal/models/create_subscription_request.py) \| [CreateSubscriptionRequestDict](paypal/models/create_subscription_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Subscription](paypal/models/subscription.py)</code> -- A successful request returns the HTTP `200 OK` status code and a JSON response body that shows subscription details.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[CreateSubscriptionErrorBody](paypal/errors/create_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 422, 500 | <code>[SubscriptionError](paypal/models/subscription_error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deactivate_billing_plan(id: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deactivates a plan, by ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.subscriptions.deactivate_billing_plan(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeactivateBillingPlanErrorBody
```

**Async**

```python
try:
    await async_client.subscriptions.deactivate_billing_plan(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeactivateBillingPlanErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the plan. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[DeactivateBillingPlanErrorBody](paypal/errors/deactivate_billing_plan_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 403, 404, 422, 500 | <code>[SubscriptionError](paypal/models/subscription_error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_billing_plan(id: str, *, request_options: RequestOptionsOrDict | None = None) -> BillingPlan</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Shows details for a plan, by ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscriptions.get_billing_plan(id)
    # TODO: Handle 'response' of type BillingPlan
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetBillingPlanErrorBody
```

**Async**

```python
try:
    response = await async_client.subscriptions.get_billing_plan(id)
    # TODO: Handle 'response' of type BillingPlan
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetBillingPlanErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the plan. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BillingPlan](paypal/models/billing_plan.py)</code> -- A successful request returns the HTTP `200 OK` status code and a JSON response body that shows plan details.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[GetBillingPlanErrorBody](paypal/errors/get_billing_plan_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 403, 404, 500 | <code>[SubscriptionError](paypal/models/subscription_error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_subscription(id: str, *, fields: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Subscription</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Shows details for a subscription, by ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscriptions.get_subscription(id)
    # TODO: Handle 'response' of type Subscription
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSubscriptionErrorBody
```

**Async**

```python
try:
    response = await async_client.subscriptions.get_subscription(id)
    # TODO: Handle 'response' of type Subscription
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the subscription. |
| <code>fields</code> | <code>str \| None</code> | List of fields that are to be returned in the response. Possible value for fields are last_failed_payment and plan.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Subscription](paypal/models/subscription.py)</code> -- A successful request returns the HTTP `200 OK` status code and a JSON response body that shows subscription details.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[GetSubscriptionErrorBody](paypal/errors/get_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 403, 404, 500 | <code>[SubscriptionError](paypal/models/subscription_error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_billing_plans(*, product_id: str | None = None, page_size: int | None = 10, page: int | None = 1, total_required: bool | None = False, prefer: str | None = "return=minimal", request_options: RequestOptionsOrDict | None = None) -> PlanCollection</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists billing plans.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscriptions.list_billing_plans()
    # TODO: Handle 'response' of type PlanCollection
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListBillingPlansErrorBody
```

**Async**

```python
try:
    response = await async_client.subscriptions.list_billing_plans()
    # TODO: Handle 'response' of type PlanCollection
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListBillingPlansErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>str \| None</code> | Filters the response by a Product ID.<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>int \| None</code> | The number of items to return in the response.<br>**Default**: <code>10</code> |
| <code>page</code> | <code>int \| None</code> | A non-zero integer which is the start index of the entire list of items to return in the response. The combination of `page=1` and `page_size=20` returns the first 20 items. The combination of `page=2` and `page_size=20` returns the next 20 items.<br>**Default**: <code>1</code> |
| <code>total_required</code> | <code>bool \| None</code> | Indicates whether to show the total count in the response.<br>**Default**: <code>False</code> |
| <code>prefer</code> | <code>str \| None</code> | The preferred server response upon successful completion of the request. Value is: return=minimal. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the id, name, description and HATEOAS links. return=representation. The server returns a complete resource representation, including the current state of the resource.<br>**Default**: <code>"return=minimal"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PlanCollection](paypal/models/plan_collection.py)</code> -- A successful request returns the HTTP `200 OK` status code and a JSON response body that lists billing plans.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[ListBillingPlansErrorBody](paypal/errors/list_billing_plans_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 500 | <code>[SubscriptionError](paypal/models/subscription_error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_subscription_transactions(id: str, start_time: str, end_time: str, *, request_options: RequestOptionsOrDict | None = None) -> TransactionsList</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists transactions for a subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscriptions.list_subscription_transactions(id, start_time, end_time)
    # TODO: Handle 'response' of type TransactionsList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListSubscriptionTransactionsErrorBody
```

**Async**

```python
try:
    response = await async_client.subscriptions.list_subscription_transactions(id, start_time, end_time)
    # TODO: Handle 'response' of type TransactionsList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListSubscriptionTransactionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the subscription. |
| <code>start_time</code> | <code>str</code> | The start time of the range of transactions to list. |
| <code>end_time</code> | <code>str</code> | The end time of the range of transactions to list. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TransactionsList](paypal/models/transactions_list.py)</code> -- A successful request returns the HTTP `200 OK` status code and a JSON response body that shows subscription details.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[ListSubscriptionTransactionsErrorBody](paypal/errors/list_subscription_transactions_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 500 | <code>[SubscriptionError](paypal/models/subscription_error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_subscriptions(*, plan_ids: str | None = None, statuses: str | None = None, created_after: str | None = None, created_before: str | None = None, status_updated_before: str | None = None, status_updated_after: str | None = None, filter: str | None = None, page_size: int | None = 10, page: int | None = 1, customer_ids: list[str] | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionCollection</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all subscriptions for merchant account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscriptions.list_subscriptions()
    # TODO: Handle 'response' of type SubscriptionCollection
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListSubscriptionsErrorBody
```

**Async**

```python
try:
    response = await async_client.subscriptions.list_subscriptions()
    # TODO: Handle 'response' of type SubscriptionCollection
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListSubscriptionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>plan_ids</code> | <code>str \| None</code> | Filters the response by list of plan IDs. Filter supports upto 70 plan IDs. URLs should not exceed a length of 2000 characters.<br>**Default**: <code>None</code> |
| <code>statuses</code> | <code>str \| None</code> | Filters the response by list of subscription statuses.<br>**Default**: <code>None</code> |
| <code>created_after</code> | <code>str \| None</code> | Filters the response by subscription creation start time for a range of subscriptions.<br>**Default**: <code>None</code> |
| <code>created_before</code> | <code>str \| None</code> | Filters the response by subscription creation end time for a range of subscriptions.<br>**Default**: <code>None</code> |
| <code>status_updated_before</code> | <code>str \| None</code> | Filters the response by status update start time for a range of subscriptions.<br>**Default**: <code>None</code> |
| <code>status_updated_after</code> | <code>str \| None</code> | Filters the response by status update end time for a range of subscriptions.<br>**Default**: <code>None</code> |
| <code>filter</code> | <code>str \| None</code> | Filter the response using complex expressions that could use comparison operators like ge, gt, le, lt and logical operators such as 'and' and 'or'.<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>int \| None</code> | The number of items to return in the response.<br>**Default**: <code>10</code> |
| <code>page</code> | <code>int \| None</code> | A non-zero integer which is the start index of the entire list of items to return in the response. The combination of `page=1` and `page_size=20` returns the first 20 items. The combination of `page=2` and `page_size=20` returns the next 20 items.<br>**Default**: <code>1</code> |
| <code>customer_ids</code> | <code>list&#91;str&#93; \| None</code> | Filters the response by comma separated vault customer IDs (FSS subscriptions only).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionCollection](paypal/models/subscription_collection.py)</code> -- A successful request returns the HTTP `200 OK` status code and a JSON response body that lists the subscriptions.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[ListSubscriptionsErrorBody](paypal/errors/list_subscriptions_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 500 | <code>[SubscriptionError](paypal/models/subscription_error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def patch_billing_plan(id: str, *, body: list[Patch | PatchDict] | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a plan with the `CREATED` or `ACTIVE` status. For an `INACTIVE` plan, you can make only status updates. You can patch these attributes and objects: Attribute or object Operations description replace payment_preferences.auto_bill_outstanding replace taxes.percentage replace payment_preferences.payment_failure_threshold replace payment_preferences.setup_fee replace payment_preferences.setup_fee_failure_action replace name replace

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.subscriptions.patch_billing_plan(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PatchBillingPlanErrorBody
```

**Async**

```python
try:
    await async_client.subscriptions.patch_billing_plan(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PatchBillingPlanErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the plan. |
| <code>body</code> | <code>list&#91;[Patch](paypal/models/patch.py) \| [PatchDict](paypal/models/patch.py)&#93; \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[PatchBillingPlanErrorBody](paypal/errors/patch_billing_plan_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 422, 500 | <code>[SubscriptionError](paypal/models/subscription_error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def patch_subscription(id: str, *, body: list[Patch | PatchDict] | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a subscription which could be in ACTIVE or SUSPENDED status. You can override plan level default attributes by providing customised values for plan path in the patch request. You cannot update attributes that have already completed (Example - trial cycles can’t be updated if completed). Once overridden, changes to plan resource will not impact subscription. Any price update will not impact billing cycles within next 10 days (Applicable only for subscriptions funded by PayPal account). Following are the fields eligible for patch. Attribute or object Operations billing_info.outstanding_balance replace custom_id add,replace plan.billing_cycles[@sequence==n]. pricing_scheme.fixed_price add,replace plan.billing_cycles[@sequence==n]. pricing_scheme.tiers replace plan.billing_cycles[@sequence==n]. total_cycles replace plan.payment_preferences. auto_bill_outstanding replace plan.payment_preferences. payment_failure_threshold replace plan.taxes.inclusive add,replace plan.taxes.percentage add,replace shipping_amount add,replace start_time replace subscriber.shipping_address add,replace subscriber.payment_source (for subscriptions funded by card payments) replace

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.subscriptions.patch_subscription(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PatchSubscriptionErrorBody
```

**Async**

```python
try:
    await async_client.subscriptions.patch_subscription(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PatchSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID for the subscription. |
| <code>body</code> | <code>list&#91;[Patch](paypal/models/patch.py) \| [PatchDict](paypal/models/patch.py)&#93; \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[PatchSubscriptionErrorBody](paypal/errors/patch_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 422, 500 | <code>[SubscriptionError](paypal/models/subscription_error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def revise_subscription(id: str, *, body: ModifySubscriptionRequest | ModifySubscriptionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ModifySubscriptionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the quantity of the product or service in a subscription. You can also use this method to switch the plan and update the `shipping_amount`, `shipping_address` values for the subscription. This type of update requires the buyer's consent.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscriptions.revise_subscription(id)
    # TODO: Handle 'response' of type ModifySubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReviseSubscriptionErrorBody
```

**Async**

```python
try:
    response = await async_client.subscriptions.revise_subscription(id)
    # TODO: Handle 'response' of type ModifySubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReviseSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the subscription. |
| <code>body</code> | <code>[ModifySubscriptionRequest](paypal/models/modify_subscription_request.py) \| [ModifySubscriptionRequestDict](paypal/models/modify_subscription_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ModifySubscriptionResponse](paypal/models/modify_subscription_response.py)</code> -- A successful request returns the HTTP `200 OK` status code and a JSON response body that shows subscription details.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[ReviseSubscriptionErrorBody](paypal/errors/revise_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 422, 500 | <code>[SubscriptionError](paypal/models/subscription_error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def suspend_subscription(id: str, *, body: SuspendSubscription | SuspendSubscriptionDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Suspends the subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.subscriptions.suspend_subscription(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SuspendSubscriptionErrorBody
```

**Async**

```python
try:
    await async_client.subscriptions.suspend_subscription(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SuspendSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the subscription. |
| <code>body</code> | <code>[SuspendSubscription](paypal/models/suspend_subscription.py) \| [SuspendSubscriptionDict](paypal/models/suspend_subscription.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[SuspendSubscriptionErrorBody](paypal/errors/suspend_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 422, 500 | <code>[SubscriptionError](paypal/models/subscription_error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_billing_plan_pricing_schemes(id: str, *, body: UpdatePricingSchemesRequest | UpdatePricingSchemesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates pricing for a plan. For example, you can update a regular billing cycle from $5 per month to $7 per month.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.subscriptions.update_billing_plan_pricing_schemes(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateBillingPlanPricingSchemesErrorBody
```

**Async**

```python
try:
    await async_client.subscriptions.update_billing_plan_pricing_schemes(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateBillingPlanPricingSchemesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID for the plan. |
| <code>body</code> | <code>[UpdatePricingSchemesRequest](paypal/models/update_pricing_schemes_request.py) \| [UpdatePricingSchemesRequestDict](paypal/models/update_pricing_schemes_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[UpdateBillingPlanPricingSchemesErrorBody](paypal/errors/update_billing_plan_pricing_schemes_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 422, 500 | <code>[SubscriptionError](paypal/models/subscription_error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## TransactionSearch

> Source: [TransactionSearch](paypal/apis/transaction_search.py)

<details>
<summary><code>def search_balances(*, as_of_time: str | None = None, currency_code: str | None = None, request_options: RequestOptionsOrDict | None = None) -> BalancesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all balances. Specify date time to list balances for that time that appear in the response. Notes: It takes a maximum of three hours for balances to appear in the list balances call. This call lists balances upto the previous three years.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.transaction_search.search_balances()
    # TODO: Handle 'response' of type BalancesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchBalancesErrorBody
```

**Async**

```python
try:
    response = await async_client.transaction_search.search_balances()
    # TODO: Handle 'response' of type BalancesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchBalancesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>as_of_time</code> | <code>str \| None</code> | List balances in the response at the date time provided, will return the last refreshed balance in the system when not provided.<br>**Default**: <code>None</code> |
| <code>currency_code</code> | <code>str \| None</code> | Filters the transactions in the response by a [three-character ISO-4217 currency code](https://developer.paypal.com/api/rest/reference/currency-codes/) for the PayPal transaction currency.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BalancesResponse](paypal/models/balances_response.py)</code> -- A successful request returns the HTTP `200 OK` status code and a JSON response body that lists balances .

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[SearchBalancesErrorBody](paypal/errors/search_balances_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 500 | <code>[DefaultError](paypal/models/default_error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_transactions(start_date: str, end_date: str, *, transaction_id: str | None = None, transaction_type: str | None = None, transaction_status: str | None = None, transaction_amount: str | None = None, transaction_currency: str | None = None, payment_instrument_type: str | None = None, store_id: str | None = None, terminal_id: str | None = None, fields: str | None = "transaction_info", balance_affecting_records_only: str | None = "Y", page_size: int | None = 100, page: int | None = 1, request_options: RequestOptionsOrDict | None = None) -> SearchResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists transactions. Specify one or more query parameters to filter the transaction that appear in the response. Notes: If you specify one or more optional query parameters, the ending_balance response field is empty. It takes a maximum of three hours for executed transactions to appear in the list transactions call. This call lists transaction for the previous three years.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.transaction_search.search_transactions(start_date, end_date)
    # TODO: Handle 'response' of type SearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transaction_search.search_transactions(start_date, end_date)
    # TODO: Handle 'response' of type SearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>start_date</code> | <code>str</code> | Filters the transactions in the response by a start date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required. Fractional seconds are optional. |
| <code>end_date</code> | <code>str</code> | Filters the transactions in the response by an end date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required. Fractional seconds are optional. The maximum supported range is 31 days. |
| <code>transaction_id</code> | <code>str \| None</code> | Filters the transactions in the response by a PayPal transaction ID. A valid transaction ID is 17 characters long, except for an order ID, which is 19 characters long. Note: A transaction ID is not unique in the reporting system. The response can list two transactions with the same ID. One transaction can be balance affecting while the other is non-balance affecting.<br>**Default**: <code>None</code> |
| <code>transaction_type</code> | <code>str \| None</code> | Filters the transactions in the response by a PayPal transaction event code. See [Transaction event codes](/docs/integration/direct/transaction-search/transaction-event-codes/).<br>**Default**: <code>None</code> |
| <code>transaction_status</code> | <code>str \| None</code> | Filters the transactions in the response by a PayPal transaction status code. Value is: Status code Description D PayPal or merchant rules denied the transaction. P The transaction is pending. The transaction was created but waits for another payment process to complete, such as an ACH transaction, before the status changes to S. S The transaction successfully completed without a denial and after any pending statuses. V A successful transaction was reversed and funds were refunded to the original sender.<br>**Default**: <code>None</code> |
| <code>transaction_amount</code> | <code>str \| None</code> | Filters the transactions in the response by a gross transaction amount range. Specify the range as ` TO `, where ` ` is the lower limit of the gross PayPal transaction amount and ` ` is the upper limit of the gross transaction amount. Specify the amounts in lower denominations. For example, to search for transactions from $5.00 to $10.05, specify `[500 TO 1005]`. Note:The values must be URL encoded.<br>**Default**: <code>None</code> |
| <code>transaction_currency</code> | <code>str \| None</code> | Filters the transactions in the response by a [three-character ISO-4217 currency code](https://developer.paypal.com/api/rest/reference/currency-codes/) for the PayPal transaction currency.<br>**Default**: <code>None</code> |
| <code>payment_instrument_type</code> | <code>str \| None</code> | Filters the transactions in the response by a payment instrument type. Value is either: CREDITCARD. Returns a direct credit card transaction with a corresponding value. DEBITCARD. Returns a debit card transaction with a corresponding value. If you omit this parameter, the API does not apply this filter.<br>**Default**: <code>None</code> |
| <code>store_id</code> | <code>str \| None</code> | Filters the transactions in the response by a store ID.<br>**Default**: <code>None</code> |
| <code>terminal_id</code> | <code>str \| None</code> | Filters the transactions in the response by a terminal ID.<br>**Default**: <code>None</code> |
| <code>fields</code> | <code>str \| None</code> | Indicates which fields appear in the response. Value is a single field or a comma-separated list of fields. The transaction_info value returns only the transaction details in the response. To include all fields in the response, specify fields=all. Valid fields are: transaction_info. The transaction information. Includes the ID of the PayPal account of the payee, the PayPal-generated transaction ID, the PayPal-generated base ID, the PayPal reference ID type, the transaction event code, the date and time when the transaction was initiated and was last updated, the transaction amounts including the PayPal fee, any discounts, insurance, the transaction status, and other information about the transaction. payer_info. The payer information. Includes the PayPal customer account ID and the payer's email address, primary phone number, name, country code, address, and whether the payer is verified or unverified. shipping_info. The shipping information. Includes the recipient's name, the shipping method for this order, the shipping address for this order, and the secondary address associated with this order. auction_info. The auction information. Includes the name of the auction site, the auction site URL, the ID of the customer who makes the purchase in the auction, and the date and time when the auction closes. cart_info. The cart information. Includes an array of item details, whether the item amount or the shipping amount already includes tax, and the ID of the invoice for PayPal-generated invoices. incentive_info. An array of incentive detail objects. Each object includes the incentive, such as a special offer or coupon, the incentive amount, and the incentive program code that identifies a merchant loyalty or incentive program. store_info. The store information. Includes the ID of the merchant store and the terminal ID for the checkout stand in the merchant store.<br>**Default**: <code>"transaction_info"</code> |
| <code>balance_affecting_records_only</code> | <code>str \| None</code> | Indicates whether the response includes only balance-impacting transactions or all transactions. Value is either: Y. The default. The response includes only balance transactions. N. The response includes all transactions.<br>**Default**: <code>"Y"</code> |
| <code>page_size</code> | <code>int \| None</code> | The number of items to return in the response. So, the combination of `page=1` and `page_size=20` returns the first 20 items. The combination of `page=2` and `page_size=20` returns the next 20 items.<br>**Default**: <code>100</code> |
| <code>page</code> | <code>int \| None</code> | The zero-relative start index of the entire list of items that are returned in the response. So, the combination of `page=1` and `page_size=20` returns the first 20 items.<br>**Default**: <code>1</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SearchResponse](paypal/models/search_response.py)</code> -- A successful request returns the HTTP `200 OK` status code and a JSON response body that lists transactions .

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[RawError](paypal/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Vault

> Source: [Vault](paypal/apis/vault.py)

<details>
<summary><code>def create_payment_token(body: PaymentTokenRequest | PaymentTokenRequestDict, *, pay_pal_request_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> PaymentTokenResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a Payment Token from the given payment source and adds it to the Vault of the associated customer.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.vault.create_payment_token(body)
    # TODO: Handle 'response' of type PaymentTokenResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreatePaymentTokenErrorBody
```

**Async**

```python
try:
    response = await async_client.vault.create_payment_token(body)
    # TODO: Handle 'response' of type PaymentTokenResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreatePaymentTokenErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentTokenRequest](paypal/models/payment_token_request.py) \| [PaymentTokenRequestDict](paypal/models/payment_token_request.py)</code> | Payment Token creation with a financial instrument and an optional customer_id. |
| <code>pay_pal_request_id</code> | <code>str \| None</code> | The server stores keys for 3 hours.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PaymentTokenResponse](paypal/models/payment_token_response.py)</code> -- Idempotent response for a successful creation of payment token.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[CreatePaymentTokenErrorBody](paypal/errors/create_payment_token_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 422, 500 | <code>[Error](paypal/models/error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_setup_token(body: SetupTokenRequest | SetupTokenRequestDict, *, pay_pal_request_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> SetupTokenResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a Setup Token from the given payment source and adds it to the Vault of the associated customer.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.vault.create_setup_token(body)
    # TODO: Handle 'response' of type SetupTokenResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateSetupTokenErrorBody
```

**Async**

```python
try:
    response = await async_client.vault.create_setup_token(body)
    # TODO: Handle 'response' of type SetupTokenResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateSetupTokenErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SetupTokenRequest](paypal/models/setup_token_request.py) \| [SetupTokenRequestDict](paypal/models/setup_token_request.py)</code> | Setup Token creation with a instrument type optional financial instrument details and customer_id. |
| <code>pay_pal_request_id</code> | <code>str \| None</code> | The server stores keys for 3 hours.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SetupTokenResponse](paypal/models/setup_token_response.py)</code> -- Idempotent response for a successful creation of setup token.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[CreateSetupTokenErrorBody](paypal/errors/create_setup_token_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 422, 500 | <code>[Error](paypal/models/error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_payment_token(id: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Delete the payment token associated with the payment token id.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.vault.delete_payment_token(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeletePaymentTokenErrorBody
```

**Async**

```python
try:
    await async_client.vault.delete_payment_token(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeletePaymentTokenErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | ID of the payment token. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[DeletePaymentTokenErrorBody](paypal/errors/delete_payment_token_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 500 | <code>[Error](paypal/models/error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_payment_token(id: str, *, request_options: RequestOptionsOrDict | None = None) -> PaymentTokenResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a readable representation of vaulted payment source associated with the payment token id.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.vault.get_payment_token(id)
    # TODO: Handle 'response' of type PaymentTokenResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPaymentTokenErrorBody
```

**Async**

```python
try:
    response = await async_client.vault.get_payment_token(id)
    # TODO: Handle 'response' of type PaymentTokenResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPaymentTokenErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | ID of the payment token. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PaymentTokenResponse](paypal/models/payment_token_response.py)</code> -- Successful execution.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[GetPaymentTokenErrorBody](paypal/errors/get_payment_token_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 404, 422, 500 | <code>[Error](paypal/models/error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_setup_token(id: str, *, request_options: RequestOptionsOrDict | None = None) -> SetupTokenResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a readable representation of temporarily vaulted payment source associated with the setup token id.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.vault.get_setup_token(id)
    # TODO: Handle 'response' of type SetupTokenResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSetupTokenErrorBody
```

**Async**

```python
try:
    response = await async_client.vault.get_setup_token(id)
    # TODO: Handle 'response' of type SetupTokenResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSetupTokenErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | ID of the setup token. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SetupTokenResponse](paypal/models/setup_token_response.py)</code> -- Found requested setup-token, returned a payment method associated with the token.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[GetSetupTokenErrorBody](paypal/errors/get_setup_token_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 404, 422, 500 | <code>[Error](paypal/models/error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_customer_payment_tokens(customer_id: str, *, page_size: int | None = 5, page: int | None = 1, total_required: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> CustomerVaultPaymentTokensResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns all payment tokens for a customer.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.vault.list_customer_payment_tokens(customer_id)
    # TODO: Handle 'response' of type CustomerVaultPaymentTokensResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListCustomerPaymentTokensErrorBody
```

**Async**

```python
try:
    response = await async_client.vault.list_customer_payment_tokens(customer_id)
    # TODO: Handle 'response' of type CustomerVaultPaymentTokensResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListCustomerPaymentTokensErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>customer_id</code> | <code>str</code> | A unique identifier representing a specific customer in merchant's/partner's system or records. |
| <code>page_size</code> | <code>int \| None</code> | A non-negative, non-zero integer indicating the maximum number of results to return at one time.<br>**Default**: <code>5</code> |
| <code>page</code> | <code>int \| None</code> | A non-negative, non-zero integer representing the page of the results.<br>**Default**: <code>1</code> |
| <code>total_required</code> | <code>bool \| None</code> | A boolean indicating total number of items (total_items) and pages (total_pages) are expected to be returned in the response.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](paypal/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CustomerVaultPaymentTokensResponse](paypal/models/customer_vault_payment_tokens_response.py)</code> -- Successful execution.

**OnError**: <code>[ApiError](paypal/core/exceptions.py)&#91;[ListCustomerPaymentTokensErrorBody](paypal/errors/list_customer_payment_tokens_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 500 | <code>[Error](paypal/models/error.py)</code> |
| anything unmapped | <code>[RawError](paypal/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

