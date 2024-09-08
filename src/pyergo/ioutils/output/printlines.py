from typing import Optional

from ..constants import NLBR


def PrintLines(n : int = 1):
    """
    Print lines to the console.

    Args:
        n (int, optional): The number of lines to print. Defaults to 1.
    """
    str_ = NLBR * n
    print(str_, end='')

    
