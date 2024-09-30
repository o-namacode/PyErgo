from os import system
from typing import Callable, Optional, Union, overload

from ...exceptions.err_commmand_not_found import CommandNotFoundError

from ...ioutils.constants import IO__DEFAULT_MAX_WIDTH
from ...exceptions.err_argument_missing import ArgumentMissingError

from ...ioutils.output import PrintBorder, PrintWithBorder, PrintLines, Print
from ...ioutils.getinput import getinput

from .stubs import MenuItem

class Menu:
    """
    A class to create and manage a menu system.

    Attributes:
        title (str): The title of the menu.
        description (Optional[str]): A description of the menu.
        menu_items (list[Union[MenuItem, 'Menu']]): The items in the menu.
        f_top_level (bool): Flag indicating if the menu is a top-level menu.
        f_in_loop (bool): Flag indicating if the menu is currently in a loop.
        f_exit (bool): Flag indicating if the menu should exit.
        f_submenu (bool): Flag indicating if the menu is a submenu.
        parent (Optional['Menu']): The parent menu if this is a submenu.
    """

    def __init__(
            self,
            title: Optional[str] = None,
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
        """
        Returns the unique key for the menu, generated from the title if not provided.

        Returns:
            str: The unique key for the menu.
        """
        if hasattr(self,'__key'):
            return self.__key

        return self.title.lower().replace(" ", "_")

    @property
    def issubmenu(self) -> bool:
        """
        Checks if the menu is a submenu.

        Returns:
            bool: True if the menu is a submenu, False otherwise.
        """
        return hasattr(self,'__key') and hasattr(self,'parent')


    def clear(self):
        """
        Clears all menu items from the menu.
        """
        self.menu_items = []
    
    def build(self):
        """
        Builds the menu using the provided menu builder function.
        """
        self._builder(self)

    def reset(self):
        """
        Resets the menu by clearing and rebuilding it.
        """
        self.clear()
        self.build()
    
    @overload
    def add(self, key: str, description: str, action: Callable, display_condition: Union[bool, Callable] = True) -> 'Menu':
        """
        Overloaded method to add a menu item using key, description, action, and display condition.
        """
        ...

    @overload
    def add(self, item: MenuItem) -> 'Menu':
        """
        Overloaded method to add a MenuItem directly.
        """
        ...
    
    def add(self, item_or_key: Union[str, MenuItem], description: Optional[str] = None, action: Optional[Callable] = None, display_condition: Union[bool, Callable] = True) -> 'Menu':
        """
        Adds a menu item or a key to the menu.

        Args:
            item_or_key (Union[str, MenuItem]): The key or MenuItem to add.
            description (Optional[str]): Description of the menu item.
            action (Optional[Callable]): Action to execute when the item is selected.
            display_condition (Union[bool, Callable]): Condition for displaying the item.

        Returns:
            Menu: The current menu instance.
        """
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
        """
        Removes a menu item by key or MenuItem.

        Args:
            item_or_key (Union[str, MenuItem]): The key or MenuItem to remove.

        Returns:
            Menu: The current menu instance.
        """
        if isinstance(item_or_key, MenuItem):
            self.menu_items.remove(item_or_key)
        else:
            self.menu_items = [item for item in self.menu_items if item.key != item_or_key]
        return self
    

    @property
    def commands(self) -> list[str]:
        """
        Returns a list of active command keys from the menu items.

        Returns:
            list[str]: List of active command keys.
        """
        return [item.key for item in self.menu_items if isinstance(item, MenuItem) and item.active]

    @property
    def commands_visible(self) -> list[str]:
        """
        Returns a list of visible command keys from the menu
        """
        return [item.key for item in self.menu_items if isinstance(item, MenuItem) and item.visible]
        
    def commands_str(self, sort: bool = False) -> str:
        """
        Generates a string representation of the commands.

        Args:
            sort (bool): Whether to sort the commands.

        Returns:
            str: String representation of the commands.
        """
        cmds = []
        # Logic to generate command strings
        if sort:
            cmds = sorted(self.commands)
        else:
            cmds = self.commands
        return ", ".join(cmds)

    def exists(self, key: str) -> bool:
        """
        Checks if a command exists in the menu.

        Args:
            key (str): The command key to check.

        Returns:
            bool: True if the command exists, False otherwise.
        """
        return key in self.commands

    def get(self, key: str) -> Optional[MenuItem]:
        """
        Retrieves a MenuItem by its key.

        Args:
            key (str): The command key.

        Returns:
            Optional[MenuItem]: The MenuItem if found, None otherwise.
        """
        for item in self.menu_items:
            if isinstance(item, MenuItem) and item.key == key:
                return item
        return None

    def execute(self, key: str, *args, **kwargs):
        """
        Executes the action associated with a command key.

        Args:
            key (str): The command key.
            *args: Additional arguments for the action.
            **kwargs: Additional keyword arguments for the action.

        Returns:
            Any: The result of the action execution.

        Raises:
            CommandNotFoundError: If the command key does not exist.
        """
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
            fn_loop_step_after_menu :  callable = lambda: None,

            fn_clear_console :  callable = lambda: system("cls"),
            clear_console : bool = True,

            sort_menu_items :  bool = True,
            ):
        self.f_in_loop = True
        fn_preloop()
        while not self.f_exit:
            if clear_console:
                fn_clear_console()

            if self.f_exit:
                break

            fn_loop_step()
            if display_menu:
                self.display_menu(
                    inline = False,
                    sort = sort_menu_items,
                )

            fn_loop_step_after_menu()

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


    def add_quit_option(self):
        self.add("q", "Exit the current menu.", self.exit)