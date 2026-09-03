from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ItemCategory(str, Enum):
    """The item category type."""

    DIGITAL_GOODS = "DIGITAL_GOODS"
    """Goods that are stored, delivered, and used in their electronic format. This value is not currently supported for
    API callers that leverage the PayPal for Commerce Platform product."""

    PHYSICAL_GOODS = "PHYSICAL_GOODS"
    """A tangible item that can be shipped with proof of delivery."""

    DONATION = "DONATION"
    """A contribution or gift for which no good or service is exchanged, usually to a not for profit organization."""

    __str__ = str.__str__


ItemCategoryOrStr: TypeAlias = Annotated[ItemCategory | str, open_enum_validator(ItemCategory)]
