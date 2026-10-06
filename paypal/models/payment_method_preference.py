from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.payee_payment_method_preference import PayeePaymentMethodPreference, PayeePaymentMethodPreferenceOrStr
from .enums.standard_entry_class_code import StandardEntryClassCode, StandardEntryClassCodeOrStr


class PaymentMethodPreference(SdkBaseModel):
    """The customer and merchant payment preferences."""

    payee_preferred: PayeePaymentMethodPreferenceOrStr = PayeePaymentMethodPreference.UNRESTRICTED
    """The merchant-preferred payment methods."""

    standard_entry_class_code: StandardEntryClassCodeOrStr = StandardEntryClassCode.WEB
    """NACHA (the regulatory body governing the ACH network) requires that API callers (merchants, partners) obtain the
    consumer’s explicit authorization before initiating a transaction. To stay compliant, you’ll need to make sure that
    you retain a compliant authorization for each transaction that you originate to the ACH Network using this API. ACH
    transactions are categorized (using SEC codes) by how you capture authorization from the Receiver (the person whose
    bank account is being debited or credited). PayPal supports the following SEC codes."""


class PaymentMethodPreferenceDict(TypedDict):
    payee_preferred: NotRequired[PayeePaymentMethodPreferenceOrStr]
    standard_entry_class_code: NotRequired[StandardEntryClassCodeOrStr]
