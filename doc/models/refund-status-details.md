
# Refund Status Details

The details of the refund status.

*This model accepts additional fields of type Any.*

## Structure

`RefundStatusDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | [`RefundIncompleteReason`](../../doc/models/refund-incomplete-reason.md) | Optional | The reason why the refund has the `PENDING` or `FAILED` status. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.refund_incomplete_reason import RefundIncompleteReason
from paypal.models.refund_status_details import RefundStatusDetails

refund_status_details = RefundStatusDetails(
    reason=RefundIncompleteReason.ECHECK,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

