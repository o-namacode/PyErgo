import textwrap

from ..constants import IO__DEFAULT_MAX_WIDTH, IO__LEFT_PAD, NLBR
from ..helper import get_left_pad_str


def Print(
        *args,
        max_width: int = IO__DEFAULT_MAX_WIDTH,
        left_pad: int = IO__LEFT_PAD,
        nl: int = 1,

        break_on_hyphens: bool = True,
        break_long_words: bool = False,
        
        drop_whitespace: bool = True,
        expand_tabs: bool = True,
        fix_sentence_endings: bool = True,
        tabsize: int = 4,

        join_nl: bool = True,

        multiline_str : bool = False,
):
    """
    Print text to the console.

    Args:
        args (Any): The arguments to print.
        max_width (int, optional): The maximum width of the text. Defaults to IO__DEFAULT_MAX_WIDTH.
        left_pad (int, optional): The left padding to print. Defaults to IO__LEFT_PAD.
        break_on_hyphens (bool, optional): Whether to break on hyphens. Defaults to True.
        break_long_words (bool, optional): Whether to break long words. Defaults to False.
        break_on_whitespace (bool, optional): Whether to break on whitespace. Defaults to True.
        drop_whitespace (bool, optional): Whether to drop whitespace. Defaults to True.
        expand_tabs (bool, optional): Whether to expand tabs. Defaults to True.
        fix_sentence_endings (bool, optional): Whether to fix sentence endings. Defaults to True.
        tabsize (int, optional): The size of a tab. Defaults to 4.
        nl (int, optional): The number of new lines to print. Defaults to 0.
        multiline_str (bool, optional): Whether to print a multiline string. Defaults to False.
    """

    if len(args) == 1:
        text = args[0]
    else:
        text = NLBR.join(args) if join_nl else " ".join(args)

    if multiline_str:
        wrapped_text = text
    else:        
        wrapped_text = textwrap.fill(
            text,
            max_width + left_pad,

            initial_indent=get_left_pad_str(left_pad),
            subsequent_indent=get_left_pad_str(left_pad),

            tabsize=tabsize,
            expand_tabs=expand_tabs,

            break_on_hyphens=break_on_hyphens,
            break_long_words=break_long_words,

            drop_whitespace=drop_whitespace,
            fix_sentence_endings=fix_sentence_endings
        )

    wrapped_text = wrapped_text + NLBR * nl
    
    content = ""
    for line in wrapped_text.splitlines():
        content += get_left_pad_str(left_pad) + line.strip() + NLBR
    
    print(content, end='')

