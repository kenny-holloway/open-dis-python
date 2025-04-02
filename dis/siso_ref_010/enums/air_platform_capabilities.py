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
  *  UID 451, marshal size 32,
  * AirPlatformCapabilities
  */

"""

class AirPlatformCapabilitiesBitField(ctypes.Structure):
    _fields_ = [
        # (bit position 0, boolean) Describes whether the entity is able to supply some type of ammunition in response to an appropriate service request,  use {@link UInt8} values for this field
        ("_ammunitionSupply", UByte, 1),

        # (bit position 1, boolean) Describes whether the entity is able to supply some type of fuel in response to an appropriate service request,  use {@link UInt8} values for this field
        ("_fuelSupply", UByte, 1),

        # (bit position 2, boolean) Describes whether the entity is able to provide recovery (e.g., towing) services in response to an appropriate service request,  use {@link UInt8} values for this field
        ("_recovery", UByte, 1),

        # (bit position 3, boolean) Describes whether the entity is able to supply certain repair services in response to an appropriate service request,  use {@link UInt8} values for this field
        ("_repair", UByte, 1),

        # (bit position 4, boolean) Describes whether the entity is equipped with Automatic Dependent Surveillance - Broadcast (ADS-B),  use {@link UInt8} values for this field
        ("_aDSB", UByte, 1),

        # (bit position 5, boolean) The Entity is able to carry a payload in a sling load. The extended appearance record (if available) will identify the current sling load status and entity association and/or entity offset records (if available) will provide additional sling load details (such as payload).,  use {@link UInt8} values for this field
        ("_slingLoadCarrier", UByte, 1),

        # (bit position 6, boolean) The Entity is able to be carried as a sling load payload. The extended appearance record (if available) will identify if it is currently sling loaded and entity association and/or entity offset records (if available) will provide additional sling load details (such as carrier).,  use {@link UInt8} values for this field
        ("_slingLoadable", UByte, 1),

        # (bit position 7, boolean) The Entity is an IED or contains an IED. The extended appearance record (if available) will identify how well hidden the IED is on the Entity. An Attached Part (if applicable, for instance a jury-rigged munition does not apply here) will identify the IED explicitly.,  use {@link UInt8} values for this field
        ("_iEDPresenceIndicator", UByte, 1),

        # (bit position 8, boolean) The Entity (normally a virtual manned module) can be task organized into an existing mixed mode unit (where mixed mode is intended to comprise a combination of computer-generated forces and virtual or even live forces).,  use {@link UInt8} values for this field
        ("_taskOrganizable", UByte, 1),

        # (bit position 9, boolean) Describes whether the entity is equipped with Large Aircraft Infrared Countermeasures (LAIRCM),  use {@link UInt8} values for this field
        ("_lAIRCM", UByte, 1)
    ]

class AirPlatformCapabilities(ctypes.Union):
    _fields_ = [
        ("capabilities", AirPlatformCapabilitiesBitField),
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

    def set_aDSB(self, value : UInt8):
        self.capabilities._aDSB = int(value)
    def get_aDSB(self) -> UInt8:
        return self.capabilities._aDSB
    ADSB = property(get_aDSB, set_aDSB)

    def set_slingLoadCarrier(self, value : UInt8):
        self.capabilities._slingLoadCarrier = int(value)
    def get_slingLoadCarrier(self) -> UInt8:
        return self.capabilities._slingLoadCarrier
    SlingLoadCarrier = property(get_slingLoadCarrier, set_slingLoadCarrier)

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

    def set_lAIRCM(self, value : UInt8):
        self.capabilities._lAIRCM = int(value)
    def get_lAIRCM(self) -> UInt8:
        return self.capabilities._lAIRCM
    LAIRCM = property(get_lAIRCM, set_lAIRCM)


    def to_string(self):
        outputStream = ""
        outputStream += format(self.asbyte, '#032b') + "\n"
        outputStream += "AmmunitionSupply : " +  str(self.AmmunitionSupply) + "\n"
        outputStream += "FuelSupply : " +  str(self.FuelSupply) + "\n"
        outputStream += "Recovery : " +  str(self.Recovery) + "\n"
        outputStream += "Repair : " +  str(self.Repair) + "\n"
        outputStream += "ADSB : " +  str(self.ADSB) + "\n"
        outputStream += "SlingLoadCarrier : " +  str(self.SlingLoadCarrier) + "\n"
        outputStream += "SlingLoadable : " +  str(self.SlingLoadable) + "\n"
        outputStream += "IEDPresenceIndicator : " +  str(self.IEDPresenceIndicator) + "\n"
        outputStream += "TaskOrganizable : " +  str(self.TaskOrganizable) + "\n"
        outputStream += "LAIRCM : " +  str(self.LAIRCM) + "\n"
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
