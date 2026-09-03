from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetAuthorizedPaymentErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetAuthorizedPaymentError:
    def map(self, response: HttpResponse) -> GetAuthorizedPaymentErrorBody:
        match response.status_code:
            case 401 | 403 | 404:
                return decode_json[Error](response)
            case 500:
                return RawError(response)
            case _:
                return RawError(response)


get_authorized_payment_error_mapper: Final[ErrorMapper[GetAuthorizedPaymentErrorBody]] = _GetAuthorizedPaymentError()
