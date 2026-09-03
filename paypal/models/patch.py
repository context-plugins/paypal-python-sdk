from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.patch_op import PatchOpOrStr


class Patch(SdkBaseModel):
    """The JSON patch object to apply partial updates to resources."""

    op: PatchOpOrStr
    """The operation."""

    path: Optional[str] = UNSET
    """The JSON Pointer to the target document location at which to complete the operation."""

    value: Optional[Any] = UNSET
    """The value to apply. The remove, copy, and move operations do not require a value. Since JSON Patch allows any
    type for value, the type property is not specified."""

    from_: Optional[str] = Field(default=UNSET, alias="from")
    """The JSON Pointer to the target document location from which to move the value. Required for the move
    operation."""


class PatchDict(TypedDict):
    op: PatchOpOrStr
    path: NotRequired[str]
    value: NotRequired[Any]
    from_: NotRequired[str]
