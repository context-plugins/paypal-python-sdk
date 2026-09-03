<!-- Generated file — do not edit; regenerated with the SDK. -->

# TransactionSearch — operations

Accessor: `client.transaction_search` · Source: `paypal/apis/transaction_search.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.transaction_search.search_balances

- **Route**: `GET /v1/reporting/balances`
- **Auth**: `oauth2`
- **Signature**: `def search_balances(*, as_of_time: str | None = None, currency_code: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `as_of_time` — query · `currency_code` — query
- **Returns (parsed)**: `BalancesResponse`
- **Returns (raw)**: `ApiResult[BalancesResponse, SearchBalancesErrorBody]`
- **Error**: `SearchBalancesErrorBody` — **Case A (typed)**
- **Error arms**: `DefaultError` [400, 403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BalancesResponse` | `paypal/models/balances_response.py` |
| `SearchBalancesErrorBody` | `paypal/errors/search_balances_error.py` |
| `DefaultError` | `paypal/models/default_error.py` |

### client.transaction_search.search_transactions

- **Route**: `GET /v1/reporting/transactions`
- **Auth**: `oauth2`
- **Signature**: `def search_transactions(start_date: str, end_date: str, *, transaction_id: str | None = None, transaction_type: str | None = None, transaction_status: str | None = None, transaction_amount: str | None = None, transaction_currency: str | None = None, payment_instrument_type: str | None = None, store_id: str | None = None, terminal_id: str | None = None, fields: str | None = "transaction_info", balance_affecting_records_only: str | None = "Y", page_size: int | None = 100, page: int | None = 1, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `start_date`, `end_date`
- **Params**: `start_date` — query · `end_date` — query · `transaction_id` — query · `transaction_type` — query · `transaction_status` — query · `transaction_amount` — query · `transaction_currency` — query · `payment_instrument_type` — query · `store_id` — query · `terminal_id` — query · `fields` — query · `balance_affecting_records_only` — query · `page_size` — query · `page` — query
- **Returns (parsed)**: `SearchResponse`
- **Returns (raw)**: `ApiResult[SearchResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchResponse` | `paypal/models/search_response.py` |

