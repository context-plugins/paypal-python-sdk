from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.subscription_error import SubscriptionError

ActivateBillingPlanErrorBody: TypeAlias = SubscriptionError | RawError


@dataclass(frozen=True, slots=True)
class _ActivateBillingPlanError:
    def map(self, response: HttpResponse) -> ActivateBillingPlanErrorBody:
        match response.status_code:
            case 401 | 403 | 404 | 422 | 500:
                return decode_json[SubscriptionError](response)
            case _:
                return RawError(response)


activate_billing_plan_error_mapper: Final[ErrorMapper[ActivateBillingPlanErrorBody]] = _ActivateBillingPlanError()
