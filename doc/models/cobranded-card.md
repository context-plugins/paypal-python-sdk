
# Cobranded Card

Details about the merchant cobranded card used for order purchase.

*This model accepts additional fields of type Any.*

## Structure

`CobrandedCard`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `labels` | `List[str]` | Optional | Array of labels for the cobranded card.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `25`, *Minimum Length*: `1`, *Maximum Length*: `256` |
| `payee` | [`PayeeBase`](../../doc/models/payee-base.md) | Optional | The details for the merchant who receives the funds and fulfills the order. The merchant is also known as the payee. |
| `amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.cobranded_card import CobrandedCard
from paypal.models.money import Money
from paypal.models.payee_base import PayeeBase

cobranded_card = CobrandedCard(
    labels=[
        'labels0',
        'labels1',
        'labels2'
    ],
    payee=PayeeBase(
        email_address='email_address4',
        merchant_id='merchant_id6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    amount=Money(
        currency_code='currency_code6',
        value='value0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

