from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CheckoutOption(SdkBaseModel):
    """A checkout option as a name-and-value pair."""

    checkout_option_name: Optional[str] = UNSET
    """The checkout option name, such as ``color`` or ``texture``."""

    checkout_option_value: Optional[str] = UNSET
    """The checkout option value. For example, the checkout option ``color`` might be ``blue`` or ``red`` while the
    checkout option ``texture`` might be ``smooth`` or ``rippled``."""


class CheckoutOptionDict(TypedDict):
    checkout_option_name: NotRequired[str]
    checkout_option_value: NotRequired[str]
