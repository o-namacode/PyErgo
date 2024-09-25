class PasswordLengthError(Exception):
    """Custom exception for password length errors."""

    @classmethod
    def TooShort(cls, min_length: int):
        return cls(f"Password must be at least {min_length} characters long.")

    @classmethod
    def TooLong(cls, max_length: int):
        return cls(f"Password must not exceed {max_length} characters.")
    