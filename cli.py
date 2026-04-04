#!/usr/bin/env python3
import argparse
import sys
import socket
from scanner.utils.ip_utils import validate_ip, is_private_ip, list_subnet_hosts
from scanner.utils.port_utils import get_service_name, list_listening_ports_local
from scanner.core.port_scanner import scan_ports, scan_port, is_host_up, udp_scan, measure_rtt
# ==================== COLORS ==================== #
G  = "\033[92m"   # bright green
DG = "\033[32m"   # dark green
R  = "\033[0m"    # reset
DIM = "\033[2m"

# ==================== BANNER ==================== #
_ART = r"""
    )                                                 
 ( /(           )                         )           
 )\())   (   ( /(              (       ( /(      (    
((_)\   ))\  )\())(   `  )    ))\  (   )\()) (   )(   
 _((_) /((_)(_))/ )\  /(/(   /((_) )\ (_))/  )\ (()\  
| \| |(_))  | |_ ((_)((_)_\ (_))  ((_)| |_  ((_) ((_) 
| .` |/ -_) |  _|(_-<| '_ \)/ -_)/ _| |  _|/ _ \| '_| 
|_|\_|\___|  \__|/__/| .__/ \___|\__|  \__|\___/|_|   
                     |_|"""
def BANNER():
    print(G + _ART + R)

DESCRIPTION = (
    "  " + DG + "Netspector -- A lightweight, fast network scanner built from scratch in Python.\n"
    "  " + DG + "It provides essential network reconnaissance features with a clean CLI" + R + "\n"
    "  " + DIM + "usage: python main.py <command> [options]" + R + "\n"
)

# ==================== SIMPLE OUTPUT ==================== #
def ok(msg):   print(f"[+] {msg}")
def err(msg):  print(f"[!] {msg}")
def info(msg): print(f"[*] {msg}")

# ==================== HELPER: DOMAIN RESOLUTION ==================== #
def resolve_host(host):
    """Return IP string or None if invalid / resolution fails."""
    if validate_ip(host):
        return host
    try:
        ip = socket.gethostbyname(host)
        info(f"Resolved {host} → {ip}")
        return ip
    except socket.gaierror:
        return None

# ==================== EXISTING COMMANDS (with domain resolution added) ==================== #
def cmd_scan(args):
    ip = resolve_host(args.ip)
    if not ip:
        err(f"Cannot resolve {args.ip}")
        return
    info(f"Scanning {ip} ports {args.start}-{args.end}...")
    results = scan_ports(ip, args.start, args.end)
    if not results:
        print("[-] No open ports")
        return
    ok(f"{len(results)} open ports:")
    for port, _ in results:
        print(f"  {port}/tcp → {get_service_name(port)}")

def cmd_scan_port(args):
    ip = resolve_host(args.ip)
    if not ip:
        err(f"Cannot resolve {args.ip}")
        return
    info(f"Checking {ip}:{args.port}...")
    if scan_port(ip, args.port):
        ok("OPEN")
    else:
        print("[-] CLOSED")

def cmd_ping(args):
    ip = resolve_host(args.ip)
    if not ip:
        err(f"Cannot resolve {args.ip}")
        return
    print(is_host_up(ip))

def cmd_private(args):
    ip = resolve_host(args.ip)
    if not ip:
        err(f"Cannot resolve {args.ip}")
        return
    result = is_private_ip(ip)
    if "private" in result:
        ok(result)
    else:
        info(result)

def cmd_listening(args):
    ports = list_listening_ports_local()
    if not ports:
        print("[-] No listening ports")
        return
    ok(f"{len(ports)} ports listening:")
    for p in ports:
        print(f"  {p} → {get_service_name(int(p))}")

# ==================== NEW COMMANDS ==================== #
def cmd_udp(args):
    ip = resolve_host(args.ip)
    if not ip:
        err(f"Cannot resolve {args.ip}")
        return
    info(f"UDP scanning {ip} ports 1-{args.max_port}...")
    results = udp_scan(ip, args.max_port)
    if not results:
        print("[-] No UDP ports responded")
        return
    ok("UDP scan results:")
    for port, status in results:
        print(f"  {port}/udp {status}")

