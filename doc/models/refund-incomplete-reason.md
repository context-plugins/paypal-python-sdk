
# Refund Incomplete Reason

The reason why the refund has the `PENDING` or `FAILED` status.

*This model accepts additional fields of type Any.*

## Enumeration

`RefundIncompleteReason`

## Fields

| Name | Description |
|  --- | --- |
| `ECHECK` | The customer's account is funded through an eCheck, which has not yet cleared. |

## Example

```python
from paypal.models.refund_incomplete_reason import RefundIncompleteReason

refund_incomplete_reason = RefundIncompleteReason.ECHECK
```

