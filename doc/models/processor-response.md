
# Processor Response

The processor response information for payment requests, such as direct credit card transactions.

*This model accepts additional fields of type Any.*

## Structure

`ProcessorResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `avs_code` | [`AvsCode`](../../doc/models/avs-code.md) | Optional, Read-only | The address verification code for Visa, Discover, Mastercard, or American Express transactions. |
| `cvv_code` | [`CvvCode`](../../doc/models/cvv-code.md) | Optional, Read-only | The card verification value code for for Visa, Discover, Mastercard, or American Express. |
| `response_code` | [`ProcessorResponseCode`](../../doc/models/processor-response-code.md) | Optional, Read-only | Processor response code for the non-PayPal payment processor errors. |
| `payment_advice_code` | [`PaymentAdviceCode`](../../doc/models/payment-advice-code.md) | Optional, Read-only | The declined payment transactions might have payment advice codes. The card networks, like Visa and Mastercard, return payment advice codes. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.avs_code import AvsCode
from paypal.models.cvv_code import CvvCode
from paypal.models.payment_advice_code import PaymentAdviceCode
from paypal.models.processor_response import ProcessorResponse
from paypal.models.processor_response_code import ProcessorResponseCode

processor_response = ProcessorResponse(
    avs_code=AvsCode.AVS_3,
    cvv_code=CvvCode.CVV_3,
    response_code=ProcessorResponseCode.RESPONSE_PCNR,
    payment_advice_code=PaymentAdviceCode.PAYMENTADVICE_28,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

