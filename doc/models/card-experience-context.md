
# Card Experience Context

Customizes the payer experience during the 3DS Approval for payment.

*This model accepts additional fields of type Any.*

## Structure

`CardExperienceContext`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `return_url` | `str` | Optional | Describes the URL. |
| `cancel_url` | `str` | Optional | Describes the URL. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.card_experience_context import CardExperienceContext

card_experience_context = CardExperienceContext(
    return_url='return_url2',
    cancel_url='cancel_url4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

