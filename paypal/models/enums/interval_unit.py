from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IntervalUnit(str, Enum):
    """The interval at which the subscription is charged or billed."""

    DAY = "DAY"
    """A daily billing cycle."""

    WEEK = "WEEK"
    """A weekly billing cycle."""

    MONTH = "MONTH"
    """A monthly billing cycle."""

    YEAR = "YEAR"
    """A yearly billing cycle."""

    __str__ = str.__str__


IntervalUnitOrStr: TypeAlias = Annotated[IntervalUnit | str, open_enum_validator(IntervalUnit)]
