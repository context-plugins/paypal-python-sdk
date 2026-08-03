
# Token Type

The tokenization method that generated the ID.

*This model accepts additional fields of type Any.*

## Enumeration

`TokenType`

## Fields

| Name | Description |
|  --- | --- |
| `BILLING_AGREEMENT` | The PayPal billing agreement ID. References an approved recurring payment for goods or services. |

## Example

```python
from paypal.models.token_type import TokenType

token_type = TokenType.BILLING_AGREEMENT
```

