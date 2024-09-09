from abc import ABC
from datetime import datetime
from typing import Optional, Union
from uuid import UUID, uuid4

from ..ctypes_ import UserRoleList


class IUserAccount (ABC):
    id : str
    username : str

    created_at : datetime
    updated_at : datetime

    roles : UserRoleList

    def __init__(self, id : Optional[Union[str, UUID]] = None, **kwargs):
        uid = UUID(id) if id is not None else uuid4()
        self.id = str(uid).replace('-', '')

        for key, value in kwargs.items():
            if hasattr(self, key):
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(value) if isinstance(value, str) else value)
                elif key == 'roles':
                    setattr(self, key, UserRoleList.from_json(value) if isinstance(value, (list, dict)) else value)
                else:
                    setattr(self, key, value)
            else:
                raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{key}'")
    
    def __str__(self):
        return f"UserAccount(id={self.id}, username={self.username})"
    
    def __repr__(self):
        return f"UserAccount(id={self.id}, username={self.username})"
    
    def __eq__(self, other):
        return self.id == other.id and self.username == other.username
    
    def to_dict(self):
        """
        Convert the object to a dictionary.

        Returns:
            dict: A dictionary representation of the object.
        """
        dt = {}

        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dt[key] = value.isoformat()
            elif isinstance(value, UserRoleList):
                dt[key] = value.to_dict()
            else:
                if hasattr(value, 'to_dict') and callable(getattr(value, 'to_dict')):
                    dt[key] = value.to_dict()
                else:
                    dt[key] = value

        return dt
    
    @classmethod
    def from_dict(cls, data : dict):
        return cls(**data)
