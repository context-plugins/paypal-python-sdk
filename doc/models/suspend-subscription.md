
# Suspend Subscription

The suspend subscription request details.

*This model accepts additional fields of type Any.*

## Structure

`SuspendSubscription`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | `str` | Required | The reason for suspension of the Subscription.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `128`, *Pattern*: `^.*$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.suspend_subscription import SuspendSubscription

suspend_subscription = SuspendSubscription(
    reason='reason2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

