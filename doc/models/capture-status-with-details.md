
# Capture Status with Details

The status and status details of a captured payment.

*This model accepts additional fields of type Any.*

## Structure

`CaptureStatusWithDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`CaptureStatus`](../../doc/models/capture-status.md) | Optional, Read-only | The status of the captured payment. |
| `status_details` | [`CaptureStatusDetails`](../../doc/models/capture-status-details.md) | Optional | The details of the captured payment status. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.capture_incomplete_reason import CaptureIncompleteReason
from paypal.models.capture_status import CaptureStatus
from paypal.models.capture_status_details import CaptureStatusDetails
from paypal.models.capture_status_with_details import CaptureStatusWithDetails

capture_status_with_details = CaptureStatusWithDetails(
    status=CaptureStatus.REFUNDED,
    status_details=CaptureStatusDetails(
        reason=CaptureIncompleteReason.VERIFICATION_REQUIRED,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

