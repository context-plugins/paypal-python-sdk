from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetCapturedPaymentErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetCapturedPaymentError:
    def map(self, status_code: int, content: bytes) -> GetCapturedPaymentErrorBody:
        match status_code:
            case 401 | 403 | 404:
                return decode_json[Error](content)
            case 500:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


get_captured_payment_error_mapper: Final[ErrorMapper[GetCapturedPaymentErrorBody]] = _GetCapturedPaymentError()
