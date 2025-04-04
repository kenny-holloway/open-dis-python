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
  *  UID 454, marshal size 32,
  * SpacePlatformCapabilities
  */

"""

class SpacePlatformCapabilitiesBitField(ctypes.Structure):
    _fields_ = [
        # (bit position 0, boolean) Describes whether the entity is able to supply some type of ammunition in response to an appropriate service request,  use {@link UInt8} values for this field
        ("_ammunitionSupply", UByte, 1),

        # (bit position 1, boolean) Describes whether the entity is able to supply some type of fuel in response to an appropriate service request,  use {@link UInt8} values for this field
        ("_fuelSupply", UByte, 1),

        # (bit position 2, boolean) Describes whether the entity is able to provide recovery (e.g., towing) services in response to an appropriate service request,  use {@link UInt8} values for this field
        ("_recovery", UByte, 1),

        # (bit position 3, boolean) Describes whether the entity is able to supply certain repair services in response to an appropriate service request,  use {@link UInt8} values for this field
        ("_repair", UByte, 1),

        # (bit position 4, boolean) This entry is reserved for backward compatibility and may not be reused,  use {@link UInt8} values for this field
        ("_reserved", UByte, 1)
    ]

class SpacePlatformCapabilities(ctypes.Union):
    _fields_ = [
        ("capabilities", SpacePlatformCapabilitiesBitField),
        ("asbyte", UInt8)
    ]

    def set_ammunitionSupply(self, value : UInt8):
        self.capabilities._ammunitionSupply = int(value)
    def get_ammunitionSupply(self) -> UInt8:
        return self.capabilities._ammunitionSupply
    AmmunitionSupply = property(get_ammunitionSupply, set_ammunitionSupply)

    def set_fuelSupply(self, value : UInt8):
        self.capabilities._fuelSupply = int(value)
    def get_fuelSupply(self) -> UInt8:
        return self.capabilities._fuelSupply
    FuelSupply = property(get_fuelSupply, set_fuelSupply)

    def set_recovery(self, value : UInt8):
        self.capabilities._recovery = int(value)
    def get_recovery(self) -> UInt8:
        return self.capabilities._recovery
    Recovery = property(get_recovery, set_recovery)

    def set_repair(self, value : UInt8):
        self.capabilities._repair = int(value)
    def get_repair(self) -> UInt8:
        return self.capabilities._repair
    Repair = property(get_repair, set_repair)

    def set_reserved(self, value : UInt8):
        self.capabilities._reserved = int(value)
    def get_reserved(self) -> UInt8:
        return self.capabilities._reserved
    Reserved = property(get_reserved, set_reserved)


    def to_string(self):
        outputStream = ""
        outputStream += format(self.asbyte, '#032b') + "\n"
        outputStream += "AmmunitionSupply : " +  str(self.AmmunitionSupply) + "\n"
        outputStream += "FuelSupply : " +  str(self.FuelSupply) + "\n"
        outputStream += "Recovery : " +  str(self.Recovery) + "\n"
        outputStream += "Repair : " +  str(self.Repair) + "\n"
        outputStream += "Reserved : " +  str(self.Reserved) + "\n"
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
