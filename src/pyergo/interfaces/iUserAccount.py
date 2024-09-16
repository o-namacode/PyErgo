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
        """
        Initializes a new instance of IUserAccount.

        Args:
            id (Optional[Union[str, UUID]]): Unique identifier for the user account. 
                                               If None, a new UUID is generated.
            **kwargs: Additional attributes to set on the instance.

        Raises:
            AttributeError: If an invalid attribute is provided in kwargs.
        """
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
        """
        Returns a string representation of the user account.

        Returns:
            str: A string containing the ID and username of the user account.
        """
        return f"UserAccount(id={self.id}, username={self.username})"
    
    def __repr__(self):
        """
        Returns a detailed string representation of the user account for debugging.

        Returns:
            str: A string representation including the ID and username.
        """
        return f"UserAccount(id={self.id}, username={self.username})"
    
    def __eq__(self, other):
        """
        Compares this user account with another for equality.

        Args:
            other (IUserAccount): Another user account to compare against.

        Returns:
            bool: True if both accounts have the same ID and username, False otherwise.
        """
        return self.id == other.id and self.username == other.username
    
    def to_dict(self):
        """
        Converts the user account instance into a dictionary representation.

        Returns:
            dict: A dictionary representation of the user account, with formatted datetime 
                  attributes and roles.
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
        """
        Creates an instance of IUserAccount from a dictionary of attributes.

        Args:
            data (dict): A dictionary containing the attributes to set on the user account.

        Returns:
            IUserAccount: An instance of IUserAccount populated with the provided data.
        """
        return cls(**data)
