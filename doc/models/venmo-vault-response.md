
# Venmo Vault Response

The details about a saved venmo payment source.

*This model accepts additional fields of type Any.*

## Structure

`VenmoVaultResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The PayPal-generated ID for the saved payment source.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255` |
| `status` | [`VenmoVaultResponseStatus`](../../doc/models/venmo-vault-response-status.md) | Optional | The vault status.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `links` | [`List[LinkDescription]`](../../doc/models/link-description.md) | Optional, Read-only | An array of request-related HATEOAS links.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `10` |
| `customer` | [`CustomerInformation`](../../doc/models/customer-information.md) | Optional | This object represents a merchant’s customer, allowing them to store contact details, and track all payments associated with the same customer. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.customer_information import CustomerInformation
from paypal.models.link_description import LinkDescription
from paypal.models.link_http_method import LinkHttpMethod
from paypal.models.name import Name
from paypal.models.phone_number import PhoneNumber
from paypal.models.phone_type import PhoneType
from paypal.models.phone_with_type import PhoneWithType
from paypal.models.venmo_vault_response import VenmoVaultResponse
from paypal.models.venmo_vault_response_status import VenmoVaultResponseStatus

venmo_vault_response = VenmoVaultResponse(
    id='id6',
    status=VenmoVaultResponseStatus.APPROVED,
    links=[
        LinkDescription(
            href='href6',
            rel='rel0',
            method=LinkHttpMethod.HEAD,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        LinkDescription(
            href='href6',
            rel='rel0',
            method=LinkHttpMethod.HEAD,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        LinkDescription(
            href='href6',
            rel='rel0',
            method=LinkHttpMethod.HEAD,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    customer=CustomerInformation(
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
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

