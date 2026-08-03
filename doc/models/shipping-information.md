
# Shipping Information

The shipping information.

*This model accepts additional fields of type Any.*

## Structure

`ShippingInformation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | The recipient's name.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9_'\-., ":;\!?]*$` |
| `method` | `str` | Optional | The shipping method that is associated with this order.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9_'\-., ":;\!?]*$` |
| `address` | [`SimplePostalAddressCoarseGrained`](../../doc/models/simple-postal-address-coarse-grained.md) | Optional | A simple postal address with coarse-grained fields. Do not use for an international address. Use for backward compatibility only. Does not contain phone. |
| `secondary_shipping_address` | [`SimplePostalAddressCoarseGrained`](../../doc/models/simple-postal-address-coarse-grained.md) | Optional | A simple postal address with coarse-grained fields. Do not use for an international address. Use for backward compatibility only. Does not contain phone. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.shipping_information import ShippingInformation
from paypal.models.simple_postal_address_coarse_grained import SimplePostalAddressCoarseGrained

shipping_information = ShippingInformation(
    name='name4',
    method='method8',
    address=SimplePostalAddressCoarseGrained(
        line_1='line18',
        city='city6',
        country_code='country_code6',
        line_2='line20',
        state='state2',
        postal_code='postal_code8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    secondary_shipping_address=SimplePostalAddressCoarseGrained(
        line_1='line16',
        city='city4',
        country_code='country_code4',
        line_2='line28',
        state='state0',
        postal_code='postal_code6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

