def read_csv(filename: str) -> str:
    with open(filename) as f:
        return f.read()
