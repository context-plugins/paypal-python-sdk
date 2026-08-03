
# Card Authentication Response

Results of Authentication such as 3D Secure.

*This model accepts additional fields of type Any.*

## Structure

`CardAuthenticationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `three_d_secure` | [`ThreeDSecureCardAuthenticationResponse`](../../doc/models/three-d-secure-card-authentication-response.md) | Optional | Results of 3D Secure Authentication. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.card_authentication_response import CardAuthenticationResponse
from paypal.models.enrollment_status import EnrollmentStatus
from paypal.models.pa_res_status import PaResStatus
from paypal.models.three_d_secure_card_authentication_response import ThreeDSecureCardAuthenticationResponse

card_authentication_response = CardAuthenticationResponse(
    three_d_secure=ThreeDSecureCardAuthenticationResponse(
        authentication_status=PaResStatus.CHALLENGEREQUIRED,
        enrollment_status=EnrollmentStatus.ENROLLED,
        authentication_id='authentication_id6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

