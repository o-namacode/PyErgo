from ..constants import IO__DEFAULT_MAX_WIDTH, IO__DEFAULT_BORDER_CHAR
from .print_ import Print

def PrintBorder(width: int = IO__DEFAULT_MAX_WIDTH, border_char: str = IO__DEFAULT_BORDER_CHAR, nl: int = 0):
    """
    Prints a border line with the specified width and character.

    Args:
        width (int, optional): The total width of the border. Defaults to 80.
        border_char (str, optional): The character used for the border. Defaults to "*".
        nl (int, optional): Number of newlines to print after the border. Defaults to 1.

    Returns:
        None
    """
    border = border_char * width

    Print(border, nl=nl, concat_nl=False)