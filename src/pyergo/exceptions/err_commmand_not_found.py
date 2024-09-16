class CommandNotFoundError(Exception):
    def __init__(self, command : str, *args: object) -> None:
        super().__init__(f"Command `{command}` Not Found.")