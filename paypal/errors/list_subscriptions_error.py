from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.subscription_error import SubscriptionError

ListSubscriptionsErrorBody: TypeAlias = SubscriptionError | RawError


@dataclass(frozen=True, slots=True)
class _ListSubscriptionsError:
    def map(self, response: HttpResponse) -> ListSubscriptionsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 500:
                return decode_json[SubscriptionError](response)
            case _:
                return RawError(response)


list_subscriptions_error_mapper: Final[ErrorMapper[ListSubscriptionsErrorBody]] = _ListSubscriptionsError()
