from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.subscription_error import SubscriptionError

GetSubscriptionErrorBody: TypeAlias = SubscriptionError | RawError


@dataclass(frozen=True, slots=True)
class _GetSubscriptionError:
    def map(self, response: HttpResponse) -> GetSubscriptionErrorBody:
        match response.status_code:
            case 401 | 403 | 404 | 500:
                return decode_json[SubscriptionError](response)
            case _:
                return RawError(response)


get_subscription_error_mapper: Final[ErrorMapper[GetSubscriptionErrorBody]] = _GetSubscriptionError()
