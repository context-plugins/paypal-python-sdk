from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .authorization_with_additional_data import AuthorizationWithAdditionalData, AuthorizationWithAdditionalDataDict
from .orders_capture import OrdersCapture, OrdersCaptureDict
from .refund import Refund, RefundDict


class PaymentCollection(SdkBaseModel):
    """The collection of payments, or transactions, for a purchase unit in an order. For example, authorized payments,
    captured payments, and refunds."""

    authorizations: Optional[list[AuthorizationWithAdditionalData]] = UNSET
    """An array of authorized payments for a purchase unit. A purchase unit can have zero or more authorized
    payments."""

    captures: Optional[list[OrdersCapture]] = UNSET
    """An array of captured payments for a purchase unit. A purchase unit can have zero or more captured payments."""

    refunds: Optional[list[Refund]] = UNSET
    """An array of refunds for a purchase unit. A purchase unit can have zero or more refunds."""


class PaymentCollectionDict(TypedDict):
    authorizations: NotRequired[list[AuthorizationWithAdditionalData | AuthorizationWithAdditionalDataDict]]
    captures: NotRequired[list[OrdersCapture | OrdersCaptureDict]]
    refunds: NotRequired[list[Refund | RefundDict]]
