from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProcessorResponseCode(str, Enum):
    """Processor response code for the non-PayPal payment processor errors."""

    _0000 = "0000"
    """APPROVED."""

    _00_N7 = "00N7"
    """CVV2_FAILURE_POSSIBLE_RETRY_WITH_CVV."""

    _0100 = "0100"
    """REFERRAL."""

    _0390 = "0390"
    """ACCOUNT_NOT_FOUND."""

    _0500 = "0500"
    """DO_NOT_HONOR."""

    _0580 = "0580"
    """UNAUTHORIZED_TRANSACTION."""

    _0800 = "0800"
    """BAD_RESPONSE_REVERSAL_REQUIRED."""

    _0880 = "0880"
    """CRYPTOGRAPHIC_FAILURE."""

    _0890 = "0890"
    """UNACCEPTABLE_PIN."""

    _0960 = "0960"
    """SYSTEM_MALFUNCTION."""

    _0_R00 = "0R00"
    """CANCELLED_PAYMENT."""

    _1000 = "1000"
    """PARTIAL_AUTHORIZATION."""

    _10_BR = "10BR"
    """ISSUER_REJECTED."""

    _1300 = "1300"
    """INVALID_DATA_FORMAT."""

    _1310 = "1310"
    """INVALID_AMOUNT."""

    _1312 = "1312"
    """INVALID_TRANSACTION_CARD_ISSUER_ACQUIRER."""

    _1317 = "1317"
    """INVALID_CAPTURE_DATE."""

    _1320 = "1320"
    """INVALID_CURRENCY_CODE."""

    _1330 = "1330"
    """INVALID_ACCOUNT."""

    _1335 = "1335"
    """INVALID_ACCOUNT_RECURRING."""

    _1340 = "1340"
    """INVALID_TERMINAL."""

    _1350 = "1350"
    """INVALID_MERCHANT."""

    _1352 = "1352"
    """RESTRICTED_OR_INACTIVE_ACCOUNT."""

    _1360 = "1360"
    """BAD_PROCESSING_CODE."""

    _1370 = "1370"
    """INVALID_MCC."""

    _1380 = "1380"
    """INVALID_EXPIRATION."""

    _1382 = "1382"
    """INVALID_CARD_VERIFICATION_VALUE."""

    _1384 = "1384"
    """INVALID_LIFE_CYCLE_OF_TRANSACTION."""

    _1390 = "1390"
    """INVALID_ORDER."""

    _1393 = "1393"
    """TRANSACTION_CANNOT_BE_COMPLETED."""

    _5100 = "5100"
    """GENERIC_DECLINE."""

    _5110 = "5110"
    """CVV2_FAILURE."""

    _5120 = "5120"
    """INSUFFICIENT_FUNDS."""

    _5130 = "5130"
    """INVALID_PIN."""

    _5135 = "5135"
    """DECLINED_PIN_TRY_EXCEEDED."""

    _5140 = "5140"
    """CARD_CLOSED."""

    _5150 = "5150"
    """PICKUP_CARD_SPECIAL_CONDITIONS. Try using another card. Do not retry the same card."""

    _5160 = "5160"
    """UNAUTHORIZED_USER."""

    _5170 = "5170"
    """AVS_FAILURE."""

    _5180 = "5180"
    """INVALID_OR_RESTRICTED_CARD. Try using another card. Do not retry the same card."""

    _5190 = "5190"
    """SOFT_AVS."""

    _5200 = "5200"
    """DUPLICATE_TRANSACTION."""

    _5210 = "5210"
    """INVALID_TRANSACTION."""

    _5400 = "5400"
    """EXPIRED_CARD."""

    _5500 = "5500"
    """INCORRECT_PIN_REENTER."""

    _5650 = "5650"
    """DECLINED_SCA_REQUIRED."""

    _5700 = "5700"
    """TRANSACTION_NOT_PERMITTED. Outside of scope of accepted business."""

    _5710 = "5710"
    """TX_ATTEMPTS_EXCEED_LIMIT."""

    _5800 = "5800"
    """REVERSAL_REJECTED."""

    _5900 = "5900"
    """INVALID_ISSUE."""

    _5910 = "5910"
    """ISSUER_NOT_AVAILABLE_NOT_RETRIABLE."""

    _5920 = "5920"
    """ISSUER_NOT_AVAILABLE_RETRIABLE."""

    _5930 = "5930"
    """CARD_NOT_ACTIVATED."""

    _5950 = "5950"
    """DECLINED_DUE_TO_UPDATED_ACCOUNT. External decline as an updated card has been issued."""

    _6300 = "6300"
    """ACCOUNT_NOT_ON_FILE."""

    _7600 = "7600"
    """APPROVED_NON_CAPTURE."""

    _7700 = "7700"
    """ERROR_3DS."""

    _7710 = "7710"
    """AUTHENTICATION_FAILED."""

    _7800 = "7800"
    """BIN_ERROR."""

    _7900 = "7900"
    """PIN_ERROR."""

    _8000 = "8000"
    """PROCESSOR_SYSTEM_ERROR."""

    _8010 = "8010"
    """HOST_KEY_ERROR."""

    _8020 = "8020"
    """CONFIGURATION_ERROR."""

    _8030 = "8030"
    """UNSUPPORTED_OPERATION."""

    _8100 = "8100"
    """FATAL_COMMUNICATION_ERROR."""

    _8110 = "8110"
    """RETRIABLE_COMMUNICATION_ERROR."""

    _8220 = "8220"
    """SYSTEM_UNAVAILABLE."""

    _9100 = "9100"
    """DECLINED_PLEASE_RETRY. Retry."""

    _9500 = "9500"
    """SUSPECTED_FRAUD. Try using another card. Do not retry the same card."""

    _9510 = "9510"
    """SECURITY_VIOLATION."""

    _9520 = "9520"
    """LOST_OR_STOLEN. Try using another card. Do not retry the same card."""

    _9530 = "9530"
    """HOLD_CALL_CENTER. The merchant must call the number on the back of the card. POS scenario."""

    _9540 = "9540"
    """REFUSED_CARD."""

    _9600 = "9600"
    """UNRECOGNIZED_RESPONSE_CODE."""

    PCNR = "PCNR"
    """CONTINGENCIES_NOT_RESOLVED."""

    PCVV = "PCVV"
    """CVV_FAILURE."""

    PP06 = "PP06"
    """ACCOUNT_CLOSED. A previously open account is now closed"""

    PPRN = "PPRN"
    """REATTEMPT_NOT_PERMITTED."""

    PPAD = "PPAD"
    """BILLING_ADDRESS."""

    PPAB = "PPAB"
    """ACCOUNT_BLOCKED_BY_ISSUER."""

    PPAE = "PPAE"
    """AMEX_DISABLED."""

    PPAG = "PPAG"
    """ADULT_GAMING_UNSUPPORTED."""

    PPAI = "PPAI"
    """AMOUNT_INCOMPATIBLE."""

    PPAR = "PPAR"
    """AUTH_RESULT."""

    PPAU = "PPAU"
    """MCC_CODE."""

    PPAV = "PPAV"
    """ARC_AVS."""

    PPAX = "PPAX"
    """AMOUNT_EXCEEDED."""

    PPBG = "PPBG"
    """BAD_GAMING."""

    PPC2 = "PPC2"
    """ARC_CVV."""

    PPCE = "PPCE"
    """CE_REGISTRATION_INCOMPLETE."""

    PPCO = "PPCO"
    """COUNTRY."""

    PPCR = "PPCR"
    """CREDIT_ERROR."""

    PPCT = "PPCT"
    """CARD_TYPE_UNSUPPORTED."""

    PPCU = "PPCU"
    """CURRENCY_USED_INVALID."""

    PPD3 = "PPD3"
    """SECURE_ERROR_3DS."""

    PPDC = "PPDC"
    """DCC_UNSUPPORTED."""

    PPDI = "PPDI"
    """DINERS_REJECT."""

    PPDV = "PPDV"
    """AUTH_MESSAGE."""

    PPDT = "PPDT"
    """DECLINE_THRESHOLD_BREACH."""

    PPEF = "PPEF"
    """EXPIRED_FUNDING_INSTRUMENT."""

    PPEL = "PPEL"
    """EXCEEDS_FREQUENCY_LIMIT."""

    PPER = "PPER"
    """INTERNAL_SYSTEM_ERROR."""

    PPEX = "PPEX"
    """EXPIRY_DATE."""

    PPFE = "PPFE"
    """FUNDING_SOURCE_ALREADY_EXISTS."""

    PPFI = "PPFI"
    """INVALID_FUNDING_INSTRUMENT."""

    PPFR = "PPFR"
    """RESTRICTED_FUNDING_INSTRUMENT."""

    PPFV = "PPFV"
    """FIELD_VALIDATION_FAILED."""

    PPGR = "PPGR"
    """GAMING_REFUND_ERROR."""

    PPH1 = "PPH1"
    """H1_ERROR."""

    PPIF = "PPIF"
    """IDEMPOTENCY_FAILURE."""

    PPII = "PPII"
    """INVALID_INPUT_FAILURE."""

    PPIM = "PPIM"
    """ID_MISMATCH."""

    PPIT = "PPIT"
    """INVALID_TRACE_ID."""

    PPLR = "PPLR"
    """LATE_REVERSAL."""

    PPLS = "PPLS"
    """LARGE_STATUS_CODE."""

    PPMB = "PPMB"
    """MISSING_BUSINESS_RULE_OR_DATA."""

    PPMC = "PPMC"
    """BLOCKED_Mastercard."""

    PPMD = "PPMD"
    """DEPRECATED The PPMD value has been deprecated."""

    PPNC = "PPNC"
    """NOT_SUPPORTED_NRC."""

    PPNL = "PPNL"
    """EXCEEDS_NETWORK_FREQUENCY_LIMIT."""

    PPNM = "PPNM"
    """NO_MID_FOUND."""

    PPNT = "PPNT"
    """NETWORK_ERROR."""

    PPPH = "PPPH"
    """NO_PHONE_FOR_DCC_TRANSACTION."""

    PPPI = "PPPI"
    """INVALID_PRODUCT."""

    PPPM = "PPPM"
    """INVALID_PAYMENT_METHOD."""

    PPQC = "PPQC"
    """QUASI_CASH_UNSUPPORTED."""

    PPRE = "PPRE"
    """UNSUPPORT_REFUND_ON_PENDING_BC."""

    PPRF = "PPRF"
    """INVALID_PARENT_TRANSACTION_STATUS."""

    PPRR = "PPRR"
    """MERCHANT_NOT_REGISTERED."""

    PPS0 = "PPS0"
    """BANKAUTH_ROW_MISMATCH."""

    PPS1 = "PPS1"
    """BANKAUTH_ROW_SETTLED."""

    PPS2 = "PPS2"
    """BANKAUTH_ROW_VOIDED."""

    PPS3 = "PPS3"
    """BANKAUTH_EXPIRED."""

    PPS4 = "PPS4"
    """CURRENCY_MISMATCH."""

    PPS5 = "PPS5"
    """CREDITCARD_MISMATCH."""

    PPS6 = "PPS6"
    """AMOUNT_MISMATCH."""

    PPSC = "PPSC"
    """ARC_SCORE."""

    PPSD = "PPSD"
    """STATUS_DESCRIPTION."""

    PPSE = "PPSE"
    """AMEX_DENIED."""

    PPTE = "PPTE"
    """VERIFICATION_TOKEN_EXPIRED."""

    PPTF = "PPTF"
    """INVALID_TRACE_REFERENCE."""

    PPTI = "PPTI"
    """INVALID_TRANSACTION_ID."""

    PPTR = "PPTR"
    """VERIFICATION_TOKEN_REVOKED."""

    PPTT = "PPTT"
    """TRANSACTION_TYPE_UNSUPPORTED."""

    PPTV = "PPTV"
    """INVALID_VERIFICATION_TOKEN."""

    PPUA = "PPUA"
    """USER_NOT_AUTHORIZED."""

    PPUC = "PPUC"
    """CURRENCY_CODE_UNSUPPORTED."""

    PPUE = "PPUE"
    """UNSUPPORT_ENTITY."""

    PPUI = "PPUI"
    """UNSUPPORT_INSTALLMENT."""

    PPUP = "PPUP"
    """UNSUPPORT_POS_FLAG."""

    PPUR = "PPUR"
    """UNSUPPORTED_REVERSAL."""

    PPVC = "PPVC"
    """VALIDATE_CURRENCY."""

    PPVE = "PPVE"
    """VALIDATION_ERROR."""

    PPVT = "PPVT"
    """VIRTUAL_TERMINAL_UNSUPPORTED."""

    __str__ = str.__str__


ProcessorResponseCodeOrStr: TypeAlias = Annotated[
    ProcessorResponseCode | str, open_enum_validator(ProcessorResponseCode)
]
