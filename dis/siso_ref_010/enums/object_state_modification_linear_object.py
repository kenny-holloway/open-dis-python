'''
/*
 * Copyright (c) 2008-2022, MOVES Institute, Naval Postgraduate School (NPS). All rights reserved.
 * This work is provided under a BSD-style open-source license, see project
 * <a href="https://savage.nps.edu/opendis7-java/license.html" target="_blank">license.html</a> and <a href="https://savage.nps.edu/opendis7-java/license.txt" target="_blank">license.txt</a>
 */
 // header autogenerated using string template dis7javalicense.txt
'''


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
  *  UID 241, marshal size 16,
  * ObjectStateModificationLinearObject
  */

"""

class ObjectStateModificationLinearObjectBitField(ctypes.Structure):
    _fields_ = [
        # (bit position 0, boolean) Describes whether the location of the linear segment has been modified since the last update number,  use {@link UInt8} values for this field
        ("_isLocationModified", UByte, 1),

        # (bit position 1, boolean) Describes whether the orientation of the linear segment has been modified since the last update number,  use {@link UInt8} values for this field
        ("_isOrientationModified", UByte, 1)
    ]

class ObjectStateModificationLinearObject(ctypes.Union):
    _fields_ = [
        ("capabilities", ObjectStateModificationLinearObjectBitField),
        ("asbyte", UInt8)
    ]

    def set_isLocationModified(self, value : UInt8):
        self.capabilities._isLocationModified = int(value)
    def get_isLocationModified(self) -> UInt8:
        return self.capabilities._isLocationModified
    IsLocationModified = property(get_isLocationModified, set_isLocationModified)

    def set_isOrientationModified(self, value : UInt8):
        self.capabilities._isOrientationModified = int(value)
    def get_isOrientationModified(self) -> UInt8:
        return self.capabilities._isOrientationModified
    IsOrientationModified = property(get_isOrientationModified, set_isOrientationModified)


    def to_string(self):
        outputStream = ""
        outputStream += format(self.asbyte, '#032b') + "\n"
        outputStream += "IsLocationModified : " +  str(self.IsLocationModified) + "\n"
        outputStream += "IsOrientationModified : " +  str(self.IsOrientationModified) + "\n"
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
