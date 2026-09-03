from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pay_pal_payment_token import PayPalPaymentToken, PayPalPaymentTokenDict
from .setup_token_response_card import SetupTokenResponseCard, SetupTokenResponseCardDict
from .venmo_payment_token import VenmoPaymentToken, VenmoPaymentTokenDict


class SetupTokenResponsePaymentSource(SdkBaseModel):
    """The setup payment method details."""

    card: Optional[SetupTokenResponseCard] = UNSET
    paypal: Optional[PayPalPaymentToken] = UNSET
    """Full representation of a PayPal Payment Token."""

    venmo: Optional[VenmoPaymentToken] = UNSET
    """Full representation of a Venmo Payment Token."""


class SetupTokenResponsePaymentSourceDict(TypedDict):
    card: NotRequired[SetupTokenResponseCard | SetupTokenResponseCardDict]
    paypal: NotRequired[PayPalPaymentToken | PayPalPaymentTokenDict]
    venmo: NotRequired[VenmoPaymentToken | VenmoPaymentTokenDict]
