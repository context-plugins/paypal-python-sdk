
# Activate Subscription Request

The activate subscription request details.

*This model accepts additional fields of type Any.*

## Structure

`ActivateSubscriptionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | `str` | Optional | The reason for activation of a subscription. Required to reactivate the subscription.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `128`, *Pattern*: `^.*$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.activate_subscription_request import ActivateSubscriptionRequest

activate_subscription_request = ActivateSubscriptionRequest(
    reason='reason4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

