
# Authorization Status with Details

The status fields and status details for an authorized payment.

*This model accepts additional fields of type Any.*

## Structure

`AuthorizationStatusWithDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`AuthorizationStatus`](../../doc/models/authorization-status.md) | Optional, Read-only | The status for the authorized payment. |
| `status_details` | [`AuthorizationStatusDetails`](../../doc/models/authorization-status-details.md) | Optional | The details of the authorized payment status. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.authorization_incomplete_reason import AuthorizationIncompleteReason
from paypal.models.authorization_status import AuthorizationStatus
from paypal.models.authorization_status_details import AuthorizationStatusDetails
from paypal.models.authorization_status_with_details import AuthorizationStatusWithDetails

authorization_status_with_details = AuthorizationStatusWithDetails(
    status=AuthorizationStatus.DENIED,
    status_details=AuthorizationStatusDetails(
        reason=AuthorizationIncompleteReason.PENDING_REVIEW,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

