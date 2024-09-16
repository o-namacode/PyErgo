from os import system
from typing import Callable, Optional, Union, overload

from ...ioutils.constants import IO__DEFAULT_MAX_WIDTH
from ...exceptions import ArgumentMissingError, CommandNotFoundError

from ...ioutils.output import PrintBorder, PrintWithBorder, PrintLines, Print
from ...ioutils.getinput import getinput

from .stubs import MenuItem

class Menu:
    def __init__(
            self,
            title: str,
            description: Optional[str] = None,

            key: Optional[str] = None,
            parent: Optional['Menu'] = None,

            menu_builder: Callable[['Menu'], None] = lambda menu: None,
            menu_items: list[Union[MenuItem, 'Menu']] = [],
            ):
        
        

        # Menu Details
        self.title = title
        self.description = description

        # Menu Elements
        self._builder = menu_builder
        self.menu_items = menu_items

        # Flags
        self.f_top_level = False
        self.f_in_loop = False
        self.f_exit = False
        self.f_submenu = key is not None

        if key:
            self.__key = key

            if parent is None:
                raise ArgumentMissingError('parent')
            
            self.parent = parent

    @property
    def key(self) -> str:
        if hasattr(self,'__key'):
            return self.__key

        return self.title.lower().replace(" ", "_")

    @property
    def issubmenu(self) -> bool:
        return hasattr(self,'__key') and hasattr(self,'parent')


    def clear(self):
        self.menu_items = []
    
    def build(self):
        self._builder(self)

    def reset(self):
        self.clear()
        self.build()
    
    @overload
    def add(self, key: str, description: str, action: Callable, display_condition: Union[bool, Callable] = True) -> 'Menu':
        ...

    @overload
    def add(self, item: MenuItem) -> 'Menu':
        ...
    
    def add(self, item_or_key: Union[str, MenuItem], description: Optional[str] = None, action: Optional[Callable] = None, display_condition: Union[bool, Callable] = True) -> 'Menu':
        if isinstance(item_or_key, MenuItem):
            self.menu_items.append(item_or_key)
        else:
            self.menu_items.append(
                MenuItem(
                    key=item_or_key,
                    description=description,
                    action=action,
                    display_condition=display_condition,
                    parent=self
                )
            )
        return self

    def remove(self, item_or_key: Union[str, MenuItem]) -> 'Menu':
        if isinstance(item_or_key, MenuItem):
            self.menu_items.remove(item_or_key)
        else:
            self.menu_items = [item for item in self.menu_items if item.key != item_or_key]
        return self
    

    @property
    def commands(self) -> list[str]:
        return [item.key for item in self.menu_items if isinstance(item, MenuItem) and item.active]

    @property
    def commands_visible(self) -> list[str]:
        return [item.key for item in self.menu_items if isinstance(item, MenuItem) and item.visible]
        

    def exists(self, key: str) -> bool:
        return key in self.commands
    
    def get(self, key: str) -> Optional[MenuItem]:
        for item in self.menu_items:
            if isinstance(item, MenuItem) and item.key == key:
                return item
        return None

    def execute(self, key: str, *args, **kwargs):
        item = self.get(key)
        if item:
            args = item.action_args + args
            kwargs = {**item.action_kwargs, **kwargs}
            return item.execute(*args, **kwargs)
        else:
            raise CommandNotFoundError(key)
    
    def display_menu(
        self,
        inline: bool = False,
        width: Optional[int] = IO__DEFAULT_MAX_WIDTH,
        sort: bool = True,

        
        ):
        cmd_len = width // 3
        desc_len = width - cmd_len - 1

        items = []

        for item in self.menu_items:
            if isinstance(item, MenuItem):            
                if item.visible:
                    items.append(item)
                    continue

        if sort:
            items = sorted(items, key=lambda x: (x.key in ['logout', 'q', 'exit'], x.key))

        def build_str(a, b, sep = "|"):
            return a.ljust(cmd_len) + sep + " " * 4 + b.ljust(desc_len - 4)

        if not inline:
            if self.title:
                PrintBorder(width=width)
                PrintWithBorder(self.title, width=width)
                PrintBorder(width=width)
                if self.description:
                    PrintWithBorder(self.description, width=width)
                    PrintBorder(width=width)

            if len(items) > 0:
                PrintBorder(width=width)
                PrintWithBorder(build_str("Command", "Description"), width=width)
                PrintBorder(width=width)

            for item in items:
                if isinstance(item, MenuItem) and item.visible:
                    PrintWithBorder(build_str(item.key, item.description), width=width)
            PrintBorder(width=width)
            PrintLines(2)
    
    def loop(
            self,

            display_menu :  bool = True,
            display_available_commands :  bool = True,

            fn_preloop :  callable = lambda: None,
            fn_postloop :  callable = lambda: None,
            fn_loop_step :  callable = lambda: None,

            fn_clear_console :  callable = lambda: system("cls"),

            sort_menu_items :  bool = True,
            ):
        self.f_in_loop = True
        fn_preloop()
        while not self.f_exit:
            fn_clear_console()

            if self.f_exit:
                break

            fn_loop_step()
            if display_menu:
                self.display_menu(
                    inline = False,
                    sort = sort_menu_items,
                )

            if display_available_commands:
                commands_str = "Available commands: " + ", ".join(self.commands)
                Print(commands_str)

            if self.f_exit:
                break

            userinput = getinput(allow_empty = True)
            
            if not userinput:
                continue

            cmd, *args = userinput.split(" ")

            if cmd.lower() in self.commands:
                self.execute(cmd, *args)
            else:
                Print(f"Command not found: {userinput}")


        fn_postloop()
        self.f_in_loop = False


