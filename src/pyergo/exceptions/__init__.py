class CommandNotFoundError(Exception):
    def __init__(self, command : str, *args: object) -> None:
        super().__init__(f"Command `{command}` Not Found.")
class ArgumentMissingError(Exception):
    def __init__(self, argname : str, *args: object) -> None:
        super().__init__(f"Argument `{argname}` missing.")
