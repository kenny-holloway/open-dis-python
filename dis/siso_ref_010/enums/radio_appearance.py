'''
/*
 * Copyright (c) 2008-2022, MOVES Institute, Naval Postgraduate School (NPS). All rights reserved.
 * This work is provided under a BSD-style open-source license, see project
 * <a href="https://savage.nps.edu/opendis7-java/license.html" target="_blank">license.html</a> and <a href="https://savage.nps.edu/opendis7-java/license.txt" target="_blank">license.txt</a>
 */
 // header autogenerated using string template dis7javalicense.txt
'''

from .appearance_entityor_object_state import AppearanceEntityorObjectState

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
  *  UID 41, marshal size 32,
  * RadioAppearance
  */

"""

class RadioAppearanceBitField(ctypes.Structure):
    _fields_ = [
        # (bit position 21, boolean) Describes whether the entity is frozen and should not be dead reckoned,  use {@link UInt8} values for this field
        ("_isFrozen", UByte, 1),

        # (bit position 23, boolean) Describes whether the entity is active or deactivated,  use {@link AppearanceEntityorObjectState} values for this field
        ("_state", UByte, 1)
    ]

class RadioAppearance(ctypes.Union):
    _fields_ = [
        ("capabilities", RadioAppearanceBitField),
        ("asbyte", UInt8)
    ]

    def set_isFrozen(self, value : UInt8):
        self.capabilities._isFrozen = int(value)
    def get_isFrozen(self) -> UInt8:
        return self.capabilities._isFrozen
    IsFrozen = property(get_isFrozen, set_isFrozen)

    def set_state(self, value : AppearanceEntityorObjectState):
        self.capabilities._state = int(value)
    def get_state(self) -> AppearanceEntityorObjectState:
        return AppearanceEntityorObjectState.get_enum(self._state)
    State = property(get_state, set_state)


    def to_string(self):
        outputStream = ""
        outputStream += format(self.asbyte, '#032b') + "\n"
        outputStream += "IsFrozen : " +  str(self.IsFrozen) + "\n"
        outputStream += "State : " +  self.State.get_description + "\n"
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
        return 32 
