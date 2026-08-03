
# Frequency

The frequency of the billing cycle.

*This model accepts additional fields of type Any.*

## Structure

`Frequency`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Required | The interval at which the subscription is charged or billed.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `24`, *Pattern*: `^[A-Z_]+$` |
| `interval_count` | `int` | Optional | The number of intervals after which a subscriber is billed. For example, if the `interval_unit` is `DAY` with an `interval_count` of  `2`, the subscription is billed once every two days. The following table lists the maximum allowed values for the `interval_count` for each `interval_unit`: Interval unit Maximum interval count DAY 365 WEEK 52 MONTH 12 YEAR 1<br><br>**Default**: `1`<br><br>**Constraints**: `>= 1`, `<= 365` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.frequency import Frequency
from paypal.models.interval_unit import IntervalUnit

frequency = Frequency(
    interval_unit=IntervalUnit.DAY,
    interval_count=1,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

