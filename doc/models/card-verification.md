
# Card Verification

The API caller can opt in to verify the card through PayPal offered verification services (e.g. Smart Dollar Auth, 3DS).

*This model accepts additional fields of type Any.*

## Structure

`CardVerification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `method` | [`SubscriptionCardVerificationMethod`](../../doc/models/subscription-card-verification-method.md) | Optional | The method used for card verification.<br><br>**Default**: `"SCA_WHEN_REQUIRED"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.card_verification import CardVerification
from paypal.models.subscription_card_verification_method import SubscriptionCardVerificationMethod

card_verification = CardVerification(
    method=SubscriptionCardVerificationMethod.SCA_WHEN_REQUIRED,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

