
# Sepa Debit Request

An API resource denoting a request to securely store a SEPA Debit.

*This model accepts additional fields of type Any.*

## Structure

`SepaDebitRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `experience_context` | [`SepaDebitExperienceContext`](../../doc/models/sepa-debit-experience-context.md) | Optional | Customizes the payer experience during the approval process for the SEPA Debit payment. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.sepa_debit_experience_context import SepaDebitExperienceContext
from paypal.models.sepa_debit_request import SepaDebitRequest

sepa_debit_request = SepaDebitRequest(
    experience_context=SepaDebitExperienceContext(
        return_url='return_url4',
        cancel_url='cancel_url6',
        locale='locale6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

