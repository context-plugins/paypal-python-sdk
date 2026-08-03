
# Application Context Shipping Preference

The location from which the shipping address is derived., The location from which the shipping address is derived., The shipping preference. This only applies to PayPal payment source., The shipping preference. This only applies to PayPal payment source., The location from which the shipping address is derived., DEPRECATED. DEPRECATED. The shipping preference: Displays the shipping address to the customer. Enables the customer to choose an address on the PayPal site. Restricts the customer from changing the address during the payment-approval process. .  The fields in `application_context` are now available in the `experience_context` object under the `payment_source` which supports them (eg. `payment_source.paypal.experience_context.shipping_preference`). Please specify this field in the `experience_context` object instead of the `application_context` object., The location from which the shipping address is derived., The location from which the shipping address is derived., The shipping preference. This only applies to PayPal payment source., The shipping preference. This only applies to PayPal payment source.

## Enumeration

`ApplicationContextShippingPreference`

## Fields

| Name | Description |
|  --- | --- |
| `GET_FROM_FILE` | Get the customer-provided shipping address on the PayPal site. |
| `NO_SHIPPING` | Redacts the shipping address from the PayPal site. Recommended for digital goods. |
| `SET_PROVIDED_ADDRESS` | Get the merchant-provided address. The customer cannot change this address on the PayPal site. If merchant does not pass an address, customer can choose the address on PayPal pages. |

## Example

```python
from paypal.models.application_context_shipping_preference import ApplicationContextShippingPreference

application_context_shipping_preference = ApplicationContextShippingPreference.GET_FROM_FILE
```

