from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VenmoVaultResponseStatus(str, Enum):
    """The vault status."""

    VAULTED = "VAULTED"
    """The payment source has been saved in your customer's vault. This vault status reflects ``/v3/vault`` status."""

    CREATED = "CREATED"
    """DEPRECATED. The payment source has been saved in your customer's vault. This status applies to deprecated
    integration patterns and will not be returned for v3/vault integrations."""

    APPROVED = "APPROVED"
    """Customer has approved the action of saving the specified payment_source into their vault. Use
    v3/vault/payment-tokens with given setup_token to save the payment source in the vault"""

    __str__ = str.__str__


VenmoVaultResponseStatusOrStr: TypeAlias = Annotated[
    VenmoVaultResponseStatus | str, open_enum_validator(VenmoVaultResponseStatus)
]
