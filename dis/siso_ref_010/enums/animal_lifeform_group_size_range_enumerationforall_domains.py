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
  *  UID 130, marshal size 8;
  * AnimalLifeFormGroupSizeRangeEnumerationforallDomains has 14 enumerations total.
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

class AnimalLifeFormGroupSizeRangeEnumerationforallDomains(ExtensibleEnum, metaclass=EnumMeta):
    UNKNOWN = EnumValue(-1, "UNKNOWN Enum")
    number_of_animals_range_from_201_to_249 = EnumValue(201, "Number of animals range from 201 to 249")
    number_of_animals_range_from_250_to_299 = EnumValue(202, "Number of animals range from 250 to 299")
    number_of_animals_range_from_300_to_399 = EnumValue(203, "Number of animals range from 300 to 399")
    number_of_animals_range_from_400_to_499 = EnumValue(204, "Number of animals range from 400 to 499")
    number_of_animals_range_from_500_to_999 = EnumValue(205, "Number of animals range from 500 to 999")
    number_of_animals_range_from_1_000_to_1_499 = EnumValue(206, "Number of animals range from 1,000 to 1,499")
    number_of_animals_range_from_1_500_to_1_999 = EnumValue(207, "Number of animals range from 1,500 to 1,999")
    number_of_animals_range_from_2_000_to_2_999 = EnumValue(208, "Number of animals range from 2,000 to 2,999")
    number_of_animals_range_from_3_000_to_4_999 = EnumValue(210, "Number of animals range from 3,000 to 4,999")
    number_of_animals_range_from_5_000_to_6_999 = EnumValue(212, "Number of animals range from 5,000 to 6,999")
    number_of_animals_range_from_7_000_to_9_999 = EnumValue(214, "Number of animals range from 7,000 to 9,999")
    number_of_animals_range_from_10_000_to_19_999 = EnumValue(216, "Number of animals range from 10,000 to 19,999")
    number_of_animals_range_from_20_000_to_50_000 = EnumValue(218, "Number of animals range from 20,000 to 50,000")
    number_of_animals_range_greater_than_50_000 = EnumValue(220, "Number of animals range greater than 50,000")
    default = number_of_animals_range_from_201_to_249

    def get_marshaled_size(self):
        return 8
