from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetRefundErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetRefundError:
    def map(self, response: HttpResponse) -> GetRefundErrorBody:
        match response.status_code:
            case 401 | 403 | 404:
                return decode_json[Error](response)
            case 500:
                return RawError(response)
            case _:
                return RawError(response)


get_refund_error_mapper: Final[ErrorMapper[GetRefundErrorBody]] = _GetRefundError()
