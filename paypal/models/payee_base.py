from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PayeeBase(SdkBaseModel):
    """The details for the merchant who receives the funds and fulfills the order. The merchant is also known as the
    payee."""

    email_address: Optional[str] = UNSET
    """The internationalized email address. Note: Up to 64 characters are allowed before and 255 characters are allowed
    after the @ sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern
    verifies that an unquoted @ sign exists."""

    merchant_id: Optional[str] = UNSET
    """The account identifier for a PayPal account."""


class PayeeBaseDict(TypedDict):
    email_address: NotRequired[str]
    merchant_id: NotRequired[str]
