from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.subscription_error import SubscriptionError

CreateSubscriptionErrorBody: TypeAlias = SubscriptionError | RawError


@dataclass(frozen=True, slots=True)
class _CreateSubscriptionError:
    def map(self, response: HttpResponse) -> CreateSubscriptionErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[SubscriptionError](response)
            case _:
                return RawError(response)


create_subscription_error_mapper: Final[ErrorMapper[CreateSubscriptionErrorBody]] = _CreateSubscriptionError()
