from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.payee_payment_method_preference import PayeePaymentMethodPreferenceOrStr


class PaymentMethod(SdkBaseModel):
    """The customer and merchant payment preferences."""

    payee_preferred: Optional[PayeePaymentMethodPreferenceOrStr] = UNSET
    """The merchant-preferred payment methods."""


class PaymentMethodDict(TypedDict):
    payee_preferred: NotRequired[PayeePaymentMethodPreferenceOrStr]
