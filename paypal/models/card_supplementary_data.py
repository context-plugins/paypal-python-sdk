from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .level2_card_processing_data import Level2CardProcessingData, Level2CardProcessingDataDict
from .level3_card_processing_data import Level3CardProcessingData, Level3CardProcessingDataDict


class CardSupplementaryData(SdkBaseModel):
    """Merchants and partners can add Level 2 and 3 data to payments to reduce risk and payment processing costs. For
    more information about processing payments, see checkout or multiparty checkout."""

    level_2: Optional[Level2CardProcessingData] = UNSET
    """The level 2 card processing data collections. If your merchant account has been configured for Level 2 processing
    this field will be passed to the processor on your behalf. Please contact your PayPal Technical Account Manager to
    define level 2 data for your business."""

    level_3: Optional[Level3CardProcessingData] = UNSET
    """The level 3 card processing data collections, If your merchant account has been configured for Level 3 processing
    this field will be passed to the processor on your behalf. Please contact your PayPal Technical Account Manager to
    define level 3 data for your business."""


class CardSupplementaryDataDict(TypedDict):
    level_2: NotRequired[Level2CardProcessingData | Level2CardProcessingDataDict]
    level_3: NotRequired[Level3CardProcessingData | Level3CardProcessingDataDict]
