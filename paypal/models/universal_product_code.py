from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.upc_type import UpcTypeOrStr


class UniversalProductCode(SdkBaseModel):
    """The Universal Product Code of the item."""

    type_: UpcTypeOrStr = Field(alias="type")
    """The Universal Product Code type."""

    code: str
    """The UPC product code of the item."""


class UniversalProductCodeDict(TypedDict):
    type_: UpcTypeOrStr
    code: str
