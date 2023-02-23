from csv import reader
from .types import Server, List


def parse_csv_to_schema(csv_input_string: str) -> List[Server]:
    servers = []
    for line in csv_input_string.split("\n")[1:]:
        host_port = line.split(";")
        print(host_port)
    return []
