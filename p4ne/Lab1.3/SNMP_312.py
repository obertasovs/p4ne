from easysnmp import Session

def fetch_snmp_data(host, community, oid):
    # Create an SNMP session
    session = Session(hostname=host, community=community, version=2)  # SNMPv2c

    # Fetch the SNMP data
    try:
        response = session.get(oid)
        print(f"{response.oid} = {response.value}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    host = "10.31.70.209"  # Replace with your SNMP host IP
    community = "public"  # Replace with your SNMP community string
    oid = "1.3.6.1.2.1.1.1.0"  # Example OID for system description (sysDescr)

    fetch_snmp_data(host, community, oid)