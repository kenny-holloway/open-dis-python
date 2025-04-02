"""
/**
 * Copyright (c) 2008-2022, MOVES Institute, Naval Postgraduate School (NPS). All rights reserved.
 * This work is provided under a BSD-style open-source license, see project
 * <a href="https://savage.nps.edu/opendis7-java/license.html" target="_blank">license.html</a> and <a href="https://savage.nps.edu/opendis7-java/license.txt" target="_blank">license.txt</a>
 */
// header autogenerated using string template dis7javalicense.txt

"""


from ObjectType import ObjectType
from PlatformDomain import PlatformDomain
from ObjectKind import ObjectKind

import ctypes
UInt8 = ctypes.c_uint8

"""
/**
 *  autogenerated using string template objecttype.txt
 * package edu.nps.moves.dis7.enumerations.PointObject.Culturalfeature.ContainerBasedBuilding;
 * SISO-REF-010-v34 (2024-10-15)
 *
 * ObjectType uid: 226
 */
"""

class ContainerBasedBuildingHouseDouble(ObjectType):
   def __init__(self):
        domain = PlatformDomain(1)  # PointObject
        objectKind = ObjectKind(3)  # Cultural feature
        category = UInt8(8)  # Container-Based Building
        subCategory = UInt8(4)  # Container-Based Building, House, Double
