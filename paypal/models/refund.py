from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.refund_status import RefundStatusOrStr
from .link_description import LinkDescription, LinkDescriptionDict
from .money import Money, MoneyDict
from .payee_base import PayeeBase, PayeeBaseDict
from .refund_status_details import RefundStatusDetails, RefundStatusDetailsDict
from .seller_payable_breakdown import SellerPayableBreakdown, SellerPayableBreakdownDict


class Refund(SdkBaseModel):
    """The refund information."""

    status: Optional[RefundStatusOrStr] = UNSET
    """The status of the refund."""

    status_details: Optional[RefundStatusDetails] = UNSET
    """The details of the refund status."""

    id: Optional[str] = UNSET
    """The PayPal-generated ID for the refund."""

    amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    invoice_id: Optional[str] = UNSET
    """The API caller-provided external invoice number for this order. Appears in both the payer's transaction history
    and the emails that the payer receives."""

    custom_id: Optional[str] = UNSET
    """The API caller-provided external ID. Used to reconcile API caller-initiated transactions with PayPal
    transactions. Appears in transaction and settlement reports."""

    acquirer_reference_number: Optional[str] = UNSET
    """Reference ID issued for the card transaction. This ID can be used to track the transaction across processors,
    card brands and issuing banks."""

    note_to_payer: Optional[str] = UNSET
    """The reason for the refund. Appears in both the payer's transaction history and the emails that the payer
    receives."""

    seller_payable_breakdown: Optional[SellerPayableBreakdown] = UNSET
    """The breakdown of the refund."""

    payer: Optional[PayeeBase] = UNSET
    """The details for the merchant who receives the funds and fulfills the order. The merchant is also known as the
    payee."""

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


class RefundDict(TypedDict):
    status: NotRequired[RefundStatusOrStr]
    status_details: NotRequired[RefundStatusDetails | RefundStatusDetailsDict]
    id: NotRequired[str]
    amount: NotRequired[Money | MoneyDict]
    invoice_id: NotRequired[str]
    custom_id: NotRequired[str]
    acquirer_reference_number: NotRequired[str]
    note_to_payer: NotRequired[str]
    seller_payable_breakdown: NotRequired[SellerPayableBreakdown | SellerPayableBreakdownDict]
    payer: NotRequired[PayeeBase | PayeeBaseDict]
    links: NotRequired[list[LinkDescription | LinkDescriptionDict]]
    create_time: NotRequired[str]
    update_time: NotRequired[str]
