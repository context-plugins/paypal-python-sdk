
# Phone with Type

The phone information.

*This model accepts additional fields of type Any.*

## Structure

`PhoneWithType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `phone_type` | [`PhoneType`](../../doc/models/phone-type.md) | Optional | The phone type. |
| `phone_number` | [`PhoneNumber`](../../doc/models/phone-number.md) | Required | The phone number, in its canonical international [E.164 numbering plan format](https://www.itu.int/rec/T-REC-E.164/en). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.phone_number import PhoneNumber
from paypal.models.phone_type import PhoneType
from paypal.models.phone_with_type import PhoneWithType

phone_with_type = PhoneWithType(
    phone_number=PhoneNumber(
        national_number='national_number6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    phone_type=PhoneType.PAGER,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

