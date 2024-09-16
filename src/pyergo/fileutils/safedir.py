from pathlib import Path
from typing import Union


def safedir(path: Union[str, Path]) -> Path:
    """
    Ensures that the specified directory exists. If it does not exist, it creates the directory.

    Args:
        path (Union[str, Path]): The path to the directory to ensure.

    Returns:
        Path: A Path object representing the specified directory.
    """
    if isinstance(path, str):
        path = Path(path)


    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
    return path
