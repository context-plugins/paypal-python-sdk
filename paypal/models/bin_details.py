from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BinDetails(SdkBaseModel):
    """Bank Identification Number (BIN) details used to fund a payment."""

    bin: Optional[str] = UNSET
    """The Bank Identification Number (BIN) signifies the number that is being used to identify the granular level
    details (except the PII information) of the card."""

    issuing_bank: Optional[str] = UNSET
    """The issuer of the card instrument."""

    bin_country_code: Optional[str] = UNSET
    """The `two-character ISO 3166-1 code <https://developer.paypal.com/api/rest/reference/country-codes/>`__ that
    identifies the country or region. Note: The country code for Great Britain is GB and not UK as used in the top-level
    domain names for that country. Use the ``C2`` country code for China worldwide for comparable uncontrolled price
    (CUP) method, bank card, and cross-border transactions."""

    products: Optional[list[str]] = UNSET
    """The type of card product assigned to the BIN by the issuer. These values are defined by the issuer and may change
    over time. Some examples include: PREPAID_GIFT, CONSUMER, CORPORATE."""


class BinDetailsDict(TypedDict):
    bin: NotRequired[str]
    issuing_bank: NotRequired[str]
    bin_country_code: NotRequired[str]
    products: NotRequired[list[str]]
