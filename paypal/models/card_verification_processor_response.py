from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.avs_code import AvsCodeOrStr
from .enums.cvv_code import CvvCodeOrStr


class CardVerificationProcessorResponse(SdkBaseModel):
    """The processor response information for payment requests, such as direct credit card transactions."""

    avs_code: Optional[AvsCodeOrStr] = UNSET
    """The address verification code for Visa, Discover, Mastercard, or American Express transactions."""

    cvv_code: Optional[CvvCodeOrStr] = UNSET
    """The card verification value code for for Visa, Discover, Mastercard, or American Express."""


class CardVerificationProcessorResponseDict(TypedDict):
    avs_code: NotRequired[AvsCodeOrStr]
    cvv_code: NotRequired[CvvCodeOrStr]
