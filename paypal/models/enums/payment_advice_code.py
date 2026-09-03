from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentAdviceCode(str, Enum):
    """The declined payment transactions might have payment advice codes. The card networks, like Visa and Mastercard,
    return payment advice codes."""

    _01 = "01"
    """For Mastercard, expired card account upgrade or portfolio sale conversion. Obtain new account information before
    next billing cycle."""

    _02 = "02"
    """For Mastercard, over credit limit or insufficient funds. Retry the transaction 72 hours later. For Visa, the card
    holder wants to stop only one specific payment in the recurring payment relationship. The merchant must NOT resubmit
    the same transaction. The merchant can continue the billing process in the subsequent billing period."""

    _03 = "03"
    """For Mastercard, account closed as fraudulent. Obtain another type of payment from customer due to account being
    closed or fraud. Possible reason: Account closed as fraudulent. For Visa, the card holder wants to stop all
    recurring payment transactions for a specific merchant. Stop recurring payment requests."""

    _04 = "04"
    """For Mastercard, token requirements not fulfilled for this token type."""

    _21 = "21"
    """For Mastercard, the card holder has been unsuccessful at canceling recurring payment through merchant. Stop
    recurring payment requests. For Visa, all recurring payments were canceled for the card number requested. Stop
    recurring payment requests."""

    _22 = "22"
    """For Mastercard, merchant does not qualify for product code."""

    _24 = "24"
    """For Mastercard, retry after 1 hour."""

    _25 = "25"
    """For Mastercard, retry after 24 hours."""

    _26 = "26"
    """For Mastercard, retry after 2 days."""

    _27 = "27"
    """For Mastercard, retry after 4 days."""

    _28 = "28"
    """For Mastercard, retry after 6 days."""

    _29 = "29"
    """For Mastercard, retry after 8 days."""

    _30 = "30"
    """For Mastercard, retry after 10 days ."""

    _40 = "40"
    """For Mastercard, consumer non-reloadable prepaid card."""

    _43 = "43"
    """For Mastercard, consumer multi-use virtual card number."""

    __str__ = str.__str__


PaymentAdviceCodeOrStr: TypeAlias = Annotated[PaymentAdviceCode | str, open_enum_validator(PaymentAdviceCode)]
