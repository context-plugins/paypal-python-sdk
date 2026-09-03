from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

ReauthorizePaymentErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _ReauthorizePaymentError:
    def map(self, response: HttpResponse) -> ReauthorizePaymentErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 422:
                return decode_json[Error](response)
            case 500:
                return RawError(response)
            case _:
                return RawError(response)


reauthorize_payment_error_mapper: Final[ErrorMapper[ReauthorizePaymentErrorBody]] = _ReauthorizePaymentError()
