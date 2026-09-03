from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error import DefaultError

SearchBalancesErrorBody: TypeAlias = DefaultError | RawError


@dataclass(frozen=True, slots=True)
class _SearchBalancesError:
    def map(self, response: HttpResponse) -> SearchBalancesErrorBody:
        match response.status_code:
            case 400 | 403 | 500:
                return decode_json[DefaultError](response)
            case _:
                return RawError(response)


search_balances_error_mapper: Final[ErrorMapper[SearchBalancesErrorBody]] = _SearchBalancesError()
