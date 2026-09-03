from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.token_type import TokenTypeOrStr


class Token(SdkBaseModel):
    """The tokenized payment source to fund a payment."""

    id: str
    """The PayPal-generated ID for the token."""

    type_: TokenTypeOrStr = Field(alias="type")
    """The tokenization method that generated the ID."""


class TokenDict(TypedDict):
    id: str
    type_: TokenTypeOrStr
