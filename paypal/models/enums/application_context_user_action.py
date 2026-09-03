from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ApplicationContextUserAction(str, Enum):
    """Configures the label name to ``Continue`` or ``Subscribe Now`` for subscription consent experience."""

    CONTINUE = "CONTINUE"
    """After you redirect the customer to the PayPal subscription consent page, a Continue button appears. Use this
    option when you want to control the activation of the subscription and do not want PayPal to activate the
    subscription."""

    SUBSCRIBE_NOW = "SUBSCRIBE_NOW"
    """After you redirect the customer to the PayPal subscription consent page, a Subscribe Now button appears. Use this
    option when you want PayPal to activate the subscription."""

    __str__ = str.__str__


ApplicationContextUserActionOrStr: TypeAlias = Annotated[
    ApplicationContextUserAction | str, open_enum_validator(ApplicationContextUserAction)
]
