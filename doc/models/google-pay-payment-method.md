
# Google Pay Payment Method

The type of the payment credential. Currently, only CARD is supported.

*This model accepts additional fields of type Any.*

## Enumeration

`GooglePayPaymentMethod`

## Fields

| Name | Description |
|  --- | --- |
| `CARD` | CARD is the only value that Google Pay accepts. |

## Example

```python
from paypal.models.google_pay_payment_method import GooglePayPaymentMethod

google_pay_payment_method = GooglePayPaymentMethod.CARD
```

