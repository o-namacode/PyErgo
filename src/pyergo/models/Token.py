from ..encoders.jsonencoder import PyErgoJSONEncoder
from ..enums.TokenType import TokenType
from .TokenSpecs import TokenSpecs


from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Token (Generic[T]):
    def __init__(self, value : T, specs : Optional[TokenSpecs] = None, type : Optional[TokenType] = None, name : Optional[str] = None) -> None:
        self.__val = value

        if specs:
            self.__specs = specs
        if type:
            self.__type = type
        if  name:
            self.__name = name.lower().replace(" ", "_")

    @property
    def value (self):
        return self.__val

    @value.setter
    def value (self, _):
        raise AttributeError('Token[Value] cannot be modified.')

    @property
    def specs (self):
        if hasattr(self, '__specs'):
            return self.__specs

        return TokenSpecs(
            length=len(self.value),
            type=self.__type if hasattr(self, '__type') else TokenType.UNDEFINED,
        )

    @specs.setter
    def specs (self, _):
        raise AttributeError('Token[Specifications] cannot be modified.')

    @property
    def name (self):
        if hasattr(self, '__name'):
            return getattr(self, '__name')

        return 'token_'

    @name.setter
    def name (self, _):
        raise AttributeError('Token[Name] cannot be modified.')

    @property
    def json (self, indent : int = 0):
        from json import dumps

        d = {
            'name': self.name,
            'value': self.value,
        }
        d.update(self.specs.__dict__)

        return dumps(d, cls=PyErgoJSONEncoder, indent=indent)