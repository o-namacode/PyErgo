from typing import Union
from pyergo.ioutils.output import Print, PrintError


class Messenger:
    """
    A class to handle and display messages of various types (success, info, warning, error).

    Attributes:
        messages (dict): A dictionary to store messages categorized by type.
    """

    def __init__(self):
        """
        Initializes the Messenger instance and clears any existing messages.
        """
        self.clear()

    def success(self, message: str):
        """
        Adds a success message to the messages list.

        Args:
            message (str): The success message to be added.
        """
        self.messages['success'].append(message)

    def info(self, message: str):
        """
        Adds an informational message to the messages list.

        Args:
            message (str): The informational message to be added.
        """
        self.messages['info'].append(message)

    def warning(self, message: str):
        """
        Adds a warning message to the messages list.

        Args:
            message (str): The warning message to be added.
        """
        self.messages['warning'].append(message)

    def error(self, message: Union[str, Exception]):
        """
        Adds an error message or exception to the messages list.

        Args:
            message (Union[str, Exception]): The error message or exception to be added.
        """
        self.messages['error'].append(message)
    

    @property
    def has_messages(self) -> bool:
        """
        Checks if there are any messages stored.

        Returns:
            bool: True if there are messages, False otherwise.
        """
        return any(self.messages.values())

    def clear(self):
        """
        Clears all messages from the Messenger instance.
        """
        self.messages = {
            'success': [],
            'info': [],
            'warning': [],
            'error': [],
        }

    def DisplayMessages(self):
        """
        Displays all messages stored in the Messenger instance. 
        Error messages are printed using PrintError, while other messages are printed using Print.
        """
        if not self.has_messages:
            return

        for message_type, messages in self.messages.items():
            for message in messages:
                if message_type == 'error' or isinstance(message, Exception):
                    PrintError(message)
                else:
                    Print(f"{message_type.upper()}:  {message}")