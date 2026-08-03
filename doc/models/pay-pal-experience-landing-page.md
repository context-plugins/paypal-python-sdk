
# Pay Pal Experience Landing Page

The type of landing page to show on the PayPal site for customer checkout.

*This model accepts additional fields of type Any.*

## Enumeration

`PayPalExperienceLandingPage`

## Fields

| Name | Description |
|  --- | --- |
| `LOGIN` | When the customer clicks PayPal Checkout, the customer is redirected to a page to log in to PayPal and approve the payment. |
| `GUEST_CHECKOUT` | When the customer clicks PayPal Checkout, the customer is redirected to a page to enter credit or debit card and other relevant billing information required to complete the purchase. This option has previously been also called as 'BILLING' |
| `NO_PREFERENCE` | When the customer clicks PayPal Checkout, the customer is redirected to either a page to log in to PayPal and approve the payment or to a page to enter credit or debit card and other relevant billing information required to complete the purchase, depending on their previous interaction with PayPal. |
| `BILLING` | DEPRECATED - please use GUEST_CHECKOUT. All implementations of 'BILLING' will be routed to 'GUEST_CHECKOUT'. When the customer clicks PayPal Checkout, the customer is redirected to a page to enter credit or debit card and other relevant billing information required to complete the purchase. |

## Example

```python
from paypal.models.pay_pal_experience_landing_page import PayPalExperienceLandingPage

pay_pal_experience_landing_page = PayPalExperienceLandingPage.NO_PREFERENCE
```

