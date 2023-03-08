import argparse

from rich.console import Console

from dns_checker.core.schema import ServerInfo
from dns_checker.core.utils import (
    catch_exceptions,
    csv_to_servers,
    check_servers
)


class CliAdapter:
    @catch_exceptions
    def __init__(self):
        __cli_arg_parser = self.__build_cli_arg_parser()
        __args = __cli_arg_parser.parse_args()
        self.check_dns(__args.csv_filename)

    @catch_exceptions
    def check_dns(self, filename: str):
        servers = csv_to_servers(filename)
        servers_info = check_servers(servers)
        self.print_info(servers_info)

    @catch_exceptions
    def print_info(self, servers_info: list[ServerInfo]):
        for s_info in servers_info:
            self.__print_prettified_server_info(s_info)

    def __print_prettified_server_info(self, server_info: ServerInfo, console=Console()):
        console.print(f"[[magenta bold]::{server_info.hostname}::[/magenta bold]]")

        for addr in server_info.addr_info:
            if addr.is_ip_available:
                color = "green"
                ip_info = "available"
            else:
                color = "red"
                ip_info = "not available"

            if addr.is_port_opened:
                color_p = "green"
                port_info = "opened"
            else:
                color_p = "yellow"
                port_info = "unknown"

            ip_and_port_info = (
                "is "
                f"[{color}]{ip_info:16}[/{color}]"
                " || "
                " port "
                f"[{color_p}]{port_info:8}[/{color_p}]"
            )

            time_spent = (
                f"RTT: {addr.time_spent:8.2f} ms")
            at_datetime = (
                f"[[bold] {addr.at_datetime:22} [/bold]]")

            console.print(
                f"[blue] [{str(addr.ip):15}]:[{addr.port:4}] [/blue]"
                " || "
                f"{ip_and_port_info}"
                " || "
                f"{time_spent}"
                " || "
                f"{at_datetime}"
            )

        console.print()

    def __build_cli_arg_parser(self) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(
            prog="Future trajectory - dns checker",
            description=(
                "This application resolves domain name to "
                "ip addresses and checks it's availability and opened ports"))

        parser.add_argument(
            "csv_filename",
            help="-- name of csv file where domain names are stored")

        return parser
