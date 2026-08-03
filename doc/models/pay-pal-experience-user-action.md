
# Pay Pal Experience User Action

Configures a Continue or Pay Now checkout flow.

*This model accepts additional fields of type Any.*

## Enumeration

`PayPalExperienceUserAction`

## Fields

| Name | Description |
|  --- | --- |
| `CONTINUE` | After you redirect the customer to the PayPal payment page, a Continue button appears. Use this option when the final amount is not known when the checkout flow is initiated and you want to redirect the customer to the merchant page without processing the payment. |
| `PAY_NOW` | After you redirect the customer to the PayPal payment page, a Pay Now button appears. Use this option when the final amount is known when the checkout is initiated and you want to process the payment immediately when the customer clicks Pay Now. |

## Example

```python
from paypal.models.pay_pal_experience_user_action import PayPalExperienceUserAction

pay_pal_experience_user_action = PayPalExperienceUserAction.CONTINUE
```

