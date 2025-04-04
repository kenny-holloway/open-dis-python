'''
/*
 * Copyright (c) 2008-2022, MOVES Institute, Naval Postgraduate School (NPS). All rights reserved.
 * This work is provided under a BSD-style open-source license, see project
 * <a href="https://savage.nps.edu/opendis7-java/license.html" target="_blank">license.html</a> and <a href="https://savage.nps.edu/opendis7-java/license.txt" target="_blank">license.txt</a>
 */
 // header autogenerated using string template dis7javalicense.txt
'''


from enum import Enum, EnumMeta
from pprint import pprint, pformat
from collections import OrderedDict, namedtuple
import ctypes

UInt8 = ctypes.c_uint8
UInt16 = ctypes.c_uint16
UInt32 = ctypes.c_uint32

EnumValue = namedtuple('EnumValue', ['value', 'description'])

# autogenerated using string template disenumpart1.txt
#  package edu.nps.moves.dis7.enumerations;

'''
/**
  * This <code>enum</code> type is generated from XML,
  * SisoDate : 
  * UID 29,
  * marshal size 16;
  * Country has 279 enumerations total.
  */
'''

class EnumMeta(EnumMeta):
    def __getitem__(cls, name):
        try:
            return super().__getitem__(name)
        except KeyError as error:
            return cls.UNKNOWN
    
    def __getattr__(cls, name):
        try:
            return super().__getattr__(name)
        except AttributeError as error:
            return cls.UNKNOWN

