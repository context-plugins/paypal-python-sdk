
# Payment Supplementary Data

The supplementary data.

*This model accepts additional fields of type Any.*

## Structure

`PaymentSupplementaryData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `related_ids` | [`RelatedIdentifiers`](../../doc/models/related-identifiers.md) | Optional | Identifiers related to a specific resource. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.payment_supplementary_data import PaymentSupplementaryData
from paypal.models.related_identifiers import RelatedIdentifiers

payment_supplementary_data = PaymentSupplementaryData(
    related_ids=RelatedIdentifiers(
        order_id='order_id2',
        authorization_id='authorization_id0',
        capture_id='capture_id0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

