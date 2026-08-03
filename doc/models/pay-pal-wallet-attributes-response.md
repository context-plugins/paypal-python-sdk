
# Pay Pal Wallet Attributes Response

Additional attributes associated with the use of a PayPal Wallet.

*This model accepts additional fields of type Any.*

## Structure

`PayPalWalletAttributesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vault` | [`PayPalWalletVaultResponse`](../../doc/models/pay-pal-wallet-vault-response.md) | Optional | The details about a saved PayPal Wallet payment source. |
| `cobranded_cards` | [`List[CobrandedCard]`](../../doc/models/cobranded-card.md) | Optional | An array of merchant cobranded cards used by buyer to complete an order. This array will be present if a merchant has onboarded their cobranded card with PayPal and provided corresponding label(s).<br><br>**Constraints**: *Minimum Items*: `0`, *Maximum Items*: `25` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.cobranded_card import CobrandedCard
from paypal.models.link_description import LinkDescription
from paypal.models.link_http_method import LinkHttpMethod
from paypal.models.money import Money
from paypal.models.name import Name
from paypal.models.pay_pal_wallet_attributes_response import PayPalWalletAttributesResponse
from paypal.models.pay_pal_wallet_customer import PayPalWalletCustomer
from paypal.models.pay_pal_wallet_vault_response import PayPalWalletVaultResponse
from paypal.models.pay_pal_wallet_vault_status import PayPalWalletVaultStatus
from paypal.models.payee_base import PayeeBase
from paypal.models.phone_number import PhoneNumber
from paypal.models.phone_type import PhoneType
from paypal.models.phone_with_type import PhoneWithType

pay_pal_wallet_attributes_response = PayPalWalletAttributesResponse(
    vault=PayPalWalletVaultResponse(
        id='id6',
        status=PayPalWalletVaultStatus.APPROVED,
        links=[
            LinkDescription(
                href='href6',
                rel='rel0',
                method=LinkHttpMethod.HEAD,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        customer=PayPalWalletCustomer(
            id='id0',
            email_address='email_address2',
            phone=PhoneWithType(
                phone_number=PhoneNumber(
                    national_number='national_number6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                phone_type=PhoneType.OTHER,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            name=Name(
                given_name='given_name2',
                surname='surname8',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            merchant_customer_id='merchant_customer_id2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    cobranded_cards=[
        CobrandedCard(
            labels=[
                'labels4',
                'labels3'
            ],
            payee=PayeeBase(
                email_address='email_address4',
                merchant_id='merchant_id6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            amount=Money(
                currency_code='currency_code6',
                value='value0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

