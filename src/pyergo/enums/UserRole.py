from enum import StrEnum

class UserRole(StrEnum):
    SUPER_ADMIN = "su"
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"