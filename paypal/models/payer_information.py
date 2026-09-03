from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payer_name import PayerName, PayerNameDict
from .phone import Phone, PhoneDict
from .simple_postal_address_coarse_grained import SimplePostalAddressCoarseGrained, SimplePostalAddressCoarseGrainedDict


class PayerInformation(SdkBaseModel):
    """The payer information."""

    account_id: Optional[str] = UNSET
    """The PayPal` customer account ID."""

    email_address: Optional[str] = UNSET
    """The internationalized email address. Note: Up to 64 characters are allowed before and 255 characters are allowed
    after the @ sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern
    verifies that an unquoted @ sign exists."""

    phone_number: Optional[Phone] = UNSET
    """The phone number, in its canonical international `E.164 numbering plan format
    <https://www.itu.int/rec/T-REC-E.164/en>`__."""

    address_status: Optional[str] = UNSET
    """The address status of the payer. Value is either: Y. Verified. N. Not verified."""

    payer_status: Optional[str] = UNSET
    """The status of the payer. Value is ``Y`` or ``N``."""

    payer_name: Optional[PayerName] = UNSET
    """The name of the party."""

    country_code: Optional[str] = UNSET
    """The `two-character ISO 3166-1 code </docs/integration/direct/rest/country-codes/>`__ that identifies the country
    or region. Note: The country code for Great Britain is GB and not UK as used in the top-level domain names for that
    country. Use the ``C2`` country code for China worldwide for comparable uncontrolled price (CUP) method, bank card,
    and cross-border transactions."""

    address: Optional[SimplePostalAddressCoarseGrained] = UNSET
    """A simple postal address with coarse-grained fields. Do not use for an international address. Use for backward
    compatibility only. Does not contain phone."""


class PayerInformationDict(TypedDict):
    account_id: NotRequired[str]
    email_address: NotRequired[str]
    phone_number: NotRequired[Phone | PhoneDict]
    address_status: NotRequired[str]
    payer_status: NotRequired[str]
    payer_name: NotRequired[PayerName | PayerNameDict]
    country_code: NotRequired[str]
    address: NotRequired[SimplePostalAddressCoarseGrained | SimplePostalAddressCoarseGrainedDict]
