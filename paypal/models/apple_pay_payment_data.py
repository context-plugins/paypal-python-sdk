from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ApplePayPaymentData(SdkBaseModel):
    """Information about the decrypted apple pay payment data for the token like cryptogram, eci indicator."""

    cryptogram: Optional[str] = UNSET
    """Online payment cryptogram, as defined by 3D Secure. The pattern is defined by an external party and supports
    Unicode."""

    eci_indicator: Optional[str] = UNSET
    """ECI indicator, as defined by 3- Secure. The pattern is defined by an external party and supports Unicode."""

    emv_data: Optional[str] = UNSET
    """Encoded Apple Pay EMV Payment Structure used for payments in China. The pattern is defined by an external party
    and supports Unicode."""

    pin: Optional[str] = UNSET
    """Bank Key encrypted Apple Pay PIN. The pattern is defined by an external party and supports Unicode."""


class ApplePayPaymentDataDict(TypedDict):
    cryptogram: NotRequired[str]
    eci_indicator: NotRequired[str]
    emv_data: NotRequired[str]
    pin: NotRequired[str]
