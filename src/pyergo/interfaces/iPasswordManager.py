from abc import ABC, abstractmethod


class IPasswordManager (ABC):
    @abstractmethod
    @staticmethod
    def HashPassword(password: str) -> str:
        """
        Hash a password.

        Args:
            password (str): The plain-text password to hash.

        Returns:
            str: The hashed password.
        """
        pass
    
    @abstractmethod
    @staticmethod
    def VerifyPassword(plain_password: str, hashed_password: str) -> bool:
        """
        Verify a plain-text password against a hashed password.

        Args:
            plain_password (str): The plain-text password to verify.
            hashed_password (str): The hashed password to compare against.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        pass

    @abstractmethod
    @staticmethod
    def validate_password(password: str, min_length: int = 8, require_uppercase: bool = True,
                           require_lowercase: bool = True, require_digit: bool = True,
                           require_special: bool = True, **kwargs) -> bool:
        """
        Validate a password against the specified criteria.

        Args:
            password (str): The password to validate.
            min_length (int): Minimum length of the password.
            require_uppercase (bool): Whether to require at least one uppercase letter.
            require_lowercase (bool): Whether to require at least one lowercase letter.
            require_digit (bool): Whether to require at least one digit.
            require_special (bool): Whether to require at least one special character.
            **kwargs: Additional keyword arguments.
        """
        pass
