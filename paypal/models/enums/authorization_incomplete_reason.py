from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AuthorizationIncompleteReason(str, Enum):
    """The reason why the authorized status is ``PENDING``."""

    PENDING_REVIEW = "PENDING_REVIEW"
    """Authorization is pending manual review."""

    DECLINED_BY_RISK_FRAUD_FILTERS = "DECLINED_BY_RISK_FRAUD_FILTERS"
    """Risk Filter set by the payee failed for the transaction."""

    __str__ = str.__str__


AuthorizationIncompleteReasonOrStr: TypeAlias = Annotated[
    AuthorizationIncompleteReason | str, open_enum_validator(AuthorizationIncompleteReason)
]
