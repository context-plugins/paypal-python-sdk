
# Authentication Response

Results of Authentication such as 3D Secure.

*This model accepts additional fields of type Any.*

## Structure

`AuthenticationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `liability_shift` | [`LiabilityShiftIndicator`](../../doc/models/liability-shift-indicator.md) | Optional | Liability shift indicator. The outcome of the issuer's authentication.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `three_d_secure` | [`ThreeDSecureAuthenticationResponse`](../../doc/models/three-d-secure-authentication-response.md) | Optional | Results of 3D Secure Authentication. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.authentication_response import AuthenticationResponse
from paypal.models.enrollment_status import EnrollmentStatus
from paypal.models.liability_shift_indicator import LiabilityShiftIndicator
from paypal.models.pa_res_status import PaResStatus
from paypal.models.three_d_secure_authentication_response import ThreeDSecureAuthenticationResponse

authentication_response = AuthenticationResponse(
    liability_shift=LiabilityShiftIndicator.UNKNOWN,
    three_d_secure=ThreeDSecureAuthenticationResponse(
        authentication_status=PaResStatus.CHALLENGEREQUIRED,
        enrollment_status=EnrollmentStatus.ENROLLED,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

