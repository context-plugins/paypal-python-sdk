from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer_response import CustomerResponse, CustomerResponseDict
from .link_description import LinkDescription, LinkDescriptionDict
from .payment_token_response_payment_source import (
    PaymentTokenResponsePaymentSource,
    PaymentTokenResponsePaymentSourceDict,
)


class PaymentTokenResponse(SdkBaseModel):
    """Full representation of a saved payment token."""

    id: Optional[str] = UNSET
    """The PayPal-generated ID for the vaulted payment source. This ID should be stored on the merchant's server so the
    saved payment source can be used for future transactions."""

    customer: Optional[CustomerResponse] = UNSET
    """Customer in merchant's or partner's system of records."""

    payment_source: Optional[PaymentTokenResponsePaymentSource] = UNSET
    """The vaulted payment method details."""

    links: Optional[list[LinkDescription]] = UNSET
    """An array of related `HATEOAS links <https://developer.paypal.com/api/rest/responses/#hateoas>`__."""


class PaymentTokenResponseDict(TypedDict):
    id: NotRequired[str]
    customer: NotRequired[CustomerResponse | CustomerResponseDict]
    payment_source: NotRequired[PaymentTokenResponsePaymentSource | PaymentTokenResponsePaymentSourceDict]
    links: NotRequired[list[LinkDescription | LinkDescriptionDict]]
