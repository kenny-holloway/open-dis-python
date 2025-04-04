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
  *  UID 68, marshal size 8,
  * StopFreezeFrozenBehavior
  */

"""

class StopFreezeFrozenBehaviorBitField(ctypes.Structure):
    _fields_ = [
        # (bit position 0, boolean) Describes whether a simulation application should run the internal simulation clock or not,  use {@link UInt8} values for this field
        ("_runSimulationClock", UByte, 1),

        # (bit position 1, boolean) Describes whether a simulation application should transmit updates and interactions or not,  use {@link UInt8} values for this field
        ("_transmitUpdates", UByte, 1),

        # (bit position 2, boolean) Describes whether a simulation application should update simulation models of other entities via received updates or interactions,  use {@link UInt8} values for this field
        ("_processUpdates", UByte, 1)
    ]

class StopFreezeFrozenBehavior(ctypes.Union):
    _fields_ = [
        ("capabilities", StopFreezeFrozenBehaviorBitField),
        ("asbyte", UInt8)
    ]

    def set_runSimulationClock(self, value : UInt8):
        self.capabilities._runSimulationClock = int(value)
    def get_runSimulationClock(self) -> UInt8:
        return self.capabilities._runSimulationClock
    RunSimulationClock = property(get_runSimulationClock, set_runSimulationClock)

    def set_transmitUpdates(self, value : UInt8):
        self.capabilities._transmitUpdates = int(value)
    def get_transmitUpdates(self) -> UInt8:
        return self.capabilities._transmitUpdates
    TransmitUpdates = property(get_transmitUpdates, set_transmitUpdates)

    def set_processUpdates(self, value : UInt8):
        self.capabilities._processUpdates = int(value)
    def get_processUpdates(self) -> UInt8:
        return self.capabilities._processUpdates
    ProcessUpdates = property(get_processUpdates, set_processUpdates)


    def to_string(self):
        outputStream = ""
        outputStream += format(self.asbyte, '#032b') + "\n"
        outputStream += "RunSimulationClock : " +  str(self.RunSimulationClock) + "\n"
        outputStream += "TransmitUpdates : " +  str(self.TransmitUpdates) + "\n"
        outputStream += "ProcessUpdates : " +  str(self.ProcessUpdates) + "\n"
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
        return 8 
