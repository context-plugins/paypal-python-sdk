from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.subscription_error import SubscriptionError

GetBillingPlanErrorBody: TypeAlias = SubscriptionError | RawError


@dataclass(frozen=True, slots=True)
class _GetBillingPlanError:
    def map(self, response: HttpResponse) -> GetBillingPlanErrorBody:
        match response.status_code:
            case 401 | 403 | 404 | 500:
                return decode_json[SubscriptionError](response)
            case _:
                return RawError(response)


get_billing_plan_error_mapper: Final[ErrorMapper[GetBillingPlanErrorBody]] = _GetBillingPlanError()
