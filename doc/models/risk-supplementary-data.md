
# Risk Supplementary Data

Additional information necessary to evaluate the risk profile of a transaction.

*This model accepts additional fields of type Any.*

## Structure

`RiskSupplementaryData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer` | [`ParticipantMetadata`](../../doc/models/participant-metadata.md) | Optional | Profile information of the sender or receiver. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.participant_metadata import ParticipantMetadata
from paypal.models.risk_supplementary_data import RiskSupplementaryData

risk_supplementary_data = RiskSupplementaryData(
    customer=ParticipantMetadata(
        ip_address='ip_address0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

