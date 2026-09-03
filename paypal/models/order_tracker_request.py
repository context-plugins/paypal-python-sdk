from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.shipment_carrier import ShipmentCarrierOrStr
from .order_tracker_item import OrderTrackerItem, OrderTrackerItemDict


class OrderTrackerRequest(SdkBaseModel):
    """The tracking details of an order."""

    tracking_number: Optional[str] = UNSET
    """The tracking number for the shipment. This property supports Unicode."""

    carrier: Optional[ShipmentCarrierOrStr] = UNSET
    """The carrier for the shipment. Some carriers have a global version as well as local subsidiaries. The subsidiaries
    are repeated over many countries and might also have an entry in the global list. Choose the carrier for your
    country. If the carrier is not available for your country, choose the global version of the carrier. If your carrier
    name is not in the list, set ``carrier`` to ``OTHER`` and set carrier name in ``carrier_name_other``. For allowed
    values, see Carriers."""

    carrier_name_other: Optional[str] = UNSET
    """The name of the carrier for the shipment. Provide this value only if the carrier parameter is OTHER. This
    property supports Unicode."""

    capture_id: str
    """The PayPal capture ID."""

    notify_payer: Optional[bool] = UNSET
    """If true, PayPal will send an email notification to the payer of the PayPal transaction. The email contains the
    tracking details provided through the Orders tracking API request. Independent of any value passed for
    ``notify_payer``, the payer may receive tracking notifications within the PayPal app, based on the user's
    notification preferences."""

    items: Optional[list[OrderTrackerItem]] = UNSET
    """An array of details of items in the shipment."""


class OrderTrackerRequestDict(TypedDict):
    tracking_number: NotRequired[str]
    carrier: NotRequired[ShipmentCarrierOrStr]
    carrier_name_other: NotRequired[str]
    capture_id: str
    notify_payer: NotRequired[bool]
    items: NotRequired[list[OrderTrackerItem | OrderTrackerItemDict]]
