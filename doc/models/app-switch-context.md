
# App Switch Context

Merchant provided details of the native app or mobile web browser to facilitate buyer's app switch to the PayPal consumer app.

*This model accepts additional fields of type Any.*

## Structure

`AppSwitchContext`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `native_app` | [`NativeAppContext`](../../doc/models/native-app-context.md) | Optional | Merchant provided, buyer's native app preferences to app switch to the PayPal consumer app. |
| `mobile_web` | [`MobileWebContext`](../../doc/models/mobile-web-context.md) | Optional | Buyer's mobile web browser context to app switch to the PayPal consumer app. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.app_switch_context import AppSwitchContext
from paypal.models.mobile_return_flow import MobileReturnFlow
from paypal.models.mobile_web_context import MobileWebContext
from paypal.models.native_app_context import NativeAppContext
from paypal.models.os_type import OsType

app_switch_context = AppSwitchContext(
    native_app=NativeAppContext(
        os_type=OsType.IOS,
        os_version='os_version0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    mobile_web=MobileWebContext(
        return_flow=MobileReturnFlow.AUTO,
        buyer_user_agent='buyer_user_agent8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

