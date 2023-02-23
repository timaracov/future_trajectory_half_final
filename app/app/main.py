from .core import readers, parsers, checkers
from .core.exceptions import catch_exceptions


@catch_exceptions
def main(csv_input_filename: str):
    input_data = readers.read_csv(csv_input_filename)
    parsed_servers = parsers.parse_csv_to_schema(input_data)
    checkers.check_servers(parsed_servers)
