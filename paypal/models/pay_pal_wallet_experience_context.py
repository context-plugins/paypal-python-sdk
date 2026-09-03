from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .app_switch_context import AppSwitchContext, AppSwitchContextDict
from .callback_configuration import CallbackConfiguration, CallbackConfigurationDict
from .enums.pay_pal_experience_landing_page import PayPalExperienceLandingPageOrStr
from .enums.pay_pal_experience_user_action import PayPalExperienceUserActionOrStr
from .enums.pay_pal_wallet_contact_preference import PayPalWalletContactPreferenceOrStr
from .enums.pay_pal_wallet_context_shipping_preference import PayPalWalletContextShippingPreferenceOrStr
from .enums.payee_payment_method_preference import PayeePaymentMethodPreferenceOrStr


class PayPalWalletExperienceContext(SdkBaseModel):
    """Customizes the payer experience during the approval process for payment with PayPal. Note: Partners and
    Marketplaces might configure brand_name and shipping_preference during partner account setup, which overrides the
    request values."""

    brand_name: Optional[str] = UNSET
    """The label that overrides the business name in the PayPal account on the PayPal site. The pattern is defined by an
    external party and supports Unicode."""

    locale: Optional[str] = UNSET
    """The `language tag <https://tools.ietf.org/html/bcp47#section-2>`__ for the language in which to localize the
    error-related strings, such as messages, issues, and suggested actions. The tag is made up of the `ISO 639-2
    language code <https://www.loc.gov/standards/iso639-2/php/code_list.php>`__, the optional `ISO-15924 script tag
    <https://www.unicode.org/iso15924/codelists.html>`__, and the `ISO-3166 alpha-2 country code
    <https://developer.paypal.com/api/rest/reference/country-codes/>`__ or `M49 region code
    <https://unstats.un.org/unsd/methodology/m49/>`__."""

    shipping_preference: Optional[PayPalWalletContextShippingPreferenceOrStr] = UNSET
    """The location from which the shipping address is derived."""

    contact_preference: Optional[PayPalWalletContactPreferenceOrStr] = UNSET
    """The preference to display the contact information (buyer’s shipping email & phone number) on PayPal's checkout
    for easy merchant-buyer communication."""

    return_url: Optional[str] = UNSET
    """Describes the URL."""

    cancel_url: Optional[str] = UNSET
    """Describes the URL."""

    app_switch_context: Optional[AppSwitchContext] = UNSET
    """Merchant provided details of the native app or mobile web browser to facilitate buyer's app switch to the PayPal
    consumer app."""

    landing_page: Optional[PayPalExperienceLandingPageOrStr] = UNSET
    """The type of landing page to show on the PayPal site for customer checkout."""

    user_action: Optional[PayPalExperienceUserActionOrStr] = UNSET
    """Configures a Continue or Pay Now checkout flow."""

    payment_method_preference: Optional[PayeePaymentMethodPreferenceOrStr] = UNSET
    """The merchant-preferred payment methods."""

    order_update_callback_config: Optional[CallbackConfiguration] = UNSET
    """CallBack Configuration that the merchant can provide to PayPal/Venmo."""


class PayPalWalletExperienceContextDict(TypedDict):
    brand_name: NotRequired[str]
    locale: NotRequired[str]
    shipping_preference: NotRequired[PayPalWalletContextShippingPreferenceOrStr]
    contact_preference: NotRequired[PayPalWalletContactPreferenceOrStr]
    return_url: NotRequired[str]
    cancel_url: NotRequired[str]
    app_switch_context: NotRequired[AppSwitchContext | AppSwitchContextDict]
    landing_page: NotRequired[PayPalExperienceLandingPageOrStr]
    user_action: NotRequired[PayPalExperienceUserActionOrStr]
    payment_method_preference: NotRequired[PayeePaymentMethodPreferenceOrStr]
    order_update_callback_config: NotRequired[CallbackConfiguration | CallbackConfigurationDict]
