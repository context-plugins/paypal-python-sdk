
# Subscription Payment Source

The payment source definition. To be eligible to create subscription using debit or credit card, you will need to sign up here (https://www.paypal.com/bizsignup/entry/product/ppcp). Please note, its available only for non-3DS cards and for merchants in US and AU regions.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionPaymentSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card` | [`SubscriptionCardRequest`](../../doc/models/subscription-card-request.md) | Optional | The payment card to use to fund a payment. Can be a credit or debit card. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.card_type import CardType
from paypal.models.subscription_card_request import SubscriptionCardRequest
from paypal.models.subscription_payment_source import SubscriptionPaymentSource

subscription_payment_source = SubscriptionPaymentSource(
    card=SubscriptionCardRequest(
        name='name6',
        number='number6',
        expiry='expiry4',
        security_code='security_code8',
        mtype=CardType.UNKNOWN,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

