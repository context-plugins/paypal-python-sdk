from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer import Customer, CustomerDict
from .setup_token_request_payment_source import SetupTokenRequestPaymentSource, SetupTokenRequestPaymentSourceDict


class SetupTokenRequest(SdkBaseModel):
    """Setup Token Request where the ``source`` defines the type of instrument to be stored."""

    customer: Optional[Customer] = UNSET
    """This object defines a customer in your system. Use it to manage customer profiles, save payment methods and
    contact details."""

    payment_source: SetupTokenRequestPaymentSource
    """The payment method to vault with the instrument details."""


class SetupTokenRequestDict(TypedDict):
    customer: NotRequired[Customer | CustomerDict]
    payment_source: SetupTokenRequestPaymentSource | SetupTokenRequestPaymentSourceDict
