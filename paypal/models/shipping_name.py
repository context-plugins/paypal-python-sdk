from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ShippingName(SdkBaseModel):
    """The name of the party."""

    full_name: Optional[str] = UNSET
    """When the party is a person, the party's full name."""


class ShippingNameDict(TypedDict):
    full_name: NotRequired[str]
