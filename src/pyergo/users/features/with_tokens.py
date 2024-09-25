from typing import Final, Optional
from uuid import UUID

from ...interfaces import IUserAccount

class UserWithTokens (IUserAccount):
    TOKEN_PREFIX : Final[str] = 'tk_'

    def __init__(
            self, 
            id: str | UUID | None = None, 
            
            ef__raise_error_on_key_not_found: bool = False, 
            *args, **kwargs):
        # Built-in Properties 
        self.tk_remember : Optional[str] = kwargs.get('tk_remember', None)


        super().__init__(id, ef__raise_error_on_key_not_found, *args, **kwargs)

    
    def token(self, key : str, default = None):
        aname = f"{self.TOKEN_PREFIX}{key}".lower()

        if hasattr(self, aname):
            return getattr(self, aname)
        
        if default is None:
            raise AttributeError(f"Token Attribute `{key}` not found.")
        
        return default

    def settoken(self, key : str, value):

        if key.lower().startswith(self.TOKEN_PREFIX):
            tname = key.lower()
        else:
            tname = f"{self.TOKEN_PREFIX}{key}".lower()

        setattr(self, tname, value)
        return self
