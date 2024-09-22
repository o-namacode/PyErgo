
from enum import StrEnum, auto
from typing import Generic, Optional, TypeVar


T = TypeVar("T")

class TokenType (StrEnum):
    MD5 = auto()
    UNDEFINED = auto()

class TokenSpecs:
    length : int 
    type : TokenType

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)

class Token (Generic[T]):
    def __init__(self, value, specs : Optional[TokenSpecs] = None, type : Optional[TokenType] = None) -> None:
        self.__val = value

        if specs:
            self.__specs = specs
        if type:
            self.__type = type

    @property
    def value (self):
        return self.__val
    
    @value.setter
    def value (self, _):
        raise AttributeError('Value cannot be modified.')
    
    @property
    def specs (self):
        if hasattr(self, '__specs'):
            return self.__specs
        
        return TokenSpecs(
            length=len(self.value),
            type=self.__type if hasattr(self, '__type') else TokenType.UNDEFINED,
        )
    


class TokenGenerator:
    @classmethod
    def GenerateRememberMe (cls, ):  
        from hashlib import md5  
        return Token[str](
            value=md5().hexdigest(),
            type=TokenType.MD5,
        )