from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .universal_product_code import UniversalProductCode, UniversalProductCodeDict


class OrderTrackerItem(SdkBaseModel):
    """The details of the items in the shipment."""

    name: Optional[str] = UNSET
    """The item name or title."""

    quantity: Optional[str] = UNSET
    """The item quantity. Must be a whole number."""

    sku: Optional[str] = UNSET
    """The stock keeping unit (SKU) for the item. This can contain unicode characters."""

    url: Optional[str] = UNSET
    """The URL to the item being purchased. Visible to buyer and used in buyer experiences."""

    image_url: Optional[str] = UNSET
    """The URL of the item's image. File type and size restrictions apply. An image that violates these restrictions
    will not be honored."""

    upc: Optional[UniversalProductCode] = UNSET
    """The Universal Product Code of the item."""


class OrderTrackerItemDict(TypedDict):
    name: NotRequired[str]
    quantity: NotRequired[str]
    sku: NotRequired[str]
    url: NotRequired[str]
    image_url: NotRequired[str]
    upc: NotRequired[UniversalProductCode | UniversalProductCodeDict]
