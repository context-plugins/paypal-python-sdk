from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class StoreInformation(SdkBaseModel):
    """The store information."""

    store_id: Optional[str] = UNSET
    """The ID of a store for a merchant in the system of record."""

    terminal_id: Optional[str] = UNSET
    """The terminal ID for the checkout stand in a merchant store."""


class StoreInformationDict(TypedDict):
    store_id: NotRequired[str]
    terminal_id: NotRequired[str]
