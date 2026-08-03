
# Apple Pay Experience Context

Customizes the payer experience during the approval process for the payment.

*This model accepts additional fields of type Any.*

## Structure

`ApplePayExperienceContext`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `return_url` | `str` | Required | Describes the URL. |
| `cancel_url` | `str` | Required | Describes the URL. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.apple_pay_experience_context import ApplePayExperienceContext

apple_pay_experience_context = ApplePayExperienceContext(
    return_url='return_url4',
    cancel_url='cancel_url6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

