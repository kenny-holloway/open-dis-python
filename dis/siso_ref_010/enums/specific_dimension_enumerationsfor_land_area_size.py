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
  *  UID 131, marshal size 8;
  * SpecificDimensionEnumerationsforLandAreaSize has 6 enumerations total.
  * The gaps in enumeration values are intentional and are reserved for future additions.
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

class SpecificDimensionEnumerationsforLandAreaSize(ExtensibleEnum, metaclass=EnumMeta):
    UNKNOWN = EnumValue(-1, "UNKNOWN Enum")
    small_area_2_000m2_4_000m2_5_to_1_sq_acre_ = EnumValue(222, "Small Area (2,000m2 - 4,000m2 / .5 to 1 sq. acre )")
    small_area_dense_2_000m2_4_000m2_5_to1_sq_acre = EnumValue(223, "Small Area, Dense (2,000m2 - 4,000m2 / .5 to1 sq. acre)")
    medium_area_20_000m2_41_000m2_10_to_20_sq_acres = EnumValue(224, "Medium Area (20,000m2 - 41,000m2 / 10 to 20 sq. acres)")
    medium_area_dense_20_000m2_41_000m2_10_to_20_sq_acres = EnumValue(225, "Medium Area, Dense (20,000m2 - 41,000m2 / 10 to 20 sq. acres)")
    large_area_40_000m2_81_000m2_20_to_40_sq_acres = EnumValue(226, "Large Area (40,000m2 - 81,000m2 / 20 to 40 sq. acres)")
    large_area_dense_40_000m2_81_000m2_20_to_40_sq_acres = EnumValue(227, "Large Area, Dense (40,000m2 - 81,000m2 / 20 to 40 sq. acres)")
    default = small_area_2_000m2_4_000m2_5_to_1_sq_acre_

    def get_marshaled_size(self):
        return 8
