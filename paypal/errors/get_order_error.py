from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

GetOrderErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetOrderError:
    def map(self, response: HttpResponse) -> GetOrderErrorBody:
        match response.status_code:
            case 401 | 404:
                return decode_json[Error](response)
            case _:
                return RawError(response)


get_order_error_mapper: Final[ErrorMapper[GetOrderErrorBody]] = _GetOrderError()
