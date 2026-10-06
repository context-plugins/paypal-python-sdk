from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

GetSetupTokenErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _GetSetupTokenError:
    def map(self, status_code: int, content: bytes) -> GetSetupTokenErrorBody:
        match status_code:
            case 403 | 404 | 422 | 500:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


get_setup_token_error_mapper: Final[ErrorMapper[GetSetupTokenErrorBody]] = _GetSetupTokenError()
