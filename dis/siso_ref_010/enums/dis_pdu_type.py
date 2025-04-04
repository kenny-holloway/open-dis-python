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
  * UID 4,
  * marshal size 8;
  * DISPDUType has 73 enumerations total.
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

class DisPduType(ExtensibleEnum, metaclass=EnumMeta):
    UNKNOWN = EnumValue(-1, "UNKNOWN Enum")
    other = EnumValue(0, "Other")
    entity_state = EnumValue(1, "Entity State")
    fire = EnumValue(2, "Fire")
    detonation = EnumValue(3, "Detonation")
    collision = EnumValue(4, "Collision")
    service_request = EnumValue(5, "Service Request")
    resupply_offer = EnumValue(6, "Resupply Offer")
    resupply_received = EnumValue(7, "Resupply Received")
    resupply_cancel = EnumValue(8, "Resupply Cancel")
    repair_complete = EnumValue(9, "Repair Complete")
    repair_response = EnumValue(10, "Repair Response")
    create_entity = EnumValue(11, "Create Entity")
    remove_entity = EnumValue(12, "Remove Entity")
    start_resume = EnumValue(13, "Start/Resume")
    stop_freeze = EnumValue(14, "Stop/Freeze")
    acknowledge = EnumValue(15, "Acknowledge")
    action_request = EnumValue(16, "Action Request")
    action_response = EnumValue(17, "Action Response")
    data_query = EnumValue(18, "Data Query")
    set_data = EnumValue(19, "Set Data")
    data = EnumValue(20, "Data")
    event_report = EnumValue(21, "Event Report")
    comment = EnumValue(22, "Comment")
    electromagnetic_emission = EnumValue(23, "Electromagnetic Emission")
    designator = EnumValue(24, "Designator")
    transmitter = EnumValue(25, "Transmitter")
    signal = EnumValue(26, "Signal")
    receiver = EnumValue(27, "Receiver")
    identification_friend_or_foe = EnumValue(28, "IFF")
    underwater_acoustic = EnumValue(29, "Underwater Acoustic")
    supplemental_emission_entity_state = EnumValue(30, "Supplemental Emission / Entity State")
    intercom_signal = EnumValue(31, "Intercom Signal")
    intercom_control = EnumValue(32, "Intercom Control")
    aggregate_state = EnumValue(33, "Aggregate State")
    isgroupof = EnumValue(34, "IsGroupOf")
    transfer_ownership = EnumValue(35, "Transfer Ownership")
    ispartof = EnumValue(36, "IsPartOf")
    minefield_state = EnumValue(37, "Minefield State")
    minefield_query = EnumValue(38, "Minefield Query")
    minefield_data = EnumValue(39, "Minefield Data")
    minefield_response_nack = EnumValue(40, "Minefield Response NACK")
    environmental_process = EnumValue(41, "Environmental Process")
    gridded_data = EnumValue(42, "Gridded Data")
    point_object_state = EnumValue(43, "Point Object State")
    linear_object_state = EnumValue(44, "Linear Object State")
    areal_object_state = EnumValue(45, "Areal Object State")
    time_space_position_information = EnumValue(46, "TSPI")
    appearance = EnumValue(47, "Appearance")
    articulated_parts = EnumValue(48, "Articulated Parts")
    live_entity_fire = EnumValue(49, "LE Fire")
    live_entity_detonation = EnumValue(50, "LE Detonation")
    create_entity_reliable = EnumValue(51, "Create Entity-R")
    remove_entity_reliable = EnumValue(52, "Remove Entity-R")
    start_resume_reliable = EnumValue(53, "Start/Resume-R")
    stop_freeze_reliable = EnumValue(54, "Stop/Freeze-R")
    acknowledge_reliable = EnumValue(55, "Acknowledge-R")
    action_request_reliable = EnumValue(56, "Action Request-R")
    action_response_reliable = EnumValue(57, "Action Response-R")
    data_query_reliable = EnumValue(58, "Data Query-R")
    set_data_reliable = EnumValue(59, "Set Data-R")
    data_reliable = EnumValue(60, "Data-R")
    event_report_reliable = EnumValue(61, "Event Report-R")
    comment_reliable = EnumValue(62, "Comment-R")
    record_reliable = EnumValue(63, "Record-R")
    set_record_reliable = EnumValue(64, "Set Record-R")
    record_query_reliable = EnumValue(65, "Record Query-R")
    collision_elastic = EnumValue(66, "Collision-Elastic")
    entity_state_update = EnumValue(67, "Entity State Update")
    directed_energy_fire = EnumValue(68, "Directed Energy Fire")
    entity_damage_status = EnumValue(69, "Entity Damage Status")
    information_operations_action = EnumValue(70, "Information Operations Action")
    information_operations_report = EnumValue(71, "Information Operations Report")
    attribute = EnumValue(72, "Attribute")
    default = other

    def get_marshaled_size(self):
        return 8
