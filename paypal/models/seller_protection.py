from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.dispute_category import DisputeCategoryOrStr
from .enums.seller_protection_status import SellerProtectionStatusOrStr


class SellerProtection(SdkBaseModel):
    """The level of protection offered as defined by `PayPal Seller Protection for Merchants
    <https://www.paypal.com/us/webapps/mpp/security/seller-protection>`__."""

    status: Optional[SellerProtectionStatusOrStr] = UNSET
    """Indicates whether the transaction is eligible for seller protection. For information, see `PayPal Seller
    Protection for Merchants <https://www.paypal.com/us/webapps/mpp/security/seller-protection>`__."""

    dispute_categories: Optional[list[DisputeCategoryOrStr]] = UNSET
    """An array of conditions that are covered for the transaction."""


class SellerProtectionDict(TypedDict):
    status: NotRequired[SellerProtectionStatusOrStr]
    dispute_categories: NotRequired[list[DisputeCategoryOrStr]]
