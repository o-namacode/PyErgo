from ..enums.TokenType import TokenType


class TokenSpecs:
    length : int
    type : TokenType

    def __init__(self, **kwargs) -> None:
        dkeys = self.__dict__.keys()

        for k, v in kwargs.items():
            setattr(self, k, v)