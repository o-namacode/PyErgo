import textwrap

from ..constants import IO__DEFAULT_MAX_WIDTH, IO__LEFT_PAD
from ..helper import get_left_pad_str


def Print(
        text: str,
        max_width: int = IO__DEFAULT_MAX_WIDTH,
        left_pad: int = IO__LEFT_PAD,
        nl: bool = True,

        break_on_hyphens: bool = True,
        break_long_words: bool = False,
        
        break_on_whitespace: bool = True,
        drop_whitespace: bool = True,
        expand_tabs: bool = True,
        fix_sentence_endings: bool = True,
        tabsize: int = 4
):
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

