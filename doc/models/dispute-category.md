
# Dispute Category

The condition that is covered for the transaction.

*This model accepts additional fields of type Any.*

## Enumeration

`DisputeCategory`

## Fields

| Name | Description |
|  --- | --- |
| `ITEM_NOT_RECEIVED` | The payer paid for an item that they did not receive. |
| `UNAUTHORIZED_TRANSACTION` | The payer did not authorize the payment. |

## Example

```python
from paypal.models.dispute_category import DisputeCategory

dispute_category = DisputeCategory.ITEM_NOT_RECEIVED
```

