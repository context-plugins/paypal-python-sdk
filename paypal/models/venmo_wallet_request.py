from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .venmo_wallet_additional_attributes import VenmoWalletAdditionalAttributes, VenmoWalletAdditionalAttributesDict
from .venmo_wallet_experience_context import VenmoWalletExperienceContext, VenmoWalletExperienceContextDict


class VenmoWalletRequest(SdkBaseModel):
    """Information needed to pay using Venmo."""

    vault_id: Optional[str] = UNSET
    """The PayPal-generated ID for the vaulted payment source. This ID should be stored on the merchant's server so the
    saved payment source can be used for future transactions."""

    email_address: Optional[str] = UNSET
    """The internationalized email address. Note: Up to 64 characters are allowed before and 255 characters are allowed
    after the @ sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern
    verifies that an unquoted @ sign exists."""

    experience_context: Optional[VenmoWalletExperienceContext] = UNSET
    """Customizes the buyer experience during the approval process for payment with Venmo. Note: Partners and
    Marketplaces might configure shipping_preference during partner account setup, which overrides the request
    values."""

    attributes: Optional[VenmoWalletAdditionalAttributes] = UNSET
    """Additional attributes associated with the use of this Venmo Wallet."""


class VenmoWalletRequestDict(TypedDict):
    vault_id: NotRequired[str]
    email_address: NotRequired[str]
    experience_context: NotRequired[VenmoWalletExperienceContext | VenmoWalletExperienceContextDict]
    attributes: NotRequired[VenmoWalletAdditionalAttributes | VenmoWalletAdditionalAttributesDict]
