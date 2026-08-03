
# Subscription Amount with Breakdown

The breakdown details for the amount. Includes the gross, tax, fee, and shipping amounts.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionAmountWithBreakdown`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `gross_amount` | [`Money`](../../doc/models/money.md) | Required | The currency and amount for a financial transaction, such as a balance or payment due. |
| `total_item_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `fee_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `shipping_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `tax_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `net_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.money import Money
from paypal.models.subscription_amount_with_breakdown import SubscriptionAmountWithBreakdown

subscription_amount_with_breakdown = SubscriptionAmountWithBreakdown(
    gross_amount=Money(
        currency_code='currency_code4',
        value='value0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    total_item_amount=Money(
        currency_code='currency_code8',
        value='value4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    fee_amount=Money(
        currency_code='currency_code2',
        value='value4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    shipping_amount=Money(
        currency_code='currency_code0',
        value='value6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    tax_amount=Money(
        currency_code='currency_code2',
        value='value8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    net_amount=Money(
        currency_code='currency_code6',
        value='value2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

