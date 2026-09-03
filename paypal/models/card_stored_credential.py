from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.payment_initiator import PaymentInitiatorOrStr
from .enums.stored_payment_source_payment_type import StoredPaymentSourcePaymentTypeOrStr
from .enums.stored_payment_source_usage_type import StoredPaymentSourceUsageTypeOrStr
from .network_transaction import NetworkTransaction, NetworkTransactionDict


class CardStoredCredential(SdkBaseModel):
    """Provides additional details to process a payment using a ``card`` that has been stored or is intended to be
    stored (also referred to as stored_credential or card-on-file). Parameter compatibility: ``payment_type=ONE_TIME``
    is compatible only with ``payment_initiator=CUSTOMER``. ``usage=FIRST`` is compatible only with
    ``payment_initiator=CUSTOMER``. ``previous_transaction_reference`` or ``previous_network_transaction_reference`` is
    compatible only with ``payment_initiator=MERCHANT``. Only one of the parameters - ``previous_transaction_reference``
    and ``previous_network_transaction_reference`` - can be present in the request."""

    payment_initiator: PaymentInitiatorOrStr
    """The person or party who initiated or triggered the payment."""

    payment_type: StoredPaymentSourcePaymentTypeOrStr
    """Indicates the type of the stored payment_source payment."""

    usage: Optional[StoredPaymentSourceUsageTypeOrStr] = UNSET
    """Indicates if this is a ``first`` or ``subsequent`` payment using a stored payment source (also referred to as
    stored credential or card on file)."""

    previous_network_transaction_reference: Optional[NetworkTransaction] = UNSET
    """Reference values used by the card network to identify a transaction."""


class CardStoredCredentialDict(TypedDict):
    payment_initiator: PaymentInitiatorOrStr
    payment_type: StoredPaymentSourcePaymentTypeOrStr
    usage: NotRequired[StoredPaymentSourceUsageTypeOrStr]
    previous_network_transaction_reference: NotRequired[NetworkTransaction | NetworkTransactionDict]
