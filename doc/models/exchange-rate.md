
# Exchange Rate

The exchange rate that determines the amount to convert from one currency to another currency.

*This model accepts additional fields of type Any.*

## Structure

`ExchangeRate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `source_currency` | `str` | Optional | The [three-character ISO-4217 currency code](https://developer.paypal.com/api/rest/reference/currency-codes/) that identifies the currency.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `target_currency` | `str` | Optional | The [three-character ISO-4217 currency code](https://developer.paypal.com/api/rest/reference/currency-codes/) that identifies the currency.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `value` | `str` | Optional | The target currency amount. Equivalent to one unit of the source currency. Formatted as integer or decimal value with one to 15 digits to the right of the decimal point. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.exchange_rate import ExchangeRate

exchange_rate = ExchangeRate(
    source_currency='source_currency4',
    target_currency='target_currency6',
    value='value6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

