from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AssuranceDetails(SdkBaseModel):
    """Information about cardholder possession validation and cardholder identification and verifications (ID&V)."""

    account_verified: Optional[bool] = UNSET
    """If true, indicates that Cardholder possession validation has been performed on returned payment credential."""

    card_holder_authenticated: Optional[bool] = UNSET
    """If true, indicates that identification and verifications (ID&V) was performed on the returned payment
    credential.If false, the same risk-based authentication can be performed as you would for card transactions. This
    risk-based authentication can include, but not limited to, step-up with 3D Secure protocol if applicable."""


class AssuranceDetailsDict(TypedDict):
    account_verified: NotRequired[bool]
    card_holder_authenticated: NotRequired[bool]
