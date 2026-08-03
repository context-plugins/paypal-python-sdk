
# Checkout Option

A checkout option as a name-and-value pair.

*This model accepts additional fields of type Any.*

## Structure

`CheckoutOption`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_option_name` | `str` | Optional | The checkout option name, such as `color` or `texture`.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `200`, *Pattern*: `^[a-zA-Z0-9_'\-., ":;\!?]*$` |
| `checkout_option_value` | `str` | Optional | The checkout option value. For example, the checkout option `color` might be `blue` or `red` while the checkout option `texture` might be `smooth` or `rippled`.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `200`, *Pattern*: `^[a-zA-Z0-9_'\-., ":;\!?]*$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.checkout_option import CheckoutOption

checkout_option = CheckoutOption(
    checkout_option_name='checkout_option_name6',
    checkout_option_value='checkout_option_value2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

