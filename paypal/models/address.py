from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Address(SdkBaseModel):
    """The portable international postal address. Maps to `AddressValidationMetadata
    <https://github.com/googlei18n/libaddressinput/wiki/AddressValidationMetadata>`__ and HTML 5.1 `Autofilling form
    controls: the autocomplete attribute
    <https://www.w3.org/TR/html51/sec-forms.html#autofilling-form-controls-the-autocomplete-attribute>`__."""

    address_line_1: Optional[str] = UNSET
    """The first line of the address, such as number and street, for example, ``173 Drury Lane``. Needed for data entry,
    and Compliance and Risk checks. This field needs to pass the full address."""

    address_line_2: Optional[str] = UNSET
    """The second line of the address, for example, a suite or apartment number."""

    admin_area_2: Optional[str] = UNSET
    """A city, town, or village. Smaller than ``admin_area_level_1``."""

    admin_area_1: Optional[str] = UNSET
    """The highest-level sub-division in a country, which is usually a province, state, or ISO-3166-2 subdivision. This
    data is formatted for postal delivery, for example, ``CA`` and not ``California``. Value, by country, is: UK. A
    county. US. A state. Canada. A province. Japan. A prefecture. Switzerland. A *kanton*."""

    postal_code: Optional[str] = UNSET
    """The postal code, which is the ZIP code or equivalent. Typically required for countries with a postal code or an
    equivalent. See `postal code <https://en.wikipedia.org/wiki/Postal_code>`__."""

    country_code: str
    """The `2-character ISO 3166-1 code <https://developer.paypal.com/api/rest/reference/country-codes/>`__ that
    identifies the country or region. Note: The country code for Great Britain is GB and not UK as used in the top-level
    domain names for that country. Use the ``C2`` country code for China worldwide for comparable uncontrolled price
    (CUP) method, bank card, and cross-border transactions."""


class AddressDict(TypedDict):
    address_line_1: NotRequired[str]
    address_line_2: NotRequired[str]
    admin_area_2: NotRequired[str]
    admin_area_1: NotRequired[str]
    postal_code: NotRequired[str]
    country_code: str
