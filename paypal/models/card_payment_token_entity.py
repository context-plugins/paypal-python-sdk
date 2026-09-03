from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bin_details import BinDetails, BinDetailsDict
from .card_authentication_response import CardAuthenticationResponse, CardAuthenticationResponseDict
from .card_response_address import CardResponseAddress, CardResponseAddressDict
from .card_verification_details import CardVerificationDetails, CardVerificationDetailsDict
from .enums.card_brand import CardBrandOrStr
from .enums.card_type import CardTypeOrStr
from .enums.card_verification_status import CardVerificationStatusOrStr
from .network_transaction_reference_entity import (
    NetworkTransactionReferenceEntity,
    NetworkTransactionReferenceEntityDict,
)


class CardPaymentTokenEntity(SdkBaseModel):
    """Full representation of a Card Payment Token."""

    name: Optional[str] = UNSET
    """The card holder's name as it appears on the card."""

    last_digits: Optional[str] = UNSET
    """The last digits of the payment card."""

    brand: Optional[CardBrandOrStr] = UNSET
    """The card network or brand. Applies to credit, debit, gift, and payment cards."""

    expiry: Optional[str] = UNSET
    """The year and month, in ISO-8601 ``YYYY-MM`` date format. See `Internet date and time format
    <https://tools.ietf.org/html/rfc3339#section-5.6>`__."""

    billing_address: Optional[CardResponseAddress] = UNSET
    """Address request details."""

    verification_status: Optional[CardVerificationStatusOrStr] = UNSET
    """Verification status of Card."""

    verification: Optional[CardVerificationDetails] = UNSET
    """Card Verification details including the authorization details and 3D SECURE details."""

    network_transaction_reference: Optional[NetworkTransactionReferenceEntity] = UNSET
    """Previous network transaction reference including id in response."""

    authentication_result: Optional[CardAuthenticationResponse] = UNSET
    """Results of Authentication such as 3D Secure."""

    bin_details: Optional[BinDetails] = UNSET
    """Bank Identification Number (BIN) details used to fund a payment."""

    type_: Optional[CardTypeOrStr] = Field(default=UNSET, alias="type")
    """Type of card. i.e Credit, Debit and so on."""


class CardPaymentTokenEntityDict(TypedDict):
    name: NotRequired[str]
    last_digits: NotRequired[str]
    brand: NotRequired[CardBrandOrStr]
    expiry: NotRequired[str]
    billing_address: NotRequired[CardResponseAddress | CardResponseAddressDict]
    verification_status: NotRequired[CardVerificationStatusOrStr]
    verification: NotRequired[CardVerificationDetails | CardVerificationDetailsDict]
    network_transaction_reference: NotRequired[
        NetworkTransactionReferenceEntity | NetworkTransactionReferenceEntityDict
    ]
    authentication_result: NotRequired[CardAuthenticationResponse | CardAuthenticationResponseDict]
    bin_details: NotRequired[BinDetails | BinDetailsDict]
    type_: NotRequired[CardTypeOrStr]
