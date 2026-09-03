from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TenureType(str, Enum):
    """The tenure type of the billing cycle identifies if the billing cycle is a trial(free or discounted) or regular
    billing cycle., The tenure type of the billing cycle. In case of a plan having trial cycle, only 2 trial cycles are
    allowed per plan., The type of the billing cycle."""

    REGULAR = "REGULAR"
    """A regular billing cycle to identify recurring charges for the billing agreement."""

    TRIAL = "TRIAL"
    """A trial billing cycle to identify free or discounted charge for the billing agreement. Free trails will not have
    a price object in pricing scheme where as a discounted trial would have a discounted price compared to regular
    billing cycle."""

    __str__ = str.__str__


TenureTypeOrStr: TypeAlias = Annotated[TenureType | str, open_enum_validator(TenureType)]
