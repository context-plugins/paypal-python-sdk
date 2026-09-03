from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VaultTokenRequestType(str, Enum):
    """The tokenization method that generated the ID."""

    SETUP_TOKEN = "SETUP_TOKEN"
    """The setup token, which is a temporary reference to payment source."""

    __str__ = str.__str__


VaultTokenRequestTypeOrStr: TypeAlias = Annotated[
    VaultTokenRequestType | str, open_enum_validator(VaultTokenRequestType)
]
