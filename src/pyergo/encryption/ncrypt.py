from hashlib import pbkdf2_hmac
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
import base64
import os


class EnCrypt:
    SALT_SIZE = 16

    @staticmethod
    def generate_key(hashed_password: str, salt: bytes) -> bytes:
        """
        Generate a key from a hashed password using PBKDF2.

        Args:
            hashed_password (str): The hashed password to use as a base for the key.
            salt (bytes): Salt for key derivation.

        Returns:
            bytes: The generated key.
        """
        kdf = pbkdf2_hmac(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(hashed_password.encode()))
        return key

    @staticmethod
    def encrypt(message: str, hashed_password: str) -> bytes:
        """
        Encrypt a message using a key derived from the hashed password.

        Args:
            message (str): The message to encrypt.
            hashed_password (str): The hashed password to use for encryption.

        Returns:
            bytes: The salt and encrypted message combined.
        """
        salt = os.urandom(EnCrypt.SALT_SIZE)
        key = EnCrypt.generate_key(hashed_password, salt)
        f = Fernet(key)
        encrypted_message = f.encrypt(message.encode())
        return salt + encrypted_message

    @staticmethod
    def decrypt(encrypted_data: bytes, hashed_password: str) -> str:
        """
        Decrypt a message using a key derived from the hashed password and salt.

        Args:
            encrypted_data (bytes): The salt and encrypted message combined.
            hashed_password (str): The hashed password used for encryption.

        Returns:
            str: The decrypted message.
        """
        salt = encrypted_data[:EnCrypt.SALT_SIZE]
        encrypted_message = encrypted_data[EnCrypt.SALT_SIZE:]
        key = EnCrypt.generate_key(hashed_password, salt)
        f = Fernet(key)
        decrypted_message = f.decrypt(encrypted_message)
        return decrypted_message.decode()