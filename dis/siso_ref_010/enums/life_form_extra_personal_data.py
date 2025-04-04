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
  *  UID 477, marshal size 8;
  * LifeFormExtraPersonalData has 38 enumerations total.
  * The 1's digit is reserved for Race/Ethnicity and the enumerations are taken from the U.S. OMB. The 10's digit is reserved for general age group. The 100's digit is reserved for gender, where 0 is Male and 1 is Female.
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

class LifeFormExtraPersonalData(ExtensibleEnum, metaclass=EnumMeta):
    UNKNOWN = EnumValue(-1, "UNKNOWN Enum")
    not_specified_male = EnumValue(0, "Not Specified (Male)")
    asian_male = EnumValue(1, "Asian (Male)")
    pacific_islander_male = EnumValue(2, "Pacific Islander (Male)")
    black_male = EnumValue(3, "Black (Male)")
    east_asian_male = EnumValue(4, "East Asian (Male)")
    hispanic_male = EnumValue(5, "Hispanic (Male)")
    white_male = EnumValue(6, "White (Male)")
    arab_male = EnumValue(7, "Arab (Male)")
    homogenous_country_code_male = EnumValue(8, "Homogenous Country Code (Male)")
    indigenous_country_code_male = EnumValue(9, "Indigenous Country Code (Male)")
    infant_0_months_1_year_male = EnumValue(10, "Infant (0 months-1 year) (Male)")
    toddler_1_3_years_male = EnumValue(20, "Toddler (1-3 years) (Male)")
    child_3_10_years_male = EnumValue(30, "Child (3-10 years) (Male)")
    adolescent_10_12_years_male = EnumValue(40, "Adolescent (10-12 years) (Male)")
    teenager_13_16_years_male = EnumValue(50, "Teenager (13-16 years) (Male)")
    young_adult_17_25_years_male = EnumValue(60, "Young Adult (17-25 years) (Male)")
    adult_25_55_years_male = EnumValue(70, "Adult (25-55 years) (Male)")
    senior_adult_55_70_years_male = EnumValue(80, "Senior Adult (55-70 years) (Male)")
    elderly_71PLUS_years_male = EnumValue(90, "Elderly (71+ years) (Male)")
    female = EnumValue(100, "Female")
    asian_female = EnumValue(101, "Asian (Female)")
    pacific_islander_female = EnumValue(102, "Pacific Islander (Female)")
    black_female = EnumValue(103, "Black (Female)")
    east_asian_female = EnumValue(104, "East Asian (Female)")
    hispanic_female = EnumValue(105, "Hispanic (Female)")
    white_female = EnumValue(106, "White (Female)")
    arab_female = EnumValue(107, "Arab (Female)")
    homogenous_country_code_female = EnumValue(108, "Homogenous Country Code (Female)")
    indigenous_country_code_female = EnumValue(109, "Indigenous Country Code (Female)")
    infant_0_months_1_year_female = EnumValue(110, "Infant (0 months-1 year) (Female)")
    toddler_1_3_years_female = EnumValue(120, "Toddler (1-3 years) (Female)")
    child_3_10_years_female = EnumValue(130, "Child (3-10 years) (Female)")
    adolescent_10_12_years_female = EnumValue(140, "Adolescent (10-12 years) (Female)")
    teenager_13_16_years_female = EnumValue(150, "Teenager (13-16 years) (Female)")
    young_adult_17_25_years_female = EnumValue(160, "Young Adult (17-25 years) (Female)")
    adult_25_55_years_female = EnumValue(170, "Adult (25-55 years) (Female)")
    senior_adult_55_70_years_female = EnumValue(180, "Senior Adult (55-70 years) (Female)")
    elderly_71PLUS_years_female = EnumValue(190, "Elderly (71+ years) (Female)")
    default = not_specified_male

    def get_marshaled_size(self):
        return 8
