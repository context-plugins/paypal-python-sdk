from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

AuthorizeOrderErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _AuthorizeOrderError:
    def map(self, response: HttpResponse) -> AuthorizeOrderErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 422 | 500:
                return decode_json[Error](response)
            case _:
                return RawError(response)


authorize_order_error_mapper: Final[ErrorMapper[AuthorizeOrderErrorBody]] = _AuthorizeOrderError()
