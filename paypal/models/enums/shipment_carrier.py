from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ShipmentCarrier(str, Enum):
    """The carrier for the shipment. Some carriers have a global version as well as local subsidiaries. The subsidiaries
    are repeated over many countries and might also have an entry in the global list. Choose the carrier for your
    country. If the carrier is not available for your country, choose the global version of the carrier. If your carrier
    name is not in the list, set ``carrier`` to ``OTHER`` and set carrier name in ``carrier_name_other``. For allowed
    values, see Carriers."""

    DPD_RU = "DPD_RU"
    """DPD Russia."""

    BG_BULGARIAN_POST = "BG_BULGARIAN_POST"
    """Bulgarian Posts."""

    KR_KOREA_POST = "KR_KOREA_POST"
    """Koreapost (www.koreapost.go.kr)."""

    ZA_COURIERIT = "ZA_COURIERIT"
    """Courier IT."""

    FR_EXAPAQ = "FR_EXAPAQ"
    """DPD France (formerly exapaq)."""

    ARE_EMIRATES_POST = "ARE_EMIRATES_POST"
    """Emirates Post."""

    GAC = "GAC"
    """GAC."""

    GEIS = "GEIS"
    """Geis CZ."""

    SF_EX = "SF_EX"
    """SF Express."""

    PAGO = "PAGO"
    """Pago Logistics."""

    MYHERMES = "MYHERMES"
    """MyHermes UK."""

    DIAMOND_EUROGISTICS = "DIAMOND_EUROGISTICS"
    """Diamond Eurogistics Limited."""

    CORPORATECOURIERS_WEBHOOK = "CORPORATECOURIERS_WEBHOOK"
    """Corporate Couriers."""

    BOND = "BOND"
    """Bond courier."""

    OMNIPARCEL = "OMNIPARCEL"
    """Omni Parcel."""

    SK_POSTA = "SK_POSTA"
    """Slovenska pošta."""

    PUROLATOR = "PUROLATOR"
    """purolator."""

    FETCHR_WEBHOOK = "FETCHR_WEBHOOK"
    """Mena 360 (Fetchr)."""

    THEDELIVERYGROUP = "THEDELIVERYGROUP"
    """TDG – The Delivery Group."""

    CELLO_SQUARE = "CELLO_SQUARE"
    """Cello Square."""

    TARRIVE = "TARRIVE"
    """TONDA GLOBAL."""

    COLLIVERY = "COLLIVERY"
    """MDS Collivery Pty (Ltd)."""

    MAINFREIGHT = "MAINFREIGHT"
    """Mainfreight."""

    IND_FIRSTFLIGHT = "IND_FIRSTFLIGHT"
    """First Flight Couriers."""

    ACSWORLDWIDE = "ACSWORLDWIDE"
    """ACS Worldwide Express."""

    AMSTAN = "AMSTAN"
    """Amstan Logistics."""

    OKAYPARCEL = "OKAYPARCEL"
    """OkayParcel."""

    ENVIALIA_REFERENCE = "ENVIALIA_REFERENCE"
    """Envialia Reference."""

    SEUR_ES = "SEUR_ES"
    """Seur Spain."""

    CONTINENTAL = "CONTINENTAL"
    """Continental."""

    FDSEXPRESS = "FDSEXPRESS"
    """FDSEXPRESS."""

    AMAZON_FBA_SWISHIP = "AMAZON_FBA_SWISHIP"
    """Swiship UK."""

    WYNGS = "WYNGS"
    """Wyngs."""

    DHL_ACTIVE_TRACING = "DHL_ACTIVE_TRACING"
    """DHL Active Tracing."""

    ZYLLEM = "ZYLLEM"
    """Zyllem."""

    RUSTON = "RUSTON"
    """Ruston."""

    XPOST = "XPOST"
    """Xpost.ph."""

    CORREOS_ES = "CORREOS_ES"
    """correos Express (www.correos.es)."""

    DHL_FR = "DHL_FR"
    """DHL France (www.dhl.com)."""

    PAN_ASIA = "PAN_ASIA"
    """Pan-Asia International."""

    BRT_IT = "BRT_IT"
    """BRT couriers Italy (www.brt.it)."""

    SRE_KOREA = "SRE_KOREA"
    """SRE Korea (www.srekorea.co.kr)."""

    SPEEDEE = "SPEEDEE"
    """Spee-Dee Delivery."""

    TNT_UK = "TNT_UK"
    """TNT UK Limited (www.tnt.com)."""

    VENIPAK = "VENIPAK"
    """Venipak."""

    SHREENANDANCOURIER = "SHREENANDANCOURIER"
    """SHREE NANDAN COURIER."""

    CROSHOT = "CROSHOT"
    """Croshot."""

    NIPOST_NG = "NIPOST_NG"
    """NIpost (www.nipost.gov.ng)."""

    EPST_GLBL = "EPST_GLBL"
    """ePost Global."""

    NEWGISTICS = "NEWGISTICS"
    """Newgistics."""

    POST_SLOVENIA = "POST_SLOVENIA"
    """Post of Slovenia."""

    JERSEY_POST = "JERSEY_POST"
    """Jersey Post."""

    BOMBINOEXP = "BOMBINOEXP"
    """Bombino Express Pvt."""

    WMG = "WMG"
    """WMG Delivery."""

    XQ_EXPRESS = "XQ_EXPRESS"
    """XQ Express."""

    FURDECO = "FURDECO"
    """Furdeco."""

    LHT_EXPRESS = "LHT_EXPRESS"
    """LHT Express."""

    SOUTH_AFRICAN_POST_OFFICE = "SOUTH_AFRICAN_POST_OFFICE"
    """South African Post Office."""

    SPOTON = "SPOTON"
    """SPOTON Logistics Pvt Ltd."""

    DIMERCO = "DIMERCO"
    """Dimerco Express Group."""

    CYPRUS_POST_CYP = "CYPRUS_POST_CYP"
    """cyprus post."""

    ABCUSTOM = "ABCUSTOM"
    """AB Custom Group."""

    IND_DELIVREE = "IND_DELIVREE"
    """deliverE."""

    CN_BESTEXPRESS = "CN_BESTEXPRESS"
    """Best Express."""

    DX_SFTP = "DX_SFTP"
    """DX (SFTP)."""

    PICKUPP_MYS = "PICKUPP_MYS"
    """PICK UPP."""

    FMX = "FMX"
    """FMX."""

    HELLMANN = "HELLMANN"
    """Hellmann Worldwide Logistics."""

    SHIP_IT_ASIA = "SHIP_IT_ASIA"
    """Ship It Asia."""

    KERRY_ECOMMERCE = "KERRY_ECOMMERCE"
    """Kerry eCommerce."""

    FRETERAPIDO = "FRETERAPIDO"
    """Frete Rapido."""

    PITNEY_BOWES = "PITNEY_BOWES"
    """Pitney Bowes."""

    XPRESSEN_DK = "XPRESSEN_DK"
    """Xpressen courier."""

    SEUR_SP_API = "SEUR_SP_API"
    """Spanish Seur API."""

    DELIVERYONTIME = "DELIVERYONTIME"
    """DELIVERYONTIME LOGISTICS PVT LTD."""

    JINSUNG = "JINSUNG"
    """JINSUNG TRADING."""

    TRANS_KARGO = "TRANS_KARGO"
    """Trans Kargo Internasional."""

    SWISHIP_DE = "SWISHIP_DE"
    """Swiship DE."""

    IVOY_WEBHOOK = "IVOY_WEBHOOK"
    """Ivoy courier."""

    AIRMEE_WEBHOOK = "AIRMEE_WEBHOOK"
    """Airmee couriers."""

    DHL_BENELUX = "DHL_BENELUX"
    """dhl benelux."""

    FIRSTMILE = "FIRSTMILE"
    """FirstMile."""

    FASTWAY_IR = "FASTWAY_IR"
    """Fastway Ireland."""

    HH_EXP = "HH_EXP"
    """Hua Han Logistics."""

    MYS_MYPOST_ONLINE = "MYS_MYPOST_ONLINE"
    """Mypostonline."""

    TNT_NL = "TNT_NL"
    """THT Netherland."""

    TIPSA = "TIPSA"
    """TIPSA courier."""

    TAQBIN_MY = "TAQBIN_MY"
    """TAQBIN Malaysia."""

    KGMHUB = "KGMHUB"
    """KGM Hub."""

    INTEXPRESS = "INTEXPRESS"
    """Internet Express."""

    OVERSE_EXP = "OVERSE_EXP"
    """Overseas Express."""

    ONECLICK = "ONECLICK"
    """One click delivery services."""

    ROADRUNNER_FREIGHT = "ROADRUNNER_FREIGHT"
    """Roadbull Logistics."""

    GLS_CROTIA = "GLS_CROTIA"
    """GLS Croatia."""

    MRW_FTP = "MRW_FTP"
    """MRW courier."""

    BLUEX = "BLUEX"
    """Blue Express."""

    DYLT = "DYLT"
    """Daylight Transport."""

    DPD_IR = "DPD_IR"
    """DPD Ireland."""

    SIN_GLBL = "SIN_GLBL"
    """Sin Global Express."""

    TUFFNELLS_REFERENCE = "TUFFNELLS_REFERENCE"
    """Tuffnells Parcels Express- Reference."""

    CJPACKET = "CJPACKET"
    """CJ Packet."""

    MILKMAN = "MILKMAN"
    """Milkman courier."""

    ASIGNA = "ASIGNA"
    """ASIGNA courier."""

    ONEWORLDEXPRESS = "ONEWORLDEXPRESS"
    """One World Express."""

    ROYAL_MAIL = "ROYAL_MAIL"
    """RoyalShipments."""

    VIA_EXPRESS = "VIA_EXPRESS"
    """Viaxpress."""

    TIGFREIGHT = "TIGFREIGHT"
    """TIG Freight."""

    ZTO_EXPRESS = "ZTO_EXPRESS"
    """ZTO Express."""

    TWO_GO = "TWO_GO"
    """2GO Courier."""

    IML = "IML"
    """IML courier."""

    INTEL_VALLEY = "INTEL_VALLEY"
    """Intel-Valley Supply chain (ShenZhen) Co. Ltd."""

    EFS = "EFS"
    """EFS (E-commerce Fulfillment Service)."""

    UK_UK_MAIL = "UK_UK_MAIL"
    """UK mail (ukmail.com)."""

    RAM = "RAM"
    """RAM courier."""

    ALLIEDEXPRESS = "ALLIEDEXPRESS"
    """Allied Express."""

    APC_OVERNIGHT = "APC_OVERNIGHT"
    """APC overnight (apc-overnight.com)."""

    SHIPPIT = "SHIPPIT"
    """Shippit."""

    TFM = "TFM"
    """TFM Xpress."""

    M_XPRESS = "M_XPRESS"
    """M Xpress Sdn Bhd."""

    HDB_BOX = "HDB_BOX"
    """Haidaibao (BOX)."""

    CLEVY_LINKS = "CLEVY_LINKS"
    """Clevy Links."""

    IBEONE = "IBEONE"
    """Beone Logistics."""

    FIEGE_NL = "FIEGE_NL"
    """Fiege Netherlands."""

    KWE_GLOBAL = "KWE_GLOBAL"
    """KWE Global."""

    CTC_EXPRESS = "CTC_EXPRESS"
    """CTC Express."""

    AMAZON = "AMAZON"
    """Amazon Shipping."""

    MORE_LINK = "MORE_LINK"
    """Morelink."""

    JX = "JX"
    """JX courier."""

    EASY_MAIL = "EASY_MAIL"
    """Easy Mail."""

    ADUIEPYLE = "ADUIEPYLE"
    """A Duie Pyle."""

    GB_PANTHER = "GB_PANTHER"
    """Panther."""

    EXPRESSSALE = "EXPRESSSALE"
    """Expresssale."""

    SG_DETRACK = "SG_DETRACK"
    """Detrack."""

    TRUNKRS_WEBHOOK = "TRUNKRS_WEBHOOK"
    """Trunkrs courier."""

    MATDESPATCH = "MATDESPATCH"
    """Matdespatch."""

    DICOM = "DICOM"
    """GLS Logistic Systems Canada Ltd./Dicom."""

    MBW = "MBW"
    """MBW Courier Inc.."""

    KHM_CAMBODIA_POST = "KHM_CAMBODIA_POST"
    """Cambodia Post."""

    SINOTRANS = "SINOTRANS"
    """Sinotrans."""

    BRT_IT_PARCELID = "BRT_IT_PARCELID"
    """BRT Bartolini(Parcel ID)."""

    DHL_SUPPLY_CHAIN = "DHL_SUPPLY_CHAIN"
    """DHL Supply Chain APAC."""

    DHL_PL = "DHL_PL"
    """DHL Poland."""

    TOPYOU = "TOPYOU"
    """TopYou."""

    PALEXPRESS = "PALEXPRESS"
    """PAL Express Limited."""

    DHL_SG = "DHL_SG"
    """dhl Singapore."""

    CN_WEDO = "CN_WEDO"
    """WeDo Logistics."""

    FULFILLME = "FULFILLME"
    """Fulfillme."""

    DPD_DELISTRACK = "DPD_DELISTRACK"
    """DPD delistrack."""

    UPS_REFERENCE = "UPS_REFERENCE"
    """UPS Reference."""

    CARIBOU = "CARIBOU"
    """Caribou."""

    LOCUS_WEBHOOK = "LOCUS_WEBHOOK"
    """Locus courier."""

    DSV = "DSV"
    """DSV courier."""

    P2_P_TRC = "P2P_TRC"
    """P2P TrakPak."""

    DIRECTPARCELS = "DIRECTPARCELS"
    """Direct Parcels."""

    NOVA_POSHTA_INT = "NOVA_POSHTA_INT"
    """Nova Poshta (International)."""

    FEDEX_POLAND = "FEDEX_POLAND"
    """FedEx® Poland Domestic."""

    CN_JCEX = "CN_JCEX"
    """JCEX courier."""

    FAR_INTERNATIONAL = "FAR_INTERNATIONAL"
    """FAR international."""

    IDEXPRESS = "IDEXPRESS"
    """IDEX courier."""

    GANGBAO = "GANGBAO"
    """GANGBAO Supplychain."""

    NEWAY = "NEWAY"
    """Neway Transport."""

    POSTNL_INT_3_S = "POSTNL_INT_3_S"
    """PostNL International."""

    RPX_ID = "RPX_ID"
    """RPX Indonesia."""

    DESIGNERTRANSPORT_WEBHOOK = "DESIGNERTRANSPORT_WEBHOOK"
    """Designer Transport."""

    GLS_SLOVEN = "GLS_SLOVEN"
    """GLS Slovenia."""

    PARCELLED_IN = "PARCELLED_IN"
    """Parcelled.in."""

    GSI_EXPRESS = "GSI_EXPRESS"
    """GSI EXPRESS."""

    CON_WAY = "CON_WAY"
    """Con-way Freight."""

    BROUWER_TRANSPORT = "BROUWER_TRANSPORT"
    """Brouwer Transport en Logistiek."""

    CPEX = "CPEX"
    """Captain Express International."""

    ISRAEL_POST = "ISRAEL_POST"
    """Israel Post."""

    DTDC_IN = "DTDC_IN"
    """DTDC India."""

    PTT_POST = "PTT_POST"
    """PTT Post."""

    XDE_WEBHOOK = "XDE_WEBHOOK"
    """Ximex Delivery Express."""

    TOLOS = "TOLOS"
    """Tolos courier."""

    GIAO_HANG = "GIAO_HANG"
    """Giao hàng nhanh."""

    GEODIS_ESPACE = "GEODIS_ESPACE"
    """Geodis E-space."""

    MAGYAR_HU = "MAGYAR_HU"
    """Magyar Post."""

    DOORDASH_WEBHOOK = "DOORDASH_WEBHOOK"
    """DoorDash."""

    TIKI_ID = "TIKI_ID"
    """Tiki shipment."""

    CJ_HK_INTERNATIONAL = "CJ_HK_INTERNATIONAL"
    """CJ Logistics International(Hong Kong)."""

    STAR_TRACK_EXPRESS = "STAR_TRACK_EXPRESS"
    """Star Track Express."""

    HELTHJEM = "HELTHJEM"
    """Helthjem."""

    SFB2_C = "SFB2C"
    """SF International."""

    FREIGHTQUOTE = "FREIGHTQUOTE"
    """Freightquote by C.H. Robinson."""

    LANDMARK_GLOBAL_REFERENCE = "LANDMARK_GLOBAL_REFERENCE"
    """Landmark Global Reference."""

    PARCEL2_GO = "PARCEL2GO"
    """Parcel2Go."""

    DELNEXT = "DELNEXT"
    """Delnext."""

    RCL = "RCL"
    """Red Carpet Logistics."""

    CGS_EXPRESS = "CGS_EXPRESS"
    """CGS Express."""

    HK_POST = "HK_POST"
    """Hongkong Post (www.hongkongpost.hk)."""

    SAP_EXPRESS = "SAP_EXPRESS"
    """SAP EXPRESS."""

    PARCELPOST_SG = "PARCELPOST_SG"
    """Parcel Post Singapore."""

    HERMES = "HERMES"
    """HermesWorld UK."""

    IND_SAFEEXPRESS = "IND_SAFEEXPRESS"
    """Safexpress."""

    TOPHATTEREXPRESS = "TOPHATTEREXPRESS"
    """Tophatter Express."""

    MGLOBAL = "MGLOBAL"
    """PT MGLOBAL LOGISTICS INDONESIA."""

    AVERITT = "AVERITT"
    """Averitt Express."""

    LEADER = "LEADER"
    """leader."""

    _2_EBOX = "_2EBOX"
    """2ebox courier."""

    SG_SPEEDPOST = "SG_SPEEDPOST"
    """Singapore Speedpost."""

    DBSCHENKER_SE = "DBSCHENKER_SE"
    """DB Schenker (www.dbschenker.com)."""

    ISR_POST_DOMESTIC = "ISR_POST_DOMESTIC"
    """Israel Post Domestic."""

    BESTWAYPARCEL = "BESTWAYPARCEL"
    """Best Way Parcel."""

    ASENDIA_DE = "ASENDIA_DE"
    """asendia_de."""

    NIGHTLINE_UK = "NIGHTLINE_UK"
    """nightline_uk."""

    TAQBIN_SG = "TAQBIN_SG"
    """taqbin_sg."""

    TCK_EXPRESS = "TCK_EXPRESS"
    """TCK Express."""

    ENDEAVOUR_DELIVERY = "ENDEAVOUR_DELIVERY"
    """Endeavour Delivery."""

    NANJINGWOYUAN = "NANJINGWOYUAN"
    """Nanjing Woyuan."""

    HEPPNER_FR = "HEPPNER_FR"
    """Heppner France."""

    EMPS_CN = "EMPS_CN"
    """EMPS Express."""

    FONSEN = "FONSEN"
    """Fonsen Logistics."""

    PICKRR = "PICKRR"
    """Pickrr."""

    APC_OVERNIGHT_CONNUM = "APC_OVERNIGHT_CONNUM"
    """APC Overnight Consignment."""

    STAR_TRACK_NEXT_FLIGHT = "STAR_TRACK_NEXT_FLIGHT"
    """Star Track Next Flight."""

    DAJIN = "DAJIN"
    """Shanghai Aqrum Chemical Logistics Co.Ltd."""

    UPS_FREIGHT = "UPS_FREIGHT"
    """UPS Freight."""

    POSTA_PLUS = "POSTA_PLUS"
    """Posta Plus."""

    CEVA = "CEVA"
    """CEVA LOGISTICS."""

    ANSERX = "ANSERX"
    """ANSERX courier."""

    JS_EXPRESS = "JS_EXPRESS"
    """JS EXPRESS."""

    PADTF = "PADTF"
    """padtf.com."""

    UPS_MAIL_INNOVATIONS = "UPS_MAIL_INNOVATIONS"
    """UPS Mail Innovations."""

    SYPOST = "SYPOST"
    """Sunyou Post."""

    AMAZON_SHIP_MCF = "AMAZON_SHIP_MCF"
    """Amazon Shipping + Amazon MCF."""

    YUSEN = "YUSEN"
    """Yusen Logistics."""

    BRING = "BRING"
    """Bring."""

    SDA_IT = "SDA_IT"
    """SDA Italy."""

    GBA = "GBA"
    """GBA Services Ltd."""

    NEWEGGEXPRESS = "NEWEGGEXPRESS"
    """Newegg Express."""

    SPEEDCOURIERS_GR = "SPEEDCOURIERS_GR"
    """Speed Couriers."""

    FORRUN = "FORRUN"
    """forrun Pvt Ltd (Arpatech Venture)."""

    PICKUP = "PICKUP"
    """Pickupp."""

    ECMS = "ECMS"
    """ECMS International Logistics Co.."""

    INTELIPOST = "INTELIPOST"
    """Intelipost (TMS for LATAM)."""

    FLASHEXPRESS = "FLASHEXPRESS"
    """Flash Express."""

    CN_STO = "CN_STO"
    """STO Express."""

    SEKO_SFTP = "SEKO_SFTP"
    """SEKO Worldwide."""

    HOME_DELIVERY_SOLUTIONS = "HOME_DELIVERY_SOLUTIONS"
    """Home Delivery Solutions Ltd."""

    DPD_HGRY = "DPD_HGRY"
    """DPD Hungary."""

    KERRYTTC_VN = "KERRYTTC_VN"
    """Kerry Express (Vietnam) Co Ltd."""

    JOYING_BOX = "JOYING_BOX"
    """Joying Box."""

    TOTAL_EXPRESS = "TOTAL_EXPRESS"
    """Total Express."""

    ZJS_EXPRESS = "ZJS_EXPRESS"
    """ZJS International."""

    STARKEN = "STARKEN"
    """STARKEN couriers."""

    DEMANDSHIP = "DEMANDSHIP"
    """DemandShip."""

    CN_DPEX = "CN_DPEX"
    """DPEX."""

    AUPOST_CN = "AUPOST_CN"
    """AuPost China."""

    LOGISTERS = "LOGISTERS"
    """Logisters."""

    GOGLOBALPOST = "GOGLOBALPOST"
    """Global Post."""

    GLS_CZ = "GLS_CZ"
    """GLS Czech Republic."""

    PAACK_WEBHOOK = "PAACK_WEBHOOK"
    """Paack courier."""

    GRAB_WEBHOOK = "GRAB_WEBHOOK"
    """Grab courier."""

    PARCELPOINT = "PARCELPOINT"
    """Parcelpoint."""

    ICUMULUS = "ICUMULUS"
    """iCumulus."""

    DAIGLOBALTRACK = "DAIGLOBALTRACK"
    """DAI Post."""

    GLOBAL_IPARCEL = "GLOBAL_IPARCEL"
    """i-parcel."""

    YURTICI_KARGO = "YURTICI_KARGO"
    """Yurtici Kargo."""

    CN_PAYPAL_PACKAGE = "CN_PAYPAL_PACKAGE"
    """PayPal Package."""

    PARCEL_2_POST = "PARCEL_2_POST"
    """Parcel To Post."""

    GLS_IT = "GLS_IT"
    """GLS Italy."""

    PIL_LOGISTICS = "PIL_LOGISTICS"
    """PIL Logistics (China) Co.."""

    HEPPNER = "HEPPNER"
    """Heppner Internationale Spedition GmbH & Co.."""

    GENERAL_OVERNIGHT = "GENERAL_OVERNIGHT"
    """Go!Express and logistics."""

    HAPPY2_POINT = "HAPPY2POINT"
    """Happy 2ThePoint."""

    CHITCHATS = "CHITCHATS"
    """Chit Chats."""

    SMOOTH = "SMOOTH"
    """Smooth Couriers."""

    CLE_LOGISTICS = "CLE_LOGISTICS"
    """CL E-Logistics Solutions Limited."""

    FIEGE = "FIEGE"
    """Fiege Logistics."""

    MX_CARGO = "MX_CARGO"
    """M&X cargo."""

    ZIINGFINALMILE = "ZIINGFINALMILE"
    """Ziing Final Mile Inc."""

    DAYTON_FREIGHT = "DAYTON_FREIGHT"
    """Dayton Freight."""

    TCS = "TCS"
    """TCS courier."""

    AEX = "AEX"
    """AEX Group."""

    HERMES_DE = "HERMES_DE"
    """Hermes Germany."""

    ROUTIFIC_WEBHOOK = "ROUTIFIC_WEBHOOK"
    """Routific."""

    GLOBAVEND = "GLOBAVEND"
    """Globavend."""

    CJ_LOGISTICS = "CJ_LOGISTICS"
    """CJ Logistics International."""

    PALLET_NETWORK = "PALLET_NETWORK"
    """The Pallet Network."""

    RAF_PH = "RAF_PH"
    """RAF Philippines."""

    UK_XDP = "UK_XDP"
    """XDP Express."""

    PAPER_EXPRESS = "PAPER_EXPRESS"
    """Paper Express."""

    LA_POSTE_SUIVI = "LA_POSTE_SUIVI"
    """La Poste."""

    PAQUETEXPRESS = "PAQUETEXPRESS"
    """Paquetexpress."""

    LIEFERY = "LIEFERY"
    """liefery."""

    STRECK_TRANSPORT = "STRECK_TRANSPORT"
    """Streck Transport."""

    PONY_EXPRESS = "PONY_EXPRESS"
    """Pony express."""

    ALWAYS_EXPRESS = "ALWAYS_EXPRESS"
    """Always Express."""

    GBS_BROKER = "GBS_BROKER"
    """GBS-Broker."""

    CITYLINK_MY = "CITYLINK_MY"
    """City-Link Express."""

    ALLJOY = "ALLJOY"
    """ALLJOY SUPPLY CHAIN."""

    YODEL = "YODEL"
    """yodel."""

    YODEL_DIR = "YODEL_DIR"
    """Yodel Direct."""

    STONE3_PL = "STONE3PL"
    """STONE3PL."""

    PARCELPAL_WEBHOOK = "PARCELPAL_WEBHOOK"
    """ParcelPal."""

    DHL_ECOMERCE_ASA = "DHL_ECOMERCE_ASA"
    """DHL eCommerce Asia (API)."""

    SIMPLYPOST = "SIMPLYPOST"
    """J&T Express Singapore."""

    KY_EXPRESS = "KY_EXPRESS"
    """Kua Yue Express."""

    SHENZHEN = "SHENZHEN"
    """shenzhen 1st International Logistics(Group)Co."""

    US_LASERSHIP = "US_LASERSHIP"
    """LaserShip."""

    UC_EXPRE = "UC_EXPRE"
    """ucexpress."""

    DIDADI = "DIDADI"
    """DIDADI Logistics tech."""

    CJ_KR = "CJ_KR"
    """CJ Korea Express."""

    DBSCHENKER_B2_B = "DBSCHENKER_B2B"
    """DB Schenker B2B."""

    MXE = "MXE"
    """MXE Express."""

    CAE_DELIVERS = "CAE_DELIVERS"
    """CAE Delivers."""

    PFCEXPRESS = "PFCEXPRESS"
    """PFC Express."""

    WHISTL = "WHISTL"
    """Whistl."""

    WEPOST = "WEPOST"
    """WePost Sdn Bhd."""

    DHL_PARCEL_ES = "DHL_PARCEL_ES"
    """DHL parcel Spain(www.dhl.com)."""

    DDEXPRESS = "DDEXPRESS"
    """DD Express Courier."""

    ARAMEX_AU = "ARAMEX_AU"
    """Aramex Australia (formerly Fastway AU)."""

    BNEED = "BNEED"
    """Bneed courier."""

    HK_TGX = "HK_TGX"
    """Kerry Express Hong Kong."""

    LATVIJAS_PASTS = "LATVIJAS_PASTS"
    """Latvijas Pasts."""

    VIAEUROPE = "VIAEUROPE"
    """ViaEurope."""

    CORREO_UY = "CORREO_UY"
    """Correo Uruguayo."""

    CHRONOPOST_FR = "CHRONOPOST_FR"
    """Chronopost france (www.chronopost.fr)."""

    J_NET = "J_NET"
    """J-Net."""

    _6_LS = "_6LS"
    """6ls.com."""

    BLR_BELPOST = "BLR_BELPOST"
    """Belpost."""

    BIRDSYSTEM = "BIRDSYSTEM"
    """BirdSystem."""

    DOBROPOST = "DOBROPOST"
    """DobroPost."""

    WAHANA_ID = "WAHANA_ID"
    """Wahana express (www.wahana.com)."""

    WEASHIP = "WEASHIP"
    """Weaship."""

    SONICTL = "SONICTL"
    """Sonic Transportation & Logistics."""

    KWT = "KWT"
    """Shenzhen Jinghuada Logistics Co.."""

    AFLLOG_FTP = "AFLLOG_FTP"
    """AFL LOGISTICS."""

    SKYNET_WORLDWIDE = "SKYNET_WORLDWIDE"
    """SkyNet Worldwide Express."""

    NOVA_POSHTA = "NOVA_POSHTA"
    """Nova Poshta (novaposhta.ua)."""

    SEINO = "SEINO"
    """Seino."""

    SZENDEX = "SZENDEX"
    """SZENDEX."""

    BPOST_INT = "BPOST_INT"
    """Bpost international."""

    DBSCHENKER_SV = "DBSCHENKER_SV"
    """DB Schenker Sweden."""

    AO_DEUTSCHLAND = "AO_DEUTSCHLAND"
    """AO Deutschland."""

    EU_FLEET_SOLUTIONS = "EU_FLEET_SOLUTIONS"
    """EU Fleet Solutions."""

    PCFCORP = "PCFCORP"
    """PCF Final Mile."""

    LINKBRIDGE = "LINKBRIDGE"
    """Link Bridge(BeiJing)international logistics co.."""

    PRIMAMULTICIPTA = "PRIMAMULTICIPTA"
    """PT Prima Multi Cipta."""

    COUREX = "COUREX"
    """Urbanfox."""

    ZAJIL_EXPRESS = "ZAJIL_EXPRESS"
    """Zajil Express Company."""

    COLLECTCO = "COLLECTCO"
    """CollectCo."""

    JTEXPRESS = "JTEXPRESS"
    """J&T EXPRESS MALAYSIA."""

    FEDEX_UK = "FEDEX_UK"
    """FedEx® UK."""

    USHIP = "USHIP"
    """uShip courier."""

    PIXSELL = "PIXSELL"
    """PIXSELL LOGISTICS."""

    SHIPTOR = "SHIPTOR"
    """Shiptor."""

    CDEK = "CDEK"
    """CDEK courier."""

    VNM_VIETTELPOST = "VNM_VIETTELPOST"
    """ViettelPost."""

    CJ_CENTURY = "CJ_CENTURY"
    """CJ Century."""

    GSO = "GSO"
    """GSO(GLS-USA)."""

    VIWO = "VIWO"
    """VIWO IoT."""

    SKYBOX = "SKYBOX"
    """SKYBOX."""

    KERRYTJ = "KERRYTJ"
    """Kerry TJ Logistics."""

    NTLOGISTICS_VN = "NTLOGISTICS_VN"
    """Nhat Tin Logistics."""

    SDH_SCM = "SDH_SCM"
    """lightning monkey."""

    ZINC = "ZINC"
    """Zinc courier."""

    DPE_SOUTH_AFRC = "DPE_SOUTH_AFRC"
    """DPE South Africa."""

    CESKA_CZ = "CESKA_CZ"
    """Czech Post."""

    ACS_GR = "ACS_GR"
    """ACS Courier."""

    DEALERSEND = "DEALERSEND"
    """DealerSend."""

    JOCOM = "JOCOM"
    """Jocom."""

    CSE = "CSE"
    """CSE courier."""

    TFORCE_FINALMILE = "TFORCE_FINALMILE"
    """TForce Final Mile."""

    SHIP_GATE = "SHIP_GATE"
    """ShipGate."""

    SHIPTER = "SHIPTER"
    """SHIPTER."""

    NATIONAL_SAMEDAY = "NATIONAL_SAMEDAY"
    """National Sameday."""

    YUNEXPRESS = "YUNEXPRESS"
    """YunExpress."""

    CAINIAO = "CAINIAO"
    """AliExpress Standard Shipping."""

    DMS_MATRIX = "DMS_MATRIX"
    """DMSMatrix."""

    DIRECTLOG = "DIRECTLOG"
    """Directlog (www.directlog.com.br)."""

    ASENDIA_US = "ASENDIA_US"
    """Asendia USA."""

    _3_JMSLOGISTICS = "_3JMSLOGISTICS"
    """3JMS Logistics."""

    LICCARDI_EXPRESS = "LICCARDI_EXPRESS"
    """LICCARDI EXPRESS COURIER."""

    SKY_POSTAL = "SKY_POSTAL"
    """SkyPostal."""

    CNWANGTONG = "CNWANGTONG"
    """cnwangtong."""

    POSTNORD_LOGISTICS_DK = "POSTNORD_LOGISTICS_DK"
    """ostnord denmark."""

    LOGISTIKA = "LOGISTIKA"
    """Logistika."""

    CELERITAS = "CELERITAS"
    """Celeritas Transporte."""

    PRESSIODE = "PRESSIODE"
    """Pressio."""

    SHREE_MARUTI = "SHREE_MARUTI"
    """Shree Maruti Courier Services Pvt Ltd."""

    LOGISTICSWORLDWIDE_HK = "LOGISTICSWORLDWIDE_HK"
    """Logistic Worldwide Express (LWE Honkong)."""

    EFEX = "EFEX"
    """eFEx (E-Commerce Fulfillment & Express)."""

    LOTTE = "LOTTE"
    """Lotte Global Logistics."""

    LONESTAR = "LONESTAR"
    """Lone Star Overnight."""

    APRISAEXPRESS = "APRISAEXPRESS"
    """Aprisa Express."""

    BEL_RS = "BEL_RS"
    """BEL North Russia."""

    OSM_WORLDWIDE = "OSM_WORLDWIDE"
    """OSM Worldwide."""

    WESTGATE_GL = "WESTGATE_GL"
    """Westgate Global."""

    FASTRACK = "FASTRACK"
    """Fasttrack."""

    DTD_EXPR = "DTD_EXPR"
    """DTD Express."""

    ALFATREX = "ALFATREX"
    """AlfaTrex."""

    PROMEDDELIVERY = "PROMEDDELIVERY"
    """ProMed Delivery."""

    THABIT_LOGISTICS = "THABIT_LOGISTICS"
    """Thabit Logistics."""

    HCT_LOGISTICS = "HCT_LOGISTICS"
    """HCT LOGISTICS CO.LTD.."""

    CARRY_FLAP = "CARRY_FLAP"
    """Carry-Flap Co.."""

    US_OLD_DOMINION = "US_OLD_DOMINION"
    """Old Dominion Freight Line."""

    ANICAM_BOX = "ANICAM_BOX"
    """ANICAM BOX EXPRESS."""

    WANBEXPRESS = "WANBEXPRESS"
    """WanbExpress."""

    AN_POST = "AN_POST"
    """An Post."""

    DPD_LOCAL = "DPD_LOCAL"
    """DPD Local."""

    STALLIONEXPRESS = "STALLIONEXPRESS"
    """Stallion Express."""

    RAIDEREX = "RAIDEREX"
    """RaidereX."""

    SHOPFANS = "SHOPFANS"
    """ShopfansRU LLC."""

    KYUNGDONG_PARCEL = "KYUNGDONG_PARCEL"
    """Kyungdong Parcel."""

    CHAMPION_LOGISTICS = "CHAMPION_LOGISTICS"
    """Champion Logistics."""

    PICKUPP_SGP = "PICKUPP_SGP"
    """PICK UPP (Singapore)."""

    MORNING_EXPRESS = "MORNING_EXPRESS"
    """Morning Express."""

    NACEX = "NACEX"
    """NACEX."""

    THENILE_WEBHOOK = "THENILE_WEBHOOK"
    """SortHub courier."""

    HOLISOL = "HOLISOL"
    """Holisol."""

    LBCEXPRESS_FTP = "LBCEXPRESS_FTP"
    """LBC EXPRESS INC.."""

    KURASI = "KURASI"
    """KURASI."""

    USF_REDDAWAY = "USF_REDDAWAY"
    """USF Reddaway."""

    APG = "APG"
    """APG eCommerce Solutions."""

    CN_BOXC = "CN_BOXC"
    """BoxC courier."""

    ECOSCOOTING = "ECOSCOOTING"
    """ECOSCOOTING."""

    MAINWAY = "MAINWAY"
    """Mainway."""

    PAPERFLY = "PAPERFLY"
    """Paperfly Private Limited."""

    HOUNDEXPRESS = "HOUNDEXPRESS"
    """Hound Express."""

    BOX_BERRY = "BOX_BERRY"
    """Boxberry courier."""

    EP_BOX = "EP_BOX"
    """EP-Box courier."""

    PLUS_LOG_UK = "PLUS_LOG_UK"
    """Plus UK Logistics."""

    FULFILLA = "FULFILLA"
    """Fulfilla."""

    ASE = "ASE"
    """ASE KARGO."""

    MAIL_PLUS = "MAIL_PLUS"
    """MailPlus."""

    XPO_LOGISTICS = "XPO_LOGISTICS"
    """XPO logistics."""

    WNDIRECT = "WNDIRECT"
    """wnDirect."""

    CLOUDWISH_ASIA = "CLOUDWISH_ASIA"
    """Cloudwish Asia."""

    ZELERIS = "ZELERIS"
    """Zeleris."""

    GIO_EXPRESS = "GIO_EXPRESS"
    """Gio Express."""

    OCS_WORLDWIDE = "OCS_WORLDWIDE"
    """OCS WORLDWIDE."""

    ARK_LOGISTICS = "ARK_LOGISTICS"
    """ARK Logistics."""

    AQUILINE = "AQUILINE"
    """Aquiline."""

    PILOT_FREIGHT = "PILOT_FREIGHT"
    """Pilot Freight Services."""

    QWINTRY = "QWINTRY"
    """Qwintry Logistics."""

    DANSKE_FRAGT = "DANSKE_FRAGT"
    """Danske Fragtaend."""

    CARRIERS = "CARRIERS"
    """Carriers courier."""

    AIR_CANADA_GLOBAL = "AIR_CANADA_GLOBAL"
    """Rivo (Air canada)."""

    PRESIDENT_TRANS = "PRESIDENT_TRANS"
    """PRESIDENT TRANSNET CORP."""

    STEPFORWARDFS = "STEPFORWARDFS"
    """STEP FORWARD FREIGHT SERVICE CO LTD."""

    SKYNET_UK = "SKYNET_UK"
    """Skynet UK."""

    PITTOHIO = "PITTOHIO"
    """PITT OHIO."""

    CORREOS_EXPRESS = "CORREOS_EXPRESS"
    """Correos Express."""

    RL_US = "RL_US"
    """RL Carriers."""

    DESTINY = "DESTINY"
    """Destiny Transportation."""

    UK_YODEL = "UK_YODEL"
    """Yodel (www.yodel.co.uk)."""

    COMET_TECH = "COMET_TECH"
    """CometTech."""

    DHL_PARCEL_RU = "DHL_PARCEL_RU"
    """DHL Parcel Russia."""

    TNT_REFR = "TNT_REFR"
    """TNT Reference."""

    SHREE_ANJANI_COURIER = "SHREE_ANJANI_COURIER"
    """Shree Anjani Courier."""

    MIKROPAKKET_BE = "MIKROPAKKET_BE"
    """Mikropakket Belgium."""

    ETS_EXPRESS = "ETS_EXPRESS"
    """RETS express."""

    COLIS_PRIVE = "COLIS_PRIVE"
    """Colis Privé."""

    CN_YUNDA = "CN_YUNDA"
    """Yunda Express."""

    AAA_COOPER = "AAA_COOPER"
    """AAA Cooper."""

    ROCKET_PARCEL = "ROCKET_PARCEL"
    """Rocket Parcel International."""

    _360_LION = "_360LION"
    """360 Lion Express."""

    PANDU = "PANDU"
    """PANDU."""

    PROFESSIONAL_COURIERS = "PROFESSIONAL_COURIERS"
    """PROFESSIONAL COURIERS."""

    FLYTEXPRESS = "FLYTEXPRESS"
    """FLYTEXPRESS."""

    LOGISTICSWORLDWIDE_MY = "LOGISTICSWORLDWIDE_MY"
    """LOGISTICSWORLDWIDE MY."""

    CORREOS_DE_ESPANA = "CORREOS_DE_ESPANA"
    """CORREOS DE ESPANA."""

    IMX = "IMX"
    """IMX."""

    FOUR_PX_EXPRESS = "FOUR_PX_EXPRESS"
    """FOUR PX EXPRESS."""

    XPRESSBEES = "XPRESSBEES"
    """XPRESSBEES."""

    PICKUPP_VNM = "PICKUPP_VNM"
    """pickupp_vnm."""

    STARTRACK_EXPRESS = "STARTRACK_EXPRESS"
    """startrack_express."""

    FR_COLISSIMO = "FR_COLISSIMO"
    """fr_colissimo."""

    NACEX_SPAIN_REFERENCE = "NACEX_SPAIN_REFERENCE"
    """nacex_spain_reference."""

    DHL_SUPPLY_CHAIN_AU = "DHL_SUPPLY_CHAIN_AU"
    """dhl_supply_chain_au."""

    ESHIPPING = "ESHIPPING"
    """Eshipping."""

    SHREETIRUPATI = "SHREETIRUPATI"
    """SHREE TIRUPATI COURIER SERVICES PVT. LTD.."""

    HX_EXPRESS = "HX_EXPRESS"
    """HX Express."""

    INDOPAKET = "INDOPAKET"
    """INDOPAKET."""

    CN_17_POST = "CN_17POST"
    """17 Post Service."""

    K1_EXPRESS = "K1_EXPRESS"
    """K1 Express."""

    CJ_GLS = "CJ_GLS"
    """CJ GLS."""

    MYS_GDEX = "MYS_GDEX"
    """GDEX courier."""

    NATIONEX = "NATIONEX"
    """Nationex courier."""

    ANJUN = "ANJUN"
    """Anjun couriers."""

    FARGOOD = "FARGOOD"
    """FarGood."""

    SMG_EXPRESS = "SMG_EXPRESS"
    """SMG Direct."""

    RZYEXPRESS = "RZYEXPRESS"
    """RZY Express."""

    SEFL = "SEFL"
    """Southeastern Freight Lines."""

    TNT_CLICK_IT = "TNT_CLICK_IT"
    """TNT-Click Italy."""

    HDB = "HDB"
    """Haidaibao."""

    HIPSHIPPER = "HIPSHIPPER"
    """Hipshipper."""

    RPXLOGISTICS = "RPXLOGISTICS"
    """RPX Logistics."""

    KUEHNE = "KUEHNE"
    """Kuehne + Nagel."""

    IT_NEXIVE = "IT_NEXIVE"
    """Nexive (TNT Post Italy)."""

    PTS = "PTS"
    """PTS courier."""

    SWISS_POST_FTP = "SWISS_POST_FTP"
    """Swiss Post FTP."""

    FASTRK_SERV = "FASTRK_SERV"
    """Fastrak Services."""

    _4_72 = "_4_72"
    """4-72 Entregando."""

    US_YRC = "US_YRC"
    """YRC courier."""

    POSTNL_INTL_3_S = "POSTNL_INTL_3S"
    """PostNL International 3S."""

    ELIAN_POST = "ELIAN_POST"
    """Yilian (Elian) Supply Chain."""

    CUBYN = "CUBYN"
    """Cubyn."""

    SAU_SAUDI_POST = "SAU_SAUDI_POST"
    """Saudi Post."""

    ABXEXPRESS_MY = "ABXEXPRESS_MY"
    """ABX Express."""

    HUAHAN_EXPRESS = "HUAHAN_EXPRESS"
    """HUAHANG EXPRESS."""

    ZES_EXPRESS = "ZES_EXPRESS"
    """Eshun international Logistic."""

    ZEPTO_EXPRESS = "ZEPTO_EXPRESS"
    """ZeptoExpress."""

    SKYNET_ZA = "SKYNET_ZA"
    """Skynet World Wide Express South Africa."""

    ZEEK_2_DOOR = "ZEEK_2_DOOR"
    """Zeek2Door."""

    BLINKLASTMILE = "BLINKLASTMILE"
    """Blink."""

    POSTA_UKR = "POSTA_UKR"
    """UkrPoshta."""

    CHROBINSON = "CHROBINSON"
    """C.H. Robinson Worldwide."""

    CN_POST56 = "CN_POST56"
    """Post56."""

    COURANT_PLUS = "COURANT_PLUS"
    """Courant Plus."""

    SCUDEX_EXPRESS = "SCUDEX_EXPRESS"
    """Scudex Express."""

    SHIPENTEGRA = "SHIPENTEGRA"
    """ShipEntegra."""

    B_TWO_C_EUROPE = "B_TWO_C_EUROPE"
    """B2C courier Europe."""

    COPE = "COPE"
    """Cope Sensitive Freight."""

    IND_GATI = "IND_GATI"
    """Gati-KWE."""

    CN_WISHPOST = "CN_WISHPOST"
    """WishPost."""

    NACEX_ES = "NACEX_ES"
    """NACEX Spain."""

    TAQBIN_HK = "TAQBIN_HK"
    """TAQBIN Hong Kong."""

    GLOBALTRANZ = "GLOBALTRANZ"
    """GlobalTranz."""

    HKD = "HKD"
    """Qingdao HKD International Logistics."""

    BJSHOMEDELIVERY = "BJSHOMEDELIVERY"
    """BJS Distribution courier."""

    OMNIVA = "OMNIVA"
    """Omniva."""

    SUTTON = "SUTTON"
    """Sutton Transport."""

    PANTHER_REFERENCE = "PANTHER_REFERENCE"
    """Panther Reference."""

    SFCSERVICE = "SFCSERVICE"
    """SFC Service."""

    LTL = "LTL"
    """LTL COURIER."""

    PARKNPARCEL = "PARKNPARCEL"
    """Park N Parcel."""

    SPRING_GDS = "SPRING_GDS"
    """Spring GDS."""

    ECEXPRESS = "ECEXPRESS"
    """ECexpress."""

    INTERPARCEL_AU = "INTERPARCEL_AU"
    """Interparcel Australia."""

    AGILITY = "AGILITY"
    """Agility."""

    XL_EXPRESS = "XL_EXPRESS"
    """XL Express."""

    ADERONLINE = "ADERONLINE"
    """Ader couriers."""

    DIRECTCOURIERS = "DIRECTCOURIERS"
    """Direct Couriers."""

    PLANZER = "PLANZER"
    """Planzer Group."""

    SENDING = "SENDING"
    """Sending Transporte Urgente y Comunicacion."""

    NINJAVAN_WB = "NINJAVAN_WB"
    """Ninjavan Webhook."""

    NATIONWIDE_MY = "NATIONWIDE_MY"
    """Nationwide Express Courier Services Bhd (www.nationwide.com.my)."""

    SENDIT = "SENDIT"
    """Sendit."""

    GB_ARROW = "GB_ARROW"
    """Arrow XL."""

    IND_GOJAVAS = "IND_GOJAVAS"
    """GoJavas."""

    KPOST = "KPOST"
    """Korea Post."""

    DHL_FREIGHT = "DHL_FREIGHT"
    """DHL Freight."""

    BLUECARE = "BLUECARE"
    """Bluecare Express Ltd."""

    JINDOUYUN = "JINDOUYUN"
    """jindouyun courier."""

    TRACKON = "TRACKON"
    """Trackon Couriers Pvt. Ltd."""

    GB_TUFFNELLS = "GB_TUFFNELLS"
    """Tuffnells Parcels Express."""

    TRUMPCARD = "TRUMPCARD"
    """TRUMPCARD LLC."""

    ETOTAL = "ETOTAL"
    """eTotal Solution Limited."""

    SFPLUS_WEBHOOK = "SFPLUS_WEBHOOK"
    """Zeek courier."""

    SEKOLOGISTICS = "SEKOLOGISTICS"
    """SEKO Logistics."""

    HERMES_2_MANN_HANDLING = "HERMES_2MANN_HANDLING"
    """Hermes Einrichtungs Service GmbH & Co. KG."""

    DPD_LOCAL_REF = "DPD_LOCAL_REF"
    """DPD Local reference."""

    UDS = "UDS"
    """United Delivery Service."""

    ZA_SPECIALISED_FREIGHT = "ZA_SPECIALISED_FREIGHT"
    """Specialised Freight."""

    THA_KERRY = "THA_KERRY"
    """Kerry Express Thailand."""

    PRT_INT_SEUR = "PRT_INT_SEUR"
    """SEUR International."""

    BRA_CORREIOS = "BRA_CORREIOS"
    """Correios Brazil."""

    NZ_NZ_POST = "NZ_NZ_POST"
    """New Zealand Post."""

    CN_EQUICK = "CN_EQUICK"
    """Equick China."""

    MYS_EMS = "MYS_EMS"
    """Malaysia Post EMS / Pos Laju."""

    GB_NORSK = "GB_NORSK"
    """Norsk Global."""

    ESP_MRW = "ESP_MRW"
    """MRW spain."""

    ESP_PACKLINK = "ESP_PACKLINK"
    """Packlink."""

    KANGAROO_MY = "KANGAROO_MY"
    """Kangaroo Worldwide Express."""

    RPX = "RPX"
    """RPX Online."""

    XDP_UK_REFERENCE = "XDP_UK_REFERENCE"
    """XDP Express Reference."""

    NINJAVAN_MY = "NINJAVAN_MY"
    """ninja van (www.ninjavan.co)."""

    ADICIONAL = "ADICIONAL"
    """Adicional Logistics."""

    ROADBULL = "ROADBULL"
    """Red Carpet Logistics."""

    YAKIT = "YAKIT"
    """Yakit courier."""

    MAILAMERICAS = "MAILAMERICAS"
    """MailAmericas."""

    MIKROPAKKET = "MIKROPAKKET"
    """Mikropakket."""

    DYNALOGIC = "DYNALOGIC"
    """Dynamic Logistics."""

    DHL_ES = "DHL_ES"
    """DHL Spain(www.dhl.com)."""

    DHL_PARCEL_NL = "DHL_PARCEL_NL"
    """DHL Parcel NL."""

    DHL_GLOBAL_MAIL_ASIA = "DHL_GLOBAL_MAIL_ASIA"
    """DHL Global Mail Asia (www.dhl.com)."""

    DAWN_WING = "DAWN_WING"
    """Dawn Wing."""

    GENIKI_GR = "GENIKI_GR"
    """Geniki Taxydromiki."""

    HERMESWORLD_UK = "HERMESWORLD_UK"
    """hermesworld_uk."""

    ALPHAFAST = "ALPHAFAST"
    """Alphafast (www.alphafast.com)."""

    BUYLOGIC = "BUYLOGIC"
    """buylogic."""

    EKART = "EKART"
    """Ekart logistics (ekartlogistics.com)."""

    MEX_SENDA = "MEX_SENDA"
    """mexico senda express."""

    SFC_LOGISTICS = "SFC_LOGISTICS"
    """SFC."""

    POST_SERBIA = "POST_SERBIA"
    """Posta Serbia."""

    IND_DELHIVERY = "IND_DELHIVERY"
    """Delhivery India."""

    DE_DPD_DELISTRACK = "DE_DPD_DELISTRACK"
    """DPD Germany."""

    RPD2_MAN = "RPD2MAN"
    """RPD2man Deliveries."""

    CN_SF_EXPRESS = "CN_SF_EXPRESS"
    """SF Express (www.sf-express.com)."""

    YANWEN = "YANWEN"
    """Yanwen Logistics."""

    MYS_SKYNET = "MYS_SKYNET"
    """Skynet Malaysia."""

    CORREOS_DE_MEXICO = "CORREOS_DE_MEXICO"
    """correos mexico."""

    CBL_LOGISTICA = "CBL_LOGISTICA"
    """CBL Logistica."""

    MEX_ESTAFETA = "MEX_ESTAFETA"
    """Estafeta (www.estafeta.com)."""

    AU_AUSTRIAN_POST = "AU_AUSTRIAN_POST"
    """Austrian Post (Registered)."""

    RINCOS = "RINCOS"
    """Rincos."""

    NLD_DHL = "NLD_DHL"
    """DHL Netherland."""

    RUSSIAN_POST = "RUSSIAN_POST"
    """Russian post."""

    COURIERS_PLEASE = "COURIERS_PLEASE"
    """CouriersPlease (couriersplease.com.au)."""

    POSTNORD_LOGISTICS = "POSTNORD_LOGISTICS"
    """PostNord Logistics."""

    FEDEX = "FEDEX"
    """Fedex."""

    DPE_EXPRESS = "DPE_EXPRESS"
    """DPE Express."""

    DPD = "DPD"
    """DPD."""

    ADSONE = "ADSONE"
    """ADSone."""

    IDN_JNE = "IDN_JNE"
    """JNE Express (Jalur Nugraha Ekakurir)."""

    THECOURIERGUY = "THECOURIERGUY"
    """The Courier Guy."""

    CNEXPS = "CNEXPS"
    """CNE Express."""

    PRT_CHRONOPOST = "PRT_CHRONOPOST"
    """Chronopost Portugal."""

    LANDMARK_GLOBAL = "LANDMARK_GLOBAL"
    """Landmark Global."""

    IT_DHL_ECOMMERCE = "IT_DHL_ECOMMERCE"
    """DHL International."""

    ESP_NACEX = "ESP_NACEX"
    """NACEX Spain."""

    PRT_CTT = "PRT_CTT"
    """CTT Portugal."""

    BE_KIALA = "BE_KIALA"
    """Kiala."""

    ASENDIA_UK = "ASENDIA_UK"
    """Asendia UK."""

    GLOBAL_TNT = "GLOBAL_TNT"
    """TNT global."""

    POSTUR_IS = "POSTUR_IS"
    """Iceland Post."""

    EPARCEL_KR = "EPARCEL_KR"
    """eParcel Korea."""

    INPOST_PACZKOMATY = "INPOST_PACZKOMATY"
    """InPost Paczkomaty."""

    IT_POSTE_ITALIA = "IT_POSTE_ITALIA"
    """Poste italiane (www.poste.it)."""

    BE_BPOST = "BE_BPOST"
    """Bpost (www.bpost.be)."""

    PL_POCZTA_POLSKA = "PL_POCZTA_POLSKA"
    """Poczta Polska (www.poczta-polska.pl)."""

    MYS_MYS_POST = "MYS_MYS_POST"
    """Malaysia Post."""

    SG_SG_POST = "SG_SG_POST"
    """Singapore Post."""

    THA_THAILAND_POST = "THA_THAILAND_POST"
    """Thailand Post (www.thailandpost.co.th)."""

    LEXSHIP = "LEXSHIP"
    """LexShip."""

    FASTWAY_NZ = "FASTWAY_NZ"
    """Fastway New Zealand."""

    DHL_AU = "DHL_AU"
    """DHL Supply Chain Australia."""

    COSTMETICSNOW = "COSTMETICSNOW"
    """Cosmetics Now."""

    PFLOGISTICS = "PFLOGISTICS"
    """PFL."""

    LOOMIS_EXPRESS = "LOOMIS_EXPRESS"
    """Loomis Express."""

    GLS_ITALY = "GLS_ITALY"
    """GLS Italy."""

    LINE = "LINE"
    """Line Clear Express & Logistics Sdn Bhd."""

    GEL_EXPRESS = "GEL_EXPRESS"
    """Gel Express Logistik."""

    HUODULL = "HUODULL"
    """Huodull."""

    NINJAVAN_SG = "NINJAVAN_SG"
    """Ninja van Singapore."""

    JANIO = "JANIO"
    """Janio Asia."""

    AO_COURIER = "AO_COURIER"
    """AO Logistics."""

    BRT_IT_SENDER_REF = "BRT_IT_SENDER_REF"
    """BRT Bartolini(Sender Reference)."""

    SAILPOST = "SAILPOST"
    """SAILPOST."""

    LALAMOVE = "LALAMOVE"
    """Lalamove."""

    NEWZEALAND_COURIERS = "NEWZEALAND_COURIERS"
    """NEW ZEALAND COURIERS."""

    ETOMARS = "ETOMARS"
    """Etomars."""

    VIRTRANSPORT = "VIRTRANSPORT"
    """VIR Transport."""

    WIZMO = "WIZMO"
    """Wizmo."""

    PALLETWAYS = "PALLETWAYS"
    """Palletways."""

    I_DIKA = "I_DIKA"
    """i-dika."""

    CFL_LOGISTICS = "CFL_LOGISTICS"
    """CFL Logistics."""

    GEMWORLDWIDE = "GEMWORLDWIDE"
    """GEM Worldwide."""

    GLOBAL_EXPRESS = "GLOBAL_EXPRESS"
    """Tai Wan Global Business."""

    LOGISTYX_TRANSGROUP = "LOGISTYX_TRANSGROUP"
    """Transgroup courier."""

    WESTBANK_COURIER = "WESTBANK_COURIER"
    """West Bank Courier."""

    ARCO_SPEDIZIONI = "ARCO_SPEDIZIONI"
    """Arco Spedizioni SP."""

    YDH_EXPRESS = "YDH_EXPRESS"
    """YDH express."""

    PARCELINKLOGISTICS = "PARCELINKLOGISTICS"
    """Parcelink Logistics."""

    CNDEXPRESS = "CNDEXPRESS"
    """CND Express."""

    NOX_NIGHT_TIME_EXPRESS = "NOX_NIGHT_TIME_EXPRESS"
    """NOX NightTimeExpress."""

    AERONET = "AERONET"
    """Aeronet couriers."""

    LTIANEXP = "LTIANEXP"
    """LTIAN EXP."""

    INTEGRA2_FTP = "INTEGRA2_FTP"
    """Integra2."""

    PARCELONE = "PARCELONE"
    """PARCEL ONE."""

    NOX_NACHTEXPRESS = "NOX_NACHTEXPRESS"
    """Innight Express Germany GmbH (nox NachtExpress)."""

    CN_CHINA_POST_EMS = "CN_CHINA_POST_EMS"
    """China Post."""

    CHUKOU1 = "CHUKOU1"
    """Chukou1."""

    GLS_SLOV = "GLS_SLOV"
    """GLS General Logistics Systems Slovakia s.r.o.."""

    ORANGE_DS = "ORANGE_DS"
    """OrangeDS (Orange Distribution Solutions Inc)."""

    JOOM_LOGIS = "JOOM_LOGIS"
    """Joom Logistics."""

    AUS_STARTRACK = "AUS_STARTRACK"
    """StarTrack (startrack.com.au)."""

    DHL = "DHL"
    """dhl Global."""

    GB_APC = "GB_APC"
    """APC postal logistics germany."""

    BONDSCOURIERS = "BONDSCOURIERS"
    """Bonds Courier Service (bondscouriers.com.au)."""

    JPN_JAPAN_POST = "JPN_JAPAN_POST"
    """Japan Post."""

    USPS = "USPS"
    """United States Postal Service."""

    WINIT = "WINIT"
    """WinIt."""

    ARG_OCA = "ARG_OCA"
    """OCA Argentina."""

    TW_TAIWAN_POST = "TW_TAIWAN_POST"
    """Taiwan Post."""

    DMM_NETWORK = "DMM_NETWORK"
    """DMM Network."""

    TNT = "TNT"
    """TNT Express."""

    BH_POSTA = "BH_POSTA"
    """BH Posta (www.posta.ba)."""

    SWE_POSTNORD = "SWE_POSTNORD"
    """Postnord sweden."""

    CA_CANADA_POST = "CA_CANADA_POST"
    """Canada Post."""

    WISELOADS = "WISELOADS"
    """Wiseloads."""

    ASENDIA_HK = "ASENDIA_HK"
    """Asendia HonKong."""

    NLD_GLS = "NLD_GLS"
    """GLS Netherland."""

    MEX_REDPACK = "MEX_REDPACK"
    """Redpack."""

    JET_SHIP = "JET_SHIP"
    """Jet-Ship Worldwide."""

    DE_DHL_EXPRESS = "DE_DHL_EXPRESS"
    """DHL Express."""

    NINJAVAN_THAI = "NINJAVAN_THAI"
    """Ninja van Thai."""

    RABEN_GROUP = "RABEN_GROUP"
    """Raben Group."""

    ESP_ASM = "ESP_ASM"
    """ASM(GLS Spain)."""

    HRV_HRVATSKA = "HRV_HRVATSKA"
    """Hrvatska posta."""

    GLOBAL_ESTES = "GLOBAL_ESTES"
    """Estes Express Lines."""

    LTU_LIETUVOS = "LTU_LIETUVOS"
    """Lietuvos pastas."""

    BEL_DHL = "BEL_DHL"
    """DHL Benelux."""

    AU_AU_POST = "AU_AU_POST"
    """Australia Post."""

    SPEEDEXCOURIER = "SPEEDEXCOURIER"
    """SPEEDEX couriers."""

    FR_COLIS = "FR_COLIS"
    """Colissimo."""

    ARAMEX = "ARAMEX"
    """Aramex."""

    DPEX = "DPEX"
    """DPEX (www.dpex.com)."""

    MYS_AIRPAK = "MYS_AIRPAK"
    """Airpak Express."""

    CUCKOOEXPRESS = "CUCKOOEXPRESS"
    """Cuckoo Express."""

    DPD_POLAND = "DPD_POLAND"
    """DPD Poland."""

    NLD_POSTNL = "NLD_POSTNL"
    """PostNL International."""

    NIM_EXPRESS = "NIM_EXPRESS"
    """Nim Express."""

    QUANTIUM = "QUANTIUM"
    """Quantium."""

    SENDLE = "SENDLE"
    """Sendle."""

    ESP_REDUR = "ESP_REDUR"
    """Redur Spain."""

    MATKAHUOLTO = "MATKAHUOLTO"
    """Matkahuolto."""

    CPACKET = "CPACKET"
    """Cpacket couriers."""

    POSTI = "POSTI"
    """Posti courier."""

    HUNTER_EXPRESS = "HUNTER_EXPRESS"
    """Hunter Express."""

    CHOIR_EXP = "CHOIR_EXP"
    """Choir Express Indonesia."""

    LEGION_EXPRESS = "LEGION_EXPRESS"
    """Legion Express."""

    AUSTRIAN_POST_EXPRESS = "AUSTRIAN_POST_EXPRESS"
    """austrian post."""

    GRUPO = "GRUPO"
    """Grupo ampm."""

    POSTA_RO = "POSTA_RO"
    """Post Roman (www.posta-romana.ro)."""

    INTERPARCEL_UK = "INTERPARCEL_UK"
    """Interparcel UK."""

    GLOBAL_ABF = "GLOBAL_ABF"
    """ABF Freight."""

    POSTEN_NORGE = "POSTEN_NORGE"
    """Posten Norge (www.posten.no)."""

    XPERT_DELIVERY = "XPERT_DELIVERY"
    """Xpert Delivery."""

    DHL_REFR = "DHL_REFR"
    """DHl (Reference number)."""

    DHL_HK = "DHL_HK"
    """DHL HonKong."""

    SKYNET_UAE = "SKYNET_UAE"
    """SKYNET UAE."""

    GOJEK = "GOJEK"
    """Gojek."""

    YODEL_INTNL = "YODEL_INTNL"
    """Yodel International."""

    JANCO = "JANCO"
    """Janco Ecommerce."""

    YTO = "YTO"
    """YTO Express."""

    WISE_EXPRESS = "WISE_EXPRESS"
    """Wise Express."""

    JTEXPRESS_VN = "JTEXPRESS_VN"
    """J&T Express Vietnam."""

    FEDEX_INTL_MLSERV = "FEDEX_INTL_MLSERV"
    """FedEx International MailService."""

    VAMOX = "VAMOX"
    """VAMOX."""

    AMS_GRP = "AMS_GRP"
    """AMS Group."""

    DHL_JP = "DHL_JP"
    """DHL Japan."""

    HRPARCEL = "HRPARCEL"
    """HR Parcel."""

    GESWL = "GESWL"
    """GESWL Express."""

    BLUESTAR = "BLUESTAR"
    """Blue Star."""

    CDEK_TR = "CDEK_TR"
    """CDEK TR."""

    DESCARTES = "DESCARTES"
    """Innovel courier."""

    DELTEC_UK = "DELTEC_UK"
    """Deltec Courier."""

    DTDC_EXPRESS = "DTDC_EXPRESS"
    """DTDC express."""

    TOURLINE = "TOURLINE"
    """tourline."""

    BH_WORLDWIDE = "BH_WORLDWIDE"
    """B&H Worldwide."""

    OCS = "OCS"
    """OCS ANA Group."""

    YINGNUO_LOGISTICS = "YINGNUO_LOGISTICS"
    """yingnuo logistics."""

    UPS = "UPS"
    """United Parcel Service."""

    TOLL = "TOLL"
    """Toll IPEC."""

    PRT_SEUR = "PRT_SEUR"
    """SEUR portugal."""

    DTDC_AU = "DTDC_AU"
    """DTDC Australia."""

    THA_DYNAMIC_LOGISTICS = "THA_DYNAMIC_LOGISTICS"
    """Dynamic Logistics."""

    UBI_LOGISTICS = "UBI_LOGISTICS"
    """UBI Smart Parcel."""

    FEDEX_CROSSBORDER = "FEDEX_CROSSBORDER"
    """FedEx Cross Border."""

    A1_POST = "A1POST"
    """A1Post."""

    TAZMANIAN_FREIGHT = "TAZMANIAN_FREIGHT"
    """Tazmanian Freight Systems."""

    CJ_INT_MY = "CJ_INT_MY"
    """CJ International malaysia."""

    SAIA_FREIGHT = "SAIA_FREIGHT"
    """Saia LTL Freight."""

    SG_QXPRESS = "SG_QXPRESS"
    """Qxpress."""

    NHANS_SOLUTIONS = "NHANS_SOLUTIONS"
    """Nhans Solutions."""

    DPD_FR = "DPD_FR"
    """DPD France."""

    COORDINADORA = "COORDINADORA"
    """Coordinadora."""

    ANDREANI = "ANDREANI"
    """Grupo logistico Andreani."""

    DOORA = "DOORA"
    """Doora Logistics."""

    INTERPARCEL_NZ = "INTERPARCEL_NZ"
    """Interparcel New Zealand."""

    PHL_JAMEXPRESS = "PHL_JAMEXPRESS"
    """Jam Express Philippines."""

    BEL_BELGIUM_POST = "BEL_BELGIUM_POST"
    """bel_belgium_post."""

    US_APC = "US_APC"
    """us_apc."""

    IDN_POS = "IDN_POS"
    """idn_pos."""

    FR_MONDIAL = "FR_MONDIAL"
    """fr_mondial."""

    DE_DHL = "DE_DHL"
    """DE DHL."""

    HK_RPX = "HK_RPX"
    """hk_rpx."""

    DHL_PIECEID = "DHL_PIECEID"
    """dhl_pieceid."""

    VNPOST_EMS = "VNPOST_EMS"
    """vnpost_ems."""

    RRDONNELLEY = "RRDONNELLEY"
    """rrdonnelley."""

    DPD_DE = "DPD_DE"
    """dpd_de."""

    DELCART_IN = "DELCART_IN"
    """delcart_in."""

    IMEXGLOBALSOLUTIONS = "IMEXGLOBALSOLUTIONS"
    """imexglobalsolutions."""

    ACOMMERCE = "ACOMMERCE"
    """ACOMMERCE."""

    EURODIS = "EURODIS"
    """eurodis."""

    CANPAR = "CANPAR"
    """CANPAR."""

    GLS = "GLS"
    """GLS."""

    IND_ECOM = "IND_ECOM"
    """Ecom Express."""

    ESP_ENVIALIA = "ESP_ENVIALIA"
    """Envialia."""

    DHL_UK = "DHL_UK"
    """dhl UK."""

    SMSA_EXPRESS = "SMSA_EXPRESS"
    """SMSA Express."""

    TNT_FR = "TNT_FR"
    """TNT France."""

    DEX_I = "DEX_I"
    """DEX-I courier."""

    BUDBEE_WEBHOOK = "BUDBEE_WEBHOOK"
    """Budbee courier."""

    COPA_COURIER = "COPA_COURIER"
    """Copa Airlines Courier."""

    VNM_VIETNAM_POST = "VNM_VIETNAM_POST"
    """Vietnam Post."""

    DPD_HK = "DPD_HK"
    """DPD HongKong."""

    TOLL_NZ = "TOLL_NZ"
    """Toll New Zealand."""

    ECHO = "ECHO"
    """Echo courier."""

    FEDEX_FR = "FEDEX_FR"
    """FedEx® Freight."""

    BORDEREXPRESS = "BORDEREXPRESS"
    """Border Express."""

    MAILPLUS_JPN = "MAILPLUS_JPN"
    """MailPlus (Japan)."""

    TNT_UK_REFR = "TNT_UK_REFR"
    """TNT UK Reference."""

    KEC = "KEC"
    """KEC courier."""

    DPD_RO = "DPD_RO"
    """DPD Romania."""

    TNT_JP = "TNT_JP"
    """TNT_JP."""

    TH_CJ = "TH_CJ"
    """TH_CJ."""

    EC_CN = "EC_CN"
    """EC_CN."""

    FASTWAY_UK = "FASTWAY_UK"
    """FASTWAY_UK."""

    FASTWAY_US = "FASTWAY_US"
    """FASTWAY_US."""

    GLS_DE = "GLS_DE"
    """GLS_DE."""

    GLS_ES = "GLS_ES"
    """GLS_ES."""

    GLS_FR = "GLS_FR"
    """GLS_FR."""

    MONDIAL_BE = "MONDIAL_BE"
    """MONDIAL_BE."""

    SGT_IT = "SGT_IT"
    """SGT_IT."""

    TNT_CN = "TNT_CN"
    """TNT_CN."""

    TNT_DE = "TNT_DE"
    """TNT_DE."""

    TNT_ES = "TNT_ES"
    """TNT_ES."""

    TNT_PL = "TNT_PL"
    """TNT_PL."""

    PARCELFORCE = "PARCELFORCE"
    """PARCELFORCE."""

    SWISS_POST = "SWISS_POST"
    """SWISS POST."""

    TOLL_IPEC = "TOLL_IPEC"
    """TOLL IPEC."""

    AIR_21 = "AIR_21"
    """AIR 21."""

    AIRSPEED = "AIRSPEED"
    """AIRSPEED."""

    BERT = "BERT"
    """BERT."""

    BLUEDART = "BLUEDART"
    """BLUEDART."""

    COLLECTPLUS = "COLLECTPLUS"
    """COLLECTPLUS."""

    COURIERPLUS = "COURIERPLUS"
    """COURIERPLUS."""

    COURIER_POST = "COURIER_POST"
    """COURIER POST."""

    DHL_GLOBAL_MAIL = "DHL_GLOBAL_MAIL"
    """dhl_global_mail."""

    DPD_UK = "DPD_UK"
    """dpd_uk."""

    DELTEC_DE = "DELTEC_DE"
    """DELTEC DE."""

    DEUTSCHE_DE = "DEUTSCHE_DE"
    """deutsche_de."""

    DOTZOT = "DOTZOT"
    """DOTZOT."""

    ELTA_GR = "ELTA_GR"
    """elta_gr."""

    EMS_CN = "EMS_CN"
    """ems_cn."""

    ECARGO = "ECARGO"
    """ECARGO."""

    ENSENDA = "ENSENDA"
    """ENSENDA."""

    FERCAM_IT = "FERCAM_IT"
    """fercam_it."""

    FASTWAY_ZA = "FASTWAY_ZA"
    """fastway_za."""

    FASTWAY_AU = "FASTWAY_AU"
    """fastway_au."""

    FIRST_LOGISITCS = "FIRST_LOGISITCS"
    """first_logisitcs."""

    GEODIS = "GEODIS"
    """GEODIS."""

    GLOBEGISTICS = "GLOBEGISTICS"
    """GLOBEGISTICS."""

    GREYHOUND = "GREYHOUND"
    """GREYHOUND."""

    JETSHIP_MY = "JETSHIP_MY"
    """jetship_my."""

    LION_PARCEL = "LION_PARCEL"
    """LION PARCEL."""

    AEROFLASH = "AEROFLASH"
    """AEROFLASH."""

    ONTRAC = "ONTRAC"
    """ONTRAC."""

    SAGAWA = "SAGAWA"
    """SAGAWA."""

    SIODEMKA = "SIODEMKA"
    """SIODEMKA."""

    STARTRACK = "STARTRACK"
    """startrack."""

    TNT_AU = "TNT_AU"
    """tnt_au."""

    TNT_IT = "TNT_IT"
    """tnt_it."""

    TRANSMISSION = "TRANSMISSION"
    """TRANSMISSION."""

    YAMATO = "YAMATO"
    """YAMATO."""

    DHL_IT = "DHL_IT"
    """dhl_it."""

    DHL_AT = "DHL_AT"
    """dhl_at."""

    LOGISTICSWORLDWIDE_KR = "LOGISTICSWORLDWIDE_KR"
    """LOGISTICSWORLDWIDE KR."""

    GLS_SPAIN = "GLS_SPAIN"
    """gls_spain."""

    AMAZON_UK_API = "AMAZON_UK_API"
    """amazon_uk_api."""

    DPD_FR_REFERENCE = "DPD_FR_REFERENCE"
    """dpd_fr_reference."""

    DHLPARCEL_UK = "DHLPARCEL_UK"
    """dhlparcel_uk."""

    MEGASAVE = "MEGASAVE"
    """megasave."""

    QUALITYPOST = "QUALITYPOST"
    """qualitypost."""

    IDS_LOGISTICS = "IDS_LOGISTICS"
    """ids_logistics."""

    JOYINGBOX = "JOYINGBOX"
    """joyingbox."""

    PANTHER_ORDER_NUMBER = "PANTHER_ORDER_NUMBER"
    """panther_order_number."""

    WATKINS_SHEPARD = "WATKINS_SHEPARD"
    """watkins_shepard."""

    FASTTRACK = "FASTTRACK"
    """fasttrack."""

    UP_EXPRESS = "UP_EXPRESS"
    """up_express."""

    ELOGISTICA = "ELOGISTICA"
    """elogistica."""

    ECOURIER = "ECOURIER"
    """ecourier."""

    CJ_PHILIPPINES = "CJ_PHILIPPINES"
    """cj_philippines."""

    SPEEDEX = "SPEEDEX"
    """speedex."""

    ORANGECONNEX = "ORANGECONNEX"
    """orangeconnex."""

    TECOR = "TECOR"
    """tecor."""

    SAEE = "SAEE"
    """saee."""

    GLS_ITALY_FTP = "GLS_ITALY_FTP"
    """gls_italy_ftp."""

    DELIVERE = "DELIVERE"
    """delivere."""

    YYCOM = "YYCOM"
    """yycom."""

    ADICIONAL_PT = "ADICIONAL_PT"
    """Adicional Logistics."""

    DKSH = "DKSH"
    """DKSH."""

    NIPPON_EXPRESS_FTP = "NIPPON_EXPRESS_FTP"
    """Nippon Express."""

    GOLS = "GOLS"
    """GO Logistics & Storage."""

    FUJEXP = "FUJEXP"
    """FUJIE EXPRESS."""

    QTRACK = "QTRACK"
    """QTrack."""

    OMLOGISTICS_API = "OMLOGISTICS_API"
    """OM LOGISTICS LTD."""

    GDPHARM = "GDPHARM"
    """GDPharm Logistics."""

    MISUMI_CN = "MISUMI_CN"
    """MISUMI Group Inc.."""

    AIR_CANADA = "AIR_CANADA"
    """Rivo."""

    CITY56_WEBHOOK = "CITY56_WEBHOOK"
    """City Express."""

    SAGAWA_API = "SAGAWA_API"
    """Sagawa."""

    KEDAEX = "KEDAEX"
    """KedaEX."""

    PGEON_API = "PGEON_API"
    """Pgeon."""

    WEWORLDEXPRESS = "WEWORLDEXPRESS"
    """We World Express."""

    JT_LOGISTICS = "JT_LOGISTICS"
    """J&T International logistics."""

    TRUSK = "TRUSK"
    """Trusk France."""

    VIAXPRESS = "VIAXPRESS"
    """ViaXpress."""

    DHL_SUPPLYCHAIN_ID = "DHL_SUPPLYCHAIN_ID"
    """DHL Supply Chain Indonesia."""

    ZUELLIGPHARMA_SFTP = "ZUELLIGPHARMA_SFTP"
    """Zuellig Pharma Korea."""

    MEEST = "MEEST"
    """Meest."""

    TOLL_PRIORITY = "TOLL_PRIORITY"
    """Toll Priority."""

    MOTHERSHIP_API = "MOTHERSHIP_API"
    """Mothership."""

    CAPITAL = "CAPITAL"
    """Capital Transport."""

    EUROPAKET_API = "EUROPAKET_API"
    """Europacket+."""

    HFD = "HFD"
    """HFD."""

    TOURLINE_REFERENCE = "TOURLINE_REFERENCE"
    """Tourline Express."""

    GIO_ECOURIER = "GIO_ECOURIER"
    """GIO Express Inc."""

    CN_LOGISTICS = "CN_LOGISTICS"
    """CN Logistics."""

    PANDION = "PANDION"
    """Pandion."""

    BPOST_API = "BPOST_API"
    """Bpost API."""

    PASSPORTSHIPPING = "PASSPORTSHIPPING"
    """Passport Shipping."""

    PAKAJO = "PAKAJO"
    """Pakajo World."""

    DACHSER = "DACHSER"
    """DACHSER."""

    YUSEN_SFTP = "YUSEN_SFTP"
    """Yusen Logistics."""

    SHYPLITE = "SHYPLITE"
    """Shypmax."""

    XYY = "XYY"
    """Xingyunyi Logistics."""

    MWD = "MWD"
    """Metropolitan Warehouse & Delivery."""

    FAXECARGO = "FAXECARGO"
    """Faxe Cargo."""

    MAZET = "MAZET"
    """Groupe Mazet."""

    FIRST_LOGISTICS_API = "FIRST_LOGISTICS_API"
    """First Logistics."""

    SPRINT_PACK = "SPRINT_PACK"
    """SPRINT PACK."""

    HERMES_DE_FTP = "HERMES_DE_FTP"
    """Hermes Germany."""

    CONCISE = "CONCISE"
    """Concise."""

    KERRY_EXPRESS_TW_API = "KERRY_EXPRESS_TW_API"
    """Kerry Express TaiWan."""

    EWE = "EWE"
    """EWE Global Express."""

    FASTDESPATCH = "FASTDESPATCH"
    """Fast Despatch Logistics Limited."""

    ABCUSTOM_SFTP = "ABCUSTOM_SFTP"
    """AB Custom Group."""

    CHAZKI = "CHAZKI"
    """Chazki."""

    SHIPPIE = "SHIPPIE"
    """Shippie."""

    GEODIS_API = "GEODIS_API"
    """GEODIS - Distribution & Express."""

    NAQEL_EXPRESS = "NAQEL_EXPRESS"
    """Naqel Express."""

    PAPA_WEBHOOK = "PAPA_WEBHOOK"
    """Papa."""

    FORWARDAIR = "FORWARDAIR"
    """Forward Air."""

    DIALOGO_LOGISTICA_API = "DIALOGO_LOGISTICA_API"
    """Dialogo Logistica."""

    LALAMOVE_API = "LALAMOVE_API"
    """Lalamove."""

    TOMYDOOR = "TOMYDOOR"
    """Tomydoor."""

    KRONOS_WEBHOOK = "KRONOS_WEBHOOK"
    """Kronos Express."""

    JTCARGO = "JTCARGO"
    """J&T CARGO."""

    T_CAT = "T_CAT"
    """T-cat."""

    CONCISE_WEBHOOK = "CONCISE_WEBHOOK"
    """Concise."""

    TELEPORT_WEBHOOK = "TELEPORT_WEBHOOK"
    """Teleport."""

    CUSTOMCO_API = "CUSTOMCO_API"
    """The Custom Companies."""

    SPX_TH = "SPX_TH"
    """Shopee Xpress."""

    BOLLORE_LOGISTICS = "BOLLORE_LOGISTICS"
    """Bollore Logistics."""

    CLICKLINK_SFTP = "CLICKLINK_SFTP"
    """ClickLink."""

    M3_LOGISTICS = "M3LOGISTICS"
    """M3 Logistics."""

    VNPOST_API = "VNPOST_API"
    """Vietnam Post."""

    AXLEHIRE_FTP = "AXLEHIRE_FTP"
    """Axlehire."""

    SHADOWFAX = "SHADOWFAX"
    """Shadowfax."""

    MYHERMES_UK_API = "MYHERMES_UK_API"
    """EVRi."""

    DAIICHI = "DAIICHI"
    """Daiichi Freight System Inc."""

    MENSAJEROSURBANOS_API = "MENSAJEROSURBANOS_API"
    """Mensajeros Urbanos."""

    POLARSPEED = "POLARSPEED"
    """PolarSpeed Inc."""

    IDEXPRESS_ID = "IDEXPRESS_ID"
    """iDexpress Indonesia."""

    PAYO = "PAYO"
    """Payo."""

    WHISTL_SFTP = "WHISTL_SFTP"
    """Whistl."""

    INTEX_DE = "INTEX_DE"
    """INTEX Paketdienst GmbH."""

    TRANS2_U = "TRANS2U"
    """Trans2u."""

    PRODUCTCAREGROUP_SFTP = "PRODUCTCAREGROUP_SFTP"
    """Product Care Services Limited."""

    BIGSMART = "BIGSMART"
    """Big Smart."""

    EXPEDITORS_API_REF = "EXPEDITORS_API_REF"
    """Expeditors API Reference."""

    AITWORLDWIDE_API = "AITWORLDWIDE_API"
    """AIT."""

    WORLDCOURIER = "WORLDCOURIER"
    """World Courier."""

    QUIQUP = "QUIQUP"
    """Quiqup."""

    AGEDISS_SFTP = "AGEDISS_SFTP"
    """Agediss."""

    ANDREANI_API = "ANDREANI_API"
    """Andreani."""

    CRLEXPRESS = "CRLEXPRESS"
    """CRL Express."""

    SMARTCAT = "SMARTCAT"
    """SMARTCAT."""

    CROSSFLIGHT = "CROSSFLIGHT"
    """Crossflight Limited."""

    PROCARRIER = "PROCARRIER"
    """Pro Carrier."""

    DHL_REFERENCE_API = "DHL_REFERENCE_API"
    """DHL (Reference number)."""

    SEINO_API = "SEINO_API"
    """Seino."""

    WSPEXPRESS = "WSPEXPRESS"
    """WSP Express."""

    KRONOS = "KRONOS"
    """Kronos Express."""

    TOTAL_EXPRESS_API = "TOTAL_EXPRESS_API"
    """Total Express."""

    PARCLL = "PARCLL"
    """PARCLL."""

    XPEDIGO = "XPEDIGO"
    """Xpedigo."""

    STAR_TRACK_WEBHOOK = "STAR_TRACK_WEBHOOK"
    """StarTrack."""

    GPOST = "GPOST"
    """Georgian Post."""

    UCS = "UCS"
    """UCS."""

    DMFGROUP = "DMFGROUP"
    """DMF."""

    COORDINADORA_API = "COORDINADORA_API"
    """Coordinadora."""

    MARKEN = "MARKEN"
    """Marken."""

    NTL = "NTL"
    """NTL logistics."""

    REDJEPAKKETJE = "REDJEPAKKETJE"
    """Red je Pakketje."""

    ALLIED_EXPRESS_FTP = "ALLIED_EXPRESS_FTP"
    """Allied Express (FTP)."""

    MONDIALRELAY_ES = "MONDIALRELAY_ES"
    """Mondial Relay Spain(Punto Pack)."""

    NAEKO_FTP = "NAEKO_FTP"
    """Naeko Logistics."""

    MHI = "MHI"
    """Mhi."""

    SHIPPIFY = "SHIPPIFY"
    """Shippify, Inc."""

    MALCA_AMIT_API = "MALCA_AMIT_API"
    """Malca Amit."""

    JTEXPRESS_SG_API = "JTEXPRESS_SG_API"
    """J&T Express Singapore."""

    DACHSER_WEB = "DACHSER_WEB"
    """DACHSER."""

    FLIGHTLG = "FLIGHTLG"
    """Flight Logistics Group."""

    CAGO = "CAGO"
    """Cago."""

    COM1_EXPRESS = "COM1EXPRESS"
    """ComOne Express."""

    TONAMI_FTP = "TONAMI_FTP"
    """Tonami."""

    PACKFLEET = "PACKFLEET"
    """PACKFLEET."""

    PUROLATOR_INTERNATIONAL = "PUROLATOR_INTERNATIONAL"
    """Purolator International."""

    WINESHIPPING_WEBHOOK = "WINESHIPPING_WEBHOOK"
    """Wineshipping."""

    DHL_ES_SFTP = "DHL_ES_SFTP"
    """DHL Spain Domestic."""

    PCHOME_API = "PCHOME_API"
    """網家速配股份有限公司."""

    CESKAPOSTA_API = "CESKAPOSTA_API"
    """Czech Post."""

    GORUSH = "GORUSH"
    """Go Rush."""

    HOMERUNNER = "HOMERUNNER"
    """HomeRunner."""

    AMAZON_ORDER = "AMAZON_ORDER"
    """Amazon order."""

    EFWNOW_API = "EFWNOW_API"
    """Estes Forwarding Worldwide."""

    CBL_LOGISTICA_API = "CBL_LOGISTICA_API"
    """CBL Logistica (API)."""

    NIMBUSPOST = "NIMBUSPOST"
    """NimbusPost."""

    LOGWIN_LOGISTICS = "LOGWIN_LOGISTICS"
    """Logwin Logistics."""

    NOWLOG_API = "NOWLOG_API"
    """Sequoialog."""

    DPD_NL = "DPD_NL"
    """DPD Netherlands."""

    GODEPENDABLE = "GODEPENDABLE"
    """Dependable Supply Chain Services."""

    ESDEX = "ESDEX"
    """Top Ideal Express."""

    LOGISYSTEMS_SFTP = "LOGISYSTEMS_SFTP"
    """Kiitäjät."""

    EXPEDITORS = "EXPEDITORS"
    """Expeditors."""

    SNTGLOBAL_API = "SNTGLOBAL_API"
    """Snt Global Etrax."""

    SHIPX = "SHIPX"
    """ShipX."""

    QINTL_API = "QINTL_API"
    """Quickstat Courier LLC."""

    PACKS = "PACKS"
    """Packs."""

    POSTNL_INTERNATIONAL = "POSTNL_INTERNATIONAL"
    """PostNL International."""

    AMAZON_EMAIL_PUSH = "AMAZON_EMAIL_PUSH"
    """Amazon."""

    DHL_API = "DHL_API"
    """DHL."""

    SPX = "SPX"
    """Shopee Express."""

    AXLEHIRE = "AXLEHIRE"
    """AxleHire."""

    ICSCOURIER = "ICSCOURIER"
    """ICS COURIER."""

    DIALOGO_LOGISTICA = "DIALOGO_LOGISTICA"
    """Dialogo Logistica."""

    SHUNBANG_EXPRESS = "SHUNBANG_EXPRESS"
    """ShunBang Express."""

    TCS_API = "TCS_API"
    """TCS."""

    SF_EXPRESS_CN = "SF_EXPRESS_CN"
    """SF Express China."""

    PACKETA = "PACKETA"
    """Packeta."""

    SIC_TELIWAY = "SIC_TELIWAY"
    """Teliway SIC Express."""

    MONDIALRELAY_FR = "MONDIALRELAY_FR"
    """Mondial Relay France."""

    INTIME_FTP = "INTIME_FTP"
    """InTime."""

    JD_EXPRESS = "JD_EXPRESS"
    """京东物流."""

    FASTBOX = "FASTBOX"
    """Fastbox."""

    PATHEON = "PATHEON"
    """Patheon Logistics."""

    INDIA_POST = "INDIA_POST"
    """India Post Domestic."""

    TIPSA_REF = "TIPSA_REF"
    """Tipsa Reference."""

    ECOFREIGHT = "ECOFREIGHT"
    """Eco Freight."""

    VOX = "VOX"
    """VOX SOLUCION EMPRESARIAL SRL."""

    DIRECTFREIGHT_AU_REF = "DIRECTFREIGHT_AU_REF"
    """Direct Freight Express."""

    BESTTRANSPORT_SFTP = "BESTTRANSPORT_SFTP"
    """Best Transport."""

    AUSTRALIA_POST_API = "AUSTRALIA_POST_API"
    """Australia Post."""

    FRAGILEPAK_SFTP = "FRAGILEPAK_SFTP"
    """FragilePAK."""

    FLIPXP = "FLIPXP"
    """FlipXpress."""

    VALUE_WEBHOOK = "VALUE_WEBHOOK"
    """Value Logistics."""

    DAESHIN = "DAESHIN"
    """Daeshin."""

    SHERPA = "SHERPA"
    """Sherpa."""

    MWD_API = "MWD_API"
    """Metropolitan Warehouse & Delivery."""

    SMARTKARGO = "SMARTKARGO"
    """SmartKargo."""

    DNJ_EXPRESS = "DNJ_EXPRESS"
    """DNJ Express."""

    GOPEOPLE = "GOPEOPLE"
    """Go People."""

    MYSENDLE_API = "MYSENDLE_API"
    """mySendle."""

    ARAMEX_API = "ARAMEX_API"
    """Aramex."""

    PIDGE = "PIDGE"
    """Pidge."""

    THAIPARCELS = "THAIPARCELS"
    """TP Logistic."""

    PANTHER_REFERENCE_API = "PANTHER_REFERENCE_API"
    """Panther Reference."""

    POSTAPLUS = "POSTAPLUS"
    """Posta Plus."""

    BUFFALO = "BUFFALO"
    """BUFFALO."""

    U_ENVIOS = "U_ENVIOS"
    """U-ENVIOS."""

    ELITE_CO = "ELITE_CO"
    """Elite Express."""

    ROCHE_INTERNAL_SFTP = "ROCHE_INTERNAL_SFTP"
    """Roche Internal Courier."""

    DBSCHENKER_ICELAND = "DBSCHENKER_ICELAND"
    """DB Schenker Iceland."""

    TNT_FR_REFERENCE = "TNT_FR_REFERENCE"
    """TNT France Reference."""

    NEWGISTICSAPI = "NEWGISTICSAPI"
    """Newgistics API."""

    GLOVO = "GLOVO"
    """Glovo."""

    GWLOGIS_API = "GWLOGIS_API"
    """G.I.G."""

    SPREETAIL_API = "SPREETAIL_API"
    """Spreetail."""

    MOOVA = "MOOVA"
    """Moova."""

    PLYCONGROUP = "PLYCONGROUP"
    """Plycon Transportation Group."""

    USPS_WEBHOOK = "USPS_WEBHOOK"
    """USPS Informed Visibility - Webhook."""

    REIMAGINEDELIVERY = "REIMAGINEDELIVERY"
    """maergo."""

    EDF_FTP = "EDF_FTP"
    """Eurodifarm."""

    DAO365 = "DAO365"
    """DAO365."""

    BIOCAIR_FTP = "BIOCAIR_FTP"
    """BioCair."""

    RANSA_WEBHOOK = "RANSA_WEBHOOK"
    """Ransa."""

    SHIPXPRES = "SHIPXPRES"
    """SHIPXPRESS."""

    COURANT_PLUS_API = "COURANT_PLUS_API"
    """Courant Plus."""

    SHIPA = "SHIPA"
    """SHIPA."""

    HOMELOGISTICS = "HOMELOGISTICS"
    """Home Logistics."""

    DX = "DX"
    """DX."""

    POSTE_ITALIANE_PACCOCELERE = "POSTE_ITALIANE_PACCOCELERE"
    """Poste Italiane Paccocelere."""

    TOLL_WEBHOOK = "TOLL_WEBHOOK"
    """Toll Group."""

    LCTBR_API = "LCTBR_API"
    """LCT do Brasil."""

    DX_FREIGHT = "DX_FREIGHT"
    """DX Freight."""

    DHL_SFTP = "DHL_SFTP"
    """DHL Express."""

    SHIPROCKET = "SHIPROCKET"
    """Shiprocket X."""

    UBER_WEBHOOK = "UBER_WEBHOOK"
    """Uber."""

    STATOVERNIGHT = "STATOVERNIGHT"
    """Stat Overnight."""

    BURD = "BURD"
    """Burd Delivery."""

    FASTSHIP = "FASTSHIP"
    """Fastship Express."""

    IBVENTURE_WEBHOOK = "IBVENTURE_WEBHOOK"
    """IB Venture."""

    GATI_KWE_API = "GATI_KWE_API"
    """Gati-KWE."""

    CRYOPDP_FTP = "CRYOPDP_FTP"
    """CryoPDP."""

    HUBBED = "HUBBED"
    """HUBBED."""

    TIPSA_API = "TIPSA_API"
    """Tipsa API."""

    ARASKARGO = "ARASKARGO"
    """Aras Cargo."""

    THIJS_NL = "THIJS_NL"
    """Thijs Logistiek."""

    ATSHEALTHCARE_REFERENCE = "ATSHEALTHCARE_REFERENCE"
    """ATS Healthcare."""

    _99_MINUTOS = "99MINUTOS"
    """99minutos."""

    HELLENIC_POST = "HELLENIC_POST"
    """Hellenic (Greece) Post."""

    HSM_GLOBAL = "HSM_GLOBAL"
    """HSM Global."""

    MNX = "MNX"
    """MNX."""

    NMTRANSFER = "NMTRANSFER"
    """N&M Transfer Co., Inc.."""

    LOGYSTO = "LOGYSTO"
    """Logysto."""

    INDIA_POST_INT = "INDIA_POST_INT"
    """India Post International."""

    AMAZON_FBA_SWISHIP_IN = "AMAZON_FBA_SWISHIP_IN"
    """Swiship IN."""

    SRT_TRANSPORT = "SRT_TRANSPORT"
    """SRT Transport."""

    BOMI = "BOMI"
    """Bomi Group."""

    DELIVERR_SFTP = "DELIVERR_SFTP"
    """Deliverr."""

    HSDEXPRESS = "HSDEXPRESS"
    """HSDEXPRESS."""

    SIMPLETIRE_WEBHOOK = "SIMPLETIRE_WEBHOOK"
    """SimpleTire."""

    HUNTER_EXPRESS_SFTP = "HUNTER_EXPRESS_SFTP"
    """Hunter Express."""

    UPS_API = "UPS_API"
    """UPS."""

    WOOYOUNG_LOGISTICS_SFTP = "WOOYOUNG_LOGISTICS_SFTP"
    """WOO YOUNG LOGISTICS CO.,LTD.."""

    PHSE_API = "PHSE_API"
    """PHSE."""

    WISH_EMAIL_PUSH = "WISH_EMAIL_PUSH"
    """Wish."""

    NORTHLINE = "NORTHLINE"
    """Northline."""

    MEDAFRICA = "MEDAFRICA"
    """Med Africa Logistics."""

    DPD_AT_SFTP = "DPD_AT_SFTP"
    """DPD Austria."""

    ANTERAJA = "ANTERAJA"
    """Anteraja."""

    DHL_GLOBAL_FORWARDING_API = "DHL_GLOBAL_FORWARDING_API"
    """DHL Global Forwarding API."""

    LBCEXPRESS_API = "LBCEXPRESS_API"
    """LBC EXPRESS INC.."""

    SIMSGLOBAL = "SIMSGLOBAL"
    """Sims Global."""

    CDLDELIVERS = "CDLDELIVERS"
    """CDL Last Mile."""

    TYP = "TYP"
    """TYP."""

    TESTING_COURIER_WEBHOOK = "TESTING_COURIER_WEBHOOK"
    """Testing Courier."""

    PANDAGO_API = "PANDAGO_API"
    """Pandago."""

    ROYAL_MAIL_FTP = "ROYAL_MAIL_FTP"
    """Royal Mail."""

    THUNDEREXPRESS = "THUNDEREXPRESS"
    """Thunder Express Australia."""

    SECRETLAB_WEBHOOK = "SECRETLAB_WEBHOOK"
    """Secretlab."""

    SETEL = "SETEL"
    """Setel Express."""

    JD_WORLDWIDE = "JD_WORLDWIDE"
    """JD Worldwide."""

    DPD_RU_API = "DPD_RU_API"
    """DPD Russia."""

    ARGENTS_WEBHOOK = "ARGENTS_WEBHOOK"
    """Argents Express Group."""

    POSTONE = "POSTONE"
    """Post ONE."""

    TUSKLOGISTICS = "TUSKLOGISTICS"
    """Tusk Logistics."""

    RHENUS_UK_API = "RHENUS_UK_API"
    """Rhenus Logistics UK."""

    TAQBIN_SG_API = "TAQBIN_SG_API"
    """Yamato Singapore."""

    INNTRALOG_SFTP = "INNTRALOG_SFTP"
    """Inntralog GmbH."""

    DAYROSS = "DAYROSS"
    """Day & Ross."""

    CORREOSEXPRESS_API = "CORREOSEXPRESS_API"
    """Correos Express (API)."""

    INTERNATIONAL_SEUR_API = "INTERNATIONAL_SEUR_API"
    """International Seur API."""

    YODEL_API = "YODEL_API"
    """Yodel API."""

    HEROEXPRESS = "HEROEXPRESS"
    """Hero Express."""

    DHL_SUPPLYCHAIN_IN = "DHL_SUPPLYCHAIN_IN"
    """DHL supply chain India."""

    URGENT_CARGUS = "URGENT_CARGUS"
    """Urgent Cargus."""

    FRONTDOORCORP = "FRONTDOORCORP"
    """FRONTdoor Collective."""

    JTEXPRESS_PH = "JTEXPRESS_PH"
    """J&T Express Philippines."""

    PARCELSTARS_WEBHOOK = "PARCELSTARS_WEBHOOK"
    """Parcelstars."""

    DPD_SK_SFTP = "DPD_SK_SFTP"
    """DPD Slovakia."""

    MOVIANTO = "MOVIANTO"
    """Movianto."""

    OZEPARTS_SHIPPING = "OZEPARTS_SHIPPING"
    """Ozeparts Shipping."""

    KARGOMKOLAY = "KARGOMKOLAY"
    """KargomKolay (CargoMini)."""

    TRUNKRS = "TRUNKRS"
    """Trunkrs."""

    OMNIRPS_WEBHOOK = "OMNIRPS_WEBHOOK"
    """Omni Returns."""

    CHILEXPRESS = "CHILEXPRESS"
    """Chile Express."""

    TESTING_COURIER = "TESTING_COURIER"
    """Testing Courier."""

    JNE_API = "JNE_API"
    """JNE (API)."""

    BJSHOMEDELIVERY_FTP = "BJSHOMEDELIVERY_FTP"
    """BJS Distribution, Storage & Couriers - FTP."""

    DEXPRESS_WEBHOOK = "DEXPRESS_WEBHOOK"
    """D Express."""

    USPS_API = "USPS_API"
    """USPS API."""

    TRANSVIRTUAL = "TRANSVIRTUAL"
    """TransVirtual."""

    SOLISTICA_API = "SOLISTICA_API"
    """solistica."""

    CHIENVENTURE_WEBHOOK = "CHIENVENTURE_WEBHOOK"
    """Chienventure."""

    DPD_UK_SFTP = "DPD_UK_SFTP"
    """DPD UK."""

    INPOST_UK = "INPOST_UK"
    """InPost."""

    JAVIT = "JAVIT"
    """Javit."""

    ZTO_DOMESTIC = "ZTO_DOMESTIC"
    """ZTO Express China."""

    DHL_GT_API = "DHL_GT_API"
    """DHL Global Forwarding Guatemala."""

    CEVA_TRACKING = "CEVA_TRACKING"
    """CEVA Package."""

    KOMON_EXPRESS = "KOMON_EXPRESS"
    """Komon Express."""

    EASTWESTCOURIER_FTP = "EASTWESTCOURIER_FTP"
    """East West Courier Pte Ltd."""

    DANNIAO = "DANNIAO"
    """Danniao."""

    SPECTRAN = "SPECTRAN"
    """Spectran."""

    DELIVER_IT = "DELIVER_IT"
    """Deliver-iT."""

    RELAISCOLIS = "RELAISCOLIS"
    """Relais Colis."""

    GLS_SPAIN_API = "GLS_SPAIN_API"
    """GLS Spain."""

    POSTPLUS = "POSTPLUS"
    """PostPlus."""

    AIRTERRA = "AIRTERRA"
    """Airterra."""

    GIO_ECOURIER_API = "GIO_ECOURIER_API"
    """GIO Express Ecourier."""

    DPD_CH_SFTP = "DPD_CH_SFTP"
    """DPD Switzerland."""

    FEDEX_API = "FEDEX_API"
    """FedEx®."""

    INTERSMARTTRANS = "INTERSMARTTRANS"
    """INTERSMARTTRANS & SOLUTIONS SL."""

    HERMES_UK_SFTP = "HERMES_UK_SFTP"
    """Hermes UK."""

    EXELOT_FTP = "EXELOT_FTP"
    """Exelot Ltd.."""

    DHL_PA_API = "DHL_PA_API"
    """DHL GLOBAL FORWARDING PANAMÁ."""

    VIRTRANSPORT_SFTP = "VIRTRANSPORT_SFTP"
    """Vir Transport."""

    WORLDNET = "WORLDNET"
    """Worldnet Logistics."""

    INSTABOX_WEBHOOK = "INSTABOX_WEBHOOK"
    """Instabox."""

    KNG = "KNG"
    """Keuhne + Nagel Global."""

    FLASHEXPRESS_WEBHOOK = "FLASHEXPRESS_WEBHOOK"
    """Flash Express."""

    MAGYAR_POSTA_API = "MAGYAR_POSTA_API"
    """Magyar Posta."""

    WESHIP_API = "WESHIP_API"
    """WeShip."""

    OHI_WEBHOOK = "OHI_WEBHOOK"
    """Ohi."""

    MUDITA = "MUDITA"
    """MUDITA."""

    BLUEDART_API = "BLUEDART_API"
    """Bluedart."""

    T_CAT_API = "T_CAT_API"
    """T-cat."""

    ADS = "ADS"
    """ADS Express."""

    HERMES_IT = "HERMES_IT"
    """HR Parcel."""

    FITZMARK_API = "FITZMARK_API"
    """FitzMark."""

    POSTI_API = "POSTI_API"
    """Posti API."""

    SMSA_EXPRESS_WEBHOOK = "SMSA_EXPRESS_WEBHOOK"
    """SMSA Express."""

    TAMERGROUP_WEBHOOK = "TAMERGROUP_WEBHOOK"
    """Tamer Logistics."""

    LIVRAPIDE = "LIVRAPIDE"
    """Livrapide."""

    NIPPON_EXPRESS = "NIPPON_EXPRESS"
    """Nippon Express."""

    BETTERTRUCKS = "BETTERTRUCKS"
    """Better Trucks."""

    FAN = "FAN"
    """FAN COURIER EXPRESS."""

    PB_USPSFLATS_FTP = "PB_USPSFLATS_FTP"
    """USPS Flats (Pitney Bowes)."""

    PARCELRIGHT = "PARCELRIGHT"
    """Parcel Right."""

    ITHINKLOGISTICS = "ITHINKLOGISTICS"
    """iThink Logistics."""

    KERRY_EXPRESS_TH_WEBHOOK = "KERRY_EXPRESS_TH_WEBHOOK"
    """Kerry Logistics."""

    ECOUTIER = "ECOUTIER"
    """eCoutier."""

    SHOWL = "SHOWL"
    """SENHONG INTERNATIONAL LOGISTICS."""

    BRT_IT_API = "BRT_IT_API"
    """BRT Bartolini API."""

    RIXONHK_API = "RIXONHK_API"
    """Rixon Logistics."""

    DBSCHENKER_API = "DBSCHENKER_API"
    """DB Schenker."""

    ILYANGLOGIS = "ILYANGLOGIS"
    """Ilyang logistics."""

    MAIL_BOX_ETC = "MAIL_BOX_ETC"
    """Mail Boxes Etc.."""

    WESHIP = "WESHIP"
    """WeShip."""

    DHL_GLOBAL_MAIL_API = "DHL_GLOBAL_MAIL_API"
    """DHL eCommerce Solutions."""

    ACTIVOS24_API = "ACTIVOS24_API"
    """Activos24."""

    ATSHEALTHCARE = "ATSHEALTHCARE"
    """ATS Healthcare."""

    LUWJISTIK = "LUWJISTIK"
    """Luwjistik."""

    GW_WORLD = "GW_WORLD"
    """Gebrüder Weiss."""

    FAIRSENDEN_API = "FAIRSENDEN_API"
    """fairsenden."""

    SERVIP_WEBHOOK = "SERVIP_WEBHOOK"
    """SerVIP."""

    SWISHIP = "SWISHIP"
    """Swiship."""

    TANET = "TANET"
    """Transport Ambientales."""

    HOTSIN_CARGO = "HOTSIN_CARGO"
    """SHENZHEN HOTSIN CARGO INT'L FORWARDING CO.,LTD."""

    DIREX = "DIREX"
    """Direx."""

    HUANTONG = "HUANTONG"
    """HuanTong."""

    IMILE_API = "IMILE_API"
    """iMile."""

    AUEXPRESS = "AUEXPRESS"
    """Au Express."""

    NYTLOGISTICS = "NYTLOGISTICS"
    """NYT SUPPLY CHAIN LOGISTICS Co.,LTD."""

    DSV_REFERENCE = "DSV_REFERENCE"
    """DSV Futurewave."""

    NOVOFARMA_WEBHOOK = "NOVOFARMA_WEBHOOK"
    """Novofarma."""

    AITWORLDWIDE_SFTP = "AITWORLDWIDE_SFTP"
    """AIT."""

    SHOPOLIVE = "SHOPOLIVE"
    """Olive."""

    FNF_ZA = "FNF_ZA"
    """Fast & Furious."""

    DHL_ECOMMERCE_GC = "DHL_ECOMMERCE_GC"
    """DHL eCommerce Greater China."""

    FETCHR = "FETCHR"
    """Fetchr."""

    STARLINKS_API = "STARLINKS_API"
    """Starlinks Global."""

    YYEXPRESS = "YYEXPRESS"
    """YYEXPRESS."""

    SERVIENTREGA = "SERVIENTREGA"
    """Servientrega."""

    HANJIN = "HANJIN"
    """HanJin."""

    SPANISH_SEUR_FTP = "SPANISH_SEUR_FTP"
    """Spanish Seur."""

    DX_B2_B_CONNUM = "DX_B2B_CONNUM"
    """DX (B2B)."""

    HELTHJEM_API = "HELTHJEM_API"
    """Helthjem."""

    INEXPOST = "INEXPOST"
    """Inexpost."""

    A2_B_BA = "A2B_BA"
    """A2B Express Logistics."""

    RHENUS_GROUP = "RHENUS_GROUP"
    """Rhenus Logistics."""

    SBERLOGISTICS_RU = "SBERLOGISTICS_RU"
    """Sber Logistics."""

    MALCA_AMIT = "MALCA_AMIT"
    """Malca-Amit."""

    PPL = "PPL"
    """Professional Parcel Logistics."""

    OSM_WORLDWIDE_SFTP = "OSM_WORLDWIDE_SFTP"
    """OSM Worldwide."""

    ACILOGISTIX = "ACILOGISTIX"
    """ACI Logistix."""

    OPTIMACOURIER = "OPTIMACOURIER"
    """Optima Courier."""

    NOVA_POSHTA_API = "NOVA_POSHTA_API"
    """Nova Poshta API."""

    LOGGI = "LOGGI"
    """Loggi."""

    YIFAN = "YIFAN"
    """YiFan Express."""

    MYDYNALOGIC = "MYDYNALOGIC"
    """My DynaLogic."""

    MORNINGLOBAL = "MORNINGLOBAL"
    """Morning Global."""

    CONCISE_API = "CONCISE_API"
    """Concise."""

    FXTRAN = "FXTRAN"
    """Falcon Express."""

    DELIVERYOURPARCEL_ZA = "DELIVERYOURPARCEL_ZA"
    """Deliver Your Parcel."""

    UPARCEL = "UPARCEL"
    """uParcel."""

    MOBI_BR = "MOBI_BR"
    """Mobi Logistica."""

    LOGINEXT_WEBHOOK = "LOGINEXT_WEBHOOK"
    """T&W Delivery."""

    EMS = "EMS"
    """EMS."""

    SPEEDY = "SPEEDY"
    """Speedy."""

    ZOOM_RED = "ZOOM_RED"
    """Zoom."""

    NAVLUNGO = "NAVLUNGO"
    """Navlungo."""

    CASTLEPARCELS = "CASTLEPARCELS"
    """Castle Parcels."""

    WEEE = "WEEE"
    """Weee."""

    PACKALY = "PACKALY"
    """Packaly."""

    YUNHUIPOST = "YUNHUIPOST"
    """Yunhuipost."""

    YOUPARCEL = "YOUPARCEL"
    """YouParcel."""

    LEMAN = "LEMAN"
    """Leman."""

    MOOVIN = "MOOVIN"
    """Moovin."""

    URB_IT = "URB_IT"
    """Urb-it."""

    MULTIENTREGAPANAMA = "MULTIENTREGAPANAMA"
    """Multientrega."""

    JUSDASR = "JUSDASR"
    """Jusdasr."""

    DISCOUNTPOST = "DISCOUNTPOST"
    """Discount Post."""

    RHENUS_UK = "RHENUS_UK"
    """Rhenus Logistics UK."""

    SWISHIP_JP = "SWISHIP_JP"
    """Swiship JP."""

    GLS_US = "GLS_US"
    """GLS USA."""

    SMTL = "SMTL"
    """Southwestern Motor Transport. Inc."""

    EMEGA = "EMEGA"
    """Discount Post Emega."""

    EXPRESSONE_SV = "EXPRESSONE_SV"
    """EXPRESSONE Slovenia."""

    HEPSIJET = "HEPSIJET"
    """hepsiJET."""

    WELIVERY = "WELIVERY"
    """Welivery."""

    BRINGER = "BRINGER"
    """Bringer Parcel Services."""

    EASYROUTES = "EASYROUTES"
    """EasyRoutes."""

    MRW = "MRW"
    """MRW."""

    RPM = "RPM"
    """RPM."""

    DPD_PRT = "DPD_PRT"
    """DPD Portugal."""

    GLS_ROMANIA = "GLS_ROMANIA"
    """GLS Romania."""

    LMPARCEL = "LMPARCEL"
    """LM Parcel."""

    GTAGSM = "GTAGSM"
    """GTA GSM."""

    DOMINO = "DOMINO"
    """DOMINO."""

    ESHIPPER = "ESHIPPER"
    """eShipper."""

    TRANSPAK = "TRANSPAK"
    """Transpak Inc.."""

    XINDUS = "XINDUS"
    """Xindus."""

    AOYUE = "AOYUE"
    """Aoyue."""

    EASYPARCEL = "EASYPARCEL"
    """Easyparcel."""

    EXPRESSONE = "EXPRESSONE"
    """EXPRESSONE."""

    SENDEO_KARGO = "SENDEO_KARGO"
    """Sendeo Kargo."""

    SPEEDAF = "SPEEDAF"
    """Speedaf Express."""

    ETOWER = "ETOWER"
    """eTower."""

    GCX = "GCX"
    """GC Express."""

    NINJAVAN_VN = "NINJAVAN_VN"
    """Ninjavan Vietnam."""

    ALLEGRO = "ALLEGRO"
    """Allegro."""

    JUMPPOINT = "JUMPPOINT"
    """Jumppoint."""

    SHIPGLOBAL_US = "SHIPGLOBAL_US"
    """ShipGlobal."""

    KINISI = "KINISI"
    """Kinisi Transport Pty Ltd."""

    OAKH = "OAKH"
    """Oakh Harbour Freight Lines."""

    AWEST = "AWEST"
    """American West."""

    BARSAN = "BARSAN"
    """Barsan Global Lojistik."""

    ENERGOLOGISTIC = "ENERGOLOGISTIC"
    """Energo Logistic."""

    MADROOEX = "MADROOEX"
    """Madrooex."""

    GOBOLT = "GOBOLT"
    """GoBolt."""

    SWISS_UNIVERSAL_EXPRESS = "SWISS_UNIVERSAL_EXPRESS"
    """Swiss Universal Express."""

    IORDIRECT = "IORDIRECT"
    """IOR Direct Solutions."""

    XMSZM = "XMSZM"
    """xmszm."""

    GLS_HUN = "GLS_HUN"
    """GLS Hungary."""

    SENDY = "SENDY"
    """Sendy Express."""

    BRAUNSEXPRESS = "BRAUNSEXPRESS"
    """Brauns Express."""

    GRANDSLAMEXPRESS = "GRANDSLAMEXPRESS"
    """Grand Slam Express."""

    XGS = "XGS"
    """XGS."""

    OTSCHILE = "OTSCHILE"
    """OTS."""

    PACK_UP = "PACK_UP"
    """Pack-Up."""

    PARCELSTARS = "PARCELSTARS"
    """Parcelstars."""

    TEAMEXPRESSLLC = "TEAMEXPRESSLLC"
    """Team Express Service LLC."""

    ASYADEXPRESS = "ASYADEXPRESS"
    """Asyad Express."""

    TDN = "TDN"
    """TDN."""

    EARLYBIRD = "EARLYBIRD"
    """Early Bird."""

    CACESA = "CACESA"
    """Cacesa."""

    PARCELJET = "PARCELJET"
    """Parceljet."""

    MNG_KARGO = "MNG_KARGO"
    """MNG Kargo."""

    SUPERPACKLINE = "SUPERPACKLINE"
    """Super Pac Line."""

    SPEEDX = "SPEEDX"
    """SpeedX."""

    VESYL = "VESYL"
    """Vesyl."""

    SKYKING = "SKYKING"
    """Sky King."""

    DIRMENSAJERIA = "DIRMENSAJERIA"
    """DIR."""

    NETLOGIXGROUP = "NETLOGIXGROUP"
    """Netlogix."""

    ZYOU = "ZYOU"
    """ZYEX."""

    JAWAR = "JAWAR"
    """Jawar."""

    AGSYSTEMS = "AGSYSTEMS"
    """Associate Global Systems."""

    GPS = "GPS"
    """GPS."""

    PTT_KARGO = "PTT_KARGO"
    """PTT Kargo."""

    MAERGO = "MAERGO"
    """Maergo."""

    ARIHANTCOURIER = "ARIHANTCOURIER"
    """AICS."""

    VTFE = "VTFE"
    """VicTas Freight Express."""

    YUNANT = "YUNANT"
    """Yunant."""

    URBIFY = "URBIFY"
    """Urbify."""

    PACK_MAN = "PACK_MAN"
    """pack-man."""

    LIEFERGRUN = "LIEFERGRUN"
    """LIEFERGRUN."""

    OBIBOX = "OBIBOX"
    """Obibox."""

    PAIKEDA = "PAIKEDA"
    """Paikeda."""

    SCOTTY = "SCOTTY"
    """Scotty."""

    INTELCOM_CA = "INTELCOM_CA"
    """Intelcom."""

    SWE = "SWE"
    """swe."""

    ASENDIA = "ASENDIA"
    """Asendia Global."""

    DPD_AT = "DPD_AT"
    """DPD Austria."""

    RELAY = "RELAY"
    """Relay."""

    ATA = "ATA"
    """ATA."""

    SKYEXPRESS_INTERNATIONAL = "SKYEXPRESS_INTERNATIONAL"
    """SkyExpress Internationals."""

    SURAT_KARGO = "SURAT_KARGO"
    """Surat Kargo."""

    SGLINK = "SGLINK"
    """SG LINK."""

    FLEETOPTICSINC = "FLEETOPTICSINC"
    """FleetOptics."""

    SHOPLINE = "SHOPLINE"
    """shopline."""

    PIGGYSHIP = "PIGGYSHIP"
    """PIGGYSHIP."""

    LOGOIX = "LOGOIX"
    """LogoiX."""

    KOLAY_GELSIN = "KOLAY_GELSIN"
    """Kolay Gelsin."""

    ASSOCIATED_COURIERS = "ASSOCIATED_COURIERS"
    """Associated Couriers."""

    UPS_CHECKER = "UPS_CHECKER"
    """ups-checker."""

    WINESHIPPING = "WINESHIPPING"
    """Wineshipping."""

    SPEDISCI = "SPEDISCI"
    """Spedisci online."""

    FOURKITES = "FOURKITES"
    """Fourkites."""

    ETONAS = "ETONAS"
    """Etonas."""

    FINMILE = "FINMILE"
    """Fin Mile."""

    UNIUNI = "UNIUNI"
    """Uniuni."""

    RODONAVES = "RODONAVES"
    """Rodonaves."""

    INPOST_IT = "INPOST_IT"
    """Inpost Italy."""

    TFORCE_FREIGHT = "TFORCE_FREIGHT"
    """Tforce Freight."""

    RICHMOM = "RICHMOM"
    """Rich Mom."""

    FRANCO = "FRANCO"
    """Corriere Franco."""

    ECPARCEL = "ECPARCEL"
    """Ecparcel."""

    FEDEX_CHINA = "FEDEX_CHINA"
    """Fedex China."""

    GOFO_EXPRESS = "GOFO_EXPRESS"
    """Gofo Express."""

    SHIPBOB = "SHIPBOB"
    """Shipbob."""

    JERSEYPOST_ATLAS = "JERSEYPOST_ATLAS"
    """Jersey Post Group."""

    CORETRAILS = "CORETRAILS"
    """Coretrails."""

    RHENUS_ITALY = "RHENUS_ITALY"
    """Rhenus Logistics Italy."""

    JADLOG = "JADLOG"
    """Jadlog."""

    JITSU = "JITSU"
    """Jitsu."""

    YANWEN_EXPRESS = "YANWEN_EXPRESS"
    """Yanwen Express."""

    DASHLINK = "DASHLINK"
    """Dashlink."""

    SEINO_SUPER_EXPRESS = "SEINO_SUPER_EXPRESS"
    """Seino Super Express."""

    FLOSHIP = "FLOSHIP"
    """Floship."""

    METROSCG = "METROSCG"
    """Metro Supply Chain."""

    SENDPARCEL = "SENDPARCEL"
    """Sendparcel."""

    P2_P = "P2P"
    """P2p."""

    CN_EXPRESS = "CN_EXPRESS"
    """Cn Express."""

    CIRROTRACK = "CIRROTRACK"
    """Cirro Track."""

    LAND_LOGISTICS = "LAND_LOGISTICS"
    """Land Logistics."""

    VEHO = "VEHO"
    """Veho."""

    MEDLINE = "MEDLINE"
    """Medline."""

    VDTRACK = "VDTRACK"
    """Vdtrack."""

    SINO_SCM = "SINO_SCM"
    """Sino Scm."""

    _3_PE_EXPRESS = "3PE_EXPRESS"
    """3pe Express."""

    SWIFTX = "SWIFTX"
    """Swiftx."""

    SFYDEXPRESS = "SFYDEXPRESS"
    """Sfyd Express."""

    TOPTRANS = "TOPTRANS"
    """Toptrans."""

    OTHER = "OTHER"
    """Other."""

    __str__ = str.__str__


ShipmentCarrierOrStr: TypeAlias = Annotated[ShipmentCarrier | str, open_enum_validator(ShipmentCarrier)]
