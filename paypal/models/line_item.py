from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict
from .order_billing_plan import OrderBillingPlan, OrderBillingPlanDict
from .universal_product_code import UniversalProductCode, UniversalProductCodeDict


class LineItem(SdkBaseModel):
    """The line items for this purchase. If your merchant account has been configured for Level 3 processing this field
    will be passed to the processor on your behalf."""

    name: str
    """The item name or title."""

    quantity: str
    """The item quantity. Must be a whole number."""

    description: Optional[str] = UNSET
    """The detailed item description."""

    sku: Optional[str] = UNSET
    """The stock keeping unit (SKU) for the item."""

    url: Optional[str] = UNSET
    """The URL to the item being purchased. Visible to buyer and used in buyer experiences."""

    image_url: Optional[str] = UNSET
    """The URL of the item's image. File type and size restrictions apply. An image that violates these restrictions
    will not be honored."""

    upc: Optional[UniversalProductCode] = UNSET
    """The Universal Product Code of the item."""

    billing_plan: Optional[OrderBillingPlan] = UNSET
    """Metadata for merchant-managed recurring billing plans. Valid only during the saved payment method token or
    billing agreement creation."""

    unit_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    tax: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    commodity_code: Optional[str] = UNSET
    """Code used to classify items purchased and track the total amount spent across various categories of products and
    services. Different corporate purchasing organizations may use different standards, but the United Nations Standard
    Products and Services Code (UNSPSC) is frequently used."""

    discount_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    total_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    unit_of_measure: Optional[str] = UNSET
    """Unit of measure is a standard used to express the magnitude of a quantity in international trade. Most commonly
    used (but not limited to) examples are: Acre (ACR), Ampere (AMP), Centigram (CGM), Centimetre (CMT), Cubic inch
    (INQ), Cubic metre (MTQ), Fluid ounce (OZA), Foot (FOT), Hour (HUR), Item (ITM), Kilogram (KGM), Kilometre (KMT),
    Kilowatt (KWT), Liquid gallon (GLL), Liter (LTR), Pounds (LBS), Square foot (FTK)."""


class LineItemDict(TypedDict):
    name: str
    quantity: str
    description: NotRequired[str]
    sku: NotRequired[str]
    url: NotRequired[str]
    image_url: NotRequired[str]
    upc: NotRequired[UniversalProductCode | UniversalProductCodeDict]
    billing_plan: NotRequired[OrderBillingPlan | OrderBillingPlanDict]
    unit_amount: NotRequired[Money | MoneyDict]
    tax: NotRequired[Money | MoneyDict]
    commodity_code: NotRequired[str]
    discount_amount: NotRequired[Money | MoneyDict]
    total_amount: NotRequired[Money | MoneyDict]
    unit_of_measure: NotRequired[str]
