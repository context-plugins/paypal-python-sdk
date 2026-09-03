from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.pay_pal_reference_id_type import PayPalReferenceIdTypeOrStr
from .money import Money, MoneyDict


class TransactionInformation(SdkBaseModel):
    """The transaction information."""

    paypal_account_id: Optional[str] = UNSET
    """The ID of the PayPal account of the counterparty."""

    transaction_id: Optional[str] = UNSET
    """The PayPal-generated transaction ID."""

    paypal_reference_id: Optional[str] = UNSET
    """The PayPal-generated base ID. PayPal exclusive. Cannot be altered. Defined as a related, pre-existing transaction
    or event."""

    paypal_reference_id_type: Optional[PayPalReferenceIdTypeOrStr] = UNSET
    """The PayPal reference ID type."""

    transaction_event_code: Optional[str] = UNSET
    """A five-digit transaction event code that classifies the transaction type based on money movement and debit or
    credit. For example, T0001. See `Transaction event codes
    </docs/integration/direct/transaction-search/transaction-event-codes/>`__."""

    transaction_initiation_date: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    transaction_updated_date: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    transaction_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    fee_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    discount_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    insurance_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    sales_tax_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    shipping_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    shipping_discount_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    shipping_tax_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    other_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    tip_amount: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    transaction_status: Optional[str] = UNSET
    """A code that indicates the transaction status. Value is: Status code Description D PayPal or merchant rules denied
    the transaction. P The transaction is pending. The transaction was created but waits for another payment process to
    complete, such as an ACH transaction, before the status changes to S. S The transaction successfully completed
    without a denial and after any pending statuses. V A successful transaction was fully reversed and funds were
    refunded to the original sender."""

    transaction_subject: Optional[str] = UNSET
    """The subject of payment. The payer passes this value to the payee. The payer controls this data through the
    interface through which he or she sends the data."""

    transaction_note: Optional[str] = UNSET
    """A special note that the payer passes to the payee. Might contain special customer requests, such as shipping
    instructions."""

    payment_tracking_id: Optional[str] = UNSET
    """The payment tracking ID, which is a unique ID that partners specify to either get information about a payment or
    request a refund."""

    bank_reference_id: Optional[str] = UNSET
    """The bank reference ID. The bank provides this value for an ACH transaction."""

    ending_balance: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    available_balance: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    invoice_id: Optional[str] = UNSET
    """The invoice ID that is sent by the merchant with the transaction. Note: If an invoice ID was sent with the
    capture request, the value is reported. Otherwise, the invoice ID of the authorizing transaction is reported."""

    custom_field: Optional[str] = UNSET
    """The merchant-provided custom text. Note: Usually, this field includes the unique ID for payments made with
    MassPay type transaction."""

    protection_eligibility: Optional[str] = UNSET
    """Indicates whether the transaction is eligible for protection. Value is: 01. Eligible. 02. Not eligible 03.
    Partially eligible."""

    credit_term: Optional[str] = UNSET
    """The credit term. The time span covered by the installment payments as expressed in the term length plus the
    length time unit code."""

    credit_transactional_fee: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    credit_promotional_fee: Optional[Money] = UNSET
    """The currency and amount for a financial transaction, such as a balance or payment due."""

    annual_percentage_rate: Optional[str] = UNSET
    """The percentage, as a fixed-point, signed decimal number. For example, define a 19.99% interest rate as
    ``19.99``."""

    payment_method_type: Optional[str] = UNSET
    """The payment method that was used for a transaction. Value is PUI, installment, or mEFT. Note: Appears only for
    pay upon invoice (PUI), installment, and mEFT transactions. Merchants and partners in the EMEA region can use this
    attribute to note transactions that attract turn-over tax."""

    instrument_type: Optional[str] = UNSET
    """A high-level classification of the type of financial instrument that was used to fund a payment. The pattern is
    not provided because the value is defined by an external party. E.g. PAYPAL, CREDIT_CARD, DEBIT_CARD, APPLE_PAY,
    BANK , VENMO ,Pay Upon Invoice, Pay Later or Alternative Payment Methods (APM)."""

    instrument_sub_type: Optional[str] = UNSET
    """A finer-grained classification of the financial instrument that was used to fund a payment. For example, ``Visa
    card`` or a ``Mastercard`` for a credit card, BANKCARD ,DISCOVER etc. The pattern is not provided because the value
    is defined by an external party."""


class TransactionInformationDict(TypedDict):
    paypal_account_id: NotRequired[str]
    transaction_id: NotRequired[str]
    paypal_reference_id: NotRequired[str]
    paypal_reference_id_type: NotRequired[PayPalReferenceIdTypeOrStr]
    transaction_event_code: NotRequired[str]
    transaction_initiation_date: NotRequired[str]
    transaction_updated_date: NotRequired[str]
    transaction_amount: NotRequired[Money | MoneyDict]
    fee_amount: NotRequired[Money | MoneyDict]
    discount_amount: NotRequired[Money | MoneyDict]
    insurance_amount: NotRequired[Money | MoneyDict]
    sales_tax_amount: NotRequired[Money | MoneyDict]
    shipping_amount: NotRequired[Money | MoneyDict]
    shipping_discount_amount: NotRequired[Money | MoneyDict]
    shipping_tax_amount: NotRequired[Money | MoneyDict]
    other_amount: NotRequired[Money | MoneyDict]
    tip_amount: NotRequired[Money | MoneyDict]
    transaction_status: NotRequired[str]
    transaction_subject: NotRequired[str]
    transaction_note: NotRequired[str]
    payment_tracking_id: NotRequired[str]
    bank_reference_id: NotRequired[str]
    ending_balance: NotRequired[Money | MoneyDict]
    available_balance: NotRequired[Money | MoneyDict]
    invoice_id: NotRequired[str]
    custom_field: NotRequired[str]
    protection_eligibility: NotRequired[str]
    credit_term: NotRequired[str]
    credit_transactional_fee: NotRequired[Money | MoneyDict]
    credit_promotional_fee: NotRequired[Money | MoneyDict]
    annual_percentage_rate: NotRequired[str]
    payment_method_type: NotRequired[str]
    instrument_type: NotRequired[str]
    instrument_sub_type: NotRequired[str]
