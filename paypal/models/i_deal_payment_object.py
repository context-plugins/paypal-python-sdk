from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IDealPaymentObject(SdkBaseModel):
    """Information used to pay using iDEAL."""

    name: Optional[str] = UNSET
    """The full name representation like Mr J Smith."""

    country_code: Optional[str] = UNSET
    """The `two-character ISO 3166-1 code <https://developer.paypal.com/api/rest/reference/country-codes/>`__ that
    identifies the country or region. Note: The country code for Great Britain is GB and not UK as used in the top-level
    domain names for that country. Use the ``C2`` country code for China worldwide for comparable uncontrolled price
    (CUP) method, bank card, and cross-border transactions."""

    bic: Optional[str] = UNSET
    """The business identification code (BIC). In payments systems, a BIC is used to identify a specific business, most
    commonly a bank."""

    iban_last_chars: Optional[str] = UNSET
    """The last characters of the IBAN used to pay."""


class IDealPaymentObjectDict(TypedDict):
    name: NotRequired[str]
    country_code: NotRequired[str]
    bic: NotRequired[str]
    iban_last_chars: NotRequired[str]
