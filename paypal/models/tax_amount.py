from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict


class TaxAmount(SdkBaseModel):
    """The tax levied by a government on the purchase of goods or services."""

    tax_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""


class TaxAmountDict(TypedDict):
    tax_amount: NotRequired[Money | MoneyDict]
