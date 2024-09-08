from typing import Optional

from ..constants import IO__LEFT_PAD, NLBR
from ..helper import get_left_pad_str


def getinput(
        prompt: Optional[str] = "",
        left_pad: Optional[int] = IO__LEFT_PAD,
        cursor: Optional[str] = None,
        nl: bool = True,

        strip: bool = True,
        lower: bool = False,
):
    """
    Get input from the user.

    Args:
        prompt (Optional[str], optional): The prompt to print. Defaults to "".
        left_pad (Optional[int], optional): The left padding to print. Defaults to IO__LEFT_PAD.
        cursor (Optional[str], optional): The cursor to print. Defaults to None.
        nl (bool, optional): Whether to print a new line. Defaults to True.
        strip (bool, optional): Whether to strip the input. Defaults to True.
        lower (bool, optional): Whether to convert the input to lowercase. Defaults to False.

    Returns:
        str: The input.
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

    ui = input(_prompt)

    if not ui:
        return None
    if strip:
        ui = ui.strip()
    if lower:
        ui = ui.lower()

    return ui

