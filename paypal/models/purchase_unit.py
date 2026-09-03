from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount_with_breakdown import AmountWithBreakdown, AmountWithBreakdownDict
from .item import Item, ItemDict
from .payee_base import PayeeBase, PayeeBaseDict
from .payment_collection import PaymentCollection, PaymentCollectionDict
from .payment_instruction import PaymentInstruction, PaymentInstructionDict
from .shipping_with_tracking_details import ShippingWithTrackingDetails, ShippingWithTrackingDetailsDict
from .supplementary_data import SupplementaryData, SupplementaryDataDict


class PurchaseUnit(SdkBaseModel):
    """The purchase unit details. Used to capture required information for the payment contract."""

    reference_id: Optional[str] = UNSET
    """The API caller-provided external ID for the purchase unit. Required for multiple purchase units when you must
    update the order through ``PATCH``. If you omit this value and the order contains only one purchase unit, PayPal
    sets this value to ``default``. Note: If there are multiple purchase units, reference_id is required for each
    purchase unit."""

    amount: Optional[AmountWithBreakdown] = UNSET
    """The total order amount with an optional breakdown that provides details, such as the total item amount, total tax
    amount, shipping, handling, insurance, and discounts, if any. If you specify ``amount.breakdown``, the amount equals
    ``item_total`` plus ``tax_total`` plus ``shipping`` plus ``handling`` plus ``insurance`` minus ``shipping_discount``
    minus discount. The amount must be a positive number. For listed of supported currencies and decimal precision, see
    the PayPal REST APIs Currency Codes."""

    payee: Optional[PayeeBase] = UNSET
    """The merchant who receives the funds and fulfills the order. The merchant is also known as the payee."""

    payment_instruction: Optional[PaymentInstruction] = UNSET
    """Any additional payment instructions to be consider during payment processing. This processing instruction is
    applicable for Capturing an order or Authorizing an Order."""

    description: Optional[str] = UNSET
    """The purchase description."""

    custom_id: Optional[str] = UNSET
    """The API caller-provided external ID. Used to reconcile API caller-initiated transactions with PayPal
    transactions. Appears in transaction and settlement reports."""

    invoice_id: Optional[str] = UNSET
    """The API caller-provided external invoice ID for this order."""

    id: Optional[str] = UNSET
    """The PayPal-generated ID for the purchase unit. This ID appears in both the payer's transaction history and the
    emails that the payer receives. In addition, this ID is available in transaction and settlement reports that
    merchants and API callers can use to reconcile transactions. This ID is only available when an order is saved by
    calling v2/checkout/orders/id/save."""

    soft_descriptor: Optional[str] = UNSET
    """The payment descriptor on account transactions on the customer's credit card statement, that PayPal sends to
    processors. The maximum length of the soft descriptor information that you can pass in the API field is 22
    characters, in the following format:22 - len(PAYPAL * (8)) - len(Descriptor in Payment Receiving Preferences of
    Merchant account + 1)The PAYPAL prefix uses 8 characters. The soft descriptor supports the following ASCII
    characters: Alphanumeric characters Dashes Asterisks Periods (.) Spaces For Wallet payments marketplace
    integrations: The merchant descriptor in the Payment Receiving Preferences must be the marketplace name. You can't
    use the remaining space to show the customer service number. The remaining spaces can be a combination of seller
    name and country. For unbranded payments (Direct Card) marketplace integrations, use a combination of the seller
    name and phone number."""

    items: Optional[list[Item]] = UNSET
    """An array of items that the customer purchases from the merchant."""

    shipping: Optional[ShippingWithTrackingDetails] = UNSET
    """The order shipping details."""

    supplementary_data: Optional[SupplementaryData] = UNSET
    """Supplementary data about a payment. This object passes information that can be used to improve risk assessments
    and processing costs, for example, by providing Level 2 and Level 3 payment data."""

    payments: Optional[PaymentCollection] = UNSET
    """The collection of payments, or transactions, for a purchase unit in an order. For example, authorized payments,
    captured payments, and refunds."""

    most_recent_errors: Optional[list[Any]] = UNSET
    """The error reason code and description that are the reason for the most recent order decline."""


class PurchaseUnitDict(TypedDict):
    reference_id: NotRequired[str]
    amount: NotRequired[AmountWithBreakdown | AmountWithBreakdownDict]
    payee: NotRequired[PayeeBase | PayeeBaseDict]
    payment_instruction: NotRequired[PaymentInstruction | PaymentInstructionDict]
    description: NotRequired[str]
    custom_id: NotRequired[str]
    invoice_id: NotRequired[str]
    id: NotRequired[str]
    soft_descriptor: NotRequired[str]
    items: NotRequired[list[Item | ItemDict]]
    shipping: NotRequired[ShippingWithTrackingDetails | ShippingWithTrackingDetailsDict]
    supplementary_data: NotRequired[SupplementaryData | SupplementaryDataDict]
    payments: NotRequired[PaymentCollection | PaymentCollectionDict]
    most_recent_errors: NotRequired[list[Any]]
