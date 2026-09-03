from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CreateOrderTrackingErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CreateOrderTrackingError:
    def map(self, response: HttpResponse) -> CreateOrderTrackingErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 422 | 500:
                return decode_json[Error](response)
            case _:
                return RawError(response)


create_order_tracking_error_mapper: Final[ErrorMapper[CreateOrderTrackingErrorBody]] = _CreateOrderTrackingError()
