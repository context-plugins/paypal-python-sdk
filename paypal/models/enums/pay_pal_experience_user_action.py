from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PayPalExperienceUserAction(str, Enum):
    """Configures a Continue or Pay Now checkout flow."""

    CONTINUE = "CONTINUE"
    """After you redirect the customer to the PayPal payment page, a Continue button appears. Use this option when the
    final amount is not known when the checkout flow is initiated and you want to redirect the customer to the merchant
    page without processing the payment."""

    PAY_NOW = "PAY_NOW"
    """After you redirect the customer to the PayPal payment page, a Pay Now button appears. Use this option when the
    final amount is known when the checkout is initiated and you want to process the payment immediately when the
    customer clicks Pay Now."""

    __str__ = str.__str__


PayPalExperienceUserActionOrStr: TypeAlias = Annotated[
    PayPalExperienceUserAction | str, open_enum_validator(PayPalExperienceUserAction)
]
