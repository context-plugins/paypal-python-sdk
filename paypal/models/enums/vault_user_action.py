from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VaultUserAction(str, Enum):
    """User Action on action to be performed after a successful payer approval."""

    SETUP_NOW = "SETUP_NOW"
    """After you redirect the customer to the PayPal payment page, a Setup Now button appears. Use this option when no
    additional inputs are needed from merchant site and to create the billing agreement immediately when the customer
    clicks Setup Now."""

    CONTINUE = "CONTINUE"
    """After you redirect the customer to the PayPal payment page, a Continue button appears. Use this option when you
    want to redirect the customer from the completed payment page to the merchant site for additional inputs without
    immediately creating the billing agreement."""

    __str__ = str.__str__


VaultUserActionOrStr: TypeAlias = Annotated[VaultUserAction | str, open_enum_validator(VaultUserAction)]
