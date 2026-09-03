from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CaptureIncompleteReason(str, Enum):
    """The reason why the captured payment status is ``PENDING`` or ``DENIED``."""

    BUYER_COMPLAINT = "BUYER_COMPLAINT"
    """The payer initiated a dispute for this captured payment with PayPal."""

    CHARGEBACK = "CHARGEBACK"
    """The captured funds were reversed in response to the payer disputing this captured payment with the issuer of the
    financial instrument used to pay for this captured payment."""

    ECHECK = "ECHECK"
    """The payer paid by an eCheck that has not yet cleared."""

    INTERNATIONAL_WITHDRAWAL = "INTERNATIONAL_WITHDRAWAL"
    """Visit your online account. In your **Account Overview**, accept and deny this payment."""

    OTHER = "OTHER"
    """No additional specific reason can be provided. For more information about this captured payment, visit your
    account online or contact PayPal."""

    PENDING_REVIEW = "PENDING_REVIEW"
    """The captured payment is pending manual review."""

    RECEIVING_PREFERENCE_MANDATES_MANUAL_ACTION = "RECEIVING_PREFERENCE_MANDATES_MANUAL_ACTION"
    """The payee has not yet set up appropriate receiving preferences for their account. For more information about how
    to accept or deny this payment, visit your account online. This reason is typically offered in scenarios such as
    when the currency of the captured payment is different from the primary holding currency of the payee."""

    REFUNDED = "REFUNDED"
    """The captured funds were refunded."""

    TRANSACTION_APPROVED_AWAITING_FUNDING = "TRANSACTION_APPROVED_AWAITING_FUNDING"
    """The payer must send the funds for this captured payment. This code generally appears for manual EFTs."""

    UNILATERAL = "UNILATERAL"
    """The payee does not have a PayPal account."""

    VERIFICATION_REQUIRED = "VERIFICATION_REQUIRED"
    """The payee's PayPal account is not verified."""

    DECLINED_BY_RISK_FRAUD_FILTERS = "DECLINED_BY_RISK_FRAUD_FILTERS"
    """Risk Filter set by the payee failed for the transaction."""

    __str__ = str.__str__


CaptureIncompleteReasonOrStr: TypeAlias = Annotated[
    CaptureIncompleteReason | str, open_enum_validator(CaptureIncompleteReason)
]
