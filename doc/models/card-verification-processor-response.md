
# Card Verification Processor Response

The processor response information for payment requests, such as direct credit card transactions.

## Structure

`CardVerificationProcessorResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `avs_code` | [`AvsCode`](../../doc/models/avs-code.md) | Optional, Read-only | The address verification code for Visa, Discover, Mastercard, or American Express transactions. |
| `cvv_code` | [`CvvCode`](../../doc/models/cvv-code.md) | Optional, Read-only | The card verification value code for for Visa, Discover, Mastercard, or American Express. |

## Example

```python
from paypalserversdk.models.avs_code import AvsCode
from paypalserversdk.models.card_verification_processor_response import CardVerificationProcessorResponse
from paypalserversdk.models.cvv_code import CvvCode

card_verification_processor_response = CardVerificationProcessorResponse(
    avs_code=AvsCode.AVS_S,
    cvv_code=CvvCode.CVV_E
)
```

