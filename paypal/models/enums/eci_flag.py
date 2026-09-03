from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EciFlag(str, Enum):
    """Electronic Commerce Indicator (ECI). The ECI value is part of the 2 data elements that indicate the transaction
    was processed electronically. This should be passed on the authorization transaction to the Gateway/Processor."""

    MASTERCARD_NON_3_D_SECURE_TRANSACTION = "MASTERCARD_NON_3D_SECURE_TRANSACTION"
    """Mastercard non-3-D Secure transaction."""

    MASTERCARD_ATTEMPTED_AUTHENTICATION_TRANSACTION = "MASTERCARD_ATTEMPTED_AUTHENTICATION_TRANSACTION"
    """Mastercard attempted authentication transaction."""

    MASTERCARD_FULLY_AUTHENTICATED_TRANSACTION = "MASTERCARD_FULLY_AUTHENTICATED_TRANSACTION"
    """Mastercard fully authenticated transaction."""

    FULLY_AUTHENTICATED_TRANSACTION = "FULLY_AUTHENTICATED_TRANSACTION"
    """VISA, AMEX, JCB, DINERS CLUB fully authenticated transaction."""

    ATTEMPTED_AUTHENTICATION_TRANSACTION = "ATTEMPTED_AUTHENTICATION_TRANSACTION"
    """VISA, AMEX, JCB, DINERS CLUB attempted authentication transaction."""

    NON_3_D_SECURE_TRANSACTION = "NON_3D_SECURE_TRANSACTION"
    """VISA, AMEX, JCB, DINERS CLUB non-3-D Secure transaction."""

    __str__ = str.__str__


EciFlagOrStr: TypeAlias = Annotated[EciFlag | str, open_enum_validator(EciFlag)]
