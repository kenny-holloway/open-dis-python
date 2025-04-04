'''
/*
 * Copyright (c) 2008-2022, MOVES Institute, Naval Postgraduate School (NPS). All rights reserved.
 * This work is provided under a BSD-style open-source license, see project
 * <a href="https://savage.nps.edu/opendis7-java/license.html" target="_blank">license.html</a> and <a href="https://savage.nps.edu/opendis7-java/license.txt" target="_blank">license.txt</a>
 */
 // header autogenerated using string template dis7javalicense.txt
'''


from enum import Enum, EnumMeta
from pprint import pprint, pformat
from collections import OrderedDict, namedtuple
import ctypes

UInt8 = ctypes.c_uint8
UInt16 = ctypes.c_uint16
UInt32 = ctypes.c_uint32

EnumValue = namedtuple('EnumValue', ['value', 'description'])

# autogenerated using string template disenumpart1.txt
#  package edu.nps.moves.dis7.enumerations;

'''
/**
  * This <code>enum</code> type is generated from XML,
  * SisoDate : 
  * UID 694,
  * marshal size 8;
  * CyberReconType has 75 enumerations total.
  */
'''

class EnumMeta(EnumMeta):
    def __getitem__(cls, name):
        try:
            return super().__getitem__(name)
        except KeyError as error:
            return cls.UNKNOWN
    
    def __getattr__(cls, name):
        try:
            return super().__getattr__(name)
        except AttributeError as error:
            return cls.UNKNOWN

