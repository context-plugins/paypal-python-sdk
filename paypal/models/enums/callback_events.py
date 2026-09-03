from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CallbackEvents(str, Enum):
    """CallBack event."""

    SHIPPING_ADDRESS = "SHIPPING_ADDRESS"
    """When Buyer changes or selects the shipping address on the PayPal/Venmo buyer approval flow , PayPal/Venmo will
    call merchant with the callback URL to update order totals."""

    SHIPPING_OPTIONS = "SHIPPING_OPTIONS"
    """When Buyer changes or selects the shipping options on the PayPal/Venmo buyer approval flow , PayPal/Venmo will
    call merchant with the callback URL to update order totals."""

    __str__ = str.__str__


CallbackEventsOrStr: TypeAlias = Annotated[CallbackEvents | str, open_enum_validator(CallbackEvents)]
