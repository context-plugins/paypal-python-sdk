from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.subscription_error import SubscriptionError

ListSubscriptionTransactionsErrorBody: TypeAlias = SubscriptionError | RawError


@dataclass(frozen=True, slots=True)
class _ListSubscriptionTransactionsError:
    def map(self, response: HttpResponse) -> ListSubscriptionTransactionsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 500:
                return decode_json[SubscriptionError](response)
            case _:
                return RawError(response)


list_subscription_transactions_error_mapper: Final[
    ErrorMapper[ListSubscriptionTransactionsErrorBody]
] = _ListSubscriptionTransactionsError()
