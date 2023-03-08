import socket
import platform
import subprocess

from dns_checker.core.schema import IP, IPv4, ServerResolved, Server

from .decorators import time_spent


def resolve_servers_ip_addrs(servers: list[Server]) -> list[ServerResolved]:
    resolved_servers = []
    for server in servers:
        _, _, ip_addr_list = socket.gethostbyname_ex(server.hostname)
        ipv4_addrs = [IPv4(addr) for addr in ip_addr_list]

        ip_ports = _build_ip_port_pairs(ipv4_addrs, server.ports)

        resolved_servers.append(ServerResolved(server.hostname, addresses=ip_ports))

    return resolved_servers


@time_spent
def check_if_ip_is_available(ip: IP) -> bool:
    is_windows_platform = platform.system().lower() == "windows"
    num_of_packets_param = "-n 1" if is_windows_platform else "-c 1"
    timeout_param = "-W 2"

    return 0 == subprocess.call(
        f"ping {timeout_param} {num_of_packets_param} {ip}".split(),
        stdout=subprocess.DEVNULL,
    )


@time_spent
def check_if_port_is_opened(ip: IP, port: int) -> bool:
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.settimeout(2)

    return _socket.connect_ex((str(ip), port)) == 0


def _build_ip_port_pairs(ips: list[IP], ports: list[int]):
    return [(ip, port) for port in ports for ip in ips]
