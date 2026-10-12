from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ExchangeRate(SdkBaseModel):
    """The exchange rate that determines the amount to convert from one currency to another currency."""

    source_currency: Optional[str] = UNSET
    """The `three-character ISO-4217 currency code <https://developer.paypal.com/api/rest/reference/currency-codes/>`__
    that identifies the currency."""

    target_currency: Optional[str] = UNSET
    """The `three-character ISO-4217 currency code <https://developer.paypal.com/api/rest/reference/currency-codes/>`__
    that identifies the currency."""

    value: Optional[str] = UNSET
    """The target currency amount. Equivalent to one unit of the source currency. Formatted as integer or decimal value
    with one to 15 digits to the right of the decimal point."""


class ExchangeRateDict(TypedDict):
    source_currency: NotRequired[str]
    target_currency: NotRequired[str]
    value: NotRequired[str]
