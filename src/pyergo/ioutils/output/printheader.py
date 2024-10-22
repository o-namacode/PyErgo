from ..constants import IO__DEFAULT_MAX_WIDTH, IO__DEFAULT_BORDER_CHAR

from .print_ import Print
from .printborder import PrintBorder
from .printwithborder import PrintWithBorder

def PrintHeader (
        text : str,

        width: int = IO__DEFAULT_MAX_WIDTH,
        border_char: str = IO__DEFAULT_BORDER_CHAR,
        nl: int = 1,

        center_text : bool = True,
):
    PrintBorder(width=width)
    PrintWithBorder(text, width=width, border_char=border_char, nl=nl, center_text=center_text)
    PrintBorder(width=width)