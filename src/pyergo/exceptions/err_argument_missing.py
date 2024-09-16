class ArgumentMissingError(Exception):
    def __init__(self, argname : str, *args: object) -> None:
        super().__init__(f"Argument `{argname}` missing.")