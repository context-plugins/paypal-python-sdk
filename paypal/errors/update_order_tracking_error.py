from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

UpdateOrderTrackingErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _UpdateOrderTrackingError:
    def map(self, response: HttpResponse) -> UpdateOrderTrackingErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 422 | 500:
                return decode_json[Error](response)
            case _:
                return RawError(response)


update_order_tracking_error_mapper: Final[ErrorMapper[UpdateOrderTrackingErrorBody]] = _UpdateOrderTrackingError()
