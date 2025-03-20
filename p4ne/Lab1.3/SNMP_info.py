from pysnmp.hlapi import *


def snmp_get(oid, host, community='public', port=161):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),
               UdpTransportTarget((host, port)),
               ContextData(),
               ObjectType(ObjectIdentity(oid))))
"""
    if errorIndication:
        print(f"Error: {errorIndication}")
    elif errorStatus:
        print(f"Error: {errorStatus} at {errorIndex and varBinds[int(errorIndex) - 1][0] or '?'}")
    else:
        for varBind in varBinds:
           print(f"{varBind[0]} = {varBind[1]}")
"""
    # Example usage
if name == "main":
# Replace with your SNMP OID and server details
    oid = '1.3.6.1.2.1.1.1.0'  # Example OID for system description
    host = '10.31.70.209'  # Replace with your server's IP address
    community = 'public'  # Replace with your SNMP community string

    snmp_get(oid, host, community)