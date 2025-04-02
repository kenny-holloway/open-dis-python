"""
/**
 * Copyright (c) 2008-2022, MOVES Institute, Naval Postgraduate School (NPS). All rights reserved.
 * This work is provided under a BSD-style open-source license, see project
 * <a href="https://savage.nps.edu/opendis7-java/license.html" target="_blank">license.html</a> and <a href="https://savage.nps.edu/opendis7-java/license.txt" target="_blank">license.txt</a>
 */
// header autogenerated using string template dis7javalicense.txt

"""
"""
/**
 * autogenerated using string template jammertechnique.txt
 * package edu.nps.moves.dis7.jammers.Deception.Repeater.MultipleFrequencyRepeaterMFR;
 *
 * SISO-REF-010-v34 (2024-10-15)
 *
 * Jamming technique uid: 284
 */
"""

from JammingTechnique import JammingTechnique

class MultipleFrequencyRepeaterMFR(JammingTechnique):
    def __init__(self):
        self.kind = 2 // Deception
        self.category = 130 // Repeater
        self.subCategory = 15 // Multiple Frequency Repeater (MFR)
