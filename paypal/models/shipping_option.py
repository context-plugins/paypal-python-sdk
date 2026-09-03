from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.shipping_type import ShippingTypeOrStr
from .money import Money, MoneyDict


class ShippingOption(SdkBaseModel):
    """The options that the payee or merchant offers to the payer to ship or pick up their items."""

    id: str
    """A unique ID that identifies a payer-selected shipping option."""

    label: str
    """A description that the payer sees, which helps them choose an appropriate shipping option. For example, ``Free
    Shipping``, ``USPS Priority Shipping``, ``Expédition prioritaire USPS``, or ``USPS yōuxiān fā huò``. Localize this
    description to the payer's locale."""

    type_: Optional[ShippingTypeOrStr] = Field(default=UNSET, alias="type")
    """A classification for the method of purchase fulfillment."""

    amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    selected: bool
    """If the API request sets ``selected = true``, it represents the shipping option that the payee or merchant expects
    to be pre-selected for the payer when they first view the ``shipping.options`` in the PayPal Checkout experience. As
    part of the response if a ``shipping.option`` contains ``selected=true``, it represents the shipping option that the
    payer selected during the course of checkout with PayPal. Only one ``shipping.option`` can be set to
    ``selected=true``."""


class ShippingOptionDict(TypedDict):
    id: str
    label: str
    type_: NotRequired[ShippingTypeOrStr]
    amount: NotRequired[Money | MoneyDict]
    selected: bool
