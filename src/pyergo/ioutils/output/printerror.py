from typing import Optional
from pyergo.ioutils.constants import IO__LEFT_PAD, NLBR
from pyergo.ioutils.helper import get_left_pad_str
from pyergo.ioutils.output.print_ import Print


import traceback


def PrintError(*args,
                prefix : Optional[str] = "ERROR: ",
                left_padding : int = IO__LEFT_PAD,
                show_traceback : bool = False):
    """
    Print error to the console.
    
    Args:
        args (Any): The arguments to print.
        prefix (Optional[str], optional): The prefix to print. Defaults to "ERROR: ".
        left_padding (int, optional): The left padding to print. Defaults to IO__LEFT_PAD.
        show_traceback (bool, optional): Whether to show the traceback. Defaults to False.
    """

    errstr = ""
    lpstr = get_left_pad_str(left_padding)

    for arg in args:
        errstr += lpstr + (prefix if prefix else "")
        if isinstance(arg, str):
            errstr += arg + NLBR
        elif isinstance(arg, Exception):
            errstr += str(arg) + NLBR

            if show_traceback:
                errstr += lpstr + "Traceback: " + NLBR
                errstr += lpstr + "".join(traceback.format_exception(type(arg), arg, arg.__traceback__)) + NLBR

        else:
            errstr += repr(arg) + NLBR

    Print(errstr)