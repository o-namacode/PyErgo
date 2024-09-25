from typing import Final, Optional
from uuid import UUID

from ...exceptions import PasswordLengthError, PasswordContentError
from ...interfaces import IUserAccount

class UserWithPassword (IUserAccount):
    PASSWORD_LEN_MIN = 4
    PASSWORD_REQ_UPPERCASE = False
    PASSWORD_REQ_DIGIT = False
    PASSWORD_REQ_SYMBOL = False

    def __init__(
            self, 
            id: str | UUID | None = None,
            password: Optional[str] = None, 
            
            ef__raise_error_on_key_not_found: bool = False, 
            *args, **kwargs):
        # Built-in Properties 
        self.password : Optional[str] = None
        if password:
            self.setpassw(password) 

        super().__init__(id, ef__raise_error_on_key_not_found, *args, **kwargs)
    
    def setpassw(self, val : str):
        if self.PASSWORD_LEN_MIN < len(val):
            raise PasswordLengthError.TooShort(self.PASSWORD_LEN_MIN)

        if self.PASSWORD_REQ_UPPERCASE:
            if not any(char.isupper() for char in val):
                raise PasswordContentError("Password must contain at least one uppercase letter.")

        if self.PASSWORD_REQ_DIGIT:
            if not any(char.isdigit() for char in val):
                raise PasswordContentError("Password must contain at least one digit.")
    
        if self.PASSWORD_REQ_SYMBOL:
            if not any(char in "!@#$%^&*()-+?_=,<>/~`|\\{}[]:;\"',.<>/?`~" for char in val):
                raise PasswordContentError("Password must contain at least one special character.")
            
        self.password = val