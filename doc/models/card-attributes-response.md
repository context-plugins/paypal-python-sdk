
# Card Attributes Response

Additional attributes associated with the use of this card.

*This model accepts additional fields of type Any.*

## Structure

`CardAttributesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vault` | [`CardVaultResponse`](../../doc/models/card-vault-response.md) | Optional | The details about a saved Card payment source. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.card_attributes_response import CardAttributesResponse
from paypal.models.card_customer_information import CardCustomerInformation
from paypal.models.card_vault_response import CardVaultResponse
from paypal.models.link_description import LinkDescription
from paypal.models.link_http_method import LinkHttpMethod
from paypal.models.name import Name
from paypal.models.phone_number import PhoneNumber
from paypal.models.phone_type import PhoneType
from paypal.models.phone_with_type import PhoneWithType
from paypal.models.vault_status import VaultStatus

card_attributes_response = CardAttributesResponse(
    vault=CardVaultResponse(
        id='id6',
        status=VaultStatus.APPROVED,
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
        customer=CardCustomerInformation(
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
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

