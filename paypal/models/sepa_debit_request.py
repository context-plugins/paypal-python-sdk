from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sepa_debit_experience_context import SepaDebitExperienceContext, SepaDebitExperienceContextDict


class SepaDebitRequest(SdkBaseModel):
    """An API resource denoting a request to securely store a SEPA Debit."""

    experience_context: Optional[SepaDebitExperienceContext] = UNSET
    """Customizes the payer experience during the approval process for the SEPA Debit payment."""


class SepaDebitRequestDict(TypedDict):
    experience_context: NotRequired[SepaDebitExperienceContext | SepaDebitExperienceContextDict]
