
# Refund Status

The status of the refund.

*This model accepts additional fields of type Any.*

## Enumeration

`RefundStatus`

## Fields

| Name | Description |
|  --- | --- |
| `CANCELLED` | The refund was cancelled. |
| `FAILED` | The refund could not be processed. |
| `PENDING` | The refund is pending. For more information, see status_details.reason. |
| `COMPLETED` | The funds for this transaction were debited to the customer's account. |

## Example

```python
from paypal.models.refund_status import RefundStatus

refund_status = RefundStatus.CANCELLED
```

