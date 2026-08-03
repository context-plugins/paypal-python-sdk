
# Venmo Payment Token Usage Type

The usage type associated with the Venmo payment token.

*This model accepts additional fields of type Any.*

## Enumeration

`VenmoPaymentTokenUsageType`

## Fields

| Name | Description |
|  --- | --- |
| `MERCHANT` | The Venmo Payment Token will be used for future transaction directly with a merchant. |
| `PLATFORM` | The Venmo Payment Token will be used for future transaction on a platform. A platform is typically a marketplace or a channel that a payer can purchase goods and services from multiple merchants. |

## Example

```python
from paypal.models.venmo_payment_token_usage_type import VenmoPaymentTokenUsageType

venmo_payment_token_usage_type = VenmoPaymentTokenUsageType.MERCHANT
```

