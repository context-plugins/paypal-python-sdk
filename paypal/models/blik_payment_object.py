from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .blik_one_click_payment_object import BlikOneClickPaymentObject, BlikOneClickPaymentObjectDict


class BlikPaymentObject(SdkBaseModel):
    """Information used to pay using BLIK."""

    name: Optional[str] = UNSET
    """The full name representation like Mr J Smith."""

    country_code: Optional[str] = UNSET
    """The `two-character ISO 3166-1 code <https://developer.paypal.com/api/rest/reference/country-codes/>`__ that
    identifies the country or region. Note: The country code for Great Britain is GB and not UK as used in the top-level
    domain names for that country. Use the ``C2`` country code for China worldwide for comparable uncontrolled price
    (CUP) method, bank card, and cross-border transactions."""

    email: Optional[str] = UNSET
    """The internationalized email address. Note: Up to 64 characters are allowed before and 255 characters are allowed
    after the @ sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern
    verifies that an unquoted @ sign exists."""

    one_click: Optional[BlikOneClickPaymentObject] = UNSET
    """Information used to pay using BLIK one-click flow."""


class BlikPaymentObjectDict(TypedDict):
    name: NotRequired[str]
    country_code: NotRequired[str]
    email: NotRequired[str]
    one_click: NotRequired[BlikOneClickPaymentObject | BlikOneClickPaymentObjectDict]