def cmd_rtt(args):
    # host may be domain or IP
    ip = resolve_host(args.host)
    if not ip:
        err(f"Cannot resolve {args.host}")
        return
    result = measure_rtt(ip, args.port)
    print(result)

def cmd_subnet(args):
    hosts = list_subnet_hosts(args.subnet)
    if not hosts:
        err(f"Invalid subnet: {args.subnet}")
        return
    ok(f"{len(hosts)} IPs in {args.subnet}:")
    for ip in hosts:
        print(f"  {ip}")

# ==================== PARSER ==================== #
def build_parser():
    parser = argparse.ArgumentParser(
        prog="netspector",
        description=DESCRIPTION,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = parser.add_subparsers(dest="cmd", help="Available commands")

    # scan (range)
    p = sub.add_parser("scan", help="scan a range of TCP ports")
    p.add_argument("ip")
    p.add_argument("--start", type=int, default=1)
    p.add_argument("--end", type=int, default=1000)
    p.set_defaults(func=cmd_scan)

    # scan-port (single)
    p = sub.add_parser("scan-port", help="scan a single TCP port")
    p.add_argument("ip")
    p.add_argument("port", type=int)
    p.set_defaults(func=cmd_scan_port)

    # ping
    p = sub.add_parser("ping", help="check if host is reachable (ICMP)")
    p.add_argument("ip")
    p.set_defaults(func=cmd_ping)

    # private check
    p = sub.add_parser("private", help="check if IP is private (RFC 1918)")
    p.add_argument("ip")
    p.set_defaults(func=cmd_private)

    # local listening ports
    p = sub.add_parser("listening", help="show listening ports on 127.0.0.1")
    p.set_defaults(func=cmd_listening)

    # UDP scan (new)
    p = sub.add_parser("udp", help="UDP port scan (slow, less reliable)")
    p.add_argument("ip")
    p.add_argument("--max-port", type=int, default=100, help="max port to scan (default 100)")
    p.set_defaults(func=cmd_udp)

    # RTT measurement (new)
    p = sub.add_parser("rtt", help="measure round‑trip time to a TCP port")
    p.add_argument("host")
    p.add_argument("port", type=int)
    p.set_defaults(func=cmd_rtt)

    # Subnet host lister (new)
    p = sub.add_parser("subnet", help="list all usable IPs in a CIDR subnet")
    p.add_argument("subnet", help="e.g. 192.168.1.0/24")
    p.set_defaults(func=cmd_subnet)

    return parser

# ==================== MAIN ==================== #
def main():
    BANNER()
    parser = build_parser()
    
    # If command line arguments were given, run once and exit
    if len(sys.argv) > 1:
        args = parser.parse_args()
        if not args.cmd:
            parser.print_help()
            return
        args.func(args)
        return
    
    # Otherwise, enter interactive REPL
    print(DESCRIPTION)
    print("Type 'help' for commands, 'exit' to quit.\n")
    
    while True:
        try:
            line = input("Netspector> ").strip()
            if not line:
                continue
            if line.lower() in ("exit", "quit"):
                print("Goodbye!")
                break
            if line.lower() == "help":
                parser.print_help()
                continue
            
            # Split the line respecting quotes (simple split is enough for our commands)
            args_list = line.split()
            try:
                parsed = parser.parse_args(args_list)
                if not parsed.cmd:
                    print("No command given. Type 'help'.")
                    continue
                parsed.func(parsed)
            except SystemExit:
                # argparse calls sys.exit() on error – catch it
                pass
            except Exception as e:
                print(f"[!] Error: {e}")
        except KeyboardInterrupt:
            print("\nType 'exit' to quit.")
        except EOFError:
            print("\nGoodbye!")
            break