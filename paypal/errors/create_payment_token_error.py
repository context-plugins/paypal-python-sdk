from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

CreatePaymentTokenErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CreatePaymentTokenError:
    def map(self, status_code: int, content: bytes) -> CreatePaymentTokenErrorBody:
        match status_code:
            case 400 | 403 | 404 | 422 | 500:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


create_payment_token_error_mapper: Final[ErrorMapper[CreatePaymentTokenErrorBody]] = _CreatePaymentTokenError()
