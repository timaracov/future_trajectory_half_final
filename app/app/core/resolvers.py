from socket import getaddrinfo, gethostbyname_ex
from .types import IPv4, IPv6


def resolve_dns_to_ip(dns: str) -> IPv6 | IPv4:
    ip = IPv4("0.0.0.0")
    return ip
