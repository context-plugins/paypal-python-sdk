from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .blik_experience_context import BlikExperienceContext, BlikExperienceContextDict
from .blik_level0_payment_object import BlikLevel0PaymentObject, BlikLevel0PaymentObjectDict
from .blik_one_click_payment_request import BlikOneClickPaymentRequest, BlikOneClickPaymentRequestDict


class BlikPaymentRequest(SdkBaseModel):
    """Information needed to pay using BLIK."""

    name: str
    """The full name representation like Mr J Smith."""

    country_code: str
    """The `two-character ISO 3166-1 code <https://developer.paypal.com/api/rest/reference/country-codes/>`__ that
    identifies the country or region. Note: The country code for Great Britain is GB and not UK as used in the top-level
    domain names for that country. Use the ``C2`` country code for China worldwide for comparable uncontrolled price
    (CUP) method, bank card, and cross-border transactions."""

    email: Optional[str] = UNSET
    """The internationalized email address. Note: Up to 64 characters are allowed before and 255 characters are allowed
    after the @ sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern
    verifies that an unquoted @ sign exists."""

    experience_context: Optional[BlikExperienceContext] = UNSET
    """Customizes the payer experience during the approval process for the BLIK payment."""

    level_0: Optional[BlikLevel0PaymentObject] = UNSET
    """Information used to pay using BLIK level_0 flow."""

    one_click: Optional[BlikOneClickPaymentRequest] = UNSET
    """Information used to pay using BLIK one-click flow."""


class BlikPaymentRequestDict(TypedDict):
    name: str
    country_code: str
    email: NotRequired[str]
    experience_context: NotRequired[BlikExperienceContext | BlikExperienceContextDict]
    level_0: NotRequired[BlikLevel0PaymentObject | BlikLevel0PaymentObjectDict]
    one_click: NotRequired[BlikOneClickPaymentRequest | BlikOneClickPaymentRequestDict]
