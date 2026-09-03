from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

CaptureOrderErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _CaptureOrderError:
    def map(self, response: HttpResponse) -> CaptureOrderErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 422 | 500:
                return decode_json[Error](response)
            case _:
                return RawError(response)


capture_order_error_mapper: Final[ErrorMapper[CaptureOrderErrorBody]] = _CaptureOrderError()
