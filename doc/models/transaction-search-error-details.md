
# Transaction Search Error Details

The error details. Required for client-side `4XX` errors.

*This model accepts additional fields of type Any.*

## Structure

`TransactionSearchErrorDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field` | `str` | Optional | The field that caused the error. If this field is in the body, set this value to the field's JSON pointer value. Required for client-side errors. |
| `value` | `str` | Optional | The value of the field that caused the error. |
| `location` | `str` | Optional | The location of the field that caused the error. Value is `body`, `path`, or `query`.<br><br>**Default**: `"body"` |
| `issue` | `str` | Required | The unique, fine-grained application-level error code. |
| `description` | `str` | Optional | The human-readable description for an issue. The description can change over the lifetime of an API, so clients must not depend on this value. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.transaction_search_error_details import TransactionSearchErrorDetails

transaction_search_error_details = TransactionSearchErrorDetails(
    issue='issue2',
    field='field6',
    value='value4',
    location='body',
    description='description8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

