from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Name(SdkBaseModel):
    """The name of the party."""

    given_name: Optional[str] = UNSET
    """When the party is a person, the party's given, or first, name."""

    surname: Optional[str] = UNSET
    """When the party is a person, the party's surname or family name. Also known as the last name. Required when the
    party is a person. Use also to store multiple surnames including the matronymic, or mother's, surname."""


class NameDict(TypedDict):
    given_name: NotRequired[str]
    surname: NotRequired[str]
