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
  * UID 120,
  * marshal size 8;
  * SubcategoriesforSubsurfaceCategory200Fish has 27 enumerations total.
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

class SubcategoriesforSubsurfaceCategory200Fish(ExtensibleEnum, metaclass=EnumMeta):
    UNKNOWN = EnumValue(-1, "UNKNOWN Enum")
    forage_fish_small_schooling = EnumValue(1, "Forage Fish, Small Schooling")
    herring = EnumValue(2, "Herring")
    sardines = EnumValue(3, "Sardines")
    krill = EnumValue(4, "Krill")
    squid = EnumValue(5, "Squid")
    medium_schooling_fish = EnumValue(30, "Medium Schooling Fish")
    hake = EnumValue(31, "Hake")
    cod = EnumValue(32, "Cod")
    haddock = EnumValue(33, "Haddock")
    mackerel = EnumValue(34, "Mackerel")
    large_schooling_fish = EnumValue(60, "Large Schooling Fish")
    tuna = EnumValue(61, "Tuna")
    small_shark = EnumValue(90, "Small Shark")
    dogfish_shark = EnumValue(91, "Dogfish Shark")
    medium_shark = EnumValue(120, "Medium Shark")
    mako_shark = EnumValue(121, "Mako Shark")
    hammerhead_shark = EnumValue(122, "Hammerhead Shark")
    large_shark = EnumValue(150, "Large Shark")
    great_white_shark = EnumValue(151, "Great White Shark")
    tiger_shark = EnumValue(152, "Tiger Shark")
    blue_shark = EnumValue(153, "Blue Shark")
    whale_shark = EnumValue(154, "Whale Shark")
    skate = EnumValue(180, "Skate")
    stingray = EnumValue(181, "Stingray")
    eel = EnumValue(190, "Eel")
    marlin = EnumValue(200, "Marlin")
    swordfish = EnumValue(201, "Swordfish")
    default = forage_fish_small_schooling

    def get_marshaled_size(self):
        return 8
