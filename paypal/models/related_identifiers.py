from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RelatedIdentifiers(SdkBaseModel):
    """Identifiers related to a specific resource."""

    order_id: Optional[str] = UNSET
    """Order ID related to the resource."""

    authorization_id: Optional[str] = UNSET
    """Authorization ID related to the resource."""

    capture_id: Optional[str] = UNSET
    """Capture ID related to the resource."""


class RelatedIdentifiersDict(TypedDict):
    order_id: NotRequired[str]
    authorization_id: NotRequired[str]
    capture_id: NotRequired[str]
