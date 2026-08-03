
# Callback Events

CallBack event.

*This model accepts additional fields of type Any.*

## Enumeration

`CallbackEvents`

## Fields

| Name | Description |
|  --- | --- |
| `SHIPPING_ADDRESS` | When Buyer changes or selects the shipping address on the PayPal/Venmo buyer approval flow , PayPal/Venmo will call merchant with the callback URL to update order totals. |
| `SHIPPING_OPTIONS` | When Buyer changes or selects the shipping options on the PayPal/Venmo buyer approval flow , PayPal/Venmo will call merchant with the callback URL to update order totals. |

## Example

```python
from paypal.models.callback_events import CallbackEvents

callback_events = CallbackEvents.SHIPPING_ADDRESS
```

