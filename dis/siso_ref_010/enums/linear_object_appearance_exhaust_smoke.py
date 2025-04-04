'''
/*
 * Copyright (c) 2008-2022, MOVES Institute, Naval Postgraduate School (NPS). All rights reserved.
 * This work is provided under a BSD-style open-source license, see project
 * <a href="https://savage.nps.edu/opendis7-java/license.html" target="_blank">license.html</a> and <a href="https://savage.nps.edu/opendis7-java/license.txt" target="_blank">license.txt</a>
 */
 // header autogenerated using string template dis7javalicense.txt
'''

from .appearance_object_specific_chemical_type import AppearanceObjectSpecificChemicalType

import ctypes

UInt8 = ctypes.c_uint8
UInt16 = ctypes.c_uint16
UInt32 = ctypes.c_uint32

UByte = ctypes.c_ubyte
UInt  = ctypes.c_uint

# autogenerated using string template disbitset1.txt
# package edu.nps.moves.dis7.enumerations;

"""
/**
  * Generated from XML,
  *  UID 236, marshal size 16,
  * LinearObjectAppearanceExhaustsmoke
  */

"""

class LinearObjectAppearanceExhaustSmokeBitField(ctypes.Structure):
    _fields_ = [
        # (bit position 0, length=8) 8-bit unsigned integer indicating the percent opacity of the smoke (0..100),  use {@link UInt8} values for this field
        ("_opacityPercent", UByte, 8),

        # (bit position 8, boolean) Describes whether or not the smoke is attached to the vehicle,  use {@link UInt8} values for this field
        ("_smokeIsAttached", UByte, 1),

        # (bit position 9, length=2) Describes the chemical content of the smoke,  use {@link AppearanceObjectSpecificChemicalType} values for this field
        ("_chemicalType", UByte, 2)
    ]

class LinearObjectAppearanceExhaustSmoke(ctypes.Union):
    _fields_ = [
        ("capabilities", LinearObjectAppearanceExhaustSmokeBitField),
        ("asbyte", UInt8)
    ]

    def set_opacityPercent(self, value : UInt8):
        self.capabilities._opacityPercent = int(value)
    def get_opacityPercent(self) -> UInt8:
        return self.capabilities._opacityPercent
    OpacityPercent = property(get_opacityPercent, set_opacityPercent)

    def set_smokeIsAttached(self, value : UInt8):
        self.capabilities._smokeIsAttached = int(value)
    def get_smokeIsAttached(self) -> UInt8:
        return self.capabilities._smokeIsAttached
    SmokeIsAttached = property(get_smokeIsAttached, set_smokeIsAttached)

    def set_chemicalType(self, value : AppearanceObjectSpecificChemicalType):
        self.capabilities._chemicalType = int(value)
    def get_chemicalType(self) -> AppearanceObjectSpecificChemicalType:
        return AppearanceObjectSpecificChemicalType.get_enum(self._chemicalType)
    ChemicalType = property(get_chemicalType, set_chemicalType)


    def to_string(self):
        outputStream = ""
        outputStream += format(self.asbyte, '#032b') + "\n"
        outputStream += "OpacityPercent : " +  str(self.OpacityPercent) + "\n"
        outputStream += "SmokeIsAttached : " +  str(self.SmokeIsAttached) + "\n"
        outputStream += "ChemicalType : " +  self.ChemicalType.get_description + "\n"
        return outputStream

    def __str__(self):
        return self.to_string()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

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
                elif (isinstance(value, object)):
                    diffs.update(value.diff(value2))
                else:
                    diffs.add((key, value))
                    diffs.add((key, value2))
        return(diffs)

    def get_marshaled_size(self):
        return 16 
