import ipaddress
from ipaddress import ip_address, IPv4Network

#  Validate IP + detect version
def validate_ip(ip: str) -> bool:
    try:
        ip_object = ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def get_ip_version(ip: str) -> str:
    try:
        ip_object = ipaddress.ip_address(ip)
        if ip_object.version == 4:
            return "the ip you entered is 'IPv4'!"
        else:
            return "the ip you entered is 'IPv6'!"
    except ValueError:
        return "that nor IPv4 nor IPv6!"


# Check if private network 
def is_private_ip(ip: str) -> str:
    try:
        parts = ip.split('.')
        if len(parts) == 4 and all(int(number) < 256 and int(number) in range(256) for number in parts):
            first_octet = int(parts[0])
            second_octet = int(parts[1])

            if (
                first_octet == 10 or
                (first_octet == 172 and 16 <= second_octet <= 31) or
                (first_octet == 192 and second_octet == 168)
            ):
                return 'the IP belongs to a private network'
            else:
                return 'the IP belongs to a public network'
        else:
            return "invalid ip"
    except:
        return "invalid ip"


#  List all IPs in subnet
def list_subnet_hosts(subnet: str):
    try:
        IPs = ipaddress.ip_network(subnet, strict=False)
        return [str(ip) for ip in IPs.hosts()]
    except:
        return []


#  Same subnet check 
def same_subnet(ip1: str, ip2: str, cidr: int) -> str:
    try:
        net1 = IPv4Network(f"{ip1}/{cidr}", strict=False)
        net2 = IPv4Network(f"{ip2}/{cidr}", strict=False)

        if net1.network_address == net2.network_address:
            return "Same subnet"
        else:
            return "Different subnet"
    except:
        return "Invalid input"