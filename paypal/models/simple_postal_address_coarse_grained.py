from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SimplePostalAddressCoarseGrained(SdkBaseModel):
    """A simple postal address with coarse-grained fields. Do not use for an international address. Use for backward
    compatibility only. Does not contain phone."""

    line1: str
    """The first line of the address. For example, number or street."""

    line2: Optional[str] = UNSET
    """The second line of the address. For example, suite or apartment number."""

    city: str
    """The city name."""

    state: Optional[str] = UNSET
    """The `code </docs/api/reference/state-codes/>`__ for a US state or the equivalent for other countries. Required
    for transactions if the address is in one of these countries: `Argentina
    </docs/api/reference/state-codes/#argentina>`__, `Brazil </docs/api/reference/state-codes/#brazil>`__, `Canada
    </docs/api/reference/state-codes/#canada>`__, `China </docs/api/reference/state-codes/#china>`__, `India
    </docs/api/reference/state-codes/#india>`__, `Italy </docs/api/reference/state-codes/#italy>`__, `Japan
    </docs/api/reference/state-codes/#japan>`__, `Mexico </docs/api/reference/state-codes/#mexico>`__, `Thailand
    </docs/api/reference/state-codes/#thailand>`__, or `United States </docs/api/reference/state-codes/#usa>`__. Maximum
    length is 40 single-byte characters."""

    country_code: str
    """The `two-character ISO 3166-1 code </docs/integration/direct/rest/country-codes/>`__ that identifies the country
    or region. Note: The country code for Great Britain is GB and not UK as used in the top-level domain names for that
    country. Use the ``C2`` country code for China worldwide for comparable uncontrolled price (CUP) method, bank card,
    and cross-border transactions."""

    postal_code: Optional[str] = UNSET
    """The postal code, which is the zip code or equivalent. Typically required for countries with a postal code or an
    equivalent. See `postal code <https://en.wikipedia.org/wiki/Postal_code>`__."""


class SimplePostalAddressCoarseGrainedDict(TypedDict):
    line1: str
    line2: NotRequired[str]
    city: str
    state: NotRequired[str]
    country_code: str
    postal_code: NotRequired[str]
