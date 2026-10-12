from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class P24PaymentObject(SdkBaseModel):
    """Information used to pay using P24(Przelewy24)."""

    name: Optional[str] = UNSET
    """The full name representation like Mr J Smith."""

    email: Optional[str] = UNSET
    """The internationalized email address. Note: Up to 64 characters are allowed before and 255 characters are allowed
    after the @ sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern
    verifies that an unquoted @ sign exists."""

    country_code: Optional[str] = UNSET
    """The `two-character ISO 3166-1 code <https://developer.paypal.com/api/rest/reference/country-codes/>`__ that
    identifies the country or region. Note: The country code for Great Britain is GB and not UK as used in the top-level
    domain names for that country. Use the ``C2`` country code for China worldwide for comparable uncontrolled price
    (CUP) method, bank card, and cross-border transactions."""

    payment_descriptor: Optional[str] = UNSET
    """P24 generated payment description."""

    method_id: Optional[str] = UNSET
    """Numeric identifier of the payment scheme or bank used for the payment."""

    method_description: Optional[str] = UNSET
    """Friendly name of the payment scheme or bank used for the payment."""


class P24PaymentObjectDict(TypedDict):
    name: NotRequired[str]
    email: NotRequired[str]
    country_code: NotRequired[str]
    payment_descriptor: NotRequired[str]
    method_id: NotRequired[str]
    method_description: NotRequired[str]
