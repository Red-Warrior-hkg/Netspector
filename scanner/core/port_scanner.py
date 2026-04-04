import socket
import threading
import queue
import subprocess
import ipaddress
import time
import platform

#  Scan a single TCP port
def scan_port(ip: str, port: int) -> bool:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(1)

        result = client.connect_ex((ip, port))
        client.close()

        return result == 0
    except:
        return False


#  Threaded TCP port scanner (fast)
def scan_ports(ip: str, start: int = 1, end: int = 1000):
    q = queue.Queue()
    open_ports = []

    for port in range(start, end + 1):
        q.put(port)

    def worker():
        while not q.empty():
            port = q.get()

            try:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(1)

                result = client.connect_ex((ip, port))

                if result == 0:
                    try:
                        service = socket.getservbyport(port)
                    except:
                        service = "Unknown"

                    open_ports.append((port, service))

                client.close()
            except:
                pass

            q.task_done()

    for _ in range(100):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

    q.join()
    return open_ports


# UDP Scanner
def udp_scan(ip: str, max_port: int):
    results = []

    for port in range(1, max_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(1)

        try:
            s.sendto(b"just a test", (ip, port))
            data, address = s.recvfrom(1024)
            results.append((port, "OPEN (responded)"))
        except socket.timeout:
            results.append((port, "maybe OPEN or FILTERED"))
        except:
            pass

        s.close()

    return results


# Check if host is reachable (ping)
def is_host_up(ip: str) -> str:
    try:
        ipaddress.ip_address(ip)
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        result = subprocess.run(['ping', param, '1', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return "[+] IP is reachable" if result.returncode == 0 else "[-] IP is unreachable"
    except ValueError:
        return "[!] invalid IP"


# Measure RTT (Round Trip Time)
def measure_rtt(host: str, port: int):
    s = None
    try:
        if not isinstance(port, int) or not (1 <= port <= 65535):
            return "Port must be a number between 1 and 65535"

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)

        start_t = time.perf_counter()
        s.connect((host, port))
        end_t = time.perf_counter()

        rtt = (end_t - start_t) * 1000
        return f"RTT to {host}:{port} ≈ {rtt:.6f} ms"

    except socket.gaierror as e:
        return f"DNS resolution failed for '{host}': {e}"
    except ConnectionRefusedError:
        return f"Connection refused on {host}:{port}"
    except socket.timeout:
        return f"connection to {host} timed out"
    except Exception as e:
        return f"Unexpected Error: {e}"
    finally:
        if s:
            s.close()