from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

ListCustomerPaymentTokensErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _ListCustomerPaymentTokensError:
    def map(self, response: HttpResponse) -> ListCustomerPaymentTokensErrorBody:
        match response.status_code:
            case 400 | 403 | 500:
                return decode_json[Error](response)
            case _:
                return RawError(response)


list_customer_payment_tokens_error_mapper: Final[
    ErrorMapper[ListCustomerPaymentTokensErrorBody]
] = _ListCustomerPaymentTokensError()
