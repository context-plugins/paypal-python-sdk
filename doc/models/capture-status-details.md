
# Capture Status Details

The details of the captured payment status.

*This model accepts additional fields of type Any.*

## Structure

`CaptureStatusDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | [`CaptureIncompleteReason`](../../doc/models/capture-incomplete-reason.md) | Optional | The reason why the captured payment status is `PENDING` or `DENIED`.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `64`, *Pattern*: `^[A-Z_]+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.capture_incomplete_reason import CaptureIncompleteReason
from paypal.models.capture_status_details import CaptureStatusDetails

capture_status_details = CaptureStatusDetails(
    reason=CaptureIncompleteReason.OTHER,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

