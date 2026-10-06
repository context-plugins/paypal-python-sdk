from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .order_confirm_application_context import OrderConfirmApplicationContext, OrderConfirmApplicationContextDict
from .payment_source import PaymentSource, PaymentSourceDict


class ConfirmOrderRequest(SdkBaseModel):
    """Payer confirms the intent to pay for the Order using the provided payment source."""

    payment_source: PaymentSource
    """The payment source definition."""

    application_context: Optional[OrderConfirmApplicationContext] = UNSET
    """Customizes the payer confirmation experience."""


class ConfirmOrderRequestDict(TypedDict):
    payment_source: PaymentSourceDict
    application_context: NotRequired[OrderConfirmApplicationContextDict]
