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
  * UID 474,
  * marshal size 8;
  * LifeFormHumanSpecificAssaultRifles has 80 enumerations total.
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

class LifeFormHumanSpecificAssaultRifles(ExtensibleEnum, metaclass=EnumMeta):
    UNKNOWN = EnumValue(-1, "UNKNOWN Enum")
    other = EnumValue(0, "Other")
    _45mm_interdynamics_mkr = EnumValue(1, "4.5mm Interdynamics MKR")
    _545mm_ak_74 = EnumValue(10, "5.45mm AK-74")
    _545mm_aks_74 = EnumValue(11, "5.45mm AKS-74")
    _545mm_ak_74m = EnumValue(12, "5.45mm AK-74M")
    _545mm_kbk_wz_1988_tantal = EnumValue(13, "5.45mm Kbk wz. 1988 Tantal")
    _545mm_fort_221 = EnumValue(14, "5.45mm Fort-221")
    _545mm_556mm_762mm_ipi_malyuk = EnumValue(20, "5.45mm/5.56mm/7.62mm IPI Malyuk")
    _556mm_ak_101 = EnumValue(30, "5.56mm AK-101")
    _556mm_diemaco_c7 = EnumValue(31, "5.56mm Diemaco C7")
    _556mm_colt_canada_c8_carbine = EnumValue(32, "5.56mm Colt Canada C8 Carbine")
    _556mm_giat_famas_g2 = EnumValue(33, "5.56mm GIAT FAMAS G2")
    _556mm_fn_fnc = EnumValue(34, "5.56mm FN FNC")
    _556mm_hk_g36 = EnumValue(35, "5.56mm HK G36")
    _556mm_imi_galil = EnumValue(36, "5.56mm IMI Galil")
    _556mm_insas = EnumValue(37, "5.56mm INSAS")
    _556mm_daewoo_k1 = EnumValue(38, "5.56mm Daewoo K1")
    _556mm_daewoo_k2 = EnumValue(39, "5.56mm Daewoo K2")
    _556mm_m16a1 = EnumValue(40, "5.56mm M16A1")
    _556mm_m16a2_a3_a4 = EnumValue(41, "5.56mm M16A2/A3/A4")
    _556mm_colt_m4 = EnumValue(42, "5.56mm Colt M4")
    _556mm_colt_m4_special_operations_peculiar_modification_sopmod = EnumValue(43, "5.56mm Colt M4 Special Operations Peculiar Modification (SOPMOD)")
    _556mm_ruger_mini_14 = EnumValue(44, "5.56mm Ruger Mini-14")
    _556mm_enfield_sa_80a2 = EnumValue(45, "5.56mm Enfield SA-80A2")
    _556mm_pindad_ss1_v1 = EnumValue(46, "5.56mm Pindad SS1 V1")
    _556mm_pindad_ss1_v2 = EnumValue(47, "5.56mm Pindad SS1 V2")
    _556mm_pindad_ss1_v3 = EnumValue(48, "5.56mm Pindad SS1 V3")
    _556mm_steyr_aug_a1 = EnumValue(49, "5.56mm Steyr AUG A1")
    _556mm_t65 = EnumValue(50, "5.56mm T65")
    _556mm_t91 = EnumValue(51, "5.56mm T91")
    _556mm_tavor_tar_21 = EnumValue(52, "5.56mm Tavor TAR-21")
    _556mm_type_cq_m311 = EnumValue(53, "5.56mm Type CQ / M311")
    _556mm_daewoo_k11 = EnumValue(54, "5.56mm Daewoo K11")
    _556mm_austeyr_f88 = EnumValue(55, "5.56mm Austeyr F88")
    _556mm_austeyr_f88_gla = EnumValue(56, "5.56mm Austeyr F88-GLA")
    _556mm_austeyr_f88_s_a1 = EnumValue(57, "5.56mm Austeyr F88-S-A1")
    _556mm_austeyr_f88_s_a2 = EnumValue(58, "5.56mm Austeyr F88-S-A2")
    _556mm_austeyr_f88_c = EnumValue(59, "5.56mm Austeyr F88-C")
    _556mm_austeyr_f88_s_a1c = EnumValue(60, "5.56mm Austeyr F88-S-A1C")
    _556mm_austeyr_f88_s_a1_ltr = EnumValue(61, "5.56mm Austeyr F88-S-A1 LTR")
    _556mm_austeyr_ef88 = EnumValue(62, "5.56mm Austeyr EF88")
    _556mm_bushmaster_xm15 = EnumValue(63, "5.56mm Bushmaster XM15")
    _556mm_hk416 = EnumValue(64, "5.56mm HK416")
    _556mm_f90 = EnumValue(65, "5.56mm F90")
    _556mm_f90g = EnumValue(66, "5.56mm F90(G)")
    _556mm_f90m = EnumValue(67, "5.56mm F90M")
    _556mm_f90mg = EnumValue(68, "5.56mm F90M(G)")
    _556mm_f90cqb = EnumValue(69, "5.56mm F90CQB")
    _556mm_mk17_scar_l = EnumValue(70, "5.56mm MK17 SCAR-L")
    _556mm_cz_805_bren = EnumValue(71, "5.56mm CZ 805 BREN")
    _556mm_fort_224 = EnumValue(72, "5.56mm Fort-224")
    _556mm_fort_227 = EnumValue(73, "5.56mm Fort-227")
    _556mm_zbroyar_uar_15 = EnumValue(74, "5.56mm Zbroyar UAR-15")
    _556mm_zbroyar_z_15 = EnumValue(75, "5.56mm Zbroyar Z-15")
    _556mm_762mm_cz_bren_2 = EnumValue(76, "5.56mm/7.62mm CZ BREN 2")
    _58mm_qbz_95_type_95 = EnumValue(100, "5.8mm QBZ-95 (Type 95)")
    _762mm_ak_103 = EnumValue(110, "7.62mm AK-103")
    _762mm_ak_104 = EnumValue(111, "7.62mm AK-104")
    _762mm_ak_47 = EnumValue(112, "7.62mm AK-47")
    _762mm_akm = EnumValue(113, "7.62mm AKM")
    _762mm_aks_47 = EnumValue(114, "7.62mm AKS-47")
    _762mm_hk_g3a3 = EnumValue(115, "7.62mm HK G3A3")
    _762mm_imi_galil = EnumValue(116, "7.62mm IMI Galil")
    _762mm_kls = EnumValue(117, "7.62mm KLS")
    _762mm_sks = EnumValue(118, "7.62mm SKS")
    _762mm_type_56 = EnumValue(119, "7.62mm Type 56")
    _762mm_type_63_68 = EnumValue(120, "7.62mm Type 63/68")
    _762mm_type_81 = EnumValue(121, "7.62mm Type 81")
    _762mm_mk17_scar_h = EnumValue(122, "7.62mm MK17 SCAR-H")
    _762mm_fort_228 = EnumValue(123, "7.62mm Fort-228")
    _762mm_fort_229 = EnumValue(124, "7.62mm Fort-229")
    _762mm_zbroyar_z_008_non_sniper_variant = EnumValue(125, "7.62mm Zbroyar Z-008 (non-sniper variant)")
    _762mm_zbroyar_z_10 = EnumValue(126, "7.62mm Zbroyar Z-10")
    _762mm_mayak_mz_10 = EnumValue(127, "7.62mm Mayak MZ-10")
    _762mm_stiletto_systems_stl_016_300_winchester = EnumValue(128, "7.62mm Stiletto Systems STL-016 .300 Winchester")
    _762mm_cz_bren_2_br = EnumValue(129, "7.62mm CZ BREN 2 BR")
    _762mm_sa_vz_58_p = EnumValue(130, "7.62mm Sa vz. 58 P")
    _762mm_sa_vz_58_v = EnumValue(131, "7.62mm Sa vz. 58 V")
    _68mm_m7_next_generation_squad_weapon_ngsw = EnumValue(150, "6.8mm M7 Next Generation Squad Weapon (NGSW)")
    _8mm_lebel_m16 = EnumValue(240, "8mm Lebel M16")
    default = other

    def get_marshaled_size(self):
        return 8
