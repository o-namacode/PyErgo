import json
import os
from pathlib import Path
from typing import Generator, List, TypeVar, Generic

from ..constants import PYERGO__LIBRARY_USERS_DATASTORE_DIR, PYERGO__LIBRARY_USERSFILE_DIR, PYERGO__LIBRARY_USERS_FILE_EXT
from ..interfaces import IUserAccount
from ..fileutils import safedir


T = TypeVar('T', bound=IUserAccount)

class UserManager (Generic[T]):
    USER_FILE_DIR = PYERGO__LIBRARY_USERSFILE_DIR
    USER_DATASTORE_DIR = PYERGO__LIBRARY_USERS_DATASTORE_DIR
    USER_FILE_EXT = PYERGO__LIBRARY_USERS_FILE_EXT

    @classmethod
    def filepath(cls, user : T) -> Path:
        return cls.USER_FILE_DIR / f"{user.id}{cls.USER_FILE_EXT}"
    @classmethod
    def userdatadir(cls, user : T) -> Path:
        return safedir(cls.USER_DATASTORE_DIR / f"{user.id}")


    @classmethod
    def All(cls) -> Generator[T, None, None]:
        for userfile in cls.USER_FILE_DIR.iterdir():
            if userfile.is_file() and userfile.suffix == cls.USER_FILE_EXT:
                with open(userfile, "r") as f:
                    yield cls.from_json(f.read())
    @classmethod
    def GetByUsername(cls, username: str) -> T:
        for user in cls.All():
            if user.username == username:
                return user
        return None
    @classmethod
    def GetById(cls, id: str) -> T:
        for user in cls.All():
            if user.id == id:
                return user
        return None
    

    @classmethod
    def Save(cls, user: T) -> None:
        with open(cls.filepath(user), "w") as f:
            f.write(json.dumps(user.to_dict(), indent=4))