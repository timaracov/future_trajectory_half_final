from datetime import datetime

from dns_checker.core.schema import (
    Server,
    List,
    ServerInfo,
    AddressInfo,
    ServerResolved,
)
from .net import (
    resolve_servers_ip_addrs,
    check_if_port_is_opened,
    check_if_ip_is_available,
)


def check_servers(servers: List[Server]) -> List[ServerInfo]:
    result = []
    for server in resolve_servers_ip_addrs(servers):
        server_info = _build_server_info(server)
        result.append(server_info)

    return result


def _build_server_info(server: ServerResolved) -> ServerInfo:
    addrs_info = []

    for ip, port in server.addresses:
        is_ip_available, time_spent_for_ip = check_if_ip_is_available(ip)  # type:ignore
        is_port_opened, time_spent_for_ports = check_if_port_is_opened(
            ip, port
        )  # type:ignore

        total_time_spent = time_spent_for_ip + time_spent_for_ports

        addrs_info.append(
            AddressInfo(
                ip=ip,
                port=port,
                is_ip_available=is_ip_available,
                is_port_opened=is_port_opened,
                time_spent=total_time_spent,
                at_datetime=datetime.strftime(datetime.now(), "%d/%m/%Y -- %H:%M:%S"),
            )
        )

    addrs_info.sort(key=lambda a: a.ip)

    return ServerInfo(hostname=server.hostname, addr_info=addrs_info)
