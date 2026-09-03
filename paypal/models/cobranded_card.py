from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict
from .payee_base import PayeeBase, PayeeBaseDict


class CobrandedCard(SdkBaseModel):
    """Details about the merchant cobranded card used for order purchase."""

    labels: Optional[list[str]] = UNSET
    """Array of labels for the cobranded card."""

    payee: Optional[PayeeBase] = UNSET
    """The details for the merchant who receives the funds and fulfills the order. The merchant is also known as the
    payee."""

    amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""


class CobrandedCardDict(TypedDict):
    labels: NotRequired[list[str]]
    payee: NotRequired[PayeeBase | PayeeBaseDict]
    amount: NotRequired[Money | MoneyDict]
