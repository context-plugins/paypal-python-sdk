
# Authorization Status Details

The details of the authorized payment status.

*This model accepts additional fields of type Any.*

## Structure

`AuthorizationStatusDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | [`AuthorizationIncompleteReason`](../../doc/models/authorization-incomplete-reason.md) | Optional | The reason why the authorized status is `PENDING`.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `64`, *Pattern*: `^[A-Z_]+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.authorization_incomplete_reason import AuthorizationIncompleteReason
from paypal.models.authorization_status_details import AuthorizationStatusDetails

authorization_status_details = AuthorizationStatusDetails(
    reason=AuthorizationIncompleteReason.PENDING_REVIEW,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

