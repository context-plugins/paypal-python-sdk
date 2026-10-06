from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.experience_context_shipping_preference import (
    ExperienceContextShippingPreference,
    ExperienceContextShippingPreferenceOrStr,
)
from .enums.vault_instruction_action import VaultInstructionActionOrStr
from .enums.vault_user_action import VaultUserAction, VaultUserActionOrStr


class VenmoExperienceContext(SdkBaseModel):
    """A resource representing an experience context of vault a venmo account."""

    brand_name: Optional[str] = UNSET
    """The label that overrides the business name in the PayPal account on the PayPal site. The pattern is defined by an
    external party and supports Unicode."""

    shipping_preference: ExperienceContextShippingPreferenceOrStr = ExperienceContextShippingPreference.GET_FROM_FILE
    """The shipping preference. This only applies to PayPal payment source."""

    vault_instruction: Optional[VaultInstructionActionOrStr] = UNSET
    """DEPRECATED. Vault Instruction on action to be performed after a successful payer approval."""

    user_action: VaultUserActionOrStr = VaultUserAction.CONTINUE
    """User Action on action to be performed after a successful payer approval."""


class VenmoExperienceContextDict(TypedDict):
    brand_name: NotRequired[str]
    shipping_preference: NotRequired[ExperienceContextShippingPreferenceOrStr]
    vault_instruction: NotRequired[VaultInstructionActionOrStr]
    user_action: NotRequired[VaultUserActionOrStr]
