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
  * UID 323,
  * marshal size 8;
  * EntityAssociationPhysicalAssociationType has 28 enumerations total.
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

class EntityAssociationPhysicalAssociationType(ExtensibleEnum, metaclass=EnumMeta):
    UNKNOWN = EnumValue(-1, "UNKNOWN Enum")
    not_specified = EnumValue(0, "Not Specified")
    towed_in_air_single_hook_not_specified = EnumValue(1, "Towed in Air (Single Hook, Not Specified)")
    towed_on_land = EnumValue(2, "Towed on Land")
    towed_on_water_surface = EnumValue(3, "Towed on Water Surface")
    towed_underwater = EnumValue(4, "Towed Underwater")
    mounted_attached = EnumValue(5, "Mounted Attached")
    mounted_unattached_and_unsupported = EnumValue(6, "Mounted Unattached and Unsupported")
    mounted_unattached_and_supported = EnumValue(7, "Mounted Unattached and Supported")
    towed_in_air_center_hook = EnumValue(8, "Towed in Air (Center Hook)")
    towed_in_air_forward_hook = EnumValue(9, "Towed in Air (Forward Hook)")
    towed_in_air_aft_hook = EnumValue(10, "Towed in Air (Aft Hook)")
    towed_in_air_tandem_hook_fore_and_aft = EnumValue(11, "Towed in Air (Tandem Hook - Fore and Aft)")
    towed_in_air_mismanaged_tandem_fore_and_center = EnumValue(12, "Towed in Air (Mismanaged Tandem - Fore and Center)")
    towed_in_air_mismanaged_tandem_center_and_aft = EnumValue(13, "Towed in Air (Mismanaged Tandem - Center and Aft)")
    towed_in_air_all_hooks = EnumValue(14, "Towed in Air (All Hooks)")
    hoisted = EnumValue(15, "Hoisted")
    restrained_to_a_life_form = EnumValue(30, "Restrained to a Life Form")
    restrained_to_a_platform = EnumValue(31, "Restrained to a Platform")
    restrained_to_an_object = EnumValue(32, "Restrained to an Object")
    refueling_operation = EnumValue(61, "Refueling Operation")
    search_and_rescue_basket = EnumValue(62, "Search and Rescue Basket")
    search_and_rescue_rescue_collar = EnumValue(63, "Search and Rescue Rescue Collar")
    engagement_object_2_is_being_engaged = EnumValue(64, "Engagement/Object 2 is Being Engaged")
    return_to_base_object_2_is_the_destination_object = EnumValue(65, "Return To Base/Object 2 is the Destination Object")
    line_between_communication_towers = EnumValue(90, "Line between Communication Towers")
    line_between_power_towers = EnumValue(91, "Line Between Power Towers")
    indoors = EnumValue(92, "Indoors")
    top_surface = EnumValue(93, "Top Surface")
    default = not_specified

    def get_marshaled_size(self):
        return 8
