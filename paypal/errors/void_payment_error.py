from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

VoidPaymentErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _VoidPaymentError:
    def map(self, status_code: int, content: bytes) -> VoidPaymentErrorBody:
        match status_code:
            case 401 | 403 | 404 | 409 | 422:
                return decode_json[Error](content)
            case 500:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


void_payment_error_mapper: Final[ErrorMapper[VoidPaymentErrorBody]] = _VoidPaymentError()
