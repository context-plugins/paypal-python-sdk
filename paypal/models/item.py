from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.item_category import ItemCategoryOrStr
from .money import Money, MoneyDict
from .order_billing_plan import OrderBillingPlan, OrderBillingPlanDict
from .universal_product_code import UniversalProductCode, UniversalProductCodeDict


class Item(SdkBaseModel):
    """The details for the items to be purchased."""

    name: str
    """The item name or title."""

    unit_amount: Money
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    tax: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    quantity: str
    """The item quantity. Must be a whole number."""

    description: Optional[str] = UNSET
    """The detailed item description."""

    sku: Optional[str] = UNSET
    """The stock keeping unit (SKU) for the item."""

    url: Optional[str] = UNSET
    """The URL to the item being purchased. Visible to buyer and used in buyer experiences."""

    category: Optional[ItemCategoryOrStr] = UNSET
    """The item category type."""

    image_url: Optional[str] = UNSET
    """The URL of the item's image. File type and size restrictions apply. An image that violates these restrictions
    will not be honored."""

    upc: Optional[UniversalProductCode] = UNSET
    """The Universal Product Code of the item."""

    billing_plan: Optional[OrderBillingPlan] = UNSET
    """Metadata for merchant-managed recurring billing plans. Valid only during the saved payment method token or
    billing agreement creation."""


class ItemDict(TypedDict):
    name: str
    unit_amount: Money | MoneyDict
    tax: NotRequired[Money | MoneyDict]
    quantity: str
    description: NotRequired[str]
    sku: NotRequired[str]
    url: NotRequired[str]
    category: NotRequired[ItemCategoryOrStr]
    image_url: NotRequired[str]
    upc: NotRequired[UniversalProductCode | UniversalProductCodeDict]
    billing_plan: NotRequired[OrderBillingPlan | OrderBillingPlanDict]
