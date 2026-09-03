from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .experience_context import ExperienceContext, ExperienceContextDict


class EpsPaymentRequest(SdkBaseModel):
    """Information needed to pay using eps."""

    name: str
    """The full name representation like Mr J Smith."""

    country_code: str
    """The `two-character ISO 3166-1 code <https://developer.paypal.com/api/rest/reference/country-codes/>`__ that
    identifies the country or region. Note: The country code for Great Britain is GB and not UK as used in the top-level
    domain names for that country. Use the ``C2`` country code for China worldwide for comparable uncontrolled price
    (CUP) method, bank card, and cross-border transactions."""

    experience_context: Optional[ExperienceContext] = UNSET
    """Customizes the payer experience during the approval process for the payment."""


class EpsPaymentRequestDict(TypedDict):
    name: str
    country_code: str
    experience_context: NotRequired[ExperienceContext | ExperienceContextDict]
