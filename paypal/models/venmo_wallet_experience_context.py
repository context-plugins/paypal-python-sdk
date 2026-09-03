from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .callback_configuration import CallbackConfiguration, CallbackConfigurationDict
from .enums.venmo_wallet_experience_context_shipping_preference import (
    VenmoWalletExperienceContextShippingPreferenceOrStr,
)
from .enums.venmo_wallet_experience_context_user_action import VenmoWalletExperienceContextUserActionOrStr


class VenmoWalletExperienceContext(SdkBaseModel):
    """Customizes the buyer experience during the approval process for payment with Venmo. Note: Partners and
    Marketplaces might configure shipping_preference during partner account setup, which overrides the request
    values."""

    brand_name: Optional[str] = UNSET
    """The business name of the merchant. The pattern is defined by an external party and supports Unicode."""

    shipping_preference: Optional[VenmoWalletExperienceContextShippingPreferenceOrStr] = UNSET
    """The location from which the shipping address is derived."""

    order_update_callback_config: Optional[CallbackConfiguration] = UNSET
    """CallBack Configuration that the merchant can provide to PayPal/Venmo."""

    user_action: Optional[VenmoWalletExperienceContextUserActionOrStr] = UNSET
    """Configures a Continue or Pay Now checkout flow."""


class VenmoWalletExperienceContextDict(TypedDict):
    brand_name: NotRequired[str]
    shipping_preference: NotRequired[VenmoWalletExperienceContextShippingPreferenceOrStr]
    order_update_callback_config: NotRequired[CallbackConfiguration | CallbackConfigurationDict]
    user_action: NotRequired[VenmoWalletExperienceContextUserActionOrStr]
