<!-- Generated file — do not edit; regenerated with the SDK. -->

# Vault — operations

Accessor: `client.vault` · Source: `paypal/apis/vault.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.vault.create_payment_token

- **Route**: `POST /v3/vault/payment-tokens`
- **Auth**: `oauth2`
- **Signature**: `def create_payment_token(body: PaymentTokenRequest | PaymentTokenRequestDict, *, pay_pal_request_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `pay_pal_request_id` — header `PayPal-Request-Id` · `body` — JSON body
- **Returns (parsed)**: `PaymentTokenResponse`
- **Returns (raw)**: `ApiResult[PaymentTokenResponse, CreatePaymentTokenErrorBody]`
- **Error**: `CreatePaymentTokenErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentTokenRequest` | `paypal/models/payment_token_request.py` |
| `PaymentTokenRequestDict` | `paypal/models/payment_token_request.py` |
| `PaymentTokenResponse` | `paypal/models/payment_token_response.py` |
| `CreatePaymentTokenErrorBody` | `paypal/errors/create_payment_token_error.py` |
| `Error` | `paypal/models/error.py` |

### client.vault.create_setup_token

- **Route**: `POST /v3/vault/setup-tokens`
- **Auth**: `oauth2`
- **Signature**: `def create_setup_token(body: SetupTokenRequest | SetupTokenRequestDict, *, pay_pal_request_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `pay_pal_request_id` — header `PayPal-Request-Id` · `body` — JSON body
- **Returns (parsed)**: `SetupTokenResponse`
- **Returns (raw)**: `ApiResult[SetupTokenResponse, CreateSetupTokenErrorBody]`
- **Error**: `CreateSetupTokenErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SetupTokenRequest` | `paypal/models/setup_token_request.py` |
| `SetupTokenRequestDict` | `paypal/models/setup_token_request.py` |
| `SetupTokenResponse` | `paypal/models/setup_token_response.py` |
| `CreateSetupTokenErrorBody` | `paypal/errors/create_setup_token_error.py` |
| `Error` | `paypal/models/error.py` |

### client.vault.delete_payment_token

- **Route**: `DELETE /v3/vault/payment-tokens/{id}`
- **Auth**: `oauth2`
- **Signature**: `def delete_payment_token(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeletePaymentTokenErrorBody]`
- **Error**: `DeletePaymentTokenErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeletePaymentTokenErrorBody` | `paypal/errors/delete_payment_token_error.py` |
| `Error` | `paypal/models/error.py` |

### client.vault.get_payment_token

- **Route**: `GET /v3/vault/payment-tokens/{id}`
- **Auth**: `oauth2`
- **Signature**: `def get_payment_token(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `PaymentTokenResponse`
- **Returns (raw)**: `ApiResult[PaymentTokenResponse, GetPaymentTokenErrorBody]`
- **Error**: `GetPaymentTokenErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentTokenResponse` | `paypal/models/payment_token_response.py` |
| `GetPaymentTokenErrorBody` | `paypal/errors/get_payment_token_error.py` |
| `Error` | `paypal/models/error.py` |

### client.vault.get_setup_token

- **Route**: `GET /v3/vault/setup-tokens/{id}`
- **Auth**: `oauth2`
- **Signature**: `def get_setup_token(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `SetupTokenResponse`
- **Returns (raw)**: `ApiResult[SetupTokenResponse, GetSetupTokenErrorBody]`
- **Error**: `GetSetupTokenErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404, 422, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SetupTokenResponse` | `paypal/models/setup_token_response.py` |
| `GetSetupTokenErrorBody` | `paypal/errors/get_setup_token_error.py` |
| `Error` | `paypal/models/error.py` |

### client.vault.list_customer_payment_tokens

- **Route**: `GET /v3/vault/payment-tokens`
- **Auth**: `oauth2`
- **Signature**: `def list_customer_payment_tokens(customer_id: str, *, page_size: int | None = 5, page: int | None = 1, total_required: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_id`
- **Params**: `customer_id` — query · `page_size` — query · `page` — query · `total_required` — query
- **Returns (parsed)**: `CustomerVaultPaymentTokensResponse`
- **Returns (raw)**: `ApiResult[CustomerVaultPaymentTokensResponse, ListCustomerPaymentTokensErrorBody]`
- **Error**: `ListCustomerPaymentTokensErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CustomerVaultPaymentTokensResponse` | `paypal/models/customer_vault_payment_tokens_response.py` |
| `ListCustomerPaymentTokensErrorBody` | `paypal/errors/list_customer_payment_tokens_error.py` |
| `Error` | `paypal/models/error.py` |

