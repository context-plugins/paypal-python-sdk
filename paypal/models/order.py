from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.checkout_payment_intent import CheckoutPaymentIntentOrStr
from .enums.order_status import OrderStatusOrStr
from .enums.processing_instruction import ProcessingInstructionOrStr
from .link_description import LinkDescription, LinkDescriptionDict
from .payer import Payer, PayerDict
from .payment_source_response import PaymentSourceResponse, PaymentSourceResponseDict
from .purchase_unit import PurchaseUnit, PurchaseUnitDict


class Order(SdkBaseModel):
    """The order details."""

    create_time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    update_time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    id: Optional[str] = UNSET
    """The ID of the order."""

    payment_source: Optional[PaymentSourceResponse] = UNSET
    """The payment source used to fund the payment."""

    intent: Optional[CheckoutPaymentIntentOrStr] = UNSET
    """The intent to either capture payment immediately or authorize a payment for an order after order creation."""

    processing_instruction: Optional[ProcessingInstructionOrStr] = UNSET
    """The instruction to process an order."""

    payer: Optional[Payer] = UNSET
    """DEPRECATED. The customer is also known as the payer. The Payer object was intended to only be used with the
    ``payment_source.paypal`` object. In order to make this design more clear, the details in the ``payer`` object are
    now available under ``payment_source.paypal``. Please use ``payment_source.paypal``."""

    purchase_units: Optional[list[PurchaseUnit]] = UNSET
    """An array of purchase units. Each purchase unit establishes a contract between a customer and merchant. Each
    purchase unit represents either a full or partial order that the customer intends to purchase from the merchant."""

    status: Optional[OrderStatusOrStr] = UNSET
    """The order status."""

    links: Optional[list[LinkDescription]] = UNSET
    """An array of request-related HATEOAS links. To complete payer approval, use the ``approve`` link to redirect the
    payer. The API caller has 6 hours (default setting, this which can be changed by your account manager to 24/48/72
    hours to accommodate your use case) from the time the order is created, to redirect your payer. Once redirected, the
    API caller has 6 hours for the payer to approve the order and either authorize or capture the order. If you are not
    using the PayPal JavaScript SDK to initiate PayPal Checkout (in context) ensure that you include
    ``application_context.return_url`` is specified or you will get "We're sorry, Things don't appear to be working at
    the moment" after the payer approves the payment."""


class OrderDict(TypedDict):
    create_time: NotRequired[str]
    update_time: NotRequired[str]
    id: NotRequired[str]
    payment_source: NotRequired[PaymentSourceResponse | PaymentSourceResponseDict]
    intent: NotRequired[CheckoutPaymentIntentOrStr]
    processing_instruction: NotRequired[ProcessingInstructionOrStr]
    payer: NotRequired[Payer | PayerDict]
    purchase_units: NotRequired[list[PurchaseUnit | PurchaseUnitDict]]
    status: NotRequired[OrderStatusOrStr]
    links: NotRequired[list[LinkDescription | LinkDescriptionDict]]
