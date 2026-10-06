from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

UpdateOrderTrackingErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _UpdateOrderTrackingError:
    def map(self, status_code: int, content: bytes) -> UpdateOrderTrackingErrorBody:
        match status_code:
            case 400 | 403 | 404 | 422 | 500:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


update_order_tracking_error_mapper: Final[ErrorMapper[UpdateOrderTrackingErrorBody]] = _UpdateOrderTrackingError()
