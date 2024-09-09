from typing import List, Union

from ..enums import UserRole


class UserRoleList(List[UserRole]):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        """
        Return a string representation of the UserRoleList.

        Returns:
            str: A string representation of the UserRoleList.
            """
        return f"UserRoles({', '.join([role.value.title() for role in self])})"

    def __repr__(self):
        """
        Return a string representation of the UserRoleList.

        Returns:
            str: A string representation of the UserRoleList.
            """
        return f"UserRoles({', '.join([role.value.title() for role in self])})"
    
    def to_dict(self) -> List[str]:
        """
        Generate a JSON-safe dictionary representation of the UserRoleList.
        
        Returns:
            List[str]: A list of role values as strings.
        """
        return [role.value for role in self]

    @classmethod
    def from_json(cls, data: Union[List[str], List[dict]]) -> 'UserRoleList':
        """
        Create a UserRoleList instance from JSON data.

        Args:
            data (Union[List[str], List[dict]]): A list of role values as strings or dicts.

        Returns:
            UserRoleList: A new UserRoleList instance.
        """
        roles = []
        for item in data:
            if isinstance(item, dict) and 'value' in item:
                roles.append(UserRole(item['value']))
            elif isinstance(item, str):
                roles.append(UserRole(item))
            else:
                raise ValueError(f"Invalid role data: {item}")
        return cls(roles)