
# Incentive Information

The incentive details.

*This model accepts additional fields of type Any.*

## Structure

`IncentiveInformation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `incentive_details` | [`List[IncentiveDetails]`](../../doc/models/incentive-details.md) | Optional | An array of incentive details.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `32767` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.incentive_details import IncentiveDetails
from paypal.models.incentive_information import IncentiveInformation
from paypal.models.money import Money

incentive_information = IncentiveInformation(
    incentive_details=[
        IncentiveDetails(
            incentive_type='incentive_type4',
            incentive_code='incentive_code0',
            incentive_amount=Money(
                currency_code='currency_code4',
                value='value0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            incentive_program_code='incentive_program_code4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        IncentiveDetails(
            incentive_type='incentive_type4',
            incentive_code='incentive_code0',
            incentive_amount=Money(
                currency_code='currency_code4',
                value='value0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            incentive_program_code='incentive_program_code4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        IncentiveDetails(
            incentive_type='incentive_type4',
            incentive_code='incentive_code0',
            incentive_amount=Money(
                currency_code='currency_code4',
                value='value0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            incentive_program_code='incentive_program_code4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

