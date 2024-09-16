from typing import Optional

from ..constants import IO__LEFT_PAD, NLBR
from ..helper import get_left_pad_str

from ..output.printerror import PrintError


def getinput(
        prompt: Optional[str] = "",
        left_pad: Optional[int] = IO__LEFT_PAD,
        cursor: Optional[str] = None,
        nl: bool = True,

        strip: bool = True,
        lower: bool = False,

        allow_empty: bool = False,
        empty_err_msg: str = "Input cannot be empty",

        default: str = "",
):
    """
    Get input from the user.

    Args:
        prompt (str, optional): The prompt to print. Defaults to "".
        left_pad (int, optional): The left padding to print. Defaults to IO__LEFT_PAD.
        cursor (str, optional): The cursor to print. Defaults to '> ' if None.
        nl (bool, optional): Whether to print a new line between the prompt and the input cursor. Defaults to True.

        strip (bool, optional): Whether to strip the input. Defaults to True.
        lower (bool, optional): Whether to convert the input to lowercase. Defaults to False.

        allow_empty (bool, optional): Whether to allow empty input. Defaults to False.
        empty_err_msg (str, optional): The error message to print if the input is empty. Defaults to "Input cannot be empty".

        default (str, optional): The default value to return if the input is empty. Defaults to None.

    Returns:
        str: The input.
    """

    while True:

        if cursor is None:
            cursor = '> '
        cursor_str = cursor + "  "

        _prompt = get_left_pad_str(left_pad) + prompt
        if nl:
            _prompt += NLBR
        _prompt += cursor_str if not nl else get_left_pad_str(left_pad) + cursor_str

        ui = input(_prompt)

        if not ui:
            return default
        if strip:
            ui = ui.strip()
        if lower:
            ui = ui.lower()

        if not allow_empty and not ui:
            PrintError(empty_err_msg)
            continue

        return ui


