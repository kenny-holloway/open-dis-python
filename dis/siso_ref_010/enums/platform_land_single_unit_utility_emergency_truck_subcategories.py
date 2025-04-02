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

# autogenerated using string template disenumpart1withfootnote.txt
# package edu.nps.moves.dis7.enumerations;

'''
/**
  *  UID 431, marshal size 8;
  * PlatformLandSingleUnitUtilityEmergencyTruckSubcategories has 45 enumerations total.
  * Subcategories for Land Platform Category 84
  * @see <a href="https://docs.oracle.com/javase/tutorial/java/javaOO/enum.html">Java Tutorials: Enum Types</a>
  * @see java.lang.Enum
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

class PlatformLandSingleUnitUtilityEmergencyTruckSubcategories(ExtensibleEnum, metaclass=EnumMeta):
    UNKNOWN = EnumValue(-1, "UNKNOWN Enum")
    other = EnumValue(0, "Other")
    ambulance_truck = EnumValue(1, "Ambulance Truck")
    fire_paramedic_truck = EnumValue(2, "Fire/Paramedic Truck")
    ambulance_advanced_life_support = EnumValue(3, "Ambulance, Advanced Life Support")
    ambulance_pickup_truck = EnumValue(4, "Ambulance Pickup Truck")
    fire_engine = EnumValue(10, "Fire Engine")
    aerial_ladder_fire_engine = EnumValue(11, "Aerial Ladder Fire Engine")
    airport_fire_engine = EnumValue(12, "Airport Fire Engine")
    wildland_fire_engine = EnumValue(13, "Wildland Fire Engine")
    fire_chief = EnumValue(14, "Fire Chief")
    police_paddy_wagon = EnumValue(20, "Police Paddy Wagon")
    police_swat = EnumValue(21, "Police, SWAT")
    police_bomb_squad = EnumValue(22, "Police, Bomb Squad")
    police_pickup_truck = EnumValue(23, "Police, Pickup Truck")
    hazmat = EnumValue(30, "Hazmat")
    wrecker_normal_hook_and_chain = EnumValue(40, "Wrecker, Normal Hook and Chain")
    wrecker_normal_boom = EnumValue(41, "Wrecker, Normal Boom")
    wrecker_normal_wheel_lift = EnumValue(42, "Wrecker, Normal Wheel Lift")
    wrecker_normal_flatbed = EnumValue(43, "Wrecker, Normal Flatbed")
    wrecker_normal_integrated = EnumValue(44, "Wrecker, Normal Integrated")
    wrecker_heavy_hook_and_chain = EnumValue(45, "Wrecker, Heavy Hook and Chain")
    wrecker_heavy_boom = EnumValue(46, "Wrecker, Heavy Boom")
    wrecker_heavy_wheel_lift = EnumValue(47, "Wrecker, Heavy Wheel Lift")
    wrecker_heavy_flatbed = EnumValue(48, "Wrecker, Heavy Flatbed")
    wrecker_heavy_integrated = EnumValue(49, "Wrecker, Heavy Integrated")
    postal_truck = EnumValue(60, "Postal Truck")
    street_sweeper = EnumValue(70, "Street Sweeper")
    street_sweeper_three_wheeled = EnumValue(71, "Street Sweeper, Three Wheeled")
    waste_collection_other = EnumValue(80, "Waste Collection, Other")
    waste_collection_front_loader = EnumValue(81, "Waste Collection, Front Loader")
    waste_collection_rear_loader = EnumValue(82, "Waste Collection, Rear Loader")
    waste_collection_automated_side_loader = EnumValue(83, "Waste Collection, Automated Side Loader")
    waste_collection_pneumatic_collection = EnumValue(84, "Waste Collection, Pneumatic Collection")
    waste_collection_grapple = EnumValue(85, "Waste Collection, Grapple")
    utility_truck = EnumValue(90, "Utility Truck")
    utility_truck_w_boom = EnumValue(91, "Utility Truck w/ Boom")
    aerial_work_platform_other = EnumValue(100, "Aerial Work Platform, Other")
    aerial_work_platform_scissor_lift = EnumValue(101, "Aerial Work Platform, Scissor Lift")
    aerial_work_platform_telescoping = EnumValue(102, "Aerial Work Platform, Telescoping")
    maintenance_truck = EnumValue(120, "Maintenance Truck")
    decontamination_truck = EnumValue(121, "Decontamination Truck")
    water_cannon_truck = EnumValue(122, "Water Cannon Truck")
    water_purification_truck = EnumValue(123, "Water Purification Truck")
    smoke_generator_truck = EnumValue(124, "Smoke Generator Truck")
    auto_rickshaw = EnumValue(150, "Auto Rickshaw")
    default = other

    def get_marshaled_size(self):
        return 8
