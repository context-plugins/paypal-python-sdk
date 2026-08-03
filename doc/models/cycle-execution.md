
# Cycle Execution

The regular and trial execution details for a billing cycle.

*This model accepts additional fields of type Any.*

## Structure

`CycleExecution`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tenure_type` | [`TenureType1`](../../doc/models/tenure-type-1.md) | Required, Read-only | The type of the billing cycle.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `24`, *Pattern*: `^[A-Z_]+$` |
| `sequence` | `int` | Required | The order in which to run this cycle among other billing cycles.<br><br>**Constraints**: `>= 0`, `<= 99` |
| `cycles_completed` | `int` | Required, Read-only | The number of billing cycles that have completed.<br><br>**Constraints**: `>= 0`, `<= 9999` |
| `cycles_remaining` | `int` | Optional, Read-only | For a finite billing cycle, cycles_remaining is the number of remaining cycles. For an infinite billing cycle, cycles_remaining is set as 0.<br><br>**Constraints**: `>= 0`, `<= 9999` |
| `current_pricing_scheme_version` | `int` | Optional, Read-only | The active pricing scheme version for the billing cycle.<br><br>**Constraints**: `>= 1`, `<= 99` |
| `total_cycles` | `int` | Optional, Read-only | The number of times this billing cycle gets executed. Trial billing cycles can only be executed a finite number of times (value between 1 and 999 for total_cycles). Regular billing cycles can be executed infinite times (value of 0 for total_cycles) or a finite number of times (value between 1 and 999 for total_cycles).<br><br>**Constraints**: `>= 0`, `<= 999` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.cycle_execution import CycleExecution
from paypal.models.tenure_type_1 import TenureType1

cycle_execution = CycleExecution(
    tenure_type=TenureType1.REGULAR,
    sequence=99,
    cycles_completed=216,
    cycles_remaining=92,
    current_pricing_scheme_version=99,
    total_cycles=104,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

