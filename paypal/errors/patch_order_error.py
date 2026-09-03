from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

PatchOrderErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _PatchOrderError:
    def map(self, response: HttpResponse) -> PatchOrderErrorBody:
        match response.status_code:
            case 400 | 401 | 404 | 422:
                return decode_json[Error](response)
            case _:
                return RawError(response)


patch_order_error_mapper: Final[ErrorMapper[PatchOrderErrorBody]] = _PatchOrderError()
