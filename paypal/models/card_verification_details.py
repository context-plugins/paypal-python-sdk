from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .card_verification_processor_response import (
    CardVerificationProcessorResponse,
    CardVerificationProcessorResponseDict,
)
from .enums.card_brand import CardBrandOrStr
from .money import Money, MoneyDict


class CardVerificationDetails(SdkBaseModel):
    """Card Verification details including the authorization details and 3D SECURE details."""

    network_transaction_id: Optional[str] = UNSET
    """DEPRECATED. This field is DEPRECATED. Please find the network transaction id data in the 'id' field under the
    'network_transaction_reference' object instead of the 'verification' object."""

    date: Optional[str] = UNSET
    """DEPRECATED. This field is DEPRECATED. Please find the date data in the 'date' field under the
    'network_transaction_reference' object instead of the 'verification' object."""

    network: Optional[CardBrandOrStr] = UNSET
    """DEPRECATED. This field is DEPRECATED. Please find the network data in the 'network' field under the
    'network_transaction_reference' object instead of the 'verification' object."""

    time: Optional[str] = UNSET
    """DEPRECATED. This field is DEPRECATED. Please find the time data in the 'time' field under the
    'network_transaction_reference' object instead of the 'verification' object."""

    amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    processor_response: Optional[CardVerificationProcessorResponse] = UNSET
    """The processor response information for payment requests, such as direct credit card transactions."""

    three_d_secure: Optional[Any] = UNSET
    """DEPRECATED. This field is DEPRECATED. Please find the 3D secure authentication data in the 'three_d_secure'
    object under the 'authentication_result' object instead of the 'verification' object."""


class CardVerificationDetailsDict(TypedDict):
    network_transaction_id: NotRequired[str]
    date: NotRequired[str]
    network: NotRequired[CardBrandOrStr]
    time: NotRequired[str]
    amount: NotRequired[Money | MoneyDict]
    processor_response: NotRequired[CardVerificationProcessorResponse | CardVerificationProcessorResponseDict]
    three_d_secure: NotRequired[Any]
