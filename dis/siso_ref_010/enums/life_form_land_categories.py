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
  * UID 472,
  * marshal size 8;
  * LifeFormLandCategories has 27 enumerations total.
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

class LifeFormLandCategories(ExtensibleEnum, metaclass=EnumMeta):
    UNKNOWN = EnumValue(-1, "UNKNOWN Enum")
    conventional_armed_forces = EnumValue(10, "Conventional Armed Forces")
    army = EnumValue(11, "Army")
    naval_infantry_marines = EnumValue(12, "Naval Infantry (Marines)")
    air_force = EnumValue(13, "Air Force")
    navy = EnumValue(14, "Navy")
    coast_guard = EnumValue(15, "Coast Guard")
    united_nations = EnumValue(16, "United Nations")
    special_operations_forces_sof = EnumValue(30, "Special Operations Forces (SOF)")
    law_enforcement = EnumValue(50, "Law Enforcement")
    non_military_national_government_agencies = EnumValue(70, "Non-Military National Government Agencies")
    regional_local_forces = EnumValue(90, "Regional / Local Forces")
    irregular_forces = EnumValue(100, "Irregular Forces")
    terrorist_combatant = EnumValue(101, "Terrorist Combatant")
    insurgent = EnumValue(102, "Insurgent")
    paramilitary_forces = EnumValue(110, "Paramilitary Forces")
    humanitarian_organizations = EnumValue(120, "Humanitarian Organizations")
    civilian = EnumValue(130, "Civilian")
    emergency_medical_technician_emt = EnumValue(131, "Emergency Medical Technician (EMT)")
    firefighter = EnumValue(132, "Firefighter")
    press = EnumValue(133, "Press")
    # XREF UID 100 - CLASS SubcategoriesforLandCategory200Mammal 
    mammal = EnumValue(200, "Mammal")
    # XREF UID 101 - CLASS SubcategoriesforLandCategory201Reptile 
    reptile = EnumValue(201, "Reptile")
    # XREF UID 102 - CLASS SubcategoriesforLandCategory202Amphibian 
    amphibian = EnumValue(202, "Amphibian")
    # XREF UID 103 - CLASS SubcategoriesforLandCategory203Insect 
    insect = EnumValue(203, "Insect")
    # XREF UID 104 - CLASS SubcategoriesforLandCategory204Arachnid 
    arachnid = EnumValue(204, "Arachnid")
    # XREF UID 105 - CLASS SubcategoriesforLandCategory205Mollusk 
    mollusk = EnumValue(205, "Mollusk")
    # XREF UID 106 - CLASS SubcategoriesforLandCategory206Marsupial 
    marsupial = EnumValue(206, "Marsupial")
    default = conventional_armed_forces

    def get_marshaled_size(self):
        return 8
