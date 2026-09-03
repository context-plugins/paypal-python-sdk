from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PayerBase(SdkBaseModel):
    """The customer who approves and pays for the order. The customer is also known as the payer."""

    email_address: Optional[str] = UNSET
    """The internationalized email address. Note: Up to 64 characters are allowed before and 255 characters are allowed
    after the @ sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern
    verifies that an unquoted @ sign exists."""

    payer_id: Optional[str] = UNSET
    """The account identifier for a PayPal account."""


class PayerBaseDict(TypedDict):
    email_address: NotRequired[str]
    payer_id: NotRequired[str]
