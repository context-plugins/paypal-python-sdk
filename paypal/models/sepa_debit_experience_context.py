from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SepaDebitExperienceContext(SdkBaseModel):
    """Customizes the payer experience during the approval process for the SEPA Debit payment."""

    locale: Optional[str] = UNSET
    """The `language tag <https://tools.ietf.org/html/bcp47#section-2>`__ for the language in which to localize the
    error-related strings, such as messages, issues, and suggested actions. The tag is made up of the `ISO 639-2
    language code <https://www.loc.gov/standards/iso639-2/php/code_list.php>`__, the optional `ISO-15924 script tag
    <https://www.unicode.org/iso15924/codelists.html>`__, and the `ISO-3166 alpha-2 country code
    <https://developer.paypal.com/api/rest/reference/country-codes/>`__ or `M49 region code
    <https://unstats.un.org/unsd/methodology/m49/>`__."""

    return_url: str
    """Describes the URL."""

    cancel_url: str
    """Describes the URL."""


class SepaDebitExperienceContextDict(TypedDict):
    locale: NotRequired[str]
    return_url: str
    cancel_url: str
