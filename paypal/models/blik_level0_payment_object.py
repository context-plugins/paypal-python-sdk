from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BlikLevel0PaymentObject(SdkBaseModel):
    """Information used to pay using BLIK level_0 flow."""

    auth_code: str
    """The 6-digit code used to authenticate a consumer within BLIK."""


class BlikLevel0PaymentObjectDict(TypedDict):
    auth_code: str
