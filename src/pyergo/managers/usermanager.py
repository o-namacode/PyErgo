import json
import os
from pathlib import Path
from typing import Generator, List, TypeVar, Generic

from ..interfaces import IUserAccount
from ..fileutils import safedir

T = TypeVar('T', bound=IUserAccount)

class UserManager (Generic[T]):
    USER_DATA_DIR = safedir(os.path.join(os.path.expanduser("~"), ".pyergo", "users"))
    USER_FILE_EXT = ".umf"

    @classmethod
    def filepath(cls, user : T) -> Path:
        return cls.userdatadir_for(user) / f"{user.id}{cls.USER_FILE_EXT}"
    
    @classmethod
    def userdatadir_for(cls, user : T) -> Path:
        return safedir(cls.USER_DATA_DIR / f"{user.id}")

    @classmethod
    def All(cls) -> Generator[T, None, None]:
        for folders in cls.USER_DATA_DIR.iterdir():
            if folders.is_dir():
                for userfile in folders.iterdir():
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