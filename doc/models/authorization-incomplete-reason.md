
# Authorization Incomplete Reason

The reason why the authorized status is `PENDING`.

*This model accepts additional fields of type Any.*

## Enumeration

`AuthorizationIncompleteReason`

## Fields

| Name | Description |
|  --- | --- |
| `PENDING_REVIEW` | Authorization is pending manual review. |
| `DECLINED_BY_RISK_FRAUD_FILTERS` | Risk Filter set by the payee failed for the transaction. |

## Example

```python
from paypal.models.authorization_incomplete_reason import AuthorizationIncompleteReason

authorization_incomplete_reason = AuthorizationIncompleteReason.PENDING_REVIEW
```

