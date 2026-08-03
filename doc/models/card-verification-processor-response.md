
# Card Verification Processor Response

The processor response information for payment requests, such as direct credit card transactions.

*This model accepts additional fields of type Any.*

## Structure

`CardVerificationProcessorResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `avs_code` | [`AvsCode`](../../doc/models/avs-code.md) | Optional, Read-only | The address verification code for Visa, Discover, Mastercard, or American Express transactions. |
| `cvv_code` | [`CvvCode`](../../doc/models/cvv-code.md) | Optional, Read-only | The card verification value code for for Visa, Discover, Mastercard, or American Express. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.avs_code import AvsCode
from paypal.models.card_verification_processor_response import CardVerificationProcessorResponse
from paypal.models.cvv_code import CvvCode

card_verification_processor_response = CardVerificationProcessorResponse(
    avs_code=AvsCode.AVS_S,
    cvv_code=CvvCode.CVV_E,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

