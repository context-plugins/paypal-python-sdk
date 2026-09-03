from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SetupFeeFailureAction(str, Enum):
    """The action to take on the subscription if the initial payment for the setup fails."""

    CONTINUE = "CONTINUE"
    """Continues the subscription if the initial payment for the setup fails."""

    CANCEL = "CANCEL"
    """Cancels the subscription if the initial payment for the setup fails."""

    __str__ = str.__str__


SetupFeeFailureActionOrStr: TypeAlias = Annotated[
    SetupFeeFailureAction | str, open_enum_validator(SetupFeeFailureAction)
]
