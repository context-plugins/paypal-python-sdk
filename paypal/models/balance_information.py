from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict


class BalanceInformation(SdkBaseModel):
    """The Balance information."""

    currency: str
    """The `three-character ISO-4217 currency code </docs/integration/direct/rest/currency-codes/>`__ that identifies
    the currency."""

    primary: Optional[bool] = UNSET
    """Optional field representing if the currency is primary currency or not."""

    total_balance: Money
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    available_balance: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    withheld_balance: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""


class BalanceInformationDict(TypedDict):
    currency: str
    primary: NotRequired[bool]
    total_balance: Money | MoneyDict
    available_balance: NotRequired[Money | MoneyDict]
    withheld_balance: NotRequired[Money | MoneyDict]
