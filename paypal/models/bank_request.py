from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sepa_debit_request import SepaDebitRequest, SepaDebitRequestDict


class BankRequest(SdkBaseModel):
    """A Resource representing a request to vault a Bank used for ACH Debit."""

    ach_debit: Optional[Any] = UNSET
    """A Resource representing a request to vault a ACH Debit."""

    sepa_debit: Optional[SepaDebitRequest] = UNSET
    """An API resource denoting a request to securely store a SEPA Debit."""


class BankRequestDict(TypedDict):
    ach_debit: NotRequired[Any]
    sepa_debit: NotRequired[SepaDebitRequest | SepaDebitRequestDict]
