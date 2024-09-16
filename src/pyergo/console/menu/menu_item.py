from typing import Optional, Union

from ...ioutils.constants import IO__DEFAULT_MAX_WIDTH
from ...exceptions import CommandNotFoundError

from ...ioutils.output import Print, PrintBorder

from .helpers import parse_args
from .stubs import Menu


class MenuItem:
    def __init__(self,
                 key: str,
                 description: str,

                 action: callable,
                 parent: 'Menu',

                 action_args: list = [],

                 help_text: Optional[str] = None,

                 display_condition: Union[callable, bool] = True,
                 display_name: Optional[str] = None,

                 active_condition: Union[callable, bool] = True,
                 ):
        if len(key.split(" ")) > 1:
            cmd, *args = key.split(" ")
            self.key = cmd
            self.action_args = args + action_args
        else:
            self.key = key
            self.action_args = action_args
        self.parent = parent

        self.display_name = display_name or key

        self.description = description
        self.help_text = help_text or self.description
        
        self.action = action

        self.display_condition = display_condition
        self.active_condition = active_condition

        # Validation
        if not callable(self.action):
            raise ValueError("Action must be a callable")
        if not callable(self.display_condition) and not isinstance(self.display_condition, bool):
            raise ValueError("Display condition must be a callable or a boolean")

    def __str__(self):
        return f"{self.key}: {self.display_name} - {self.description}"
    
    @property
    def visible(self) -> bool:
        if callable(self.display_condition):
            return self.display_condition()
        return self.display_condition
    
    @property
    def active (self) -> bool:
        if callable(self.active_condition):
            return self.active_condition()
        return self.active_condition
        


    def execute(self, *args):
        if "-help" in args:
            if 'help' in self.parent.commands:
                self.parent.execute('help', self.key)
            else:
                Print("Command Help".ljust(IO__DEFAULT_MAX_WIDTH, '-'))
                Print(self.help_text)
                input("Press Enter to continue...")
            return

        args, kwargs = parse_args(args)
        
        args = self.action_args + args
        return self.action(*args, **kwargs)

class SystemActionMenuItem (MenuItem):
    CONFIGURED_SYSTEMS_ACTIONS_LIST = [
        'help'
    ]

    def execute(self, *args):
        if self.key == 'help':
            # Command Help
            cmdkey = args[0] or None
            content = ""
            title = ("-" * 5 ) + "  Help  "
            
            if cmdkey:
                # Get help context for specific command
                cmd = self.parent.get(cmdkey)

                if cmd:
                    title += f"-  {cmd.display_name}  "
                    content += cmd.help_text
                else:
                    content += str(CommandNotFoundError())
            else:
                # Get General Help Menu
                pass
            title = title.ljust(IO__DEFAULT_MAX_WIDTH, '-')

            PrintBorder(IO__DEFAULT_MAX_WIDTH)
            Print(title, max_width=IO__DEFAULT_MAX_WIDTH)
            PrintBorder(IO__DEFAULT_MAX_WIDTH)
            Print(content, multiline_str=True, max_width=IO__DEFAULT_MAX_WIDTH)
            PrintBorder()
            input("Press Enter to continue...")
        else:
            return super().execute(*args)

