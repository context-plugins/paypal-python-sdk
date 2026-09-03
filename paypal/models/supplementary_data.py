from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .card_supplementary_data import CardSupplementaryData, CardSupplementaryDataDict
from .risk_supplementary_data import RiskSupplementaryData, RiskSupplementaryDataDict


class SupplementaryData(SdkBaseModel):
    """Supplementary data about a payment. This object passes information that can be used to improve risk assessments
    and processing costs, for example, by providing Level 2 and Level 3 payment data."""

    card: Optional[CardSupplementaryData] = UNSET
    """Merchants and partners can add Level 2 and 3 data to payments to reduce risk and payment processing costs. For
    more information about processing payments, see checkout or multiparty checkout."""

    risk: Optional[RiskSupplementaryData] = UNSET
    """Additional information necessary to evaluate the risk profile of a transaction."""


class SupplementaryDataDict(TypedDict):
    card: NotRequired[CardSupplementaryData | CardSupplementaryDataDict]
    risk: NotRequired[RiskSupplementaryData | RiskSupplementaryDataDict]
