
# Apple Pay Attributes Response

Additional attributes associated with the use of Apple Pay.

## Structure

`ApplePayAttributesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vault` | [`VaultResponse`](../../doc/models/vault-response.md) | Optional | The details about a saved payment source. |

## Example

```python
from paypalserversdk.models.apple_pay_attributes_response import ApplePayAttributesResponse
from paypalserversdk.models.link_description import LinkDescription
from paypalserversdk.models.link_http_method import LinkHttpMethod
from paypalserversdk.models.name import Name
from paypalserversdk.models.vault_customer import VaultCustomer
from paypalserversdk.models.vault_response import VaultResponse
from paypalserversdk.models.vault_status import VaultStatus

apple_pay_attributes_response = ApplePayAttributesResponse(
    vault=VaultResponse(
        id='id6',
        status=VaultStatus.APPROVED,
        customer=VaultCustomer(
            id='id0',
            name=Name(
                given_name='given_name2',
                surname='surname8'
            )
        ),
        links=[
            LinkDescription(
                href='href6',
                rel='rel0',
                method=LinkHttpMethod.HEAD
            )
        ]
    )
)
```

