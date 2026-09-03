from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AvsCode(str, Enum):
    """The address verification code for Visa, Discover, Mastercard, or American Express transactions."""

    A = "A"
    """For Visa, Mastercard, or Discover transactions, the address matches but the zip code does not match. For American
    Express transactions, the card holder address is correct."""

    B = "B"
    """For Visa, Mastercard, or Discover transactions, the address matches. International A."""

    C = "C"
    """For Visa, Mastercard, or Discover transactions, no values match. International N."""

    D = "D"
    """For Visa, Mastercard, or Discover transactions, the address and postal code match. International X."""

    E = "E"
    """For Visa, Mastercard, or Discover transactions, not allowed for Internet or phone transactions. For American
    Express card holder, the name is incorrect but the address and postal code match."""

    F = "F"
    """For Visa, Mastercard, or Discover transactions, the address and postal code match. UK-specific X. For American
    Express card holder, the name is incorrect but the address matches."""

    G = "G"
    """For Visa, Mastercard, or Discover transactions, global is unavailable. Nothing matches."""

    I_ = "I"
    """For Visa, Mastercard, or Discover transactions, international is unavailable. Not applicable."""

    M = "M"
    """For Visa, Mastercard, or Discover transactions, the address and postal code match. For American Express card
    holder, the name, address, and postal code match."""

    N = "N"
    """For Visa, Mastercard, or Discover transactions, nothing matches. For American Express card holder, the address
    and postal code are both incorrect."""

    P = "P"
    """For Visa, Mastercard, or Discover transactions, postal international Z. Postal code only."""

    R = "R"
    """For Visa, Mastercard, or Discover transactions, re-try the request. For American Express, the system is
    unavailable."""

    S = "S"
    """For Visa, Mastercard, Discover, or American Express, the service is not supported."""

    U = "U"
    """For Visa, Mastercard, or Discover transactions, the service is unavailable. For American Express, information is
    not available. For Maestro, the address is not checked or the acquirer had no response. The service is not
    available."""

    W = "W"
    """For Visa, Mastercard, or Discover transactions, whole ZIP code. For American Express, the card holder name,
    address, and postal code are all incorrect."""

    X = "X"
    """For Visa, Mastercard, or Discover transactions, exact match of the address and the nine-digit ZIP code. For
    American Express, the card holder name, address, and postal code are all incorrect."""

    Y = "Y"
    """For Visa, Mastercard, or Discover transactions, the address and five-digit ZIP code match. For American Express,
    the card holder address and postal code are both correct."""

    Z = "Z"
    """For Visa, Mastercard, or Discover transactions, the five-digit ZIP code matches but no address. For American
    Express, only the card holder postal code is correct."""

    NULL = "Null"
    """For Maestro, no AVS response was obtained."""

    _0 = "0"
    """For Maestro, all address information matches."""

    _1 = "1"
    """For Maestro, none of the address information matches."""

    _2 = "2"
    """For Maestro, part of the address information matches."""

    _3 = "3"
    """For Maestro, the merchant did not provide AVS information. It was not processed."""

    _4 = "4"
    """For Maestro, the address was not checked or the acquirer had no response. The service is not available."""

    __str__ = str.__str__


AvsCodeOrStr: TypeAlias = Annotated[AvsCode | str, open_enum_validator(AvsCode)]
