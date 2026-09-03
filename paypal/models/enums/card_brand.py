from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CardBrand(str, Enum):
    """The card network or brand. Applies to credit, debit, gift, and payment cards."""

    VISA = "VISA"
    """Visa card."""

    MASTERCARD = "MASTERCARD"
    """Mastercard card."""

    DISCOVER = "DISCOVER"
    """Discover card."""

    AMEX = "AMEX"
    """American Express card."""

    SOLO = "SOLO"
    """Solo debit card."""

    JCB = "JCB"
    """Japan Credit Bureau card."""

    STAR = "STAR"
    """Military Star card."""

    DELTA = "DELTA"
    """Delta Airlines card."""

    SWITCH = "SWITCH"
    """Switch credit card."""

    MAESTRO = "MAESTRO"
    """Maestro credit card."""

    CB_NATIONALE = "CB_NATIONALE"
    """Carte Bancaire (CB) credit card."""

    CONFIGOGA = "CONFIGOGA"
    """Configoga credit card."""

    CONFIDIS = "CONFIDIS"
    """Confidis credit card."""

    ELECTRON = "ELECTRON"
    """Visa Electron credit card."""

    CETELEM = "CETELEM"
    """Cetelem credit card."""

    CHINA_UNION_PAY = "CHINA_UNION_PAY"
    """China union pay credit card."""

    DINERS = "DINERS"
    """The Diners Club International banking and payment services capability network owned by Discover Financial
    Services (DFS), one of the most recognized brands in US financial services."""

    ELO = "ELO"
    """The Brazilian Elo card payment network."""

    HIPER = "HIPER"
    """The Hiper - Ingenico ePayment network."""

    HIPERCARD = "HIPERCARD"
    """The Brazilian Hipercard payment network that's widely accepted in the retail market."""

    RUPAY = "RUPAY"
    """The RuPay payment network."""

    GE = "GE"
    """The GE Credit Union 3Point card payment network."""

    SYNCHRONY = "SYNCHRONY"
    """The Synchrony Financial (SYF) payment network."""

    EFTPOS = "EFTPOS"
    """The Electronic Fund Transfer At Point of Sale(EFTPOS) Debit card payment network."""

    CARTE_BANCAIRE = "CARTE_BANCAIRE"
    """The Carte Bancaire payment network."""

    STAR_ACCESS = "STAR_ACCESS"
    """The Star Access payment network."""

    PULSE = "PULSE"
    """The Pulse payment network."""

    NYCE = "NYCE"
    """The NYCE payment network."""

    ACCEL = "ACCEL"
    """The Accel payment network."""

    UNKNOWN = "UNKNOWN"
    """UNKNOWN payment network."""

    __str__ = str.__str__


CardBrandOrStr: TypeAlias = Annotated[CardBrand | str, open_enum_validator(CardBrand)]
