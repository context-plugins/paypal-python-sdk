from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetCapturedPaymentErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetCapturedPaymentError:
    def map(self, response: HttpResponse) -> GetCapturedPaymentErrorBody:
        match response.status_code:
            case 401 | 403 | 404:
                return decode_json[Error](response)
            case 500:
                return RawError(response)
            case _:
                return RawError(response)


get_captured_payment_error_mapper: Final[ErrorMapper[GetCapturedPaymentErrorBody]] = _GetCapturedPaymentError()
