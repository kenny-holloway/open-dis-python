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
  * UID 178,
  * marshal size 16;
  * SignalTDLType has 97 enumerations total.
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

class SignalTDLType(ExtensibleEnum, metaclass=EnumMeta):
    UNKNOWN = EnumValue(-1, "UNKNOWN Enum")
    other = EnumValue(0, "Other")
    padil = EnumValue(1, "PADIL")
    nato_link_1 = EnumValue(2, "NATO Link-1")
    atdl_1 = EnumValue(3, "ATDL-1")
    link_11b_tadil_b = EnumValue(4, "Link 11B (TADIL B)")
    situational_awareness_data_link_sadl = EnumValue(5, "Situational Awareness Data Link (SADL)")
    link_16_legacy_format_jtids_tadil_j = EnumValue(6, "Link 16 Legacy Format (JTIDS/TADIL-J)")
    link_16_legacy_format_jtids_fdl_tadil_j = EnumValue(7, "Link 16 Legacy Format (JTIDS/FDL/TADIL-J)")
    link_11_tadil_a = EnumValue(8, "Link 11 (TADIL A)")
    ijms = EnumValue(9, "IJMS")
    link_4a_tadil_c = EnumValue(10, "Link 4A (TADIL C)")
    link_4c = EnumValue(11, "Link 4C")
    tibs = EnumValue(12, "TIBS")
    atl = EnumValue(13, "ATL")
    constant_source = EnumValue(14, "Constant Source")
    abbreviated_command_and_control = EnumValue(15, "Abbreviated Command and Control")
    milstar = EnumValue(16, "MILSTAR")
    aths = EnumValue(17, "ATHS")
    othgold = EnumValue(18, "OTHGOLD")
    tacelint = EnumValue(19, "TACELINT")
    weapons_data_link_aww_13 = EnumValue(20, "Weapons Data Link (AWW-13)")
    abbreviated_command_and_control_2 = EnumValue(21, "Abbreviated Command and Control")
    enhanced_position_location_reporting_system_eplrs = EnumValue(22, "Enhanced Position Location Reporting System (EPLRS)")
    position_location_reporting_system_plrs = EnumValue(23, "Position Location Reporting System (PLRS)")
    sincgars = EnumValue(24, "SINCGARS")
    have_quick_i = EnumValue(25, "HAVE QUICK I")
    have_quick_ii = EnumValue(26, "HAVE QUICK II")
    saturn = EnumValue(27, "SATURN")
    intra_flight_data_link_1 = EnumValue(28, "Intra-Flight Data Link 1")
    intra_flight_data_link_2 = EnumValue(29, "Intra-Flight Data Link 2")
    improved_data_modem_idm = EnumValue(30, "Improved Data Modem (IDM)")
    air_force_application_program_development_afapd = EnumValue(31, "Air Force Application Program Development (AFAPD)")
    cooperative_engagement_capability_cec = EnumValue(32, "Cooperative Engagement Capability (CEC)")
    forward_area_air_defense_faad_data_link_fdl = EnumValue(33, "Forward Area Air Defense (FAAD) Data Link (FDL)")
    ground_based_data_link_gbdl = EnumValue(34, "Ground Based Data Link (GBDL)")
    intra_vehicular_info_system_ivis = EnumValue(35, "Intra Vehicular Info System (IVIS)")
    marine_tactical_system_mts = EnumValue(36, "Marine Tactical System (MTS)")
    tactical_fire_direction_system_tacfire = EnumValue(37, "Tactical Fire Direction System (TACFIRE)")
    integrated_broadcast_service_ibs = EnumValue(38, "Integrated Broadcast Service (IBS)")
    airborne_information_transfer_abit = EnumValue(39, "Airborne Information Transfer (ABIT)")
    advanced_tactical_airborne_reconnaissance_system_atars_data_link = EnumValue(40, "Advanced Tactical Airborne Reconnaissance System (ATARS) Data Link")
    battle_group_passive_horizon_extension_system_bgphes_data_link = EnumValue(41, "Battle Group Passive Horizon Extension System (BGPHES) Data Link")
    common_high_bandwidth_data_link_chbdl = EnumValue(42, "Common High Bandwidth Data Link (CHBDL)")
    guardrail_interoperable_data_link_idl = EnumValue(43, "Guardrail Interoperable Data Link (IDL)")
    guardrail_common_sensor_system_one_css1_data_link = EnumValue(44, "Guardrail Common Sensor System One (CSS1) Data Link")
    guardrail_common_sensor_system_two_css2_data_link = EnumValue(45, "Guardrail Common Sensor System Two (CSS2) Data Link")
    guardrail_css2_multi_role_data_link_mrdl = EnumValue(46, "Guardrail CSS2 Multi-Role Data Link (MRDL)")
    guardrail_css2_direct_air_to_satellite_relay_dasr_data_link = EnumValue(47, "Guardrail CSS2 Direct Air to Satellite Relay (DASR) Data Link")
    line_of_sight_los_data_link_implementation_los_tether = EnumValue(48, "Line of Sight (LOS) Data Link Implementation (LOS tether)")
    lightweight_cdl_lwcdl = EnumValue(49, "Lightweight CDL (LWCDL)")
    l_52m_sr_71 = EnumValue(50, "L-52M (SR-71)")
    rivet_reach_rivet_owl_data_link = EnumValue(51, "Rivet Reach/Rivet Owl Data Link")
    senior_span = EnumValue(52, "Senior Span")
    senior_spur = EnumValue(53, "Senior Spur")
    senior_stretch = EnumValue(54, "Senior Stretch.")
    senior_year_interoperable_data_link_idl = EnumValue(55, "Senior Year Interoperable Data Link (IDL)")
    space_cdl = EnumValue(56, "Space CDL")
    tr_1_mode_mist_airborne_data_link = EnumValue(57, "TR-1 mode MIST Airborne Data Link")
    ku_band_satcom_data_link_implementation_uav = EnumValue(58, "Ku-band SATCOM Data Link Implementation (UAV)")
    mission_equipment_control_data_link_mecdl = EnumValue(59, "Mission Equipment Control Data link (MECDL)")
    radar_data_transmitting_set_data_link = EnumValue(60, "Radar Data Transmitting Set Data Link")
    surveillance_and_control_data_link_scdl = EnumValue(61, "Surveillance and Control Data Link (SCDL)")
    tactical_uav_video = EnumValue(62, "Tactical UAV Video")
    uhf_satcom_data_link_implementation_uav = EnumValue(63, "UHF SATCOM Data Link Implementation (UAV)")
    tactical_common_data_link_tcdl = EnumValue(64, "Tactical Common Data Link (TCDL)")
    low_level_air_picture_interface_llapi = EnumValue(65, "Low Level Air Picture Interface (LLAPI)")
    weapons_data_link_agm_130 = EnumValue(66, "Weapons Data Link (AGM-130)")
    automatic_identification_system_ais = EnumValue(67, "Automatic Identification System (AIS)")
    weapons_data_link_aim_120 = EnumValue(68, "Weapons Data Link (AIM-120)")
    weapons_data_link_aim_9 = EnumValue(69, "Weapons Data Link (AIM-9)")
    weapons_data_link_camm = EnumValue(70, "Weapons Data Link (CAMM)")
    gc3 = EnumValue(99, "GC3")
    link_16_standardized_format_jtids_mids_tadil_j = EnumValue(100, "Link 16 Standardized Format (JTIDS/MIDS/TADIL J)")
    link_16_enhanced_data_rate_edr_jtids_mids_tadil_j = EnumValue(101, "Link 16 Enhanced Data Rate (EDR JTIDS/MIDS/TADIL-J)")
    jtids_mids_net_data_load_tims_toms = EnumValue(102, "JTIDS/MIDS Net Data Load (TIMS/TOMS)")
    link_22 = EnumValue(103, "Link 22")
    afiwc_iads_communications_links = EnumValue(104, "AFIWC IADS Communications Links")
    f_22_intra_flight_data_link_ifdl = EnumValue(105, "F-22 Intra-Flight Data Link (IFDL)")
    l_band_satcom = EnumValue(106, "L-Band SATCOM")
    tsaf_communications_link = EnumValue(107, "TSAF Communications Link")
    enhanced_sincgars_73 = EnumValue(108, "Enhanced SINCGARS 7.3")
    f_35_multifunction_advanced_data_link_madl = EnumValue(109, "F-35 Multifunction Advanced Data Link (MADL)")
    cursor_on_target = EnumValue(110, "Cursor on Target")
    all_purpose_structured_eurocontrol_surveillance_information_exchange_asterix = EnumValue(111, "All Purpose Structured Eurocontrol Surveillance Information Exchange (ASTERIX)")
    variable_message_format_vmf_over_combat_net_radio_vmf_over_cnr = EnumValue(112, "Variable Message Format (VMF) over Combat Net Radio (VMF over CNR)")
    link_16_surrogate_for_non_nato_tdl = EnumValue(113, "Link 16 Surrogate for Non-NATO TDL")
    mq_1_9_c_band_los_uplink = EnumValue(114, "MQ-1/9 C-Band LOS Uplink")
    mq_1_9_c_band_los_downlink = EnumValue(115, "MQ-1/9 C-Band LOS Downlink")
    mq_1_9_ku_band_satcom_uplink = EnumValue(116, "MQ-1/9 Ku-Band SATCOM Uplink")
    mq_1_9_ku_band_satcom_downlink = EnumValue(117, "MQ-1/9 Ku-Band SATCOM Downlink")
    weapons_datalink_sdb_ii = EnumValue(118, "Weapons Datalink (SDB II)")
    jtac_sa_uplink = EnumValue(119, "JTAC SA Uplink")
    common_interactive_broadcast_cib = EnumValue(120, "Common Interactive Broadcast (CIB)")
    joint_range_extension_application_protocol_a_jreap_a = EnumValue(121, "Joint Range Extension Application Protocol A (JREAP A)")
    jpals_data_link = EnumValue(125, "JPALS Data Link")
    onesaf_iads_communications_link = EnumValue(126, "OneSAF IADS Communications Link")
    tactical_targeting_network_technology_ttnt_application = EnumValue(127, "Tactical Targeting Network Technology (TTNT) Application")
    default = other

    def get_marshaled_size(self):
        return 16
