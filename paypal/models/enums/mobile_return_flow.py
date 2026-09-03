from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MobileReturnFlow(str, Enum):
    """Merchant preference on how the buyer can navigate back to merchant website post approving the transaction on the
    PayPal App."""

    AUTO = "AUTO"
    """After payment approval in the PayPal App, buyer will automatically be redirected to the merchant website."""

    MANUAL = "MANUAL"
    """After payment approval in the PayPal App, buyer will be asked to manually navigate back to the merchant website
    where they started the transaction from. The buyer is shown a message like 'Return to Merchant' to return to the
    source where the transaction actually started."""

    __str__ = str.__str__


MobileReturnFlowOrStr: TypeAlias = Annotated[MobileReturnFlow | str, open_enum_validator(MobileReturnFlow)]
