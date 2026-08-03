
# Pay Pal Reference Id Type

The PayPal reference ID type.

*This model accepts additional fields of type Any.*

## Enumeration

`PayPalReferenceIdType`

## Fields

| Name | Description |
|  --- | --- |
| `ODR` | An order ID. |
| `TXN` | A transaction ID. |
| `SUB` | A subscription ID. |
| `PAP` | A pre-approved payment ID. |

## Example

```python
from paypal.models.pay_pal_reference_id_type import PayPalReferenceIdType

pay_pal_reference_id_type = PayPalReferenceIdType.SUB
```

