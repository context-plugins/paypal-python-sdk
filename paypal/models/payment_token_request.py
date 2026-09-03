from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer import Customer, CustomerDict
from .payment_token_request_payment_source import PaymentTokenRequestPaymentSource, PaymentTokenRequestPaymentSourceDict


class PaymentTokenRequest(SdkBaseModel):
    """Payment Token Request where the ``source`` defines the type of instrument to be stored."""

    customer: Optional[Customer] = UNSET
    """This object defines a customer in your system. Use it to manage customer profiles, save payment methods and
    contact details."""

    payment_source: PaymentTokenRequestPaymentSource
    """The payment method to vault with the instrument details."""


class PaymentTokenRequestDict(TypedDict):
    customer: NotRequired[Customer | CustomerDict]
    payment_source: PaymentTokenRequestPaymentSource | PaymentTokenRequestPaymentSourceDict
