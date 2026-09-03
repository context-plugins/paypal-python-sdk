from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CvvCode(str, Enum):
    """The card verification value code for for Visa, Discover, Mastercard, or American Express."""

    E = "E"
    """For Visa, Mastercard, Discover, or American Express, error - unrecognized or unknown response."""

    I_ = "I"
    """For Visa, Mastercard, Discover, or American Express, invalid or null."""

    M = "M"
    """For Visa, Mastercard, Discover, or American Express, the CVV2/CSC matches."""

    N = "N"
    """For Visa, Mastercard, Discover, or American Express, the CVV2/CSC does not match."""

    P = "P"
    """For Visa, Mastercard, Discover, or American Express, it was not processed."""

    S = "S"
    """For Visa, Mastercard, Discover, or American Express, the service is not supported."""

    U = "U"
    """For Visa, Mastercard, Discover, or American Express, unknown - the issuer is not certified."""

    X = "X"
    """For Visa, Mastercard, Discover, or American Express, no response. For Maestro, the service is not available."""

    ALL_OTHERS = "All others"
    """For Visa, Mastercard, Discover, or American Express, error."""

    _0 = "0"
    """For Maestro, the CVV2 matched."""

    _1 = "1"
    """For Maestro, the CVV2 did not match."""

    _2 = "2"
    """For Maestro, the merchant has not implemented CVV2 code handling."""

    _3 = "3"
    """For Maestro, the merchant has indicated that CVV2 is not present on card."""

    _4 = "4"
    """For Maestro, the service is not available."""

    __str__ = str.__str__


CvvCodeOrStr: TypeAlias = Annotated[CvvCode | str, open_enum_validator(CvvCode)]
