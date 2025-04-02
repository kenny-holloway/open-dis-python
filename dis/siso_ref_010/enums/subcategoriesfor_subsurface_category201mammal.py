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
  * UID 121,
  * marshal size 8;
  * SubcategoriesforSubsurfaceCategory201Mammal has 59 enumerations total.
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

class SubcategoriesforSubsurfaceCategory201Mammal(ExtensibleEnum, metaclass=EnumMeta):
    UNKNOWN = EnumValue(-1, "UNKNOWN Enum")
    whale = EnumValue(1, "Whale")
    beaked_whale = EnumValue(2, "Beaked Whale")
    beluga_whale = EnumValue(3, "Beluga Whale")
    blue_whale = EnumValue(4, "Blue Whale")
    bottlenose_whale = EnumValue(5, "Bottlenose Whale")
    northern_bottlenose_whale = EnumValue(6, "Northern Bottlenose Whale")
    southern_bottlenose_whale = EnumValue(7, "Southern Bottlenose Whale")
    bowhead_whale = EnumValue(8, "Bowhead Whale")
    brydes_whale = EnumValue(9, "Bryde's Whale")
    dwarf_sperm_whale = EnumValue(10, "Dwarf Sperm Whale")
    finback_whale = EnumValue(11, "Finback Whale")
    gray_whale = EnumValue(12, "Gray Whale")
    humpback_whale = EnumValue(13, "Humpback Whale")
    long_finned_pilot_whale = EnumValue(14, "Long-Finned Pilot Whale")
    minke_whale = EnumValue(15, "Minke Whale")
    northern_minke_whale = EnumValue(16, "Northern Minke Whale")
    southern_minke_whale = EnumValue(17, "Southern Minke Whale")
    narwhal_whale = EnumValue(18, "Narwhal Whale")
    orca_whale = EnumValue(19, "Orca Whale")
    pygmy_sperm_whale = EnumValue(20, "Pygmy Sperm Whale")
    right_whale = EnumValue(21, "Right Whale")
    north_atlantic_right_whale = EnumValue(22, "North Atlantic Right Whale")
    north_pacific_right_whale = EnumValue(23, "North Pacific Right Whale")
    southern_right_whale = EnumValue(24, "Southern Right Whale")
    sei_whale = EnumValue(25, "Sei Whale")
    short_finned_pilot_whale = EnumValue(26, "Short-Finned Pilot Whale")
    sperm_whale = EnumValue(27, "Sperm Whale")
    dolphin = EnumValue(50, "Dolphin")
    bottlenose_dolphin = EnumValue(51, "Bottlenose Dolphin")
    bottlenose_indo_pacific_dolphin = EnumValue(52, "Bottlenose Indo-Pacific Dolphin")
    bottlenose_burrunan_dolphin = EnumValue(53, "Bottlenose Burrunan Dolphin")
    atlantic_spotted_dolphin = EnumValue(54, "Atlantic Spotted Dolphin")
    australian_snubfin_dolphin = EnumValue(55, "Australian Snubfin Dolphin")
    chilean_black_dolphin = EnumValue(56, "Chilean Black Dolphin")
    chinese_white_dolphin = EnumValue(57, "Chinese White Dolphin")
    clymene_dolphin = EnumValue(58, "Clymene Dolphin")
    porpoise = EnumValue(100, "Porpoise")
    harbour_porpoise = EnumValue(101, "Harbour Porpoise")
    californian_porpoise = EnumValue(102, "Californian Porpoise")
    dalls_porpoise = EnumValue(103, "Dall's Porpoise")
    burmeisters_porpoise = EnumValue(104, "Burmeister's Porpoise")
    seal = EnumValue(120, "Seal")
    bearded_seal = EnumValue(121, "Bearded Seal")
    harbor_seal = EnumValue(122, "Harbor Seal")
    fur_seal = EnumValue(123, "Fur Seal")
    weddell_seal = EnumValue(124, "Weddell Seal")
    elephant_seal = EnumValue(125, "Elephant Seal")
    sea_lion = EnumValue(130, "Sea Lion")
    australian_sea_lion = EnumValue(131, "Australian Sea Lion")
    california_sea_lion = EnumValue(132, "California Sea Lion")
    walrus = EnumValue(140, "Walrus")
    atlantic_walrus = EnumValue(141, "Atlantic Walrus")
    pacific_walrus = EnumValue(142, "Pacific Walrus")
    otter = EnumValue(150, "Otter")
    sea_otter = EnumValue(151, "Sea Otter")
    manatee = EnumValue(160, "Manatee")
    florida_manatee = EnumValue(161, "Florida Manatee")
    dugongs = EnumValue(162, "Dugongs")
    polar_bear = EnumValue(200, "Polar Bear")
    default = whale

    def get_marshaled_size(self):
        return 8
