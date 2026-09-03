from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .capture_status_details import CaptureStatusDetails, CaptureStatusDetailsDict
from .enums.capture_status import CaptureStatusOrStr
from .enums.disbursement_mode import DisbursementModeOrStr
from .link_description import LinkDescription, LinkDescriptionDict
from .money import Money, MoneyDict
from .network_transaction import NetworkTransaction, NetworkTransactionDict
from .payee_base import PayeeBase, PayeeBaseDict
from .payment_supplementary_data import PaymentSupplementaryData, PaymentSupplementaryDataDict
from .processor_response import ProcessorResponse, ProcessorResponseDict
from .seller_protection import SellerProtection, SellerProtectionDict
from .seller_receivable_breakdown import SellerReceivableBreakdown, SellerReceivableBreakdownDict


class CapturedPayment(SdkBaseModel):
    """A captured payment."""

    status: Optional[CaptureStatusOrStr] = UNSET
    """The status of the captured payment."""

    status_details: Optional[CaptureStatusDetails] = UNSET
    """The details of the captured payment status."""

    id: Optional[str] = UNSET
    """The PayPal-generated ID for the captured payment."""

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

    final_capture: Optional[bool] = UNSET
    """Indicates whether you can make additional captures against the authorized payment. Set to ``true`` if you do not
    intend to capture additional payments against the authorization. Set to ``false`` if you intend to capture
    additional payments against the authorization."""

    seller_receivable_breakdown: Optional[SellerReceivableBreakdown] = UNSET
    """The detailed breakdown of the capture activity. This is not available for transactions that are in pending
    state."""

    disbursement_mode: Optional[DisbursementModeOrStr] = UNSET
    """The funds that are held on behalf of the merchant."""

    links: Optional[list[LinkDescription]] = UNSET
    """An array of related `HATEOAS links </docs/api/reference/api-responses/#hateoas-links>`__."""

    processor_response: Optional[ProcessorResponse] = UNSET
    """The processor response information for payment requests, such as direct credit card transactions."""

    create_time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    update_time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    supplementary_data: Optional[PaymentSupplementaryData] = UNSET
    """The supplementary data."""

    payee: Optional[PayeeBase] = UNSET
    """The details for the merchant who receives the funds and fulfills the order. The merchant is also known as the
    payee."""


class CapturedPaymentDict(TypedDict):
    status: NotRequired[CaptureStatusOrStr]
    status_details: NotRequired[CaptureStatusDetails | CaptureStatusDetailsDict]
    id: NotRequired[str]
    amount: NotRequired[Money | MoneyDict]
    invoice_id: NotRequired[str]
    custom_id: NotRequired[str]
    network_transaction_reference: NotRequired[NetworkTransaction | NetworkTransactionDict]
    seller_protection: NotRequired[SellerProtection | SellerProtectionDict]
    final_capture: NotRequired[bool]
    seller_receivable_breakdown: NotRequired[SellerReceivableBreakdown | SellerReceivableBreakdownDict]
    disbursement_mode: NotRequired[DisbursementModeOrStr]
    links: NotRequired[list[LinkDescription | LinkDescriptionDict]]
    processor_response: NotRequired[ProcessorResponse | ProcessorResponseDict]
    create_time: NotRequired[str]
    update_time: NotRequired[str]
    supplementary_data: NotRequired[PaymentSupplementaryData | PaymentSupplementaryDataDict]
    payee: NotRequired[PayeeBase | PayeeBaseDict]
