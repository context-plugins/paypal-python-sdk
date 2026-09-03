from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.google_pay_authentication_method import GooglePayAuthenticationMethodOrStr
from .enums.google_pay_payment_method import GooglePayPaymentMethodOrStr
from .google_pay_card import GooglePayCard, GooglePayCardDict


class GooglePayDecryptedTokenData(SdkBaseModel):
    """Details shared by Google for the merchant to be shared with PayPal. This is required to process the transaction
    using the Google Pay payment method."""

    message_id: Optional[str] = UNSET
    """A unique ID that identifies the message in case it needs to be revoked or located at a later time."""

    message_expiration: Optional[str] = UNSET
    """Date and time at which the message expires as UTC milliseconds since epoch. Integrators should reject any message
    that's expired."""

    payment_method: GooglePayPaymentMethodOrStr
    """The type of the payment credential. Currently, only CARD is supported."""

    card: GooglePayCard
    """The payment card used to fund a Google Pay payment. Can be a credit or debit card."""

    authentication_method: GooglePayAuthenticationMethodOrStr
    """Authentication Method which is used for the card transaction."""

    cryptogram: Optional[str] = UNSET
    """Base-64 cryptographic identifier used by card schemes to validate the token verification result. This is a
    conditionally required field if authentication_method is CRYPTOGRAM_3DS."""

    eci_indicator: Optional[str] = UNSET
    """Electronic Commerce Indicator may not always be present. It is only returned for tokens on the Visa card network.
    This value is passed through in the payment authorization request."""


class GooglePayDecryptedTokenDataDict(TypedDict):
    message_id: NotRequired[str]
    message_expiration: NotRequired[str]
    payment_method: GooglePayPaymentMethodOrStr
    card: GooglePayCard | GooglePayCardDict
    authentication_method: GooglePayAuthenticationMethodOrStr
    cryptogram: NotRequired[str]
    eci_indicator: NotRequired[str]
