from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PlanRequestStatus(str, Enum):
    """The initial state of the plan. Allowed input values are CREATED and ACTIVE."""

    CREATED = "CREATED"
    """The plan was created. You cannot create subscriptions for a plan in this state."""

    INACTIVE = "INACTIVE"
    """The plan is inactive."""

    ACTIVE = "ACTIVE"
    """The plan is active. You can only create subscriptions for a plan in this state."""

    __str__ = str.__str__


PlanRequestStatusOrStr: TypeAlias = Annotated[PlanRequestStatus | str, open_enum_validator(PlanRequestStatus)]