class ExtensibleEnum(Enum):
    @classmethod
    def add_custom_value(cls, value: int, name: str, desc:str):
        existingItem = [item for item in cls._value2member_map_ if item.value == value]

        enumValue = EnumValue(value, desc)
        obj = object.__new__(cls)
        
        obj._value_ = enumValue
        obj._name_ = name      
        obj._desc = desc
        obj.__objclass__ = cls
        
        if not existingItem:
            cls._member_map_[name] = obj
            cls._value2member_map_[enumValue] = enumValue
            cls._member_names_.append(name)
        else:
            enumIndex = list(OrderedDict(cls.__members__).keys())[value]
            cls._member_map_[enumIndex] = obj

    @property
    def get_description(self):
        return self.value.description

    @classmethod
    def to_string(cls) -> str:
        return pformat(OrderedDict(cls.__members__))

    @classmethod
    def is_valid(cls, kind: Enum) -> bool:
        if kind is cls.UNKNOWN:
            return False
        return kind in iter(cls)

    @staticmethod
    def describe(self):
        return self.name, self.value

    @classmethod
    def value_list(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def _missing_(cls, value):
        return cls.default

    @classmethod
    def get_enum_key(cls, value:int) -> str:
        for unique_key, unique_value in OrderedDict(cls.__members__).items():
            if value == unique_value.value.value:
                return unique_key
        return 'UNKNOWN'

    @classmethod
    def get_enum(cls, value:int) -> Enum:
        key = cls.get_enum_key(value)
        return getattr(cls, key)

    def __int__(self):
        return self.value.value
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
                elif (isinstance(value, Enum)):
                    diffs.add((key, value))
                    diffs.add((key, value2))
                elif (isinstance(value, object)):
                    diffs.update(value.diff(value2))
                else:
                    diffs.add((key, value))
                    diffs.add((key, value2))
        return(diffs)

class CyberReconType(ExtensibleEnum, metaclass=EnumMeta):
    UNKNOWN = EnumValue(-1, "UNKNOWN Enum")
    account_discovery = EnumValue(1, "Account Discovery")
    ad_malware = EnumValue(2, "Ad Malware")
    antivirus_trojan = EnumValue(3, "Antivirus Trojan")
    application_window_discovery = EnumValue(4, "Application Window Discovery")
    arp_scan = EnumValue(5, "ARP Scan")
    banner_grabbing = EnumValue(6, "Banner Grabbing")
    bounce_scan = EnumValue(7, "Bounce Scan")
    browser_bookmark_discovery = EnumValue(8, "Browser Bookmark Discovery")
    cloud_infrastructure_discovery = EnumValue(9, "Cloud Infrastructure Discovery")
    cloud_service_dashboard = EnumValue(10, "Cloud Service Dashboard")
    cloud_service_discovery = EnumValue(11, "Cloud Service Discovery")
    compliance = EnumValue(12, "Compliance")
    csrf = EnumValue(13, "CSRF")
    database_injection = EnumValue(14, "Database Injection")
    database_structure = EnumValue(15, "Database Structure")
    db_manufacture_version = EnumValue(16, "DB Manufacture Version")
    device = EnumValue(17, "Device")
    dns = EnumValue(18, "DNS")
    domain = EnumValue(19, "Domain")
    domain_trust_discovery = EnumValue(20, "Domain Trust Discovery")
    file_and_directory_discovery = EnumValue(21, "File And Directory Discovery")
    fin_scan = EnumValue(22, "FIN Scan")
    ftp = EnumValue(23, "FTP")
    http = EnumValue(24, "HTTP")
    idle_scan = EnumValue(25, "Idle Scan")
    igmp = EnumValue(26, "IGMP")
    input_validation = EnumValue(27, "Input Validation")
    ip = EnumValue(28, "IP")
    ldap_scan = EnumValue(29, "LDAP Scan")
    net_bios_scan = EnumValue(30, "Net Bios Scan")
    network_map = EnumValue(31, "Network Map")
    network_service_scanning = EnumValue(32, "Network Service Scanning")
    network_share_discovery = EnumValue(33, "Network Share Discovery")
    network_sniffing = EnumValue(34, "Network Sniffing")
    ntp = EnumValue(35, "NTP")
    null_scan = EnumValue(36, "NULL Scan")
    os_scan = EnumValue(37, "OS Scan")
    password_policy_discovery = EnumValue(38, "Password Policy Discovery")
    patch_history = EnumValue(39, "Patch History")
    peripheral_device_discovery = EnumValue(40, "Peripheral Device Discovery")
    permission_groups_discovery = EnumValue(41, "Permission Groups Discovery")
    ping = EnumValue(42, "Ping")
    ping_scan = EnumValue(43, "Ping Scan")
    port_scan = EnumValue(44, "Port Scan")
    port_sweep = EnumValue(45, "Port Sweep")
    ppp = EnumValue(46, "PPP")
    process_discovery = EnumValue(47, "Process Discovery")
    query_registry = EnumValue(48, "Query Registry")
    rarp = EnumValue(49, "RARP")
    remote_system_discovery = EnumValue(50, "Remote System Discovery")
    rootkit = EnumValue(51, "Rootkit")
    rpc_scan = EnumValue(52, "RPC Scan")
    service = EnumValue(53, "Service")
    slip = EnumValue(54, "SLIP")
    smtp = EnumValue(55, "SMTP")
    snmp_sweep = EnumValue(56, "SNMP Sweep")
    software_discover = EnumValue(57, "Software Discover")
    syn_scan = EnumValue(58, "SYN Scan")
    system_information_discovery = EnumValue(59, "System Information Discovery")
    system_network_configuration_discovery = EnumValue(60, "System Network Configuration Discovery")
    system_network_connections_discovery = EnumValue(61, "System Network Connections Discovery")
    system_owner_user_discovery = EnumValue(62, "System Owner User Discovery")
    system_service_discovery = EnumValue(63, "System Service Discovery")
    system_time_discovery = EnumValue(64, "System Time Discovery")
    tcp_connect = EnumValue(65, "TCP Connect")
    trace_route = EnumValue(66, "Trace Route")
    unix_linux = EnumValue(67, "UNIX - Linux")
    virtualization_sandbox_evasion = EnumValue(68, "Virtualization Sandbox Evasion")
    vulnerability = EnumValue(69, "Vulnerability")
    web_crawler = EnumValue(70, "Web Crawler")
    windows = EnumValue(71, "Windows")
    wireless_active = EnumValue(72, "Wireless Active")
    wireless_passive = EnumValue(73, "Wireless Passive")
    xmas_scan = EnumValue(74, "XMAS Scan")
    xss = EnumValue(75, "XSS")
    default = account_discovery

    def get_marshaled_size(self):
        return 8
