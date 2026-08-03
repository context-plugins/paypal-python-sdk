
# Apple Pay Attributes Response

Additional attributes associated with the use of Apple Pay.

*This model accepts additional fields of type Any.*

## Structure

`ApplePayAttributesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vault` | [`VaultResponse`](../../doc/models/vault-response.md) | Optional | The details about a saved payment source. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.apple_pay_attributes_response import ApplePayAttributesResponse
from paypal.models.link_description import LinkDescription
from paypal.models.link_http_method import LinkHttpMethod
from paypal.models.name import Name
from paypal.models.vault_customer import VaultCustomer
from paypal.models.vault_response import VaultResponse
from paypal.models.vault_status import VaultStatus

apple_pay_attributes_response = ApplePayAttributesResponse(
    vault=VaultResponse(
        id='id6',
        status=VaultStatus.APPROVED,
        customer=VaultCustomer(
            id='id0',
            name=Name(
                given_name='given_name2',
                surname='surname8',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
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
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

