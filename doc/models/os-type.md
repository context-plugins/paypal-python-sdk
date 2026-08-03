
# Os Type

Operating System type of the device that the buyer is using.

*This model accepts additional fields of type Any.*

## Enumeration

`OsType`

## Fields

| Name | Description |
|  --- | --- |
| `ANDROID` | Google Android OS. |
| `IOS` | Apple OS typically found in Apple mobile devices. |
| `OTHER` | Any other OS type. |

## Example

```python
from paypal.models.os_type import OsType

os_type = OsType.IOS
```

