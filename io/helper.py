from .constants import IO__LEFT_PAD


def get_left_pad_str(pad_width: int = IO__LEFT_PAD) -> str:
    return ' ' * pad_width


def get_left_pad_str(**kwargs) -> str:
    return ' ' * kwargs.get('left_pad', IO__LEFT_PAD)
