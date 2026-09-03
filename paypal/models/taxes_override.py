from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TaxesOverride(SdkBaseModel):
    """The tax details."""

    percentage: Optional[str] = UNSET
    """The percentage, as a fixed-point, signed decimal number. For example, define a 19.99% interest rate as
    ``19.99``."""

    inclusive: Optional[bool] = UNSET
    """Indicates whether the tax was already included in the billing amount."""


class TaxesOverrideDict(TypedDict):
    percentage: NotRequired[str]
    inclusive: NotRequired[bool]
