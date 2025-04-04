'''
/*
 * Copyright (c) 2008-2022, MOVES Institute, Naval Postgraduate School (NPS). All rights reserved.
 * This work is provided under a BSD-style open-source license, see project
 * <a href="https://savage.nps.edu/opendis7-java/license.html" target="_blank">license.html</a> and <a href="https://savage.nps.edu/opendis7-java/license.txt" target="_blank">license.txt</a>
 */
 // header autogenerated using string template dis7javalicense.txt
'''

from .appearance_linear_object_lane_marker_visible import AppearanceLinearObjectLaneMarkerVisible

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
  *  UID 237, marshal size 16,
  * LinearObjectAppearanceMinefieldLaneMarker
  */

"""

class LinearObjectAppearanceMinefieldLaneMarkerBitField(ctypes.Structure):
    _fields_ = [
        # (bit position 0, length=2) Describes the visible side of the lane marker,  use {@link AppearanceLinearObjectLaneMarkerVisible} values for this field
        ("_visibleSide", UByte, 2)
    ]

class LinearObjectAppearanceMinefieldLaneMarker(ctypes.Union):
    _fields_ = [
        ("capabilities", LinearObjectAppearanceMinefieldLaneMarkerBitField),
        ("asbyte", UInt8)
    ]

    def set_visibleSide(self, value : AppearanceLinearObjectLaneMarkerVisible):
        self.capabilities._visibleSide = int(value)
    def get_visibleSide(self) -> AppearanceLinearObjectLaneMarkerVisible:
        return AppearanceLinearObjectLaneMarkerVisible.get_enum(self._visibleSide)
    VisibleSide = property(get_visibleSide, set_visibleSide)


    def to_string(self):
        outputStream = ""
        outputStream += format(self.asbyte, '#032b') + "\n"
        outputStream += "VisibleSide : " +  self.VisibleSide.get_description + "\n"
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
