from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .authentication_response import AuthenticationResponse, AuthenticationResponseDict
from .bin_details import BinDetails, BinDetailsDict
from .card_attributes_response import CardAttributesResponse, CardAttributesResponseDict
from .card_from_request import CardFromRequest, CardFromRequestDict
from .card_stored_credential import CardStoredCredential, CardStoredCredentialDict
from .enums.card_brand import CardBrandOrStr
from .enums.card_type import CardTypeOrStr


class CardResponse(SdkBaseModel):
    """The payment card to use to fund a payment. Card can be a credit or debit card."""

    name: Optional[str] = UNSET
    """The card holder's name as it appears on the card."""

    last_digits: Optional[str] = UNSET
    """The last digits of the payment card."""

    brand: Optional[CardBrandOrStr] = UNSET
    """The card network or brand. Applies to credit, debit, gift, and payment cards."""

    available_networks: Optional[list[CardBrandOrStr]] = UNSET
    """Array of brands or networks associated with the card."""

    type_: Optional[CardTypeOrStr] = Field(default=UNSET, alias="type")
    """Type of card. i.e Credit, Debit and so on."""

    authentication_result: Optional[AuthenticationResponse] = UNSET
    """Results of Authentication such as 3D Secure."""

    attributes: Optional[CardAttributesResponse] = UNSET
    """Additional attributes associated with the use of this card."""

    from_request: Optional[CardFromRequest] = UNSET
    """Representation of card details as received in the request."""

    expiry: Optional[str] = UNSET
    """The year and month, in ISO-8601 ``YYYY-MM`` date format. See `Internet date and time format
    <https://tools.ietf.org/html/rfc3339#section-5.6>`__."""

    bin_details: Optional[BinDetails] = UNSET
    """Bank Identification Number (BIN) details used to fund a payment."""

    stored_credential: Optional[CardStoredCredential] = UNSET
    """Provides additional details to process a payment using a ``card`` that has been stored or is intended to be
    stored (also referred to as stored_credential or card-on-file). Parameter compatibility: ``payment_type=ONE_TIME``
    is compatible only with ``payment_initiator=CUSTOMER``. ``usage=FIRST`` is compatible only with
    ``payment_initiator=CUSTOMER``. ``previous_transaction_reference`` or ``previous_network_transaction_reference`` is
    compatible only with ``payment_initiator=MERCHANT``. Only one of the parameters - ``previous_transaction_reference``
    and ``previous_network_transaction_reference`` - can be present in the request."""


class CardResponseDict(TypedDict):
    name: NotRequired[str]
    last_digits: NotRequired[str]
    brand: NotRequired[CardBrandOrStr]
    available_networks: NotRequired[list[CardBrandOrStr]]
    type_: NotRequired[CardTypeOrStr]
    authentication_result: NotRequired[AuthenticationResponse | AuthenticationResponseDict]
    attributes: NotRequired[CardAttributesResponse | CardAttributesResponseDict]
    from_request: NotRequired[CardFromRequest | CardFromRequestDict]
    expiry: NotRequired[str]
    bin_details: NotRequired[BinDetails | BinDetailsDict]
    stored_credential: NotRequired[CardStoredCredential | CardStoredCredentialDict]
