
# Payment Token Request

Payment Token Request where the `source` defines the type of instrument to be stored.

*This model accepts additional fields of type Any.*

## Structure

`PaymentTokenRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer` | [`Customer`](../../doc/models/customer.md) | Optional | This object defines a customer in your system. Use it to manage customer profiles, save payment methods and contact details. |
| `payment_source` | [`PaymentTokenRequestPaymentSource`](../../doc/models/payment-token-request-payment-source.md) | Required | The payment method to vault with the instrument details. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.card_brand import CardBrand
from paypal.models.customer import Customer
from paypal.models.payment_token_request import PaymentTokenRequest
from paypal.models.payment_token_request_card import PaymentTokenRequestCard
from paypal.models.payment_token_request_payment_source import PaymentTokenRequestPaymentSource
from paypal.models.vault_token_request import VaultTokenRequest
from paypal.models.vault_token_request_type import VaultTokenRequestType

payment_token_request = PaymentTokenRequest(
    payment_source=PaymentTokenRequestPaymentSource(
        card=PaymentTokenRequestCard(
            name='name6',
            number='number6',
            expiry='expiry4',
            security_code='security_code8',
            brand=CardBrand.CB_NATIONALE,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        token=VaultTokenRequest(
            id='id6',
            mtype=VaultTokenRequestType.SETUP_TOKEN,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    customer=Customer(
        id='id0',
        merchant_customer_id='merchant_customer_id2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

