
from typing import Generic, List, TypeVar, Union

from ..ctypes_ import UserRoleList
from ..interfaces import IUserRole, IUserAccount, IUserManager


TUser = TypeVar("TUser", bound=IUserAccount)
TUserRole = TypeVar("TUserRole", bound=IUserRole)
TUserManager = TypeVar("TUserManager", bound=IUserManager)


class RoleManager (Generic[TUser, TUserRole, TUserManager]):
    @classmethod
    def Add (
        cls, 
        user : TUser, 
        role_or_roles : Union[TUserRole, List[TUserRole]],
        role_property : str = 'roles'):
        if not hasattr (user, role_property):
            raise AttributeError(f"Attribute `{role_property}` not found in user implementation.")
        
        current_roles = getattr(user, role_property)

        def _add_role(role : TUserRole):
            if role in getattr(user, role_property):
                return
            
            atr = getattr(user, role_property)

            if isinstance(atr, UserRoleList) or isinstance(atr, List[TUserRole]):
                atr.append(role)

        if isinstance(role_or_roles, List[TUserRole]):
            for rta in role_or_roles:
                _add_role(rta)
        elif isinstance(role_or_roles, TUserRole):
            _add_role(role_or_roles)

