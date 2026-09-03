from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .simple_postal_address_coarse_grained import SimplePostalAddressCoarseGrained, SimplePostalAddressCoarseGrainedDict


class ShippingInformation(SdkBaseModel):
    """The shipping information."""

    name: Optional[str] = UNSET
    """The recipient's name."""

    method: Optional[str] = UNSET
    """The shipping method that is associated with this order."""

    address: Optional[SimplePostalAddressCoarseGrained] = UNSET
    """A simple postal address with coarse-grained fields. Do not use for an international address. Use for backward
    compatibility only. Does not contain phone."""

    secondary_shipping_address: Optional[SimplePostalAddressCoarseGrained] = UNSET
    """A simple postal address with coarse-grained fields. Do not use for an international address. Use for backward
    compatibility only. Does not contain phone."""


class ShippingInformationDict(TypedDict):
    name: NotRequired[str]
    method: NotRequired[str]
    address: NotRequired[SimplePostalAddressCoarseGrained | SimplePostalAddressCoarseGrainedDict]
    secondary_shipping_address: NotRequired[SimplePostalAddressCoarseGrained | SimplePostalAddressCoarseGrainedDict]
