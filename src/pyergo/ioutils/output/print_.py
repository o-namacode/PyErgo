import textwrap

from ..constants import IO__DEFAULT_MAX_WIDTH, IO__LEFT_PAD, NLBR
from ..helper import get_left_pad_str


def Print(
        *args,
        max_width: int = IO__DEFAULT_MAX_WIDTH,
        left_pad: int = IO__LEFT_PAD,
        nl: bool = True,

        break_on_hyphens: bool = True,
        break_long_words: bool = False,
        
        break_on_whitespace: bool = True,
        drop_whitespace: bool = True,
        expand_tabs: bool = True,
        fix_sentence_endings: bool = True,
        tabsize: int = 4,

        join_nl: bool = True,
):
    """
    Print text to the console.

    Args:
        args (Any): The arguments to print.
        max_width (int, optional): The maximum width of the text. Defaults to IO__DEFAULT_MAX_WIDTH.
        left_pad (int, optional): The left padding to print. Defaults to IO__LEFT_PAD.
        nl (bool, optional): Whether to print a new line. Defaults to True.
        break_on_hyphens (bool, optional): Whether to break on hyphens. Defaults to True.
        break_long_words (bool, optional): Whether to break long words. Defaults to False.
        break_on_whitespace (bool, optional): Whether to break on whitespace. Defaults to True.
        drop_whitespace (bool, optional): Whether to drop whitespace. Defaults to True.
        expand_tabs (bool, optional): Whether to expand tabs. Defaults to True.
        fix_sentence_endings (bool, optional): Whether to fix sentence endings. Defaults to True.
        tabsize (int, optional): The size of a tab. Defaults to 4.
    """

    if len(args) == 1:
        text = args[0]
    else:
        text = NLBR.join(args) if join_nl else " ".join(args)

    wrapped_text = textwrap.fill(
        text,
        max_width,

        initial_indent=get_left_pad_str(left_pad),
        subsequent_indent=get_left_pad_str(left_pad),

        tabsize=tabsize,
        expand_tabs=expand_tabs,

        break_on_hyphens=break_on_hyphens,
        break_long_words=break_long_words,
        break_on_whitespace=break_on_whitespace,

        drop_whitespace=drop_whitespace,
        fix_sentence_endings=fix_sentence_endings
    )
        
    print(wrapped_text, end='\n' if nl else '')

    

