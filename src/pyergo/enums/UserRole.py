from enum import StrEnum

from ..interfaces import IUserRole

class UserRole( IUserRole):
    SUPER_ADMIN = "su"
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"