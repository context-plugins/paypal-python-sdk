from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .participant_metadata import ParticipantMetadata, ParticipantMetadataDict


class RiskSupplementaryData(SdkBaseModel):
    """Additional information necessary to evaluate the risk profile of a transaction."""

    customer: Optional[ParticipantMetadata] = UNSET
    """Profile information of the sender or receiver."""


class RiskSupplementaryDataDict(TypedDict):
    customer: NotRequired[ParticipantMetadata | ParticipantMetadataDict]
