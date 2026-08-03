
# Confirm Order Request

Payer confirms the intent to pay for the Order using the provided payment source.

*This model accepts additional fields of type Any.*

## Structure

`ConfirmOrderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_source` | [`PaymentSource`](../../doc/models/payment-source.md) | Required | The payment source definition. |
| `processing_instruction` | [`ProcessingInstruction`](../../doc/models/processing-instruction.md) | Optional | The instruction to process an order. |
| `application_context` | [`OrderConfirmApplicationContext`](../../doc/models/order-confirm-application-context.md) | Optional | Customizes the payer confirmation experience. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.address import Address
from paypal.models.application_context_shipping_preference import ApplicationContextShippingPreference
from paypal.models.bancontact_payment_request import BancontactPaymentRequest
from paypal.models.blik_experience_context import BlikExperienceContext
from paypal.models.blik_level_0_payment_object import BlikLevel0PaymentObject
from paypal.models.blik_one_click_payment_request import BlikOneClickPaymentRequest
from paypal.models.blik_payment_request import BlikPaymentRequest
from paypal.models.card_brand import CardBrand
from paypal.models.card_request import CardRequest
from paypal.models.confirm_order_request import ConfirmOrderRequest
from paypal.models.experience_context import ExperienceContext
from paypal.models.name import Name
from paypal.models.network_transaction import NetworkTransaction
from paypal.models.order_confirm_application_context import OrderConfirmApplicationContext
from paypal.models.pay_pal_wallet import PayPalWallet
from paypal.models.payment_initiator import PaymentInitiator
from paypal.models.payment_source import PaymentSource
from paypal.models.phone_number import PhoneNumber
from paypal.models.phone_type import PhoneType
from paypal.models.phone_with_type import PhoneWithType
from paypal.models.processing_instruction import ProcessingInstruction
from paypal.models.stored_payment_source import StoredPaymentSource
from paypal.models.stored_payment_source_payment_type import StoredPaymentSourcePaymentType
from paypal.models.stored_payment_source_usage_type import StoredPaymentSourceUsageType
from paypal.models.token import Token
from paypal.models.token_type import TokenType

confirm_order_request = ConfirmOrderRequest(
    payment_source=PaymentSource(
        card=CardRequest(
            name='name6',
            number='number6',
            expiry='expiry4',
            security_code='security_code8',
            billing_address=Address(
                country_code='country_code8',
                address_line_1='address_line_12',
                address_line_2='address_line_28',
                admin_area_2='admin_area_28',
                admin_area_1='admin_area_14',
                postal_code='postal_code0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        token=Token(
            id='id6',
            mtype=TokenType.BILLING_AGREEMENT,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        paypal=PayPalWallet(
            vault_id='vault_id0',
            email_address='email_address0',
            name=Name(
                given_name='given_name2',
                surname='surname8',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            phone=PhoneWithType(
                phone_number=PhoneNumber(
                    national_number='national_number6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                phone_type=PhoneType.OTHER,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            birth_date='birth_date8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        bancontact=BancontactPaymentRequest(
            name='name0',
            country_code='country_code0',
            experience_context=ExperienceContext(
                brand_name='brand_name2',
                locale='locale6',
                shipping_preference=ApplicationContextShippingPreference.NO_SHIPPING,
                return_url='return_url4',
                cancel_url='cancel_url6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        blik=BlikPaymentRequest(
            name='name2',
            country_code='country_code2',
            email='email4',
            experience_context=BlikExperienceContext(
                brand_name='brand_name2',
                locale='locale6',
                shipping_preference=ApplicationContextShippingPreference.NO_SHIPPING,
                return_url='return_url4',
                cancel_url='cancel_url6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            level_0=BlikLevel0PaymentObject(
                auth_code='auth_code8',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            one_click=BlikOneClickPaymentRequest(
                consumer_reference='consumer_reference2',
                auth_code='auth_code0',
                alias_label='alias_label6',
                alias_key='alias_key4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    processing_instruction=ProcessingInstruction.ORDER_COMPLETE_ON_PAYMENT_APPROVAL,
    application_context=OrderConfirmApplicationContext(
        brand_name='brand_name8',
        locale='locale2',
        return_url='return_url0',
        cancel_url='cancel_url2',
        stored_payment_source=StoredPaymentSource(
            payment_initiator=PaymentInitiator.CUSTOMER,
            payment_type=StoredPaymentSourcePaymentType.RECURRING,
            usage=StoredPaymentSourceUsageType.FIRST,
            previous_network_transaction_reference=NetworkTransaction(
                id='id6',
                date='date2',
                network=CardBrand.CONFIDIS,
                acquirer_reference_number='acquirer_reference_number8',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

