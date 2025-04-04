'''
/*
 * Copyright (c) 2008-2022, MOVES Institute, Naval Postgraduate School (NPS). All rights reserved.
 * This work is provided under a BSD-style open-source license, see project
 * <a href="https://savage.nps.edu/opendis7-java/license.html" target="_blank">license.html</a> and <a href="https://savage.nps.edu/opendis7-java/license.txt" target="_blank">license.txt</a>
 */
 // header autogenerated using string template dis7javalicense.txt
'''

from .color import Color
from .material import Material

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
  *  UID 489, marshal size 32,
  * LinearObjectAppearanceSpeedBump
  */

"""

class LinearObjectAppearanceSpeedBumpBitField(ctypes.Structure):
    _fields_ = [
        # (bit position 0, length=8) 8-bit enumeration indicating the color,  use {@link Color} values for this field
        ("_color", UByte, 8),

        # (bit position 16, length=4) 4-bit unsigned integer indicating 16 levels of contrast (low to high) distinguishing variation of object from surrounding surface,  use {@link UInt8} values for this field
        ("_contrast", UByte, 4),

        # (bit position 20, length=4) 4-bit enumeration indicating the type of material,  use {@link Material} values for this field
        ("_material", UByte, 4)
    ]

class LinearObjectAppearanceSpeedBump(ctypes.Union):
    _fields_ = [
        ("capabilities", LinearObjectAppearanceSpeedBumpBitField),
        ("asbyte", UInt8)
    ]

    def set_color(self, value : Color):
        self.capabilities._color = int(value)
    def get_color(self) -> Color:
        return Color.get_enum(self._color)
    Color = property(get_color, set_color)

    def set_contrast(self, value : UInt8):
        self.capabilities._contrast = int(value)
    def get_contrast(self) -> UInt8:
        return self.capabilities._contrast
    Contrast = property(get_contrast, set_contrast)

    def set_material(self, value : Material):
        self.capabilities._material = int(value)
    def get_material(self) -> Material:
        return Material.get_enum(self._material)
    Material = property(get_material, set_material)


    def to_string(self):
        outputStream = ""
        outputStream += format(self.asbyte, '#032b') + "\n"
        outputStream += "Color : " +  self.Color.get_description + "\n"
        outputStream += "Contrast : " +  str(self.Contrast) + "\n"
        outputStream += "Material : " +  self.Material.get_description + "\n"
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
