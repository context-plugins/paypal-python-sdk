
# Payment Token Request Payment Source

The payment method to vault with the instrument details.

*This model accepts additional fields of type Any.*

## Structure

`PaymentTokenRequestPaymentSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card` | [`PaymentTokenRequestCard`](../../doc/models/payment-token-request-card.md) | Optional | A Resource representing a request to vault a Card. |
| `token` | [`VaultTokenRequest`](../../doc/models/vault-token-request.md) | Optional | The Tokenized Payment Source representing a Request to Vault a Token. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.card_brand import CardBrand
from paypal.models.payment_token_request_card import PaymentTokenRequestCard
from paypal.models.payment_token_request_payment_source import PaymentTokenRequestPaymentSource
from paypal.models.vault_token_request import VaultTokenRequest
from paypal.models.vault_token_request_type import VaultTokenRequestType

payment_token_request_payment_source = PaymentTokenRequestPaymentSource(
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
)
```

