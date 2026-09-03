from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ExperienceContextShippingPreference(str, Enum):
    """The location from which the shipping address is derived., The shipping preference. This only applies to PayPal
    payment source., The shipping preference. This only applies to PayPal payment source., The location from which the
    shipping address is derived."""

    GET_FROM_FILE = "GET_FROM_FILE"
    """Get the customer-provided shipping address on the PayPal site."""

    NO_SHIPPING = "NO_SHIPPING"
    """Redacts the shipping address from the PayPal site. Recommended for digital goods."""

    SET_PROVIDED_ADDRESS = "SET_PROVIDED_ADDRESS"
    """Merchant sends the shipping address using purchase_units.shipping.address. The customer cannot change this
    address on the PayPal site."""

    __str__ = str.__str__


ExperienceContextShippingPreferenceOrStr: TypeAlias = Annotated[
    ExperienceContextShippingPreference | str, open_enum_validator(ExperienceContextShippingPreference)
]
