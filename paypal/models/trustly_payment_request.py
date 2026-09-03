from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .experience_context import ExperienceContext, ExperienceContextDict


class TrustlyPaymentRequest(SdkBaseModel):
    """Information needed to pay using Trustly."""

    name: str
    """The full name representation like Mr J Smith."""

    country_code: str
    """The `two-character ISO 3166-1 code <https://developer.paypal.com/api/rest/reference/country-codes/>`__ that
    identifies the country or region. Note: The country code for Great Britain is GB and not UK as used in the top-level
    domain names for that country. Use the ``C2`` country code for China worldwide for comparable uncontrolled price
    (CUP) method, bank card, and cross-border transactions."""

    email: str
    """The internationalized email address. Note: Up to 64 characters are allowed before and 255 characters are allowed
    after the @ sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern
    verifies that an unquoted @ sign exists."""

    experience_context: Optional[ExperienceContext] = UNSET
    """Customizes the payer experience during the approval process for the payment."""


class TrustlyPaymentRequestDict(TypedDict):
    name: str
    country_code: str
    email: str
    experience_context: NotRequired[ExperienceContext | ExperienceContextDict]
