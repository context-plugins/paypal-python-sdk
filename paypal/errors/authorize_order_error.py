from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

AuthorizeOrderErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AuthorizeOrderError:
    def map(self, status_code: int, content: bytes) -> AuthorizeOrderErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404 | 422 | 500:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


authorize_order_error_mapper: Final[ErrorMapper[AuthorizeOrderErrorBody]] = _AuthorizeOrderError()
