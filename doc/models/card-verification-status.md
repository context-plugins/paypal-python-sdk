
# Card Verification Status

Verification status of Card.

*This model accepts additional fields of type Any.*

## Enumeration

`CardVerificationStatus`

## Fields

| Name | Description |
|  --- | --- |
| `VERIFIED` | Card has been verified |
| `FAILED` | Card verification has failed |

## Example

```python
from paypal.models.card_verification_status import CardVerificationStatus

card_verification_status = CardVerificationStatus.VERIFIED
```

