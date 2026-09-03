from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .card_response_with_billing_address import CardResponseWithBillingAddress, CardResponseWithBillingAddressDict


class SubscriptionPaymentSourceResponse(SdkBaseModel):
    """The payment source used to fund the payment."""

    card: Optional[CardResponseWithBillingAddress] = UNSET
    """The payment card used to fund the payment. Card can be a credit or debit card."""


class SubscriptionPaymentSourceResponseDict(TypedDict):
    card: NotRequired[CardResponseWithBillingAddress | CardResponseWithBillingAddressDict]
