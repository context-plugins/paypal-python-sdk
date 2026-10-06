from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.subscription_error import SubscriptionError

GetSubscriptionErrorBody: TypeAlias = SubscriptionError | RawError


@dataclass(frozen=True, slots=True)
class _GetSubscriptionError:
    def map(self, status_code: int, content: bytes) -> GetSubscriptionErrorBody:
        match status_code:
            case 401 | 403 | 404 | 500:
                return decode_json[SubscriptionError](content)
            case _:
                return RawError(status_code, content)


get_subscription_error_mapper: Final[ErrorMapper[GetSubscriptionErrorBody]] = _GetSubscriptionError()
