
# Shipping Name

The name of the party.

*This model accepts additional fields of type Any.*

## Structure

`ShippingName`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `full_name` | `str` | Optional | When the party is a person, the party's full name.<br><br>**Constraints**: *Maximum Length*: `300` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.shipping_name import ShippingName

shipping_name = ShippingName(
    full_name='full_name6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

