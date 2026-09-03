from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TaxIdType(str, Enum):
    """The customer's tax ID type."""

    BR_CPF = "BR_CPF"
    """The individual tax ID type, typically is 11 characters long."""

    BR_CNPJ = "BR_CNPJ"
    """The business tax ID type, typically is 14 characters long."""

    __str__ = str.__str__


TaxIdTypeOrStr: TypeAlias = Annotated[TaxIdType | str, open_enum_validator(TaxIdType)]
