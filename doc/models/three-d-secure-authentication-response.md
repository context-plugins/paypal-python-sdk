
# Three D Secure Authentication Response

Results of 3D Secure Authentication.

*This model accepts additional fields of type Any.*

## Structure

`ThreeDSecureAuthenticationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authentication_status` | [`PaResStatus`](../../doc/models/pa-res-status.md) | Optional | Transactions status result identifier. The outcome of the issuer's authentication.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `enrollment_status` | [`EnrollmentStatus`](../../doc/models/enrollment-status.md) | Optional | Status of Authentication eligibility.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.enrollment_status import EnrollmentStatus
from paypal.models.pa_res_status import PaResStatus
from paypal.models.three_d_secure_authentication_response import ThreeDSecureAuthenticationResponse

three_d_secure_authentication_response = ThreeDSecureAuthenticationResponse(
    authentication_status=PaResStatus.DECOUPLEDAUTHENTICATION,
    enrollment_status=EnrollmentStatus.UNAVAILABLE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

