from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

ConfirmOrderErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _ConfirmOrderError:
    def map(self, response: HttpResponse) -> ConfirmOrderErrorBody:
        match response.status_code:
            case 400 | 403 | 422 | 500:
                return decode_json[Error](response)
            case _:
                return RawError(response)


confirm_order_error_mapper: Final[ErrorMapper[ConfirmOrderErrorBody]] = _ConfirmOrderError()
