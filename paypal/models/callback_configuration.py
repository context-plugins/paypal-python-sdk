from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.callback_events import CallbackEventsOrStr


class CallbackConfiguration(SdkBaseModel):
    """CallBack Configuration that the merchant can provide to PayPal/Venmo."""

    callback_events: list[CallbackEventsOrStr]
    """An array of callback events merchant can subscribe to for the corresponding callback url."""

    callback_url: str
    """Merchant provided CallBack url.PayPal/Venmo will use this url to call the merchant back when the events occur
    .PayPal/Venmo expects a secured url usually in the https format.merchant can append the cart id or other params part
    of the url as query or path params."""


class CallbackConfigurationDict(TypedDict):
    callback_events: list[CallbackEventsOrStr]
    callback_url: str
