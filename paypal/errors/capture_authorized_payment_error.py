from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

CaptureAuthorizedPaymentErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CaptureAuthorizedPaymentError:
    def map(self, status_code: int, content: bytes) -> CaptureAuthorizedPaymentErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404 | 409 | 422:
                return decode_json[Error](content)
            case 500:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


capture_authorized_payment_error_mapper: Final[
    ErrorMapper[CaptureAuthorizedPaymentErrorBody]
] = _CaptureAuthorizedPaymentError()
