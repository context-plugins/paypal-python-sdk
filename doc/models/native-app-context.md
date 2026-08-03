
# Native App Context

Merchant provided, buyer's native app preferences to app switch to the PayPal consumer app.

*This model accepts additional fields of type Any.*

## Structure

`NativeAppContext`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `os_type` | [`OsType`](../../doc/models/os-type.md) | Optional, Read-only | Operating System type of the device that the buyer is using.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `7`, *Pattern*: `^[A-Z_]+$` |
| `os_version` | `str` | Optional, Read-only | Operating System version of the device that the buyer is using.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `64`, *Pattern*: `^.*$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.native_app_context import NativeAppContext
from paypal.models.os_type import OsType

native_app_context = NativeAppContext(
    os_type=OsType.IOS,
    os_version='os_version6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

