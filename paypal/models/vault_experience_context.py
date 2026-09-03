from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .app_switch_context import AppSwitchContext, AppSwitchContextDict
from .enums.experience_context_shipping_preference import ExperienceContextShippingPreferenceOrStr
from .enums.vault_instruction_action import VaultInstructionActionOrStr
from .enums.vault_user_action import VaultUserActionOrStr


class VaultExperienceContext(SdkBaseModel):
    """Customizes the Vault creation flow experience for your customers."""

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

    return_url: Optional[str] = UNSET
    """The URL where the customer is redirected after customer approves leaves the flow. It is a required field for
    contingency flows like PayPal wallet, 3DS."""

    cancel_url: Optional[str] = UNSET
    """The URL where the customer is redirected after customer cancels or leaves the flow. It is a required field for
    contingency flows like PayPal wallet, 3DS."""

    shipping_preference: Optional[ExperienceContextShippingPreferenceOrStr] = UNSET
    """The shipping preference. This only applies to PayPal payment source."""

    vault_instruction: Optional[VaultInstructionActionOrStr] = UNSET
    """DEPRECATED. Vault Instruction on action to be performed after a successful payer approval."""

    app_switch_context: Optional[AppSwitchContext] = UNSET
    """Merchant provided details of the native app or mobile web browser to facilitate buyer's app switch to the PayPal
    consumer app."""

    user_action: Optional[VaultUserActionOrStr] = UNSET
    """User Action on action to be performed after a successful payer approval."""


class VaultExperienceContextDict(TypedDict):
    brand_name: NotRequired[str]
    locale: NotRequired[str]
    return_url: NotRequired[str]
    cancel_url: NotRequired[str]
    shipping_preference: NotRequired[ExperienceContextShippingPreferenceOrStr]
    vault_instruction: NotRequired[VaultInstructionActionOrStr]
    app_switch_context: NotRequired[AppSwitchContext | AppSwitchContextDict]
    user_action: NotRequired[VaultUserActionOrStr]
