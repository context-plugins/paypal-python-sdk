
# Pay Pal Wallet Experience Context

Customizes the payer experience during the approval process for payment with PayPal. Note: Partners and Marketplaces might configure brand_name and shipping_preference during partner account setup, which overrides the request values.

*This model accepts additional fields of type Any.*

## Structure

`PayPalWalletExperienceContext`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand_name` | `str` | Optional | The label that overrides the business name in the PayPal account on the PayPal site. The pattern is defined by an external party and supports Unicode.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `127`, *Pattern*: `^.*$` |
| `locale` | `str` | Optional | The [language tag](https://tools.ietf.org/html/bcp47#section-2) for the language in which to localize the error-related strings, such as messages, issues, and suggested actions. The tag is made up of the [ISO 639-2 language code](https://www.loc.gov/standards/iso639-2/php/code_list.php), the optional [ISO-15924 script tag](https://www.unicode.org/iso15924/codelists.html), and the [ISO-3166 alpha-2 country code](https://developer.paypal.com/api/rest/reference/country-codes/) or [M49 region code](https://unstats.un.org/unsd/methodology/m49/).<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `10`, *Pattern*: `^[a-z]{2}(?:-[A-Z][a-z]{3})?(?:-(?:[A-Z]{2}\|[0-9]{3}))?$` |
| `shipping_preference` | [`ApplicationContextShippingPreference`](../../doc/models/application-context-shipping-preference.md) | Optional | The location from which the shipping address is derived.<br><br>**Default**: `"GET_FROM_FILE"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `24`, *Pattern*: `^[A-Z_]+$` |
| `contact_preference` | [`PayPalWalletContactPreference`](../../doc/models/pay-pal-wallet-contact-preference.md) | Optional | The preference to display the contact information (buyer’s shipping email & phone number) on PayPal's checkout for easy merchant-buyer communication.<br><br>**Default**: `"NO_CONTACT_INFO"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `24`, *Pattern*: `^[A-Z_]+$` |
| `return_url` | `str` | Optional | Describes the URL. |
| `cancel_url` | `str` | Optional | Describes the URL. |
| `app_switch_context` | [`AppSwitchContext`](../../doc/models/app-switch-context.md) | Optional | Merchant provided details of the native app or mobile web browser to facilitate buyer's app switch to the PayPal consumer app. |
| `landing_page` | [`PayPalExperienceLandingPage`](../../doc/models/pay-pal-experience-landing-page.md) | Optional | The type of landing page to show on the PayPal site for customer checkout.<br><br>**Default**: `"NO_PREFERENCE"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `13`, *Pattern*: `^[0-9A-Z_]+$` |
| `user_action` | [`PayPalExperienceUserAction`](../../doc/models/pay-pal-experience-user-action.md) | Optional | Configures a Continue or Pay Now checkout flow.<br><br>**Default**: `"CONTINUE"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `8`, *Pattern*: `^[0-9A-Z_]+$` |
| `payment_method_preference` | [`PayeePaymentMethodPreference`](../../doc/models/payee-payment-method-preference.md) | Optional | The merchant-preferred payment methods.<br><br>**Default**: `"UNRESTRICTED"`<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255`, *Pattern*: `^[0-9A-Z_]+$` |
| `order_update_callback_config` | [`CallbackConfiguration`](../../doc/models/callback-configuration.md) | Optional | CallBack Configuration that the merchant can provide to PayPal/Venmo. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.application_context_shipping_preference import ApplicationContextShippingPreference
from paypal.models.pay_pal_experience_landing_page import PayPalExperienceLandingPage
from paypal.models.pay_pal_experience_user_action import PayPalExperienceUserAction
from paypal.models.pay_pal_wallet_contact_preference import PayPalWalletContactPreference
from paypal.models.pay_pal_wallet_experience_context import PayPalWalletExperienceContext
from paypal.models.payee_payment_method_preference import PayeePaymentMethodPreference

pay_pal_wallet_experience_context = PayPalWalletExperienceContext(
    brand_name='brand_name2',
    locale='locale6',
    shipping_preference=ApplicationContextShippingPreference.GET_FROM_FILE,
    contact_preference=PayPalWalletContactPreference.NO_CONTACT_INFO,
    return_url='return_url4',
    landing_page=PayPalExperienceLandingPage.NO_PREFERENCE,
    user_action=PayPalExperienceUserAction.CONTINUE,
    payment_method_preference=PayeePaymentMethodPreference.UNRESTRICTED,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

