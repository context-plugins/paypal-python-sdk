from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Taxes(SdkBaseModel):
    """The tax details."""

    percentage: str
    """The percentage, as a fixed-point, signed decimal number. For example, define a 19.99% interest rate as
    ``19.99``."""

    inclusive: Optional[bool] = UNSET
    """Indicates whether the tax was already included in the billing amount."""


class TaxesDict(TypedDict):
    percentage: str
    inclusive: NotRequired[bool]
