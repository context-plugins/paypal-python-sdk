from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.payee_payment_method_preference import PayeePaymentMethodPreferenceOrStr
from .enums.standard_entry_class_code import StandardEntryClassCodeOrStr


class PaymentMethodPreference(SdkBaseModel):
    """The customer and merchant payment preferences."""

    payee_preferred: Optional[PayeePaymentMethodPreferenceOrStr] = UNSET
    """The merchant-preferred payment methods."""

    standard_entry_class_code: Optional[StandardEntryClassCodeOrStr] = UNSET
    """NACHA (the regulatory body governing the ACH network) requires that API callers (merchants, partners) obtain the
    consumer’s explicit authorization before initiating a transaction. To stay compliant, you’ll need to make sure that
    you retain a compliant authorization for each transaction that you originate to the ACH Network using this API. ACH
    transactions are categorized (using SEC codes) by how you capture authorization from the Receiver (the person whose
    bank account is being debited or credited). PayPal supports the following SEC codes."""


class PaymentMethodPreferenceDict(TypedDict):
    payee_preferred: NotRequired[PayeePaymentMethodPreferenceOrStr]
    standard_entry_class_code: NotRequired[StandardEntryClassCodeOrStr]
