
# Universal Product Code

The Universal Product Code of the item.

*This model accepts additional fields of type Any.*

## Structure

`UniversalProductCode`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`UpcType`](../../doc/models/upc-type.md) | Required | The Universal Product Code type.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `5`, *Pattern*: `^[0-9A-Z_-]+$` |
| `code` | `str` | Required | The UPC product code of the item.<br><br>**Constraints**: *Minimum Length*: `6`, *Maximum Length*: `17`, *Pattern*: `^[0-9]{0,17}$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.universal_product_code import UniversalProductCode
from paypal.models.upc_type import UpcType

universal_product_code = UniversalProductCode(
    mtype=UpcType.UPC_5,
    code='code2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

