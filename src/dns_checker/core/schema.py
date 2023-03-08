from typing import List
from ipaddress import IPv4Address, IPv6Address
from dataclasses import dataclass


IPv4 = IPv4Address
IPv6 = IPv6Address

IP = IPv4 or IPv6
Port = int


@dataclass
class Server:
    hostname: str
    ports: List[int]


@dataclass
class ServerResolved:
    hostname: str
    addresses: List[tuple[IP, Port]]


@dataclass
class AddressInfo:
    ip: IP
    port: int
    is_ip_available: bool
    is_port_opened: bool
    time_spent: float
    at_datetime: str


@dataclass
class ServerInfo:
    hostname: str
    addr_info: List[AddressInfo]

    def to_dict(self):
        s_info_as_dict = {"hostname": self.hostname, "addr_info": []}

        for a_info in self.addr_info:
            s_info_as_dict["addr_info"].append(
                {
                    "ip": str(a_info.ip),
                    "port": a_info.port,
                    "is_ip_available": a_info.is_ip_available,
                    "is_port_opened": a_info.is_port_opened,
                    "time_spent": str(a_info.time_spent),
                    "at_datetime": a_info.at_datetime,
                }
            )

        return s_info_as_dict
