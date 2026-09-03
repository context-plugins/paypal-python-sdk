from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderApplicationContextLandingPage(str, Enum):
    """DEPRECATED. DEPRECATED. The type of landing page to show on the PayPal site for customer checkout. The fields in
    ``application_context`` are now available in the ``experience_context`` object under the ``payment_source`` which
    supports them (eg. ``payment_source.paypal.experience_context.landing_page``). Please specify this field in the
    ``experience_context`` object instead of the ``application_context`` object."""

    LOGIN = "LOGIN"
    """When the customer clicks PayPal Checkout, the customer is redirected to a page to log in to PayPal and approve
    the payment."""

    BILLING = "BILLING"
    """When the customer clicks PayPal Checkout, the customer is redirected to a page to enter credit or debit card and
    other relevant billing information required to complete the purchase."""

    NO_PREFERENCE = "NO_PREFERENCE"
    """When the customer clicks PayPal Checkout, the customer is redirected to either a page to log in to PayPal and
    approve the payment or to a page to enter credit or debit card and other relevant billing information required to
    complete the purchase, depending on their previous interaction with PayPal."""

    __str__ = str.__str__


OrderApplicationContextLandingPageOrStr: TypeAlias = Annotated[
    OrderApplicationContextLandingPage | str, open_enum_validator(OrderApplicationContextLandingPage)
]
