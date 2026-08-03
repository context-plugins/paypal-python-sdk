
# Vault Venmo Request

A resource representing a request to vault Venmo.

*This model accepts additional fields of type Any.*

## Structure

`VaultVenmoRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | The description displayed to the consumer on the approval flow for a digital wallet, as well as on the merchant view of the payment token management experience. exp: PayPal.com.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `128`, *Pattern*: `^.*$` |
| `usage_pattern` | [`UsagePattern`](../../doc/models/usage-pattern.md) | Optional | Expected business/charge model for the billing agreement.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `30`, *Pattern*: `^[0-9A-Z_]+$` |
| `shipping` | [`VaultedDigitalWalletShippingDetails`](../../doc/models/vaulted-digital-wallet-shipping-details.md) | Optional | The shipping details. |
| `permit_multiple_payment_tokens` | `bool` | Optional | Create multiple payment tokens for the same payer, merchant/platform combination. Use this when the customer has not logged in at merchant/platform. The payment token thus generated, can then also be used to create the customer account at merchant/platform. Use this also when multiple payment tokens are required for the same payer, different customer at merchant/platform. This helps to identify customers distinctly even though they may share the same PayPal account. This only applies to PayPal payment source.<br><br>**Default**: `False` |
| `usage_type` | [`PayPalPaymentTokenUsageType`](../../doc/models/pay-pal-payment-token-usage-type.md) | Optional | The usage type associated with a digital wallet payment token.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `customer_type` | [`PayPalPaymentTokenCustomerType`](../../doc/models/pay-pal-payment-token-customer-type.md) | Optional | The customer type associated with a digital wallet payment token. This is to indicate whether the customer acting on the merchant / platform is either a business or a consumer.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `experience_context` | [`VenmoExperienceContext`](../../doc/models/venmo-experience-context.md) | Optional | A resource representing an experience context of vault a venmo account. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.address import Address
from paypal.models.fulfillment_type import FulfillmentType
from paypal.models.pay_pal_payment_token_usage_type import PayPalPaymentTokenUsageType
from paypal.models.phone_number_with_country_code import PhoneNumberWithCountryCode
from paypal.models.shipping_name import ShippingName
from paypal.models.usage_pattern import UsagePattern
from paypal.models.vault_venmo_request import VaultVenmoRequest
from paypal.models.vaulted_digital_wallet_shipping_details import VaultedDigitalWalletShippingDetails

vault_venmo_request = VaultVenmoRequest(
    description='description0',
    usage_pattern=UsagePattern.SUBSCRIPTION_PREPAID,
    shipping=VaultedDigitalWalletShippingDetails(
        name=ShippingName(
            full_name='full_name6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        email_address='email_address2',
        phone_number=PhoneNumberWithCountryCode(
            country_code='country_code2',
            national_number='national_number6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        mtype=FulfillmentType.SHIPPING,
        address=Address(
            country_code='country_code6',
            address_line_1='address_line_16',
            address_line_2='address_line_26',
            admin_area_2='admin_area_20',
            admin_area_1='admin_area_12',
            postal_code='postal_code8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    permit_multiple_payment_tokens=False,
    usage_type=PayPalPaymentTokenUsageType.MERCHANT,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

