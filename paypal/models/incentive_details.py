from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict


class IncentiveDetails(SdkBaseModel):
    """The incentive details."""

    incentive_type: Optional[str] = UNSET
    """The type of incentive, such as a special offer or coupon."""

    incentive_code: Optional[str] = UNSET
    """The code that identifies an incentive, such as a coupon."""

    incentive_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    incentive_program_code: Optional[str] = UNSET
    """The incentive program code that identifies a merchant loyalty or incentive program."""


class IncentiveDetailsDict(TypedDict):
    incentive_type: NotRequired[str]
    incentive_code: NotRequired[str]
    incentive_amount: NotRequired[Money | MoneyDict]
    incentive_program_code: NotRequired[str]
