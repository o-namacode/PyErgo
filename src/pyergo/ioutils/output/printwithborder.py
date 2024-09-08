from ..constants import IO__DEFAULT_MAX_WIDTH, IO__DEFAULT_BORDER_CHAR
from .print_ import Print

def PrintWithBorder(text: str, width: int = IO__DEFAULT_MAX_WIDTH, border_char: str = IO__DEFAULT_BORDER_CHAR, nl: int = 1):
    text = text.ljust(width - 4)
    Print(f"{border_char} {text} {border_char}".ljust(width), nl=nl)

