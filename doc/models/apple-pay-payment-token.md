
# Apple Pay Payment Token

A resource representing a response for Apple Pay.

*This model accepts additional fields of type Any.*

## Structure

`ApplePayPaymentToken`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card` | [`ApplePayCard`](../../doc/models/apple-pay-card.md) | Optional | The payment card to be used to fund a payment. Can be a credit or debit card. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.address import Address
from paypal.models.apple_pay_card import ApplePayCard
from paypal.models.apple_pay_payment_token import ApplePayPaymentToken
from paypal.models.card_brand import CardBrand
from paypal.models.card_type import CardType

apple_pay_payment_token = ApplePayPaymentToken(
    card=ApplePayCard(
        name='name6',
        last_digits='last_digits0',
        mtype=CardType.UNKNOWN,
        brand=CardBrand.CB_NATIONALE,
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
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

