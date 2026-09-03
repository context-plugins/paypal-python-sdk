from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .mobile_web_context import MobileWebContext, MobileWebContextDict
from .native_app_context import NativeAppContext, NativeAppContextDict


class AppSwitchContext(SdkBaseModel):
    """Merchant provided details of the native app or mobile web browser to facilitate buyer's app switch to the PayPal
    consumer app."""

    native_app: Optional[NativeAppContext] = UNSET
    """Merchant provided, buyer's native app preferences to app switch to the PayPal consumer app."""

    mobile_web: Optional[MobileWebContext] = UNSET
    """Buyer's mobile web browser context to app switch to the PayPal consumer app."""


class AppSwitchContextDict(TypedDict):
    native_app: NotRequired[NativeAppContext | NativeAppContextDict]
    mobile_web: NotRequired[MobileWebContext | MobileWebContextDict]
