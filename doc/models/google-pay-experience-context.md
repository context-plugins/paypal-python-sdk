
# Google Pay Experience Context

Customizes the payer experience during the approval process for the payment.

*This model accepts additional fields of type Any.*

## Structure

`GooglePayExperienceContext`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `return_url` | `str` | Required | Describes the URL. |
| `cancel_url` | `str` | Required | Describes the URL. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.google_pay_experience_context import GooglePayExperienceContext

google_pay_experience_context = GooglePayExperienceContext(
    return_url='return_url0',
    cancel_url='cancel_url2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

