
# Customer Vault Payment Tokens Response

Collection of payment tokens saved for a given customer.

*This model accepts additional fields of type Any.*

## Structure

`CustomerVaultPaymentTokensResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_items` | `int` | Optional | Total number of items.<br><br>**Constraints**: `>= 1`, `<= 50` |
| `total_pages` | `int` | Optional | Total number of pages.<br><br>**Constraints**: `>= 1`, `<= 10` |
| `customer` | [`VaultResponseCustomer`](../../doc/models/vault-response-customer.md) | Optional | This object defines a customer in your system. Use it to manage customer profiles, save payment methods and contact details. |
| `payment_tokens` | [`List[PaymentTokenResponse]`](../../doc/models/payment-token-response.md) | Optional | **Constraints**: *Minimum Items*: `0`, *Maximum Items*: `64` |
| `links` | [`List[LinkDescription]`](../../doc/models/link-description.md) | Optional, Read-only | An array of related [HATEOAS links](https://developer.paypal.com/api/rest/responses/#hateoas).<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `32` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from paypal.models.address import Address
from paypal.models.apple_pay_card import ApplePayCard
from paypal.models.apple_pay_payment_token import ApplePayPaymentToken
from paypal.models.card_brand import CardBrand
from paypal.models.card_payment_token_entity import CardPaymentTokenEntity
from paypal.models.card_response_address import CardResponseAddress
from paypal.models.card_type import CardType
from paypal.models.customer_response import CustomerResponse
from paypal.models.customer_vault_payment_tokens_response import CustomerVaultPaymentTokensResponse
from paypal.models.fulfillment_type import FulfillmentType
from paypal.models.link_description import LinkDescription
from paypal.models.link_http_method import LinkHttpMethod
from paypal.models.pay_pal_payment_token import PayPalPaymentToken
from paypal.models.pay_pal_payment_token_usage_type import PayPalPaymentTokenUsageType
from paypal.models.payment_token_response import PaymentTokenResponse
from paypal.models.payment_token_response_payment_source import PaymentTokenResponsePaymentSource
from paypal.models.phone_number_with_country_code import PhoneNumberWithCountryCode
from paypal.models.shipping_name import ShippingName
from paypal.models.usage_pattern import UsagePattern
from paypal.models.vault_response_customer import VaultResponseCustomer
from paypal.models.vaulted_digital_wallet_shipping_details import VaultedDigitalWalletShippingDetails
from paypal.models.venmo_payment_token import VenmoPaymentToken

customer_vault_payment_tokens_response = CustomerVaultPaymentTokensResponse(
    total_items=42,
    total_pages=10,
    customer=VaultResponseCustomer(
        id='id0',
        merchant_customer_id='merchant_customer_id2',
        links=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    payment_tokens=[
        PaymentTokenResponse(
            id='id4',
            customer=CustomerResponse(
                id='id0',
                merchant_customer_id='merchant_customer_id2',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            payment_source=PaymentTokenResponsePaymentSource(
                card=CardPaymentTokenEntity(
                    name='name6',
                    last_digits='last_digits0',
                    brand=CardBrand.CB_NATIONALE,
                    expiry='expiry4',
                    billing_address=CardResponseAddress(
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
                paypal=PayPalPaymentToken(
                    description='description2',
                    usage_pattern=UsagePattern.THRESHOLD_PREPAID,
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
                ),
                venmo=VenmoPaymentToken(
                    description='description6',
                    usage_pattern=UsagePattern.UNSCHEDULED_PREPAID,
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
                ),
                apple_pay=ApplePayPaymentToken(
                    card=ApplePayCard(
                        name='name6',
                        last_digits='last_digits0',
                        mtype=CardType.UNKNOWN,
                        brand=CardBrand.CB_NATIONALE,
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
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            links=[
                LinkDescription(
                    href='href6',
                    rel='rel0',
                    method=LinkHttpMethod.HEAD,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                LinkDescription(
                    href='href6',
                    rel='rel0',
                    method=LinkHttpMethod.HEAD,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        PaymentTokenResponse(
            id='id4',
            customer=CustomerResponse(
                id='id0',
                merchant_customer_id='merchant_customer_id2',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            payment_source=PaymentTokenResponsePaymentSource(
                card=CardPaymentTokenEntity(
                    name='name6',
                    last_digits='last_digits0',
                    brand=CardBrand.CB_NATIONALE,
                    expiry='expiry4',
                    billing_address=CardResponseAddress(
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
                paypal=PayPalPaymentToken(
                    description='description2',
                    usage_pattern=UsagePattern.THRESHOLD_PREPAID,
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
                ),
                venmo=VenmoPaymentToken(
                    description='description6',
                    usage_pattern=UsagePattern.UNSCHEDULED_PREPAID,
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
                ),
                apple_pay=ApplePayPaymentToken(
                    card=ApplePayCard(
                        name='name6',
                        last_digits='last_digits0',
                        mtype=CardType.UNKNOWN,
                        brand=CardBrand.CB_NATIONALE,
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
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            links=[
                LinkDescription(
                    href='href6',
                    rel='rel0',
                    method=LinkHttpMethod.HEAD,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                LinkDescription(
                    href='href6',
                    rel='rel0',
                    method=LinkHttpMethod.HEAD,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    links=[
        LinkDescription(
            href='href6',
            rel='rel0',
            method=LinkHttpMethod.HEAD,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        LinkDescription(
            href='href6',
            rel='rel0',
            method=LinkHttpMethod.HEAD,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

