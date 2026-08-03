
# Blik One Click Payment Object

Information used to pay using BLIK one-click flow.

*This model accepts additional fields of type Any.*

## Structure

`BlikOneClickPaymentObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `consumer_reference` | `str` | Optional | The merchant generated, unique reference serving as a primary identifier for accounts connected between Blik and a merchant.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `64`, *Pattern*: `^[ -~]{3,64}$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.blik_one_click_payment_object import BlikOneClickPaymentObject

blik_one_click_payment_object = BlikOneClickPaymentObject(
    consumer_reference='consumer_reference2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

