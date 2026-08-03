
# Plan Collection

The list of plans with details.

*This model accepts additional fields of type Any.*

## Structure

`PlanCollection`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plans` | [`List[BillingPlan]`](../../doc/models/billing-plan.md) | Optional | An array of plans.<br><br>**Constraints**: *Minimum Items*: `0`, *Maximum Items*: `32767` |
| `total_items` | `int` | Optional | The total number of items.<br><br>**Constraints**: `>= 0`, `<= 500000000` |
| `total_pages` | `int` | Optional | The total number of pages.<br><br>**Constraints**: `>= 0`, `<= 100000000` |
| `links` | [`List[LinkDescription]`](../../doc/models/link-description.md) | Optional, Read-only | An array of request-related [HATEOAS links](/docs/api/reference/api-responses/#hateoas-links).<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `10` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.billing_plan import BillingPlan
from paypal.models.link_description import LinkDescription
from paypal.models.link_http_method import LinkHttpMethod
from paypal.models.plan_collection import PlanCollection
from paypal.models.subscription_plan_status import SubscriptionPlanStatus

plan_collection = PlanCollection(
    plans=[
        BillingPlan(
            id='id4',
            product_id='product_id0',
            name='name4',
            status=SubscriptionPlanStatus.INACTIVE,
            description='description4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        BillingPlan(
            id='id4',
            product_id='product_id0',
            name='name4',
            status=SubscriptionPlanStatus.INACTIVE,
            description='description4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    total_items=68,
    total_pages=104,
    links=[
        LinkDescription(
            href='href6',
            rel='rel0',
            method=LinkHttpMethod.HEAD,
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