class ExtensibleEnum(Enum):
    @classmethod
    def add_custom_value(cls, value: int, name: str, desc:str):
        existingItem = [item for item in cls._value2member_map_ if item.value == value]

        enumValue = EnumValue(value, desc)
        obj = object.__new__(cls)
        
        obj._value_ = enumValue
        obj._name_ = name      
        obj._desc = desc
        obj.__objclass__ = cls
        
        if not existingItem:
            cls._member_map_[name] = obj
            cls._value2member_map_[enumValue] = enumValue
            cls._member_names_.append(name)
        else:
            enumIndex = list(OrderedDict(cls.__members__).keys())[value]
            cls._member_map_[enumIndex] = obj

    @property
    def get_description(self):
        return self.value.description

    @classmethod
    def to_string(cls) -> str:
        return pformat(OrderedDict(cls.__members__))

    @classmethod
    def is_valid(cls, kind: Enum) -> bool:
        if kind is cls.UNKNOWN:
            return False
        return kind in iter(cls)

    @staticmethod
    def describe(self):
        return self.name, self.value

    @classmethod
    def value_list(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def _missing_(cls, value):
        return cls.default

    @classmethod
    def get_enum_key(cls, value:int) -> str:
        for unique_key, unique_value in OrderedDict(cls.__members__).items():
            if value == unique_value.value.value:
                return unique_key
        return 'UNKNOWN'

    @classmethod
    def get_enum(cls, value:int) -> Enum:
        key = cls.get_enum_key(value)
        return getattr(cls, key)

    def __int__(self):
        return self.value.value
    def diff(self,other) -> set:
        diffs = set()
        for key, value in self.__dict__.items():
            value2 = other.__dict__[key]
            if (value != value2):
                if type(value) is list:
                    diffs.add((key, str(value)))
                    diffs.add((key, str(value2)))
                elif (type(value).__module__ == "builtins"):
                    diffs.add((key, value))
                    diffs.add((key, value2))
                elif (isinstance(value, Enum)):
                    diffs.add((key, value))
                    diffs.add((key, value2))
                elif (isinstance(value, object)):
                    diffs.update(value.diff(value2))
                else:
                    diffs.add((key, value))
                    diffs.add((key, value2))
        return(diffs)

class Country(ExtensibleEnum, metaclass=EnumMeta):
    UNKNOWN = EnumValue(-1, "UNKNOWN Enum")
    other = EnumValue(0, "Other")
    afghanistan_afg = EnumValue(1, "Afghanistan (AFG)")
    albania_alb = EnumValue(2, "Albania (ALB)")
    algeria_dza = EnumValue(3, "Algeria (DZA)")
    american_samoa_asm = EnumValue(4, "American Samoa (ASM)")
    andorra_and = EnumValue(5, "Andorra (AND)")
    angola_ago = EnumValue(6, "Angola (AGO)")
    anguilla_aia = EnumValue(7, "Anguilla (AIA)")
    antarctica_ata = EnumValue(8, "Antarctica (ATA)")
    antigua_and_barbuda_atg = EnumValue(9, "Antigua and Barbuda (ATG)")
    argentina_arg = EnumValue(10, "Argentina (ARG)")
    aruba_abw = EnumValue(11, "Aruba (ABW)")
    ashmore_and_cartier_islands_australia = EnumValue(12, "Ashmore and Cartier Islands (Australia)")
    australia_aus = EnumValue(13, "Australia (AUS)")
    austria_aut = EnumValue(14, "Austria (AUT)")
    bahamas_bhs = EnumValue(15, "Bahamas (BHS)")
    bahrain_bhr = EnumValue(16, "Bahrain (BHR)")
    baker_island_united_states = EnumValue(17, "Baker Island (United States)")
    bangladesh_bgd = EnumValue(18, "Bangladesh (BGD)")
    barbados_brb = EnumValue(19, "Barbados (BRB)")
    bassas_da_india_france = EnumValue(20, "Bassas da India (France)")
    belgium_bel = EnumValue(21, "Belgium (BEL)")
    belize_blz = EnumValue(22, "Belize (BLZ)")
    benin_ben = EnumValue(23, "Benin (BEN)")
    bermuda_bmu = EnumValue(24, "Bermuda (BMU)")
    bhutan_btn = EnumValue(25, "Bhutan (BTN)")
    bolivia_plurinational_state_of_bol = EnumValue(26, "Bolivia (Plurinational State of) (BOL)")
    botswana_bwa = EnumValue(27, "Botswana (BWA)")
    bouvet_island_bvt = EnumValue(28, "Bouvet Island (BVT)")
    brazil_bra = EnumValue(29, "Brazil (BRA)")
    british_indian_ocean_territory_iot = EnumValue(30, "British Indian Ocean Territory (IOT)")
    virgin_islands_british_vgb = EnumValue(31, "Virgin Islands (British) (VGB)")
    brunei_darussalam_brn = EnumValue(32, "Brunei Darussalam (BRN)")
    bulgaria_bgr = EnumValue(33, "Bulgaria (BGR)")
    burkina_faso_bfa = EnumValue(34, "Burkina Faso (BFA)")
    myanmar_mmr = EnumValue(35, "Myanmar (MMR)")
    burundi_bdi = EnumValue(36, "Burundi (BDI)")
    cambodia_khm = EnumValue(37, "Cambodia (KHM)")
    cameroon_cmr = EnumValue(38, "Cameroon (CMR)")
    canada_can = EnumValue(39, "Canada (CAN)")
    cabo_verde_cpv = EnumValue(40, "Cabo Verde (CPV)")
    cayman_islands_cym = EnumValue(41, "Cayman Islands (CYM)")
    central_african_republic_caf = EnumValue(42, "Central African Republic (CAF)")
    chad_tcd = EnumValue(43, "Chad (TCD)")
    chile_chl = EnumValue(44, "Chile (CHL)")
    china_peoples_republic_of_chn = EnumValue(45, "China, People's Republic of (CHN)")
    christmas_island_cxr = EnumValue(46, "Christmas Island (CXR)")
    cocos_keeling_islands_cck = EnumValue(47, "Cocos (Keeling) Islands (CCK)")
    colombia_col = EnumValue(48, "Colombia (COL)")
    comoros_com = EnumValue(49, "Comoros (COM)")
    congo_cog = EnumValue(50, "Congo (COG)")
    cook_islands_cok = EnumValue(51, "Cook Islands (COK)")
    coral_sea_islands_australia = EnumValue(52, "Coral Sea Islands (Australia)")
    costa_rica_cri = EnumValue(53, "Costa Rica (CRI)")
    cuba_cub = EnumValue(54, "Cuba (CUB)")
    cyprus_cyp = EnumValue(55, "Cyprus (CYP)")
    czechoslovakia_csk = EnumValue(56, "Czechoslovakia (CSK)")
    denmark_dnk = EnumValue(57, "Denmark (DNK)")
    djibouti_dji = EnumValue(58, "Djibouti (DJI)")
    dominica_dma = EnumValue(59, "Dominica (DMA)")
    dominican_republic_dom = EnumValue(60, "Dominican Republic (DOM)")
    ecuador_ecu = EnumValue(61, "Ecuador (ECU)")
    egypt_egy = EnumValue(62, "Egypt (EGY)")
    el_salvador_slv = EnumValue(63, "El Salvador (SLV)")
    equatorial_guinea_gnq = EnumValue(64, "Equatorial Guinea (GNQ)")
    ethiopia_eth = EnumValue(65, "Ethiopia (ETH)")
    europa_island_france = EnumValue(66, "Europa Island (France)")
    falkland_islands_malvinas_flk = EnumValue(67, "Falkland Islands (Malvinas) (FLK)")
    faroe_islands_fro = EnumValue(68, "Faroe Islands (FRO)")
    fiji_fji = EnumValue(69, "Fiji (FJI)")
    finland_fin = EnumValue(70, "Finland (FIN)")
    france_fra = EnumValue(71, "France (FRA)")
    french_guiana_guf = EnumValue(72, "French Guiana (GUF)")
    french_polynesia_pyf = EnumValue(73, "French Polynesia (PYF)")
    french_southern_territories_atf = EnumValue(74, "French Southern Territories (ATF)")
    gabon_gab = EnumValue(75, "Gabon (GAB)")
    gambia_the_gmb = EnumValue(76, "Gambia, The (GMB)")
    gaza_strip_israel = EnumValue(77, "Gaza Strip (Israel)")
    germany_deu = EnumValue(78, "Germany (DEU)")
    ghana_gha = EnumValue(79, "Ghana (GHA)")
    gibraltar_gib = EnumValue(80, "Gibraltar (GIB)")
    glorioso_islands_france = EnumValue(81, "Glorioso Islands (France)")
    greece_grc = EnumValue(82, "Greece (GRC)")
    greenland_grl = EnumValue(83, "Greenland (GRL)")
    grenada_grd = EnumValue(84, "Grenada (GRD)")
    guadeloupe_glp = EnumValue(85, "Guadeloupe (GLP)")
    guam_gum = EnumValue(86, "Guam (GUM)")
    guatemala_gtm = EnumValue(87, "Guatemala (GTM)")
    guernsey_ggy = EnumValue(88, "Guernsey (GGY)")
    guinea_gin = EnumValue(89, "Guinea (GIN)")
    guinea_bissau_gnb = EnumValue(90, "Guinea-Bissau (GNB)")
    guyana_guy = EnumValue(91, "Guyana (GUY)")
    haiti_hti = EnumValue(92, "Haiti (HTI)")
    heard_island_and_mcdonald_islands_hmd = EnumValue(93, "Heard Island and McDonald Islands (HMD)")
    honduras_hnd = EnumValue(94, "Honduras (HND)")
    hong_kong_hkg = EnumValue(95, "Hong Kong (HKG)")
    howland_island_united_states = EnumValue(96, "Howland Island (United States)")
    hungary_hun = EnumValue(97, "Hungary (HUN)")
    iceland_isl = EnumValue(98, "Iceland (ISL)")
    india_ind = EnumValue(99, "India (IND)")
    indonesia_idn = EnumValue(100, "Indonesia (IDN)")
    iran_islamic_republic_of_irn = EnumValue(101, "Iran (Islamic Republic of) (IRN)")
    iraq_irq = EnumValue(102, "Iraq (IRQ)")
    ireland_irl = EnumValue(104, "Ireland (IRL)")
    israel_isr = EnumValue(105, "Israel (ISR)")
    italy_ita = EnumValue(106, "Italy (ITA)")
    cote_divoire_civ = EnumValue(107, "Cote d'Ivoire (CIV)")
    jamaica_jam = EnumValue(108, "Jamaica (JAM)")
    jan_mayen_norway = EnumValue(109, "Jan Mayen (Norway)")
    japan_jpn = EnumValue(110, "Japan (JPN)")
    jarvis_island_united_states = EnumValue(111, "Jarvis Island (United States)")
    jersey_jey = EnumValue(112, "Jersey (JEY)")
    johnston_atoll_united_states = EnumValue(113, "Johnston Atoll (United States)")
    jordan_jor = EnumValue(114, "Jordan (JOR)")
    juan_de_nova_island = EnumValue(115, "Juan de Nova Island")
    kenya_ken = EnumValue(116, "Kenya (KEN)")
    kingman_reef_united_states = EnumValue(117, "Kingman Reef (United States)")
    kiribati_kir = EnumValue(118, "Kiribati (KIR)")
    korea_democratic_peoples_republic_of_prk = EnumValue(119, "Korea (Democratic People's Republic of) (PRK)")
    korea_republic_of_kor = EnumValue(120, "Korea (Republic of) (KOR)")
    kuwait_kwt = EnumValue(121, "Kuwait (KWT)")
    lao_peoples_democratic_republic_lao = EnumValue(122, "Lao People's Democratic Republic (LAO)")
    lebanon_lbn = EnumValue(123, "Lebanon (LBN)")
    lesotho_lso = EnumValue(124, "Lesotho (LSO)")
    liberia_lbr = EnumValue(125, "Liberia (LBR)")
    libya_lby = EnumValue(126, "Libya (LBY)")
    liechtenstein_lie = EnumValue(127, "Liechtenstein (LIE)")
    luxembourg_lux = EnumValue(128, "Luxembourg (LUX)")
    madagascar_mdg = EnumValue(129, "Madagascar (MDG)")
    macao_mac = EnumValue(130, "Macao (MAC)")
    malawi_mwi = EnumValue(131, "Malawi (MWI)")
    malaysia_mys = EnumValue(132, "Malaysia (MYS)")
    maldives_mdv = EnumValue(133, "Maldives (MDV)")
    mali_mli = EnumValue(134, "Mali (MLI)")
    malta_mlt = EnumValue(135, "Malta (MLT)")
    isle_of_man_imn = EnumValue(136, "Isle of Man (IMN)")
    marshall_islands_mhl = EnumValue(137, "Marshall Islands (MHL)")
    martinique_mtq = EnumValue(138, "Martinique (MTQ)")
    mauritania_mrt = EnumValue(139, "Mauritania (MRT)")
    mauritius_mus = EnumValue(140, "Mauritius (MUS)")
    mayotte_myt = EnumValue(141, "Mayotte (MYT)")
    mexico_mex = EnumValue(142, "Mexico (MEX)")
    micronesia_federated_states_of_fsm = EnumValue(143, "Micronesia (Federated States of) (FSM)")
    monaco_mco = EnumValue(144, "Monaco (MCO)")
    mongolia_mng = EnumValue(145, "Mongolia (MNG)")
    montserrat_msr = EnumValue(146, "Montserrat (MSR)")
    morocco_mar = EnumValue(147, "Morocco (MAR)")
    mozambique_moz = EnumValue(148, "Mozambique (MOZ)")
    namibia_nam = EnumValue(149, "Namibia (NAM)")
    nauru_nru = EnumValue(150, "Nauru (NRU)")
    navassa_island_united_states = EnumValue(151, "Navassa Island (United States)")
    nepal_npl = EnumValue(152, "Nepal (NPL)")
    netherlands_nld = EnumValue(153, "Netherlands (NLD)")
    netherlands_antilles_curacao_bonaire_saba_sint_maarten_sint_eustatius = EnumValue(154, "Netherlands Antilles (Curacao, Bonaire, Saba, Sint Maarten Sint Eustatius)")
    new_caledonia_ncl = EnumValue(155, "New Caledonia (NCL)")
    new_zealand_nzl = EnumValue(156, "New Zealand (NZL)")
    nicaragua_nic = EnumValue(157, "Nicaragua (NIC)")
    niger_ner = EnumValue(158, "Niger (NER)")
    nigeria_nga = EnumValue(159, "Nigeria (NGA)")
    niue_niu = EnumValue(160, "Niue (NIU)")
    norfolk_island_nfk = EnumValue(161, "Norfolk Island (NFK)")
    northern_mariana_islands_mnp = EnumValue(162, "Northern Mariana Islands (MNP)")
    norway_nor = EnumValue(163, "Norway (NOR)")
    oman_omn = EnumValue(164, "Oman (OMN)")
    pakistan_pak = EnumValue(165, "Pakistan (PAK)")
    palmyra_atoll_united_states = EnumValue(166, "Palmyra Atoll (United States)")
    panama_pan = EnumValue(168, "Panama (PAN)")
    papua_new_guinea_png = EnumValue(169, "Papua New Guinea (PNG)")
    paracel_islands_international_occupied_by_china_also_claimed_by_taiwan_and_vietnam = EnumValue(170, "Paracel Islands (International - Occupied by China, also claimed by Taiwan and Vietnam)")
    paraguay_pry = EnumValue(171, "Paraguay (PRY)")
    peru_per = EnumValue(172, "Peru (PER)")
    philippines_phl = EnumValue(173, "Philippines (PHL)")
    pitcairn_pcn = EnumValue(174, "Pitcairn (PCN)")
    poland_pol = EnumValue(175, "Poland (POL)")
    portugal_prt = EnumValue(176, "Portugal (PRT)")
    puerto_rico_pri = EnumValue(177, "Puerto Rico (PRI)")
    qatar_qat = EnumValue(178, "Qatar (QAT)")
    reunion_reu = EnumValue(179, "Reunion (REU)")
    romania_rou = EnumValue(180, "Romania (ROU)")
    rwanda_rwa = EnumValue(181, "Rwanda (RWA)")
    saint_kitts_and_nevis_kna = EnumValue(182, "Saint Kitts and Nevis (KNA)")
    saint_helena_ascension_and_tristan_da_cunha_shn = EnumValue(183, "Saint Helena, Ascension and Tristan da Cunha (SHN)")
    saint_lucia_lca = EnumValue(184, "Saint Lucia (LCA)")
    saint_pierre_and_miquelon_spm = EnumValue(185, "Saint Pierre and Miquelon (SPM)")
    saint_vincent_and_the_grenadines_vct = EnumValue(186, "Saint Vincent and the Grenadines (VCT)")
    san_marino_smr = EnumValue(187, "San Marino (SMR)")
    sao_tome_and_principe_stp = EnumValue(188, "Sao Tome and Principe (STP)")
    saudi_arabia_sau = EnumValue(189, "Saudi Arabia (SAU)")
    senegal_sen = EnumValue(190, "Senegal (SEN)")
    seychelles_syc = EnumValue(191, "Seychelles (SYC)")
    sierra_leone_sle = EnumValue(192, "Sierra Leone (SLE)")
    singapore_sgp = EnumValue(193, "Singapore (SGP)")
    solomon_islands_slb = EnumValue(194, "Solomon Islands (SLB)")
    somalia_som = EnumValue(195, "Somalia (SOM)")
    south_georgia_and_the_south_sandwich_islands_sgs = EnumValue(196, "South Georgia and the South Sandwich Islands (SGS)")
    south_africa_zaf = EnumValue(197, "South Africa (ZAF)")
    spain_esp = EnumValue(198, "Spain (ESP)")
    spratly_islands_international_parts_occupied_and_claimed_by_china_malaysia_philippines_taiwan_vietnam = EnumValue(199, "Spratly Islands (International - parts occupied and claimed by China,Malaysia, Philippines, Taiwan, Vietnam)")
    sri_lanka_lka = EnumValue(200, "Sri Lanka (LKA)")
    sudan_sdn = EnumValue(201, "Sudan (SDN)")
    suriname_sur = EnumValue(202, "Suriname (SUR)")
    svalbard_norway = EnumValue(203, "Svalbard (Norway)")
    eswatini_swz = EnumValue(204, "Eswatini (SWZ)")
    sweden_swe = EnumValue(205, "Sweden (SWE)")
    switzerland_che = EnumValue(206, "Switzerland (CHE)")
    syrian_arab_republic_syr = EnumValue(207, "Syrian Arab Republic (SYR)")
    taiwan_province_of_china_twn = EnumValue(208, "Taiwan, Province of China (TWN)")
    tanzania_united_republic_of_tza = EnumValue(209, "Tanzania, United Republic of (TZA)")
    thailand_tha = EnumValue(210, "Thailand (THA)")
    togo_tgo = EnumValue(211, "Togo (TGO)")
    tokelau_tkl = EnumValue(212, "Tokelau (TKL)")
    tonga_ton = EnumValue(213, "Tonga (TON)")
    trinidad_and_tobago_tto = EnumValue(214, "Trinidad and Tobago (TTO)")
    tromelin_island_france = EnumValue(215, "Tromelin Island (France)")
    palau_plw = EnumValue(216, "Palau (PLW)")
    tunisia_tun = EnumValue(217, "Tunisia (TUN)")
    turkiye_republic_of_tur = EnumValue(218, "Turkiye (Republic of) (TUR)")
    turks_and_caicos_islands_tca = EnumValue(219, "Turks and Caicos Islands (TCA)")
    tuvalu_tuv = EnumValue(220, "Tuvalu (TUV)")
    uganda_uga = EnumValue(221, "Uganda (UGA)")
    russia_rus = EnumValue(222, "Russia (RUS)")
    united_arab_emirates_are = EnumValue(223, "United Arab Emirates (ARE)")
    united_kingdom_of_great_britain_and_northern_ireland_gbr = EnumValue(224, "United Kingdom of Great Britain and Northern Ireland (GBR)")
    united_states_of_america_usa = EnumValue(225, "United States of America (USA)")
    uruguay_ury = EnumValue(226, "Uruguay (URY)")
    vanuatu_vut = EnumValue(227, "Vanuatu (VUT)")
    holy_see_vat = EnumValue(228, "Holy See (VAT)")
    venezuela_bolivarian_republic_of_ven = EnumValue(229, "Venezuela (Bolivarian Republic of) (VEN)")
    viet_nam_vnm = EnumValue(230, "Viet Nam (VNM)")
    virgin_islands_us_vir = EnumValue(231, "Virgin Islands (U.S.) (VIR)")
    wake_island_united_states = EnumValue(232, "Wake Island (United States)")
    wallis_and_futuna_wlf = EnumValue(233, "Wallis and Futuna (WLF)")
    western_sahara_esh = EnumValue(234, "Western Sahara (ESH)")
    west_bank_israel = EnumValue(235, "West Bank (Israel)")
    samoa_wsm = EnumValue(236, "Samoa (WSM)")
    yemen_yem = EnumValue(237, "Yemen (YEM)")
    serbia_and_montenegro = EnumValue(240, "Serbia and Montenegro")
    zaire = EnumValue(241, "Zaire")
    zambia_zmb = EnumValue(242, "Zambia (ZMB)")
    zimbabwe_zwe = EnumValue(243, "Zimbabwe (ZWE)")
    armenia_arm = EnumValue(244, "Armenia (ARM)")
    azerbaijan_aze = EnumValue(245, "Azerbaijan (AZE)")
    belarus_blr = EnumValue(246, "Belarus (BLR)")
    bosnia_and_herzegovina_bih = EnumValue(247, "Bosnia and Herzegovina (BIH)")
    clipperton_island_france = EnumValue(248, "Clipperton Island (France)")
    croatia_hrv = EnumValue(249, "Croatia (HRV)")
    estonia_est = EnumValue(250, "Estonia (EST)")
    georgia_geo = EnumValue(251, "Georgia (GEO)")
    kazakhstan_kaz = EnumValue(252, "Kazakhstan (KAZ)")
    kyrgyzstan_kgz = EnumValue(253, "Kyrgyzstan (KGZ)")
    latvia_lva = EnumValue(254, "Latvia (LVA)")
    lithuania_ltu = EnumValue(255, "Lithuania (LTU)")
    north_macedonia_mkd = EnumValue(256, "North Macedonia (MKD)")
    midway_islands_united_states = EnumValue(257, "Midway Islands (United States)")
    moldova_republic_of_mda = EnumValue(258, "Moldova (Republic of) (MDA)")
    montenegro_mne = EnumValue(259, "Montenegro (MNE)")
    russia = EnumValue(260, "Russia")
    serbia_and_montenegro_montenegro_to_separate = EnumValue(261, "Serbia and Montenegro (Montenegro to separate)")
    slovenia_svn = EnumValue(262, "Slovenia (SVN)")
    tajikistan_tjk = EnumValue(263, "Tajikistan (TJK)")
    turkmenistan_tkm = EnumValue(264, "Turkmenistan (TKM)")
    ukraine_ukr = EnumValue(265, "Ukraine (UKR)")
    uzbekistan_uzb = EnumValue(266, "Uzbekistan (UZB)")
    czech_republic_cze = EnumValue(267, "Czech Republic (CZE)")
    slovakia_svk = EnumValue(268, "Slovakia (SVK)")
    aaland_islands_ala = EnumValue(269, "Aaland Islands (ALA)")
    bonaire_sint_eustatius_and_saba_bes = EnumValue(270, "Bonaire, Sint Eustatius and Saba (BES)")
    congo_democratic_republic_of_the_cod = EnumValue(271, "Congo (Democratic Republic of the) (COD)")
    curacao_cuw = EnumValue(272, "Curacao (CUW)")
    eritrea_eri = EnumValue(273, "Eritrea (ERI)")
    saint_barthelemy_blm = EnumValue(274, "Saint Barthelemy (BLM)")
    saint_martin_french_part_maf = EnumValue(275, "Saint Martin (French Part) (MAF)")
    serbia_srb = EnumValue(276, "Serbia (SRB)")
    sint_maarten_dutch_part_sxm = EnumValue(277, "Sint Maarten (Dutch part) (SXM)")
    south_sudan_ssd = EnumValue(278, "South Sudan (SSD)")
    svalbard_and_jan_mayen_sjm = EnumValue(279, "Svalbard and Jan Mayen (SJM)")
    timor_leste_tls = EnumValue(280, "Timor-Leste (TLS)")
    united_states_minor_outlying_islands_umi = EnumValue(281, "United States Minor Outlying Islands (UMI)")
    palestine_state_of_pse = EnumValue(282, "Palestine, State of (PSE)")
    default = other

    def get_marshaled_size(self):
        return 16
