from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.subscription_error import SubscriptionError

PatchSubscriptionErrorBody: TypeAlias = SubscriptionError | RawError


@dataclass(frozen=True, slots=True)
class _PatchSubscriptionError:
    def map(self, response: HttpResponse) -> PatchSubscriptionErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 422 | 500:
                return decode_json[SubscriptionError](response)
            case _:
                return RawError(response)


patch_subscription_error_mapper: Final[ErrorMapper[PatchSubscriptionErrorBody]] = _PatchSubscriptionError()
