from typing import Protocol, Generator, TypeVar
from pathlib import Path

T = TypeVar('T')

class IUserManager(Protocol[T]):
    @classmethod
    def filepath(cls, user: T) -> Path:
        ...

    @classmethod
    def userdatadir_for(cls, user: T) -> Path:
        ...

    @classmethod
    def All(cls) -> Generator[T, None, None]:
        ...

    @classmethod
    def GetByUsername(cls, username: str) -> T:
        ...

    @classmethod
    def GetById(cls, id: str) -> T:
        ...

    @classmethod
    def Save(cls, user: T) -> None:
        ...