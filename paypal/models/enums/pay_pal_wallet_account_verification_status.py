from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PayPalWalletAccountVerificationStatus(str, Enum):
    """The account status indicates whether the buyer has verified the financial details associated with their PayPal
    account."""

    VERIFIED = "VERIFIED"
    """The buyer has completed the verification of the financial details associated with this PayPal account. For
    example: confirming their bank account."""

    UNVERIFIED = "UNVERIFIED"
    """The buyer has not completed the verification of the financial details associated with this PayPal account. For
    example: confirming their bank account."""

    __str__ = str.__str__


PayPalWalletAccountVerificationStatusOrStr: TypeAlias = Annotated[
    PayPalWalletAccountVerificationStatus | str, open_enum_validator(PayPalWalletAccountVerificationStatus)
]
