from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.order_tracker_status import OrderTrackerStatusOrStr
from .link_description import LinkDescription, LinkDescriptionDict
from .order_tracker_item import OrderTrackerItem, OrderTrackerItemDict


class OrderTrackerResponse(SdkBaseModel):
    """The tracking response on creation of tracker."""

    id: Optional[str] = UNSET
    """The tracker id."""

    status: Optional[OrderTrackerStatusOrStr] = UNSET
    """The status of the item shipment."""

    items: Optional[list[OrderTrackerItem]] = UNSET
    """An array of details of items in the shipment."""

    links: Optional[list[LinkDescription]] = UNSET
    """An array of request-related HATEOAS links."""

    create_time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""

    update_time: Optional[str] = UNSET
    """The date and time, in `Internet date and time format <https://tools.ietf.org/html/rfc3339#section-5.6>`__.
    Seconds are required while fractional seconds are optional. Note: The regular expression provides guidance but does
    not reject all invalid dates."""


class OrderTrackerResponseDict(TypedDict):
    id: NotRequired[str]
    status: NotRequired[OrderTrackerStatusOrStr]
    items: NotRequired[list[OrderTrackerItem | OrderTrackerItemDict]]
    links: NotRequired[list[LinkDescription | LinkDescriptionDict]]
    create_time: NotRequired[str]
    update_time: NotRequired[str]
