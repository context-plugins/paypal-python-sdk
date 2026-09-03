from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.application_context_user_action import ApplicationContextUserActionOrStr
from .enums.experience_context_shipping_preference import ExperienceContextShippingPreferenceOrStr
from .payment_method import PaymentMethod, PaymentMethodDict


class SubscriptionApplicationContext(SdkBaseModel):
    """The application context, which customizes the payer experience during the subscription approval process with
    PayPal."""

    brand_name: Optional[str] = UNSET
    """The label that overrides the business name in the PayPal account on the PayPal site."""

    locale: Optional[str] = UNSET
    """The BCP 47-formatted locale of pages that the PayPal payment experience shows. PayPal supports a five-character
    code. For example, ``da-DK``, ``he-IL``, ``id-ID``, ``ja-JP``, ``no-NO``, ``pt-BR``, ``ru-RU``, ``sv-SE``,
    ``th-TH``, ``zh-CN``, ``zh-HK``, or ``zh-TW``."""

    shipping_preference: Optional[ExperienceContextShippingPreferenceOrStr] = UNSET
    """The location from which the shipping address is derived."""

    user_action: Optional[ApplicationContextUserActionOrStr] = UNSET
    """Configures the label name to ``Continue`` or ``Subscribe Now`` for subscription consent experience."""

    payment_method: Optional[PaymentMethod] = UNSET
    """The customer and merchant payment preferences."""

    return_url: str
    """The URL where the customer is redirected after the customer approves the payment."""

    cancel_url: str
    """The URL where the customer is redirected after the customer cancels the payment."""


class SubscriptionApplicationContextDict(TypedDict):
    brand_name: NotRequired[str]
    locale: NotRequired[str]
    shipping_preference: NotRequired[ExperienceContextShippingPreferenceOrStr]
    user_action: NotRequired[ApplicationContextUserActionOrStr]
    payment_method: NotRequired[PaymentMethod | PaymentMethodDict]
    return_url: str
    cancel_url: str
