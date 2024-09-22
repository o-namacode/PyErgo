
from typing import Generic, List, TypeVar, Union

from ..interfaces import IUserRole, IUserAccount, IUserManager


TUser = TypeVar("TUser", bound=IUserAccount)
TUserRole = TypeVar("TUserRole", bound=IUserRole)
TUserManager = TypeVar("TUserManager", bound=IUserManager)


class RoleManager (Generic[TUser, TUserRole, TUserManager]):
    @classmethod
    def Add (cls, user : TUser, role_or_roles : Union[TUserRole, List[TUserRole]]):
        if not hasattr (user, 'roles'):
            raise AttributeError("Attribute `roles` not found in user implementation.")
        
        current_roles = user.roles

        def _add_role(role : TUserRole):
            if role in user.roles:
                return
            
            user.roles.append(role)

        if isinstance(role_or_roles, List[TUserRole]):
            for rta in role_or_roles:
                _add_role(rta)
        elif isinstance(role_or_roles, TUserRole):
            _add_role(role_or_roles)
