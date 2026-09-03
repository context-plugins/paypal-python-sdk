from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount_with_breakdown import AmountWithBreakdown, AmountWithBreakdownDict
from .item_request import ItemRequest, ItemRequestDict
from .payee_base import PayeeBase, PayeeBaseDict
from .payment_instruction import PaymentInstruction, PaymentInstructionDict
from .shipping_details import ShippingDetails, ShippingDetailsDict
from .supplementary_data import SupplementaryData, SupplementaryDataDict


class PurchaseUnitRequest(SdkBaseModel):
    """The purchase unit request. Includes required information for the payment contract."""

    reference_id: Optional[str] = UNSET
    """The API caller-provided external ID for the purchase unit. Required for multiple purchase units when you must
    update the order through ``PATCH``. If you omit this value and the order contains only one purchase unit, PayPal
    sets this value to ``default``."""

    amount: AmountWithBreakdown
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
    """This field supports up to 3,000 characters, but any content beyond 127 characters (including spaces) will be
    truncated. The 127 character limit is reflected in the response representation of this field. The purchase
    description. The maximum length of the character is dependent on the type of characters used. The character length
    is specified assuming a US ASCII character. Depending on type of character; (e.g. accented character, Japanese
    characters) the number of characters that that can be specified as input might not equal the permissible max
    length."""

    custom_id: Optional[str] = UNSET
    """The API caller-provided external ID. Used to reconcile client transactions with PayPal transactions. Appears in
    transaction and settlement reports but is not visible to the payer."""

    invoice_id: Optional[str] = UNSET
    """The API caller-provided external invoice number for this order. Appears in both the payer's transaction history
    and the emails that the payer receives. invoice_id values are required to be unique within each merchant account by
    default. Although the uniqueness validation is configurable, disabling this behavior will remove the account's
    ability to use invoice_id in other APIs as an identifier. It is highly recommended to keep a unique invoice_id for
    each Order."""

    soft_descriptor: Optional[str] = UNSET
    """This field supports up to 127 characters, but any content beyond 22 characters (including spaces) will be
    truncated. The 22 character limit is reflected in the response representation of this field. The soft descriptor is
    the dynamic text used to construct the statement descriptor that appears on a payer's card statement. If an Order is
    paid using the "PayPal Wallet", the statement descriptor will appear in following format on the payer's card
    statement: PAYPAL_prefix+(space)+merchant_descriptor+(space)+ soft_descriptor Note: The merchant descriptor is the
    descriptor of the merchant’s payment receiving preferences which can be seen by logging into the merchant account
    https://www.sandbox.paypal.com/businessprofile/settings/info/edit The PAYPAL prefix uses 8 characters. Only the
    first 22 characters will be displayed in the statement. For example, if: The PayPal prefix toggle is PAYPAL *. The
    merchant descriptor in the profile is Janes Gift. The soft descriptor is 800-123-1234. Then, the statement
    descriptor on the card is PAYPAL * Janes Gift 80."""

    items: Optional[list[ItemRequest]] = UNSET
    """An array of items that the customer purchases from the merchant."""

    shipping: Optional[ShippingDetails] = UNSET
    """The shipping details."""

    supplementary_data: Optional[SupplementaryData] = UNSET
    """Supplementary data about a payment. This object passes information that can be used to improve risk assessments
    and processing costs, for example, by providing Level 2 and Level 3 payment data."""


class PurchaseUnitRequestDict(TypedDict):
    reference_id: NotRequired[str]
    amount: AmountWithBreakdown | AmountWithBreakdownDict
    payee: NotRequired[PayeeBase | PayeeBaseDict]
    payment_instruction: NotRequired[PaymentInstruction | PaymentInstructionDict]
    description: NotRequired[str]
    custom_id: NotRequired[str]
    invoice_id: NotRequired[str]
    soft_descriptor: NotRequired[str]
    items: NotRequired[list[ItemRequest | ItemRequestDict]]
    shipping: NotRequired[ShippingDetails | ShippingDetailsDict]
    supplementary_data: NotRequired[SupplementaryData | SupplementaryDataDict]
