from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderTrackerStatus(str, Enum):
    """The status of the item shipment."""

    CANCELLED = "CANCELLED"
    """The shipment was cancelled and the tracking number no longer applies."""

    SHIPPED = "SHIPPED"
    """The merchant has assigned a tracking number to the items being shipped from the Order. This does not correspond
    to the carrier's actual status for the shipment. The latest status of the parcel must be retrieved from the
    carrier."""

    __str__ = str.__str__


OrderTrackerStatusOrStr: TypeAlias = Annotated[OrderTrackerStatus | str, open_enum_validator(OrderTrackerStatus)]
