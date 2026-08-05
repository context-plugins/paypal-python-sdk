
# Merchant Preferences 1

The merchant preferences for a subscription.

## Structure

`MerchantPreferences1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `return_url` | `str` | Optional | The URL where the customer is redirected after the customer approves the payment.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `4000` |
| `cancel_url` | `str` | Optional | The URL where the customer is redirected after the customer cancels the payment.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `4000` |

## Example

```python
from paypalserversdk.models.merchant_preferences_1 import MerchantPreferences1

merchant_preferences_1 = MerchantPreferences1(
    return_url='return_url4',
    cancel_url='cancel_url6'
)
```

