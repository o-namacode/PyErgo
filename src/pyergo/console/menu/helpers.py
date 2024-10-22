from typing import Any


def parse_args(args : tuple[Any]) :
    """
    Parse the arguments for a MenuItem execution.
    """
    _args, _kwargs = [], {}

    # Convert args to Generator Type
    g_args = (arg for arg in args)

    for arg in g_args:
        if "=" in arg:
            key, value = arg.split("=")
            _kwargs[key] = value
        elif arg.startswith("-"):
            # Set the flag to True
            _kwargs[arg[1:]] = True
        elif arg.startswith("--"):
            # Set the value to the next arg
            try:
                _kwargs[arg[2:]] = next(g_args)
            except StopIteration:
                raise ValueError(f"Missing value for argument: {arg}")
        else:
            _args.append(arg)

    return _args, _kwargs