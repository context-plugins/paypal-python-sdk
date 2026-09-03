from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.tax_id_type import TaxIdTypeOrStr


class TaxInfo(SdkBaseModel):
    """The tax ID of the customer. The customer is also known as the payer. Both ``tax_id`` and ``tax_id_type`` are
    required."""

    tax_id: str
    """The customer's tax ID value."""

    tax_id_type: TaxIdTypeOrStr
    """The customer's tax ID type."""


class TaxInfoDict(TypedDict):
    tax_id: str
    tax_id_type: TaxIdTypeOrStr
