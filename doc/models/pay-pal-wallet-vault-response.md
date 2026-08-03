
# Pay Pal Wallet Vault Response

The details about a saved PayPal Wallet payment source.

*This model accepts additional fields of type Any.*

## Structure

`PayPalWalletVaultResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The PayPal-generated ID for the saved payment source.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255` |
| `status` | [`PayPalWalletVaultStatus`](../../doc/models/pay-pal-wallet-vault-status.md) | Optional | The vault status.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `links` | [`List[LinkDescription]`](../../doc/models/link-description.md) | Optional, Read-only | An array of request-related HATEOAS links.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `10` |
| `customer` | [`PayPalWalletCustomer`](../../doc/models/pay-pal-wallet-customer.md) | Optional | The details about a customer in PayPal's system of record. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.link_description import LinkDescription
from paypal.models.link_http_method import LinkHttpMethod
from paypal.models.name import Name
from paypal.models.pay_pal_wallet_customer import PayPalWalletCustomer
from paypal.models.pay_pal_wallet_vault_response import PayPalWalletVaultResponse
from paypal.models.pay_pal_wallet_vault_status import PayPalWalletVaultStatus
from paypal.models.phone_number import PhoneNumber
from paypal.models.phone_type import PhoneType
from paypal.models.phone_with_type import PhoneWithType

pay_pal_wallet_vault_response = PayPalWalletVaultResponse(
    id='id0',
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
)
```

