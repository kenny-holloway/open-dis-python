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
  *  UID 462, marshal size 32,
  * SensorEmitterCapabilities
  */

"""

class SensorEmitterCapabilitiesBitField(ctypes.Structure):
    _fields_ = [
        # (bit position 0, length=5) This entry is reserved for backward compatibility and may not be reused,  use {@link UInt8} values for this field
        ("_reserved", UByte, 5),

        # (bit position 6, boolean) The Entity is able to be carried as a sling load payload. The extended appearance record (if available) will identify if it is currently sling loaded and entity association and/or entity offset records (if available) will provide additional sling load details (such as carrier).,  use {@link UInt8} values for this field
        ("_slingLoadable", UByte, 1),

        # (bit position 7, boolean) The Entity is an IED or contains an IED. The extended appearance record (if available) will identify how well hidden the IED is on the Entity. An Attached Part (if applicable, for instance a jury-rigged munition does not apply here) will identify the IED explicitly.,  use {@link UInt8} values for this field
        ("_iEDPresenceIndicator", UByte, 1),

        # (bit position 8, boolean) The Entity (normally a virtual manned module) can be task organized into an existing mixed mode unit (where mixed mode is intended to comprise a combination of computer-generated forces and virtual or even live forces).,  use {@link UInt8} values for this field
        ("_taskOrganizable", UByte, 1)
    ]

class SensorEmitterCapabilities(ctypes.Union):
    _fields_ = [
        ("capabilities", SensorEmitterCapabilitiesBitField),
        ("asbyte", UInt8)
    ]

    def set_reserved(self, value : UInt8):
        self.capabilities._reserved = int(value)
    def get_reserved(self) -> UInt8:
        return self.capabilities._reserved
    Reserved = property(get_reserved, set_reserved)

    def set_slingLoadable(self, value : UInt8):
        self.capabilities._slingLoadable = int(value)
    def get_slingLoadable(self) -> UInt8:
        return self.capabilities._slingLoadable
    SlingLoadable = property(get_slingLoadable, set_slingLoadable)

    def set_iEDPresenceIndicator(self, value : UInt8):
        self.capabilities._iEDPresenceIndicator = int(value)
    def get_iEDPresenceIndicator(self) -> UInt8:
        return self.capabilities._iEDPresenceIndicator
    IEDPresenceIndicator = property(get_iEDPresenceIndicator, set_iEDPresenceIndicator)

    def set_taskOrganizable(self, value : UInt8):
        self.capabilities._taskOrganizable = int(value)
    def get_taskOrganizable(self) -> UInt8:
        return self.capabilities._taskOrganizable
    TaskOrganizable = property(get_taskOrganizable, set_taskOrganizable)


    def to_string(self):
        outputStream = ""
        outputStream += format(self.asbyte, '#032b') + "\n"
        outputStream += "Reserved : " +  str(self.Reserved) + "\n"
        outputStream += "SlingLoadable : " +  str(self.SlingLoadable) + "\n"
        outputStream += "IEDPresenceIndicator : " +  str(self.IEDPresenceIndicator) + "\n"
        outputStream += "TaskOrganizable : " +  str(self.TaskOrganizable) + "\n"
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
