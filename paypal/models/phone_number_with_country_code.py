from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PhoneNumberWithCountryCode(SdkBaseModel):
    """The phone number in its canonical international `E.164 numbering plan format
    <https://www.itu.int/rec/T-REC-E.164/en>`__., The phone number, in its canonical international `E.164 numbering plan
    format <https://www.itu.int/rec/T-REC-E.164/en>`__., The phone number, in its canonical international `E.164
    numbering plan format <https://www.itu.int/rec/T-REC-E.164/en>`__."""

    country_code: str
    """The country calling code (CC), in its canonical international `E.164 numbering plan format
    <https://www.itu.int/rec/T-REC-E.164/en>`__. The combined length of the CC and the national number must not be
    greater than 15 digits. The national number consists of a national destination code (NDC) and subscriber number
    (SN)."""

    national_number: str
    """The national number, in its canonical international `E.164 numbering plan format
    <https://www.itu.int/rec/T-REC-E.164/en>`__. The combined length of the country calling code (CC) and the national
    number must not be greater than 15 digits. The national number consists of a national destination code (NDC) and
    subscriber number (SN)."""


class PhoneNumberWithCountryCodeDict(TypedDict):
    country_code: str
    national_number: str
