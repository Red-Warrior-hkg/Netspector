# ==================== port_utils.py ==================== #

import subprocess
import platform

# ==================== SERVICE MAP ==================== #

SERVICE_MAP = {
    20: "FTP Data Transfer",
    21: "FTP Control",
    22: "SSH Remote Login Protocol",
    23: "Telnet",
    25: "SMTP Email Routing",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    69: "TFTP",
    80: "HTTP Web Traffic",
    110: "POP3 Email",
    119: "NNTP Usenet",
    123: "NTP Time Synchronization",
    135: "Microsoft RPC",
    137: "NetBIOS Name Service",
    138: "NetBIOS Datagram Service",
    139: "NetBIOS Session Service",
    143: "IMAP Email",
    161: "SNMP",
    162: "SNMP Trap",
    179: "BGP",
    389: "LDAP",
    443: "HTTPS Secure Web Traffic",
    445: "Microsoft-DS SMB File Sharing",
    465: "SMTPS",
    514: "Syslog",
    587: "SMTP (Submission)",
    636: "LDAPS",
    993: "IMAPS",
    995: "POP3S",
    1433: "Microsoft SQL Server",
    1521: "Oracle Database",
    1723: "PPTP VPN",
    3306: "MySQL Database",
    3389: "RDP Remote Desktop",
    5432: "PostgreSQL Database",
    5900: "VNC Remote Desktop",
    6379: "Redis",
    8080: "HTTP Alternate",
    8443: "HTTPS Alternate"
}


# ==================== PORT VALIDATION ==================== #

def is_valid_port(port: int) -> bool:
    if not isinstance(port, int):
        return False
    return 0 <= port <= 65535


# ==================== PRIVILEGED PORT ==================== #

def is_privileged_port(port: int) -> bool:
    if not is_valid_port(port):
        return False
    return 0 <= port <= 1023


# ==================== LOCAL LISTENING PORTS ==================== #

def list_listening_ports_local() -> list[int]:
    ports = []
    os_name = platform.system()

    try:
        if os_name == "Windows":
            result = subprocess.run(
                ["netstat", "-an"],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="ignore"
            )
            lines = result.stdout.splitlines()

            for line in lines:
                if "127.0.0.1" in line and "LISTEN" in line:
                    try:
                        port = int(line.split(":")[1].split()[0])
                        ports.append(port)
                    except:
                        continue

        elif os_name == "Linux":
            result = subprocess.run(
                ["ss", "-lnt"],
                capture_output=True,
                text=True
            )
            lines = result.stdout.splitlines()

            for line in lines:
                if "127.0.0.1" in line:
                    try:
                        port = int(line.split(":")[1].split()[0])
                        ports.append(port)
                    except:
                        continue

        elif os_name == "Darwin":  # macOS
            result = subprocess.run(
                ["lsof", "-iTCP", "-sTCP:LISTEN"],
                capture_output=True,
                text=True
            )
            lines = result.stdout.splitlines()

            for line in lines:
                if "127.0.0.1" in line:
                    try:
                        port = int(line.split(":")[1].split()[0])
                        ports.append(port)
                    except:
                        continue

    except Exception:
        # fail-safe (no crash)
        return []

    return list(set(ports))  # remove duplicates


# ==================== HELPER ==================== #
def get_service_name(port: int) -> str:
    return SERVICE_MAP.get(port, "Unknown")
