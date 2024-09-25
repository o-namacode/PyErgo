import bcrypt

from ..interfaces import IPasswordManager

class PasswordManager(IPasswordManager):
    @staticmethod
    def HashPassword(password: str) -> str:
        """
        Hash a password using bcrypt.

        Args:
            password (str): The plain-text password to hash.

        Returns:
            str: The hashed password.
        """
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

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
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    
    @staticmethod
    def validate_password(password: str, min_length: int = 8, require_uppercase: bool = True, 
                           require_lowercase: bool = True, require_digit: bool = True, 
                           require_special: bool = True) -> bool:
        from ..exceptions import LengthError, UppercaseError, LowercaseError, DigitError, SpecialCharError
        """
        Validate a password against the specified criteria.

        Args:
            password (str): The password to validate.
            min_length (int): Minimum length of the password.
            require_uppercase (bool): Whether to require at least one uppercase letter.
            require_lowercase (bool): Whether to require at least one lowercase letter.
            require_digit (bool): Whether to require at least one digit.
            require_special (bool): Whether to require at least one special character.
        """

        if len(password) < min_length:
            raise LengthError(f"Password must be at least {min_length} characters long", min_length)
        if require_uppercase and not any(c.isupper() for c in password):
            raise UppercaseError("Password must contain at least one uppercase letter")
        if require_lowercase and not any(c.islower() for c in password):
            raise LowercaseError("Password must contain at least one lowercase letter")
        if require_digit and not any(c.isdigit() for c in password):
            raise DigitError("Password must contain at least one digit")
        if require_special and not any(not c.isalnum() for c in password):
            raise SpecialCharError("Password must contain at least one special character")
        return True

