from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

PatchOrderErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _PatchOrderError:
    def map(self, status_code: int, content: bytes) -> PatchOrderErrorBody:
        match status_code:
            case 400 | 401 | 404 | 422:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


patch_order_error_mapper: Final[ErrorMapper[PatchOrderErrorBody]] = _PatchOrderError()
