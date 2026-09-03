from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .update_pricing_scheme import UpdatePricingScheme, UpdatePricingSchemeDict


class UpdatePricingSchemesRequest(SdkBaseModel):
    """The update pricing scheme request details."""

    pricing_schemes: list[UpdatePricingScheme]
    """An array of pricing schemes."""


class UpdatePricingSchemesRequestDict(TypedDict):
    pricing_schemes: list[UpdatePricingScheme | UpdatePricingSchemeDict]
