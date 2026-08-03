
# Blik Level 0 Payment Object

Information used to pay using BLIK level_0 flow.

*This model accepts additional fields of type Any.*

## Structure

`BlikLevel0PaymentObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auth_code` | `str` | Required | The 6-digit code used to authenticate a consumer within BLIK.<br><br>**Constraints**: *Minimum Length*: `6`, *Maximum Length*: `6`, *Pattern*: `^[0-9]{6}$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.blik_level_0_payment_object import BlikLevel0PaymentObject

blik_level_0_payment_object = BlikLevel0PaymentObject(
    auth_code='auth_code8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

