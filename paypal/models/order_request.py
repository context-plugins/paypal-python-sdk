from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.checkout_payment_intent import CheckoutPaymentIntentOrStr
from .enums.processing_instruction import ProcessingInstructionOrStr
from .order_application_context import OrderApplicationContext, OrderApplicationContextDict
from .payer import Payer, PayerDict
from .payment_source import PaymentSource, PaymentSourceDict
from .purchase_unit_request import PurchaseUnitRequest, PurchaseUnitRequestDict


class OrderRequest(SdkBaseModel):
    """The order request details."""

    intent: CheckoutPaymentIntentOrStr
    """The intent to either capture payment immediately or authorize a payment for an order after order creation."""

    processing_instruction: Optional[ProcessingInstructionOrStr] = UNSET
    """The instruction to process an order."""

    payer: Optional[Payer] = UNSET
    """DEPRECATED. The customer is also known as the payer. The Payer object was intended to only be used with the
    ``payment_source.paypal`` object. In order to make this design more clear, the details in the ``payer`` object are
    now available under ``payment_source.paypal``. Please use ``payment_source.paypal``."""

    purchase_units: list[PurchaseUnitRequest]
    """An array of purchase units. Each purchase unit establishes a contract between a payer and the payee. Each
    purchase unit represents either a full or partial order that the payer intends to purchase from the payee."""

    payment_source: Optional[PaymentSource] = UNSET
    """The payment source definition."""

    application_context: Optional[OrderApplicationContext] = UNSET
    """Customizes the payer experience during the approval process for the payment with PayPal. Note: Partners and
    Marketplaces might configure brand_name and shipping_preference during partner account setup, which overrides the
    request values."""


class OrderRequestDict(TypedDict):
    intent: CheckoutPaymentIntentOrStr
    processing_instruction: NotRequired[ProcessingInstructionOrStr]
    payer: NotRequired[Payer | PayerDict]
    purchase_units: list[PurchaseUnitRequest | PurchaseUnitRequestDict]
    payment_source: NotRequired[PaymentSource | PaymentSourceDict]
    application_context: NotRequired[OrderApplicationContext | OrderApplicationContextDict]
