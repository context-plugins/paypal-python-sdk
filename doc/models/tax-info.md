
# Tax Info

The tax ID of the customer. The customer is also known as the payer. Both `tax_id` and `tax_id_type` are required.

*This model accepts additional fields of type Any.*

## Structure

`TaxInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tax_id` | `str` | Required | The customer's tax ID value.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `14`, *Pattern*: `([a-zA-Z0-9])` |
| `tax_id_type` | [`TaxIdType`](../../doc/models/tax-id-type.md) | Required | The customer's tax ID type.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `14`, *Pattern*: `^[A-Z0-9_]+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.tax_id_type import TaxIdType
from paypal.models.tax_info import TaxInfo

tax_info = TaxInfo(
    tax_id='tax_id4',
    tax_id_type=TaxIdType.BR_CPF,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

