from getpass import getpass
from typing import Optional

from ..constants import IO__LEFT_PAD, NLBR
from ..helper import get_left_pad_str


def getpw(
        prompt: Optional[str] = None,
        left_pad: Optional[int] = IO__LEFT_PAD,
        cursor: Optional[str] = None,
        nl: bool = True,

        strip: bool = True,
):
    if cursor is None:
        cursor = '> '
    cursor_str = cursor + "  "

    _prompt = get_left_pad_str(left_pad) + prompt
    if nl:
        _prompt += NLBR
    _prompt += cursor_str if not nl else get_left_pad_str(left_pad) + cursor_str

    if nl:
        _prompt += NLBR
        
    ui = getpass(_prompt)

    if strip:
        ui = ui.strip()

    return ui