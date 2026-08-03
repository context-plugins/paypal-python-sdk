
# Seller Protection

The level of protection offered as defined by [PayPal Seller Protection for Merchants](https://www.paypal.com/us/webapps/mpp/security/seller-protection).

*This model accepts additional fields of type Any.*

## Structure

`SellerProtection`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`SellerProtectionStatus`](../../doc/models/seller-protection-status.md) | Optional, Read-only | Indicates whether the transaction is eligible for seller protection. For information, see [PayPal Seller Protection for Merchants](https://www.paypal.com/us/webapps/mpp/security/seller-protection). |
| `dispute_categories` | [`List[DisputeCategory]`](../../doc/models/dispute-category.md) | Optional, Read-only | An array of conditions that are covered for the transaction. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.dispute_category import DisputeCategory
from paypal.models.seller_protection import SellerProtection
from paypal.models.seller_protection_status import SellerProtectionStatus

seller_protection = SellerProtection(
    status=SellerProtectionStatus.NOT_ELIGIBLE,
    dispute_categories=[
        DisputeCategory.ITEM_NOT_RECEIVED,
        DisputeCategory.UNAUTHORIZED_TRANSACTION
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

