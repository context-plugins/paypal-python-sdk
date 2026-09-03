from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.eci_flag import EciFlagOrStr


class NetworkToken(SdkBaseModel):
    """The Third Party Network token used to fund a payment."""

    number: str
    """Third party network token number."""

    expiry: str
    """The year and month, in ISO-8601 ``YYYY-MM`` date format. See `Internet date and time format
    <https://tools.ietf.org/html/rfc3339#section-5.6>`__."""

    cryptogram: Optional[str] = UNSET
    """An Encrypted one-time use value that's sent along with Network Token. This field is not required to be present
    for recurring transactions."""

    eci_flag: Optional[EciFlagOrStr] = UNSET
    """Electronic Commerce Indicator (ECI). The ECI value is part of the 2 data elements that indicate the transaction
    was processed electronically. This should be passed on the authorization transaction to the Gateway/Processor."""

    token_requestor_id: Optional[str] = UNSET
    """A TRID, or a Token Requestor ID, is an identifier used by merchants to request network tokens from card networks.
    A TRID is a precursor to obtaining a network token for a credit card primary account number (PAN), and will aid in
    enabling secure card on file (COF) payments and reducing fraud."""


class NetworkTokenDict(TypedDict):
    number: str
    expiry: str
    cryptogram: NotRequired[str]
    eci_flag: NotRequired[EciFlagOrStr]
    token_requestor_id: NotRequired[str]
