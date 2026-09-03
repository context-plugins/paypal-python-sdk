from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount_breakdown import AmountBreakdown, AmountBreakdownDict


class AmountWithBreakdown(SdkBaseModel):
    """The total order amount with an optional breakdown that provides details, such as the total item amount, total tax
    amount, shipping, handling, insurance, and discounts, if any. If you specify ``amount.breakdown``, the amount equals
    ``item_total`` plus ``tax_total`` plus ``shipping`` plus ``handling`` plus ``insurance`` minus ``shipping_discount``
    minus discount. The amount must be a positive number. For listed of supported currencies and decimal precision, see
    the PayPal REST APIs Currency Codes."""

    currency_code: str
    """The `three-character ISO-4217 currency code <https://developer.paypal.com/api/rest/reference/currency-codes/>`__
    that identifies the currency."""

    value: str
    """The value, which might be: An integer for currencies like ``JPY`` that are not typically fractional. A decimal
    fraction for currencies like ``TND`` that are subdivided into thousandths. For the required number of decimal places
    for a currency code, see `Currency Codes <https://developer.paypal.com/api/rest/reference/currency-codes/>`__."""

    breakdown: Optional[AmountBreakdown] = UNSET
    """The breakdown of the amount. Breakdown provides details such as total item amount, total tax amount, shipping,
    handling, insurance, and discounts, if any."""


class AmountWithBreakdownDict(TypedDict):
    currency_code: str
    value: str
    breakdown: NotRequired[AmountBreakdown | AmountBreakdownDict]
