from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .stored_payment_source import StoredPaymentSource, StoredPaymentSourceDict


class OrderConfirmApplicationContext(SdkBaseModel):
    """Customizes the payer confirmation experience."""

    brand_name: Optional[str] = UNSET
    """Label to present to your payer as part of the PayPal hosted web experience."""

    locale: Optional[str] = UNSET
    """The `language tag <https://tools.ietf.org/html/bcp47#section-2>`__ for the language in which to localize the
    error-related strings, such as messages, issues, and suggested actions. The tag is made up of the `ISO 639-2
    language code <https://www.loc.gov/standards/iso639-2/php/code_list.php>`__, the optional `ISO-15924 script tag
    <https://www.unicode.org/iso15924/codelists.html>`__, and the `ISO-3166 alpha-2 country code
    <https://developer.paypal.com/api/rest/reference/country-codes/>`__ or `M49 region code
    <https://unstats.un.org/unsd/methodology/m49/>`__."""

    return_url: Optional[str] = UNSET
    """The URL where the customer is redirected after the customer approves the payment."""

    cancel_url: Optional[str] = UNSET
    """The URL where the customer is redirected after the customer cancels the payment."""

    stored_payment_source: Optional[StoredPaymentSource] = UNSET
    """Provides additional details to process a payment using a ``payment_source`` that has been stored or is intended
    to be stored (also referred to as stored_credential or card-on-file). Parameter compatibility:
    ``payment_type=ONE_TIME`` is compatible only with ``payment_initiator=CUSTOMER``. ``usage=FIRST`` is compatible only
    with ``payment_initiator=CUSTOMER``. ``previous_transaction_reference`` or
    ``previous_network_transaction_reference`` is compatible only with ``payment_initiator=MERCHANT``. Only one of the
    parameters - ``previous_transaction_reference`` and ``previous_network_transaction_reference`` - can be present in
    the request."""


class OrderConfirmApplicationContextDict(TypedDict):
    brand_name: NotRequired[str]
    locale: NotRequired[str]
    return_url: NotRequired[str]
    cancel_url: NotRequired[str]
    stored_payment_source: NotRequired[StoredPaymentSource | StoredPaymentSourceDict]
