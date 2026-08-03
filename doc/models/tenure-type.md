
# Tenure Type

The tenure type of the billing cycle. In case of a plan having trial cycle, only 2 trial cycles are allowed per plan., The tenure type of the billing cycle identifies if the billing cycle is a trial(free or discounted) or regular billing cycle., The tenure type of the billing cycle. In case of a plan having trial cycle, only 2 trial cycles are allowed per plan., The type of the billing cycle., The tenure type of the billing cycle identifies if the billing cycle is a trial(free or discounted) or regular billing cycle.

## Enumeration

`TenureType`

## Fields

| Name | Description |
|  --- | --- |
| `REGULAR` | A regular billing cycle. |
| `TRIAL` | A trial billing cycle. |

## Example

```python
from paypal.models.tenure_type import TenureType

tenure_type = TenureType.REGULAR
```

