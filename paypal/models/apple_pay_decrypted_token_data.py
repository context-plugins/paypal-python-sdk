from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .apple_pay_payment_data import ApplePayPaymentData, ApplePayPaymentDataDict
from .apple_pay_tokenized_card import ApplePayTokenizedCard, ApplePayTokenizedCardDict
from .enums.apple_pay_payment_data_type import ApplePayPaymentDataTypeOrStr
from .money import Money, MoneyDict


class ApplePayDecryptedTokenData(SdkBaseModel):
    """Information about the Payment data obtained by decrypting Apple Pay token."""

    transaction_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    tokenized_card: ApplePayTokenizedCard
    """The payment card to use to fund a payment. Can be a credit or debit card."""

    device_manufacturer_id: Optional[str] = UNSET
    """Apple Pay Hex-encoded device manufacturer identifier. The pattern is defined by an external party and supports
    Unicode."""

    payment_data_type: Optional[ApplePayPaymentDataTypeOrStr] = UNSET
    """Indicates the type of payment data passed, in case of Non China the payment data is 3DSECURE and for China it is
    EMV."""

    payment_data: Optional[ApplePayPaymentData] = UNSET
    """Information about the decrypted apple pay payment data for the token like cryptogram, eci indicator."""


class ApplePayDecryptedTokenDataDict(TypedDict):
    transaction_amount: NotRequired[Money | MoneyDict]
    tokenized_card: ApplePayTokenizedCard | ApplePayTokenizedCardDict
    device_manufacturer_id: NotRequired[str]
    payment_data_type: NotRequired[ApplePayPaymentDataTypeOrStr]
    payment_data: NotRequired[ApplePayPaymentData | ApplePayPaymentDataDict]
