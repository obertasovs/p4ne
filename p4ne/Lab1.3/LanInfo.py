from pysnmp.hlapi import *
#from pysnmp.hlapi import getCmd

#import re
#import importlib
#import importlib.util
#import sys

"""
result = getCmd(SnmpEngine(),
                CommunityData("public", mpModel=0),
                UdpTransportTarget(("10.31.70.209", 161)),
                ContextData(),
                ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
"""

for request in result:
    for var in request[3]:
        print(var)