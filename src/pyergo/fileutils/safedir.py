from pathlib import Path
from typing import Union


def safedir(path: Union[str, Path]) -> Path:
    if isinstance(path, str):
        path = Path(path)


    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
    return path
