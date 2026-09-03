from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DeletePaymentTokenErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DeletePaymentTokenError:
    def map(self, response: HttpResponse) -> DeletePaymentTokenErrorBody:
        match response.status_code:
            case 400 | 403 | 500:
                return decode_json[Error](response)
            case _:
                return RawError(response)


delete_payment_token_error_mapper: Final[ErrorMapper[DeletePaymentTokenErrorBody]] = _DeletePaymentTokenError()
