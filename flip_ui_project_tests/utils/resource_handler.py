from pathlib import Path


def get_path(file_name):
    return str(Path(__file__).parent.parent.parent.joinpath(f"{file_name}"))
