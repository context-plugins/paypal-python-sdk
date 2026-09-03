from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer import Customer, CustomerDict
from .enums.payment_token_status import PaymentTokenStatusOrStr
from .link_description import LinkDescription, LinkDescriptionDict
from .setup_token_response_payment_source import SetupTokenResponsePaymentSource, SetupTokenResponsePaymentSourceDict


class SetupTokenResponse(SdkBaseModel):
    """Minimal representation of a cached setup token."""

    id: Optional[str] = UNSET
    """The PayPal-generated ID for the vaulted payment source. This ID should be stored on the merchant's server so the
    saved payment source can be used for future transactions."""

    customer: Optional[Customer] = UNSET
    """This object defines a customer in your system. Use it to manage customer profiles, save payment methods and
    contact details."""

    status: Optional[PaymentTokenStatusOrStr] = UNSET
    """The status of the payment token."""

    payment_source: Optional[SetupTokenResponsePaymentSource] = UNSET
    """The setup payment method details."""

    links: Optional[list[LinkDescription]] = UNSET
    """An array of related `HATEOAS links <https://developer.paypal.com/api/rest/responses/#hateoas>`__."""


class SetupTokenResponseDict(TypedDict):
    id: NotRequired[str]
    customer: NotRequired[Customer | CustomerDict]
    status: NotRequired[PaymentTokenStatusOrStr]
    payment_source: NotRequired[SetupTokenResponsePaymentSource | SetupTokenResponsePaymentSourceDict]
    links: NotRequired[list[LinkDescription | LinkDescriptionDict]]
