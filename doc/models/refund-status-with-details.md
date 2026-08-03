
# Refund Status with Details

The refund status with details.

*This model accepts additional fields of type Any.*

## Structure

`RefundStatusWithDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`RefundStatus`](../../doc/models/refund-status.md) | Optional, Read-only | The status of the refund. |
| `status_details` | [`RefundStatusDetails`](../../doc/models/refund-status-details.md) | Optional | The details of the refund status. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.refund_incomplete_reason import RefundIncompleteReason
from paypal.models.refund_status import RefundStatus
from paypal.models.refund_status_details import RefundStatusDetails
from paypal.models.refund_status_with_details import RefundStatusWithDetails

refund_status_with_details = RefundStatusWithDetails(
    status=RefundStatus.PENDING,
    status_details=RefundStatusDetails(
        reason=RefundIncompleteReason.ECHECK,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

