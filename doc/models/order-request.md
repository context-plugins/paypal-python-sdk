
# Order Request

The order request details.

*This model accepts additional fields of type Any.*

## Structure

`OrderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `intent` | [`CheckoutPaymentIntent`](../../doc/models/checkout-payment-intent.md) | Required | The intent to either capture payment immediately or authorize a payment for an order after order creation. |
| `processing_instruction` | [`ProcessingInstruction`](../../doc/models/processing-instruction.md) | Optional | The instruction to process an order. |
| `payer` | [`Payer`](../../doc/models/payer.md) | Optional | DEPRECATED. The customer is also known as the payer. The Payer object was intended to only be used with the `payment_source.paypal` object. In order to make this design more clear, the details in the `payer` object are now available under `payment_source.paypal`. Please use `payment_source.paypal`. |
| `purchase_units` | [`List[PurchaseUnitRequest]`](../../doc/models/purchase-unit-request.md) | Required | An array of purchase units. Each purchase unit establishes a contract between a payer and the payee. Each purchase unit represents either a full or partial order that the payer intends to purchase from the payee.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `10` |
| `payment_source` | [`PaymentSource`](../../doc/models/payment-source.md) | Optional | The payment source definition. |
| `application_context` | [`OrderApplicationContext`](../../doc/models/order-application-context.md) | Optional | Customizes the payer experience during the approval process for the payment with PayPal. Note: Partners and Marketplaces might configure brand_name and shipping_preference during partner account setup, which overrides the request values. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.address import Address
from paypal.models.amount_breakdown import AmountBreakdown
from paypal.models.amount_with_breakdown import AmountWithBreakdown
from paypal.models.application_context_shipping_preference import ApplicationContextShippingPreference
from paypal.models.bancontact_payment_request import BancontactPaymentRequest
from paypal.models.blik_experience_context import BlikExperienceContext
from paypal.models.blik_level_0_payment_object import BlikLevel0PaymentObject
from paypal.models.blik_one_click_payment_request import BlikOneClickPaymentRequest
from paypal.models.blik_payment_request import BlikPaymentRequest
from paypal.models.card_request import CardRequest
from paypal.models.checkout_payment_intent import CheckoutPaymentIntent
from paypal.models.disbursement_mode import DisbursementMode
from paypal.models.experience_context import ExperienceContext
from paypal.models.money import Money
from paypal.models.name import Name
from paypal.models.order_application_context import OrderApplicationContext
from paypal.models.order_application_context_landing_page import OrderApplicationContextLandingPage
from paypal.models.order_application_context_user_action import OrderApplicationContextUserAction
from paypal.models.order_request import OrderRequest
from paypal.models.pay_pal_wallet import PayPalWallet
from paypal.models.payee_base import PayeeBase
from paypal.models.payer import Payer
from paypal.models.payment_instruction import PaymentInstruction
from paypal.models.payment_source import PaymentSource
from paypal.models.phone_number import PhoneNumber
from paypal.models.phone_type import PhoneType
from paypal.models.phone_with_type import PhoneWithType
from paypal.models.platform_fee import PlatformFee
from paypal.models.processing_instruction import ProcessingInstruction
from paypal.models.purchase_unit_request import PurchaseUnitRequest
from paypal.models.token import Token
from paypal.models.token_type import TokenType

order_request = OrderRequest(
    intent=CheckoutPaymentIntent.CAPTURE,
    purchase_units=[
        PurchaseUnitRequest(
            amount=AmountWithBreakdown(
                currency_code='currency_code6',
                value='value0',
                breakdown=AmountBreakdown(
                    item_total=Money(
                        currency_code='currency_code0',
                        value='value6',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    shipping=Money(
                        currency_code='currency_code0',
                        value='value6',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    handling=Money(
                        currency_code='currency_code2',
                        value='value8',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    tax_total=Money(
                        currency_code='currency_code4',
                        value='value0',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    insurance=Money(
                        currency_code='currency_code2',
                        value='value8',
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
            reference_id='reference_id4',
            payee=PayeeBase(
                email_address='email_address4',
                merchant_id='merchant_id6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            payment_instruction=PaymentInstruction(
                platform_fees=[
                    PlatformFee(
                        amount=Money(
                            currency_code='currency_code6',
                            value='value0',
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        payee=PayeeBase(
                            email_address='email_address4',
                            merchant_id='merchant_id6',
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    PlatformFee(
                        amount=Money(
                            currency_code='currency_code6',
                            value='value0',
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        payee=PayeeBase(
                            email_address='email_address4',
                            merchant_id='merchant_id6',
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    PlatformFee(
                        amount=Money(
                            currency_code='currency_code6',
                            value='value0',
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        payee=PayeeBase(
                            email_address='email_address4',
                            merchant_id='merchant_id6',
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    )
                ],
                disbursement_mode=DisbursementMode.INSTANT,
                payee_pricing_tier_id='payee_pricing_tier_id2',
                payee_receivable_fx_rate_id='payee_receivable_fx_rate_id0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            description='description6',
            custom_id='custom_id4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    processing_instruction=ProcessingInstruction.ORDER_COMPLETE_ON_PAYMENT_APPROVAL,
    payer=Payer(
        email_address='email_address6',
        payer_id='payer_id6',
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
        birth_date='birth_date4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
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
    application_context=OrderApplicationContext(
        brand_name='brand_name8',
        locale='locale2',
        landing_page=OrderApplicationContextLandingPage.BILLING,
        shipping_preference=ApplicationContextShippingPreference.SET_PROVIDED_ADDRESS,
        user_action=OrderApplicationContextUserAction.CONTINUE,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

