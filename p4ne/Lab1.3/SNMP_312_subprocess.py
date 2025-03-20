import subprocess


def fetch_snmp_data(host, community, oid):
    # Build the snmpget command
    command = [
        "snmpget",  # SNMP command
        "-v2c",  # SNMP version (2c)
        "-c", community,  # Community string
        host,  # SNMP host
        oid,  # OID to query
    ]

    try:
        # Run the command and capture the output
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

# Example usage
if __name__ == "__main__":
    host = "10.31.70.209"  # Replace with your SNMP host IP
    community = "public"  # Replace with your SNMP community string
    oid = "1.3.6.1.2.1.1.1.0"  # Example OID for system description (sysDescr)

    fetch_snmp_data(host, community, oid)