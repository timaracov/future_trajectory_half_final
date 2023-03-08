from dns_checker.core.schema import Server, List


def read_csv(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def csv_to_servers(filename: str) -> List[Server]:
    csv_input_string = read_csv(filename)

    servers = []
    for line in csv_input_string.split("\n")[1:]:
        match line.split(";"):
            case "", _:
                continue
            case hostname, "":
                servers.append(Server(hostname, [80, 443]))
            case hostname, port:
                try:
                    ports = list(map(int, port.split(",")))
                except ValueError:
                    continue
                else:
                    servers.append(Server(hostname, ports))

    return servers
