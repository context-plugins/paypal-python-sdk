
# Callback Configuration

CallBack Configuration that the merchant can provide to PayPal/Venmo.

*This model accepts additional fields of type Any.*

## Structure

`CallbackConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `callback_events` | [`List[CallbackEvents]`](../../doc/models/callback-events.md) | Required | An array of callback events merchant can subscribe to for the corresponding callback url.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `5`, *Unique Items Required*, *Minimum Length*: `1`, *Maximum Length*: `256`, *Pattern*: `^[0-9A-Z_]+$` |
| `callback_url` | `str` | Required | Merchant provided CallBack url.PayPal/Venmo will use this url to call the merchant back when the events occur .PayPal/Venmo expects a secured url usually in the https format.merchant can append the cart id or other params part of the url as query or path params.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `2040`, *Pattern*: `^.*$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.callback_configuration import CallbackConfiguration
from paypal.models.callback_events import CallbackEvents

callback_configuration = CallbackConfiguration(
    callback_events=[
        CallbackEvents.SHIPPING_OPTIONS,
        CallbackEvents.SHIPPING_ADDRESS,
        CallbackEvents.SHIPPING_OPTIONS
    ],
    callback_url='callback_url4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

