from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ExperienceStatus(str, Enum):
    """This field indicates the status of PayPal's Checkout experience throughout the order lifecycle. The values
    reflect the current stage of the checkout process."""

    NOT_STARTED = "NOT_STARTED"
    """PayPal checkout process has not yet begun."""

    IN_PROGRESS = "IN_PROGRESS"
    """PayPal checkout initiated. User is on the checkout page for order review before approval."""

    CANCELED = "CANCELED"
    """PayPal checkout is canceled (by closing the checkout window or clicking cancel) before the order approval."""

    APPROVED = "APPROVED"
    """Order is approved. User has completed the checkout process."""

    __str__ = str.__str__


ExperienceStatusOrStr: TypeAlias = Annotated[ExperienceStatus | str, open_enum_validator(ExperienceStatus)]
