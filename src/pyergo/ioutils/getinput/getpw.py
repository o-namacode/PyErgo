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
    """
    Get password from the user.

    Args:
        prompt (Optional[str], optional): The prompt to print. Defaults to None.
        left_pad (Optional[int], optional): The left padding to print. Defaults to IO__LEFT_PAD.
        cursor (Optional[str], optional): The cursor to print. Defaults to None.
        nl (bool, optional): Whether to print a new line. Defaults to True.
        strip (bool, optional): Whether to strip the input. Defaults to True.

    Returns:
        str: The password.
    """

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