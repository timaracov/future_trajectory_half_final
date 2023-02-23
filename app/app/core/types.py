from typing import List, Optional
from ipaddress import IPv4Address, IPv6Address


Port = int
IPv4 = IPv4Address
IPv6 = IPv6Address

Server = tuple[IPv4 | IPv6, Optional[Port]]
