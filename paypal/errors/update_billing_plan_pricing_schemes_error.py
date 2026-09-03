from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.subscription_error import SubscriptionError

UpdateBillingPlanPricingSchemesErrorBody: TypeAlias = SubscriptionError | RawError


@dataclass(frozen=True, slots=True)
class _UpdateBillingPlanPricingSchemesError:
    def map(self, response: HttpResponse) -> UpdateBillingPlanPricingSchemesErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 422 | 500:
                return decode_json[SubscriptionError](response)
            case _:
                return RawError(response)


update_billing_plan_pricing_schemes_error_mapper: Final[
    ErrorMapper[UpdateBillingPlanPricingSchemesErrorBody]
] = _UpdateBillingPlanPricingSchemesError()
