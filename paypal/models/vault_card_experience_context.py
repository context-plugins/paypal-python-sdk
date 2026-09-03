from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.vault_instruction_action import VaultInstructionActionOrStr
from .enums.vault_user_action import VaultUserActionOrStr


class VaultCardExperienceContext(SdkBaseModel):
    """A resource representing an experience context of vault a card."""

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

    vault_instruction: Optional[VaultInstructionActionOrStr] = UNSET
    """DEPRECATED. Vault Instruction on action to be performed after a successful payer approval."""

    user_action: Optional[VaultUserActionOrStr] = UNSET
    """User Action on action to be performed after a successful payer approval."""


class VaultCardExperienceContextDict(TypedDict):
    brand_name: NotRequired[str]
    locale: NotRequired[str]
    return_url: NotRequired[str]
    cancel_url: NotRequired[str]
    vault_instruction: NotRequired[VaultInstructionActionOrStr]
    user_action: NotRequired[VaultUserActionOrStr]
