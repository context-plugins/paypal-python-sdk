
# Cancel Subscription Request

The cancel subscription request details., The suspend subscription request details.

*This model accepts additional fields of type Any.*

## Structure

`CancelSubscriptionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | `str` | Required | The reason for the cancellation of a subscription.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `128`, *Pattern*: `^.*$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.cancel_subscription_request import CancelSubscriptionRequest

cancel_subscription_request = CancelSubscriptionRequest(
    reason='reason8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

