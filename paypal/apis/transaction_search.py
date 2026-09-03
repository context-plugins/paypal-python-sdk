from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.search_balances_error import SearchBalancesErrorBody, search_balances_error_mapper
from ..models.balances_response import BalancesResponse
from ..models.search_response import SearchResponse
from ..server.server import Server


class TransactionSearch:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TransactionSearchWithRawResponse(client, server, auth)

    def search_balances(
        self,
        *,
        as_of_time: str | None = None,
        currency_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BalancesResponse:
        """List all balances. Specify date time to list balances for that time that appear in the response. Notes: It
        takes a maximum of three hours for balances to appear in the list balances call. This call lists balances upto
        the previous three years.

        Args:
            as_of_time: List balances in the response at the date time provided, will return the last refreshed balance
                in the system when not provided.
            currency_code: Filters the transactions in the response by a `three-character ISO-4217 currency code
                <https://developer.paypal.com/api/rest/reference/currency-codes/>`__ for the PayPal transaction
                currency.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that lists balances .

        Raises:
            ApiError: The request is not well-formed, is syntactically incorrect, or violates schema. Authorization
                failed due to insufficient permissions. An internal server error occurred. ``error`` is ``DefaultError |
                RawError``."""
        return self._with_raw_response.search_balances(
            as_of_time=as_of_time, currency_code=currency_code, request_options=request_options
        ).unwrap()

    def search_transactions(
        self,
        start_date: str,
        end_date: str,
        *,
        transaction_id: str | None = None,
        transaction_type: str | None = None,
        transaction_status: str | None = None,
        transaction_amount: str | None = None,
        transaction_currency: str | None = None,
        payment_instrument_type: str | None = None,
        store_id: str | None = None,
        terminal_id: str | None = None,
        fields: str | None = "transaction_info",
        balance_affecting_records_only: str | None = "Y",
        page_size: int | None = 100,
        page: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchResponse:
        """Lists transactions. Specify one or more query parameters to filter the transaction that appear in the
        response. Notes: If you specify one or more optional query parameters, the ending_balance response field is
        empty. It takes a maximum of three hours for executed transactions to appear in the list transactions call. This
        call lists transaction for the previous three years.

        Args:
            start_date: Filters the transactions in the response by a start date and time, in `Internet date and time
                format <https://tools.ietf.org/html/rfc3339#section-5.6>`__. Seconds are required. Fractional seconds
                are optional.
            end_date: Filters the transactions in the response by an end date and time, in `Internet date and time
                format <https://tools.ietf.org/html/rfc3339#section-5.6>`__. Seconds are required. Fractional seconds
                are optional. The maximum supported range is 31 days.
            transaction_id: Filters the transactions in the response by a PayPal transaction ID. A valid transaction ID
                is 17 characters long, except for an order ID, which is 19 characters long. Note: A transaction ID is
                not unique in the reporting system. The response can list two transactions with the same ID. One
                transaction can be balance affecting while the other is non-balance affecting.
            transaction_type: Filters the transactions in the response by a PayPal transaction event code. See
                `Transaction event codes </docs/integration/direct/transaction-search/transaction-event-codes/>`__.
            transaction_status: Filters the transactions in the response by a PayPal transaction status code. Value is:
                Status code Description D PayPal or merchant rules denied the transaction. P The transaction is pending.
                The transaction was created but waits for another payment process to complete, such as an ACH
                transaction, before the status changes to S. S The transaction successfully completed without a denial
                and after any pending statuses. V A successful transaction was reversed and funds were refunded to the
                original sender.
            transaction_amount: Filters the transactions in the response by a gross transaction amount range. Specify
                the range as `` TO ``, where `` `` is the lower limit of the gross PayPal transaction amount and `` ``
                is the upper limit of the gross transaction amount. Specify the amounts in lower denominations. For
                example, to search for transactions from $5.00 to $10.05, specify ``[500 TO 1005]``. Note:The values
                must be URL encoded.
            transaction_currency: Filters the transactions in the response by a `three-character ISO-4217 currency code
                <https://developer.paypal.com/api/rest/reference/currency-codes/>`__ for the PayPal transaction
                currency.
            payment_instrument_type: Filters the transactions in the response by a payment instrument type. Value is
                either: CREDITCARD. Returns a direct credit card transaction with a corresponding value. DEBITCARD.
                Returns a debit card transaction with a corresponding value. If you omit this parameter, the API does
                not apply this filter.
            store_id: Filters the transactions in the response by a store ID.
            terminal_id: Filters the transactions in the response by a terminal ID.
            fields: Indicates which fields appear in the response. Value is a single field or a comma-separated list of
                fields. The transaction_info value returns only the transaction details in the response. To include all
                fields in the response, specify fields=all. Valid fields are: transaction_info. The transaction
                information. Includes the ID of the PayPal account of the payee, the PayPal-generated transaction ID,
                the PayPal-generated base ID, the PayPal reference ID type, the transaction event code, the date and
                time when the transaction was initiated and was last updated, the transaction amounts including the
                PayPal fee, any discounts, insurance, the transaction status, and other information about the
                transaction. payer_info. The payer information. Includes the PayPal customer account ID and the payer's
                email address, primary phone number, name, country code, address, and whether the payer is verified or
                unverified. shipping_info. The shipping information. Includes the recipient's name, the shipping method
                for this order, the shipping address for this order, and the secondary address associated with this
                order. auction_info. The auction information. Includes the name of the auction site, the auction site
                URL, the ID of the customer who makes the purchase in the auction, and the date and time when the
                auction closes. cart_info. The cart information. Includes an array of item details, whether the item
                amount or the shipping amount already includes tax, and the ID of the invoice for PayPal-generated
                invoices. incentive_info. An array of incentive detail objects. Each object includes the incentive, such
                as a special offer or coupon, the incentive amount, and the incentive program code that identifies a
                merchant loyalty or incentive program. store_info. The store information. Includes the ID of the
                merchant store and the terminal ID for the checkout stand in the merchant store.
            balance_affecting_records_only: Indicates whether the response includes only balance-impacting transactions
                or all transactions. Value is either: Y. The default. The response includes only balance transactions.
                N. The response includes all transactions.
            page_size: The number of items to return in the response. So, the combination of ``page=1`` and
                ``page_size=20`` returns the first 20 items. The combination of ``page=2`` and ``page_size=20`` returns
                the next 20 items.
            page: The zero-relative start index of the entire list of items that are returned in the response. So, the
                combination of ``page=1`` and ``page_size=20`` returns the first 20 items.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that lists
            transactions .

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.search_transactions(
            start_date,
            end_date,
            transaction_id=transaction_id,
            transaction_type=transaction_type,
            transaction_status=transaction_status,
            transaction_amount=transaction_amount,
            transaction_currency=transaction_currency,
            payment_instrument_type=payment_instrument_type,
            store_id=store_id,
            terminal_id=terminal_id,
            fields=fields,
            balance_affecting_records_only=balance_affecting_records_only,
            page_size=page_size,
            page=page,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> TransactionSearchWithRawResponse:
        return self._with_raw_response


class AsyncTransactionSearch:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTransactionSearchWithRawResponse(client, server, auth)

    async def search_balances(
        self,
        *,
        as_of_time: str | None = None,
        currency_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BalancesResponse:
        """List all balances. Specify date time to list balances for that time that appear in the response. Notes: It
        takes a maximum of three hours for balances to appear in the list balances call. This call lists balances upto
        the previous three years.

        Args:
            as_of_time: List balances in the response at the date time provided, will return the last refreshed balance
                in the system when not provided.
            currency_code: Filters the transactions in the response by a `three-character ISO-4217 currency code
                <https://developer.paypal.com/api/rest/reference/currency-codes/>`__ for the PayPal transaction
                currency.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that lists balances .

        Raises:
            ApiError: The request is not well-formed, is syntactically incorrect, or violates schema. Authorization
                failed due to insufficient permissions. An internal server error occurred. ``error`` is ``DefaultError |
                RawError``."""
        return (
            await self._with_raw_response.search_balances(
                as_of_time=as_of_time, currency_code=currency_code, request_options=request_options
            )
        ).unwrap()

    async def search_transactions(
        self,
        start_date: str,
        end_date: str,
        *,
        transaction_id: str | None = None,
        transaction_type: str | None = None,
        transaction_status: str | None = None,
        transaction_amount: str | None = None,
        transaction_currency: str | None = None,
        payment_instrument_type: str | None = None,
        store_id: str | None = None,
        terminal_id: str | None = None,
        fields: str | None = "transaction_info",
        balance_affecting_records_only: str | None = "Y",
        page_size: int | None = 100,
        page: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchResponse:
        """Lists transactions. Specify one or more query parameters to filter the transaction that appear in the
        response. Notes: If you specify one or more optional query parameters, the ending_balance response field is
        empty. It takes a maximum of three hours for executed transactions to appear in the list transactions call. This
        call lists transaction for the previous three years.

        Args:
            start_date: Filters the transactions in the response by a start date and time, in `Internet date and time
                format <https://tools.ietf.org/html/rfc3339#section-5.6>`__. Seconds are required. Fractional seconds
                are optional.
            end_date: Filters the transactions in the response by an end date and time, in `Internet date and time
                format <https://tools.ietf.org/html/rfc3339#section-5.6>`__. Seconds are required. Fractional seconds
                are optional. The maximum supported range is 31 days.
            transaction_id: Filters the transactions in the response by a PayPal transaction ID. A valid transaction ID
                is 17 characters long, except for an order ID, which is 19 characters long. Note: A transaction ID is
                not unique in the reporting system. The response can list two transactions with the same ID. One
                transaction can be balance affecting while the other is non-balance affecting.
            transaction_type: Filters the transactions in the response by a PayPal transaction event code. See
                `Transaction event codes </docs/integration/direct/transaction-search/transaction-event-codes/>`__.
            transaction_status: Filters the transactions in the response by a PayPal transaction status code. Value is:
                Status code Description D PayPal or merchant rules denied the transaction. P The transaction is pending.
                The transaction was created but waits for another payment process to complete, such as an ACH
                transaction, before the status changes to S. S The transaction successfully completed without a denial
                and after any pending statuses. V A successful transaction was reversed and funds were refunded to the
                original sender.
            transaction_amount: Filters the transactions in the response by a gross transaction amount range. Specify
                the range as `` TO ``, where `` `` is the lower limit of the gross PayPal transaction amount and `` ``
                is the upper limit of the gross transaction amount. Specify the amounts in lower denominations. For
                example, to search for transactions from $5.00 to $10.05, specify ``[500 TO 1005]``. Note:The values
                must be URL encoded.
            transaction_currency: Filters the transactions in the response by a `three-character ISO-4217 currency code
                <https://developer.paypal.com/api/rest/reference/currency-codes/>`__ for the PayPal transaction
                currency.
            payment_instrument_type: Filters the transactions in the response by a payment instrument type. Value is
                either: CREDITCARD. Returns a direct credit card transaction with a corresponding value. DEBITCARD.
                Returns a debit card transaction with a corresponding value. If you omit this parameter, the API does
                not apply this filter.
            store_id: Filters the transactions in the response by a store ID.
            terminal_id: Filters the transactions in the response by a terminal ID.
            fields: Indicates which fields appear in the response. Value is a single field or a comma-separated list of
                fields. The transaction_info value returns only the transaction details in the response. To include all
                fields in the response, specify fields=all. Valid fields are: transaction_info. The transaction
                information. Includes the ID of the PayPal account of the payee, the PayPal-generated transaction ID,
                the PayPal-generated base ID, the PayPal reference ID type, the transaction event code, the date and
                time when the transaction was initiated and was last updated, the transaction amounts including the
                PayPal fee, any discounts, insurance, the transaction status, and other information about the
                transaction. payer_info. The payer information. Includes the PayPal customer account ID and the payer's
                email address, primary phone number, name, country code, address, and whether the payer is verified or
                unverified. shipping_info. The shipping information. Includes the recipient's name, the shipping method
                for this order, the shipping address for this order, and the secondary address associated with this
                order. auction_info. The auction information. Includes the name of the auction site, the auction site
                URL, the ID of the customer who makes the purchase in the auction, and the date and time when the
                auction closes. cart_info. The cart information. Includes an array of item details, whether the item
                amount or the shipping amount already includes tax, and the ID of the invoice for PayPal-generated
                invoices. incentive_info. An array of incentive detail objects. Each object includes the incentive, such
                as a special offer or coupon, the incentive amount, and the incentive program code that identifies a
                merchant loyalty or incentive program. store_info. The store information. Includes the ID of the
                merchant store and the terminal ID for the checkout stand in the merchant store.
            balance_affecting_records_only: Indicates whether the response includes only balance-impacting transactions
                or all transactions. Value is either: Y. The default. The response includes only balance transactions.
                N. The response includes all transactions.
            page_size: The number of items to return in the response. So, the combination of ``page=1`` and
                ``page_size=20`` returns the first 20 items. The combination of ``page=2`` and ``page_size=20`` returns
                the next 20 items.
            page: The zero-relative start index of the entire list of items that are returned in the response. So, the
                combination of ``page=1`` and ``page_size=20`` returns the first 20 items.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful request returns the HTTP ``200 OK`` status code and a JSON response body that lists
            transactions .

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.search_transactions(
                start_date,
                end_date,
                transaction_id=transaction_id,
                transaction_type=transaction_type,
                transaction_status=transaction_status,
                transaction_amount=transaction_amount,
                transaction_currency=transaction_currency,
                payment_instrument_type=payment_instrument_type,
                store_id=store_id,
                terminal_id=terminal_id,
                fields=fields,
                balance_affecting_records_only=balance_affecting_records_only,
                page_size=page_size,
                page=page,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTransactionSearchWithRawResponse:
        return self._with_raw_response


class TransactionSearchWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def search_balances(
        self,
        *,
        as_of_time: str | None = None,
        currency_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BalancesResponse, SearchBalancesErrorBody]:
        """List all balances. Specify date time to list balances for that time that appear in the response. Notes: It
        takes a maximum of three hours for balances to appear in the list balances call. This call lists balances upto
        the previous three years.

        Args:
            as_of_time: List balances in the response at the date time provided, will return the last refreshed balance
                in the system when not provided.
            currency_code: Filters the transactions in the response by a `three-character ISO-4217 currency code
                <https://developer.paypal.com/api/rest/reference/currency-codes/>`__ for the PayPal transaction
                currency.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/reporting/balances"),
            query_params=[
                param[str | None]("as_of_time", as_of_time), param[str | None]("currency_code", currency_code)
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BalancesResponse],
            error_mapper=search_balances_error_mapper,
            request_options=request_options,
        )

    def search_transactions(
        self,
        start_date: str,
        end_date: str,
        *,
        transaction_id: str | None = None,
        transaction_type: str | None = None,
        transaction_status: str | None = None,
        transaction_amount: str | None = None,
        transaction_currency: str | None = None,
        payment_instrument_type: str | None = None,
        store_id: str | None = None,
        terminal_id: str | None = None,
        fields: str | None = "transaction_info",
        balance_affecting_records_only: str | None = "Y",
        page_size: int | None = 100,
        page: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchResponse, RawError]:
        """Lists transactions. Specify one or more query parameters to filter the transaction that appear in the
        response. Notes: If you specify one or more optional query parameters, the ending_balance response field is
        empty. It takes a maximum of three hours for executed transactions to appear in the list transactions call. This
        call lists transaction for the previous three years.

        Args:
            start_date: Filters the transactions in the response by a start date and time, in `Internet date and time
                format <https://tools.ietf.org/html/rfc3339#section-5.6>`__. Seconds are required. Fractional seconds
                are optional.
            end_date: Filters the transactions in the response by an end date and time, in `Internet date and time
                format <https://tools.ietf.org/html/rfc3339#section-5.6>`__. Seconds are required. Fractional seconds
                are optional. The maximum supported range is 31 days.
            transaction_id: Filters the transactions in the response by a PayPal transaction ID. A valid transaction ID
                is 17 characters long, except for an order ID, which is 19 characters long. Note: A transaction ID is
                not unique in the reporting system. The response can list two transactions with the same ID. One
                transaction can be balance affecting while the other is non-balance affecting.
            transaction_type: Filters the transactions in the response by a PayPal transaction event code. See
                `Transaction event codes </docs/integration/direct/transaction-search/transaction-event-codes/>`__.
            transaction_status: Filters the transactions in the response by a PayPal transaction status code. Value is:
                Status code Description D PayPal or merchant rules denied the transaction. P The transaction is pending.
                The transaction was created but waits for another payment process to complete, such as an ACH
                transaction, before the status changes to S. S The transaction successfully completed without a denial
                and after any pending statuses. V A successful transaction was reversed and funds were refunded to the
                original sender.
            transaction_amount: Filters the transactions in the response by a gross transaction amount range. Specify
                the range as `` TO ``, where `` `` is the lower limit of the gross PayPal transaction amount and `` ``
                is the upper limit of the gross transaction amount. Specify the amounts in lower denominations. For
                example, to search for transactions from $5.00 to $10.05, specify ``[500 TO 1005]``. Note:The values
                must be URL encoded.
            transaction_currency: Filters the transactions in the response by a `three-character ISO-4217 currency code
                <https://developer.paypal.com/api/rest/reference/currency-codes/>`__ for the PayPal transaction
                currency.
            payment_instrument_type: Filters the transactions in the response by a payment instrument type. Value is
                either: CREDITCARD. Returns a direct credit card transaction with a corresponding value. DEBITCARD.
                Returns a debit card transaction with a corresponding value. If you omit this parameter, the API does
                not apply this filter.
            store_id: Filters the transactions in the response by a store ID.
            terminal_id: Filters the transactions in the response by a terminal ID.
            fields: Indicates which fields appear in the response. Value is a single field or a comma-separated list of
                fields. The transaction_info value returns only the transaction details in the response. To include all
                fields in the response, specify fields=all. Valid fields are: transaction_info. The transaction
                information. Includes the ID of the PayPal account of the payee, the PayPal-generated transaction ID,
                the PayPal-generated base ID, the PayPal reference ID type, the transaction event code, the date and
                time when the transaction was initiated and was last updated, the transaction amounts including the
                PayPal fee, any discounts, insurance, the transaction status, and other information about the
                transaction. payer_info. The payer information. Includes the PayPal customer account ID and the payer's
                email address, primary phone number, name, country code, address, and whether the payer is verified or
                unverified. shipping_info. The shipping information. Includes the recipient's name, the shipping method
                for this order, the shipping address for this order, and the secondary address associated with this
                order. auction_info. The auction information. Includes the name of the auction site, the auction site
                URL, the ID of the customer who makes the purchase in the auction, and the date and time when the
                auction closes. cart_info. The cart information. Includes an array of item details, whether the item
                amount or the shipping amount already includes tax, and the ID of the invoice for PayPal-generated
                invoices. incentive_info. An array of incentive detail objects. Each object includes the incentive, such
                as a special offer or coupon, the incentive amount, and the incentive program code that identifies a
                merchant loyalty or incentive program. store_info. The store information. Includes the ID of the
                merchant store and the terminal ID for the checkout stand in the merchant store.
            balance_affecting_records_only: Indicates whether the response includes only balance-impacting transactions
                or all transactions. Value is either: Y. The default. The response includes only balance transactions.
                N. The response includes all transactions.
            page_size: The number of items to return in the response. So, the combination of ``page=1`` and
                ``page_size=20`` returns the first 20 items. The combination of ``page=2`` and ``page_size=20`` returns
                the next 20 items.
            page: The zero-relative start index of the entire list of items that are returned in the response. So, the
                combination of ``page=1`` and ``page_size=20`` returns the first 20 items.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/reporting/transactions"),
            query_params=[
                param[str]("start_date", start_date),
                param[str]("end_date", end_date),
                param[str | None]("transaction_id", transaction_id),
                param[str | None]("transaction_type", transaction_type),
                param[str | None]("transaction_status", transaction_status),
                param[str | None]("transaction_amount", transaction_amount),
                param[str | None]("transaction_currency", transaction_currency),
                param[str | None]("payment_instrument_type", payment_instrument_type),
                param[str | None]("store_id", store_id),
                param[str | None]("terminal_id", terminal_id),
                param[str | None]("fields", fields),
                param[str | None]("balance_affecting_records_only", balance_affecting_records_only),
                param[int | None]("page_size", page_size),
                param[int | None]("page", page),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTransactionSearchWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def search_balances(
        self,
        *,
        as_of_time: str | None = None,
        currency_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BalancesResponse, SearchBalancesErrorBody]:
        """List all balances. Specify date time to list balances for that time that appear in the response. Notes: It
        takes a maximum of three hours for balances to appear in the list balances call. This call lists balances upto
        the previous three years.

        Args:
            as_of_time: List balances in the response at the date time provided, will return the last refreshed balance
                in the system when not provided.
            currency_code: Filters the transactions in the response by a `three-character ISO-4217 currency code
                <https://developer.paypal.com/api/rest/reference/currency-codes/>`__ for the PayPal transaction
                currency.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/reporting/balances"),
            query_params=[
                param[str | None]("as_of_time", as_of_time), param[str | None]("currency_code", currency_code)
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BalancesResponse],
            error_mapper=search_balances_error_mapper,
            request_options=request_options,
        )

    async def search_transactions(
        self,
        start_date: str,
        end_date: str,
        *,
        transaction_id: str | None = None,
        transaction_type: str | None = None,
        transaction_status: str | None = None,
        transaction_amount: str | None = None,
        transaction_currency: str | None = None,
        payment_instrument_type: str | None = None,
        store_id: str | None = None,
        terminal_id: str | None = None,
        fields: str | None = "transaction_info",
        balance_affecting_records_only: str | None = "Y",
        page_size: int | None = 100,
        page: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchResponse, RawError]:
        """Lists transactions. Specify one or more query parameters to filter the transaction that appear in the
        response. Notes: If you specify one or more optional query parameters, the ending_balance response field is
        empty. It takes a maximum of three hours for executed transactions to appear in the list transactions call. This
        call lists transaction for the previous three years.

        Args:
            start_date: Filters the transactions in the response by a start date and time, in `Internet date and time
                format <https://tools.ietf.org/html/rfc3339#section-5.6>`__. Seconds are required. Fractional seconds
                are optional.
            end_date: Filters the transactions in the response by an end date and time, in `Internet date and time
                format <https://tools.ietf.org/html/rfc3339#section-5.6>`__. Seconds are required. Fractional seconds
                are optional. The maximum supported range is 31 days.
            transaction_id: Filters the transactions in the response by a PayPal transaction ID. A valid transaction ID
                is 17 characters long, except for an order ID, which is 19 characters long. Note: A transaction ID is
                not unique in the reporting system. The response can list two transactions with the same ID. One
                transaction can be balance affecting while the other is non-balance affecting.
            transaction_type: Filters the transactions in the response by a PayPal transaction event code. See
                `Transaction event codes </docs/integration/direct/transaction-search/transaction-event-codes/>`__.
            transaction_status: Filters the transactions in the response by a PayPal transaction status code. Value is:
                Status code Description D PayPal or merchant rules denied the transaction. P The transaction is pending.
                The transaction was created but waits for another payment process to complete, such as an ACH
                transaction, before the status changes to S. S The transaction successfully completed without a denial
                and after any pending statuses. V A successful transaction was reversed and funds were refunded to the
                original sender.
            transaction_amount: Filters the transactions in the response by a gross transaction amount range. Specify
                the range as `` TO ``, where `` `` is the lower limit of the gross PayPal transaction amount and `` ``
                is the upper limit of the gross transaction amount. Specify the amounts in lower denominations. For
                example, to search for transactions from $5.00 to $10.05, specify ``[500 TO 1005]``. Note:The values
                must be URL encoded.
            transaction_currency: Filters the transactions in the response by a `three-character ISO-4217 currency code
                <https://developer.paypal.com/api/rest/reference/currency-codes/>`__ for the PayPal transaction
                currency.
            payment_instrument_type: Filters the transactions in the response by a payment instrument type. Value is
                either: CREDITCARD. Returns a direct credit card transaction with a corresponding value. DEBITCARD.
                Returns a debit card transaction with a corresponding value. If you omit this parameter, the API does
                not apply this filter.
            store_id: Filters the transactions in the response by a store ID.
            terminal_id: Filters the transactions in the response by a terminal ID.
            fields: Indicates which fields appear in the response. Value is a single field or a comma-separated list of
                fields. The transaction_info value returns only the transaction details in the response. To include all
                fields in the response, specify fields=all. Valid fields are: transaction_info. The transaction
                information. Includes the ID of the PayPal account of the payee, the PayPal-generated transaction ID,
                the PayPal-generated base ID, the PayPal reference ID type, the transaction event code, the date and
                time when the transaction was initiated and was last updated, the transaction amounts including the
                PayPal fee, any discounts, insurance, the transaction status, and other information about the
                transaction. payer_info. The payer information. Includes the PayPal customer account ID and the payer's
                email address, primary phone number, name, country code, address, and whether the payer is verified or
                unverified. shipping_info. The shipping information. Includes the recipient's name, the shipping method
                for this order, the shipping address for this order, and the secondary address associated with this
                order. auction_info. The auction information. Includes the name of the auction site, the auction site
                URL, the ID of the customer who makes the purchase in the auction, and the date and time when the
                auction closes. cart_info. The cart information. Includes an array of item details, whether the item
                amount or the shipping amount already includes tax, and the ID of the invoice for PayPal-generated
                invoices. incentive_info. An array of incentive detail objects. Each object includes the incentive, such
                as a special offer or coupon, the incentive amount, and the incentive program code that identifies a
                merchant loyalty or incentive program. store_info. The store information. Includes the ID of the
                merchant store and the terminal ID for the checkout stand in the merchant store.
            balance_affecting_records_only: Indicates whether the response includes only balance-impacting transactions
                or all transactions. Value is either: Y. The default. The response includes only balance transactions.
                N. The response includes all transactions.
            page_size: The number of items to return in the response. So, the combination of ``page=1`` and
                ``page_size=20`` returns the first 20 items. The combination of ``page=2`` and ``page_size=20`` returns
                the next 20 items.
            page: The zero-relative start index of the entire list of items that are returned in the response. So, the
                combination of ``page=1`` and ``page_size=20`` returns the first 20 items.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/reporting/transactions"),
            query_params=[
                param[str]("start_date", start_date),
                param[str]("end_date", end_date),
                param[str | None]("transaction_id", transaction_id),
                param[str | None]("transaction_type", transaction_type),
                param[str | None]("transaction_status", transaction_status),
                param[str | None]("transaction_amount", transaction_amount),
                param[str | None]("transaction_currency", transaction_currency),
                param[str | None]("payment_instrument_type", payment_instrument_type),
                param[str | None]("store_id", store_id),
                param[str | None]("terminal_id", terminal_id),
                param[str | None]("fields", fields),
                param[str | None]("balance_affecting_records_only", balance_affecting_records_only),
                param[int | None]("page_size", page_size),
                param[int | None]("page", page),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
