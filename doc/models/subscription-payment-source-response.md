
# Subscription Payment Source Response

The payment source used to fund the payment.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionPaymentSourceResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card` | [`CardResponseWithBillingAddress`](../../doc/models/card-response-with-billing-address.md) | Optional | The payment card used to fund the payment. Card can be a credit or debit card. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.address import Address
from paypal.models.card_response_with_billing_address import CardResponseWithBillingAddress
from paypal.models.subscription_payment_source_response import SubscriptionPaymentSourceResponse

subscription_payment_source_response = SubscriptionPaymentSourceResponse(
    card=CardResponseWithBillingAddress(
        name='name6',
        billing_address=Address(
            country_code='country_code8',
            address_line_1='address_line_12',
            address_line_2='address_line_28',
            admin_area_2='admin_area_28',
            admin_area_1='admin_area_14',
            postal_code='postal_code0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        expiry='expiry4',
        currency_code='currency_code2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

