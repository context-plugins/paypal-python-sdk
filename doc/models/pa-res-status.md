
# Pa Res Status

Transactions status result identifier. The outcome of the issuer's authentication.

*This model accepts additional fields of type Any.*

## Enumeration

`PaResStatus`

## Fields

| Name | Description |
|  --- | --- |
| `SUCCESSFULAUTHENTICATION` | Successful authentication. |
| `FAILEDAUTHENTICATION` | Failed authentication / account not verified / transaction denied. |
| `UNABLETOCOMPLETEAUTHENTICATION` | Unable to complete authentication. |
| `SUCCESSFULATTEMPTSTRANSACTION` | Successful attempts transaction. |
| `CHALLENGEREQUIRED` | Challenge required for authentication. |
| `AUTHENTICATIONREJECTED` | Authentication rejected (merchant must not submit for authorization). |
| `DECOUPLEDAUTHENTICATION` | Challenge required; decoupled authentication confirmed. |
| `INFORMATIONALONLY` | Informational only; 3DS requestor challenge preference acknowledged. |

## Example

```python
from paypal.models.pa_res_status import PaResStatus

pa_res_status = PaResStatus.DECOUPLEDAUTHENTICATION
```

