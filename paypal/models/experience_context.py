from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.experience_context_shipping_preference import ExperienceContextShippingPreferenceOrStr


class ExperienceContext(SdkBaseModel):
    """Customizes the payer experience during the approval process for the payment."""

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

    shipping_preference: Optional[ExperienceContextShippingPreferenceOrStr] = UNSET
    """The location from which the shipping address is derived."""

    return_url: Optional[str] = UNSET
    """Describes the URL."""

    cancel_url: Optional[str] = UNSET
    """Describes the URL."""


class ExperienceContextDict(TypedDict):
    brand_name: NotRequired[str]
    locale: NotRequired[str]
    shipping_preference: NotRequired[ExperienceContextShippingPreferenceOrStr]
    return_url: NotRequired[str]
    cancel_url: NotRequired[str]
