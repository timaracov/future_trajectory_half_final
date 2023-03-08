# future_trajectory_half_final

To run application in terminal follow these steps:

1. Install poetry:
```sh
$ pip install poetry
```

2. Install project packages with poetry:
```sh
$ poetry install && poetry shell
```

3. Run cli app:
```sh
$ cd src
$ poetry run python -m dns_checker /path/to/csv/file.csv
```

To run application as http server, follow steps 1 and 2, then
uncomment all lines in src/dns_checker/__main__.py, and follow step 3
