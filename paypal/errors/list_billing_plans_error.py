from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.subscription_error import SubscriptionError

ListBillingPlansErrorBody: TypeAlias = SubscriptionError | RawError


@dataclass(frozen=True, slots=True)
class _ListBillingPlansError:
    def map(self, response: HttpResponse) -> ListBillingPlansErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 500:
                return decode_json[SubscriptionError](response)
            case _:
                return RawError(response)


list_billing_plans_error_mapper: Final[ErrorMapper[ListBillingPlansErrorBody]] = _ListBillingPlansError()
