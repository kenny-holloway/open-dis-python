'''
/*
 * Copyright (c) 2008-2022, MOVES Institute, Naval Postgraduate School (NPS). All rights reserved.
 * This work is provided under a BSD-style open-source license, see project
 * <a href="https://savage.nps.edu/opendis7-java/license.html" target="_blank">license.html</a> and <a href="https://savage.nps.edu/opendis7-java/license.txt" target="_blank">license.txt</a>
 */
 // header autogenerated using string template dis7javalicense.txt
'''

from .minefield_fusing_fuse_type import MinefieldFusingFuseType
from .minefield_fusing_fuse_type import MinefieldFusingFuseType

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
  *  UID 192, marshal size 16,
  * MinefieldDataFusing
  */

"""

class MinefieldDataFusingBitField(ctypes.Structure):
    _fields_ = [
        # (bit position 0, length=7) Identifies the type of the primary fuse,  use {@link MinefieldFusingFuseType} values for this field
        ("_primary", UByte, 7),

        # (bit position 7, length=7) Identifies the type of the secondary fuse,  use {@link MinefieldFusingFuseType} values for this field
        ("_secondary", UByte, 7),

        # (bit position 14, boolean) Describes whether the mine has an Anti-Handling device,  use {@link UInt8} values for this field
        ("_hasAntiHandlingDevice", UByte, 1)
    ]

class MinefieldDataFusing(ctypes.Union):
    _fields_ = [
        ("capabilities", MinefieldDataFusingBitField),
        ("asbyte", UInt8)
    ]

    def set_primary(self, value : MinefieldFusingFuseType):
        self.capabilities._primary = int(value)
    def get_primary(self) -> MinefieldFusingFuseType:
        return MinefieldFusingFuseType.get_enum(self._primary)
    Primary = property(get_primary, set_primary)

    def set_secondary(self, value : MinefieldFusingFuseType):
        self.capabilities._secondary = int(value)
    def get_secondary(self) -> MinefieldFusingFuseType:
        return MinefieldFusingFuseType.get_enum(self._secondary)
    Secondary = property(get_secondary, set_secondary)

    def set_hasAntiHandlingDevice(self, value : UInt8):
        self.capabilities._hasAntiHandlingDevice = int(value)
    def get_hasAntiHandlingDevice(self) -> UInt8:
        return self.capabilities._hasAntiHandlingDevice
    HasAntiHandlingDevice = property(get_hasAntiHandlingDevice, set_hasAntiHandlingDevice)


    def to_string(self):
        outputStream = ""
        outputStream += format(self.asbyte, '#032b') + "\n"
        outputStream += "Primary : " +  self.Primary.get_description + "\n"
        outputStream += "Secondary : " +  self.Secondary.get_description + "\n"
        outputStream += "HasAntiHandlingDevice : " +  str(self.HasAntiHandlingDevice) + "\n"
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
