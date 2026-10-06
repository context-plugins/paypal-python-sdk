from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.subscription_error import SubscriptionError

CancelSubscriptionErrorBody: TypeAlias = SubscriptionError | RawError


@dataclass(frozen=True, slots=True)
class _CancelSubscriptionError:
    def map(self, status_code: int, content: bytes) -> CancelSubscriptionErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404 | 422 | 500:
                return decode_json[SubscriptionError](content)
            case _:
                return RawError(status_code, content)


cancel_subscription_error_mapper: Final[ErrorMapper[CancelSubscriptionErrorBody]] = _CancelSubscriptionError()
