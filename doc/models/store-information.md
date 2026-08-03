
# Store Information

The store information.

*This model accepts additional fields of type Any.*

## Structure

`StoreInformation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `store_id` | `str` | Optional | The ID of a store for a merchant in the system of record.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9]*$` |
| `terminal_id` | `str` | Optional | The terminal ID for the checkout stand in a merchant store.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `60`, *Pattern*: `^[a-zA-Z0-9]*$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.store_information import StoreInformation

store_information = StoreInformation(
    store_id='store_id6',
    terminal_id='terminal_id0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

