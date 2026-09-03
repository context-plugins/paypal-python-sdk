from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CreateOrderErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CreateOrderError:
    def map(self, response: HttpResponse) -> CreateOrderErrorBody:
        match response.status_code:
            case 400 | 401 | 422:
                return decode_json[Error](response)
            case _:
                return RawError(response)


create_order_error_mapper: Final[ErrorMapper[CreateOrderErrorBody]] = _CreateOrderError()
