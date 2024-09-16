from typing import Union
from pyergo.ioutils.output import Print, PrintError


class Messenger:
    def __init__(self):
        self.clear()

    def success(self, message: str):
        self.messages['success'].append(message)

    def info(self, message: str):
        self.messages['info'].append(message)

    def warning(self, message: str):
        self.messages['warning'].append(message)

    def error(self, message: Union[str, Exception]):
        self.messages['error'].append(message)
    

    @property
    def has_messages(self) -> bool:
        return any(self.messages.values())

    def clear(self):
        self.messages = {
            'success': [],
            'info': [],
            'warning': [],
            'error': [],
        }

    def DisplayMessages(self):
        if not self.has_messages:
            return

        for message_type, messages in self.messages.items():
            for message in messages:
                if message_type == 'error' or isinstance(message, Exception):
                    PrintError(message)
                else:
                    Print(f"{message_type.upper()}:  {message}")