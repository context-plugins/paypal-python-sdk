from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .authorization_status_details import AuthorizationStatusDetails, AuthorizationStatusDetailsDict
from .enums.authorization_status import AuthorizationStatusOrStr
from .link_description import LinkDescription, LinkDescriptionDict
from .money import Money, MoneyDict
from .network_transaction import NetworkTransaction, NetworkTransactionDict
from .processor_response import ProcessorResponse, ProcessorResponseDict
from .seller_protection import SellerProtection, SellerProtectionDict


class AuthorizationWithAdditionalData(SdkBaseModel):
    """The authorization with additional payment details, such as risk assessment and processor response. These details
    are populated only for certain payment methods."""

    status: Optional[AuthorizationStatusOrStr] = UNSET
    """The status for the authorized payment."""

    status_details: Optional[AuthorizationStatusDetails] = UNSET
    """The details of the authorized payment status."""

    id: Optional[str] = UNSET
    """The PayPal-generated ID for the authorized payment."""

    amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    invoice_id: Optional[str] = UNSET
    """The API caller-provided external invoice number for this order. Appears in both the payer's transaction history
    and the emails that the payer receives."""

    custom_id: Optional[str] = UNSET
    """The API caller-provided external ID. Used to reconcile API caller-initiated transactions with PayPal
    transactions. Appears in transaction and settlement reports."""

    network_transaction_reference: Optional[NetworkTransaction] = UNSET
    """Reference values used by the card network to identify a transaction."""

    seller_protection: Optional[SellerProtection] = UNSET
    """The level of protection offered as defined by `PayPal Seller Protection for Merchants
    <https://www.paypal.com/us/webapps/mpp/security/seller-protection>`__."""

    expiration_time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    links: Optional[list[LinkDescription]] = UNSET
    """An array of related `HATEOAS links </docs/api/reference/api-responses/#hateoas-links>`__."""

    create_time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    update_time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    processor_response: Optional[ProcessorResponse] = UNSET
    """The processor response information for payment requests, such as direct credit card transactions."""


class AuthorizationWithAdditionalDataDict(TypedDict):
    status: NotRequired[AuthorizationStatusOrStr]
    status_details: NotRequired[AuthorizationStatusDetails | AuthorizationStatusDetailsDict]
    id: NotRequired[str]
    amount: NotRequired[Money | MoneyDict]
    invoice_id: NotRequired[str]
    custom_id: NotRequired[str]
    network_transaction_reference: NotRequired[NetworkTransaction | NetworkTransactionDict]
    seller_protection: NotRequired[SellerProtection | SellerProtectionDict]
    expiration_time: NotRequired[str]
    links: NotRequired[list[LinkDescription | LinkDescriptionDict]]
    create_time: NotRequired[str]
    update_time: NotRequired[str]
    processor_response: NotRequired[ProcessorResponse | ProcessorResponseDict]
