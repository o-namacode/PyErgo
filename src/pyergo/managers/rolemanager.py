
from typing import Generic, TypeVar

from ..interfaces import iUserRole, iUserAccount


TUser = TypeVar("TUser", bound=iUserAccount)
TUserRole = TypeVar("TUserRole", bound=iUserRole)


class RoleManager (Generic[TUserRole]):
    pass