
# Pay Pal Payment Token Usage Type

The usage type associated with the PayPal payment token., The usage type associated with a digital wallet payment token., The usage type associated with a digital wallet payment token.

*This model accepts additional fields of type Any.*

## Enumeration

`PayPalPaymentTokenUsageType`

## Fields

| Name | Description |
|  --- | --- |
| `MERCHANT` | The PayPal Payment Token will be used for future transaction directly with a merchant. |
| `PLATFORM` | The PayPal Payment Token will be used for future transaction on a platform. A platform is typically a marketplace or a channel that a payer can purchase goods and services from multiple merchants. |

## Example

```python
from paypal.models.pay_pal_payment_token_usage_type import PayPalPaymentTokenUsageType

pay_pal_payment_token_usage_type = PayPalPaymentTokenUsageType.MERCHANT
```

