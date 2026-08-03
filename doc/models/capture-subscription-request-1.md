
# Capture Subscription Request 1

The charge amount from the subscriber.

*This model accepts additional fields of type Any.*

## Structure

`CaptureSubscriptionRequest1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `note` | `str` | Required | The reason or note for the subscription charge.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `128`, *Pattern*: `^.*$` |
| `capture_type` | [`CaptureType`](../../doc/models/capture-type.md) | Required | The type of capture.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `24`, *Pattern*: `^[A-Z_]+$` |
| `amount` | [`Money`](../../doc/models/money.md) | Required | The currency and amount for a financial transaction, such as a balance or payment due. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.capture_subscription_request_1 import CaptureSubscriptionRequest1
from paypal.models.capture_type import CaptureType
from paypal.models.money import Money

capture_subscription_request_1 = CaptureSubscriptionRequest1(
    note='note8',
    capture_type=CaptureType.OUTSTANDING_BALANCE,
    amount=Money(
        currency_code='currency_code6',
        value='value0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

