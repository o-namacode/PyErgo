# Stub file to resolve circular imports

class Menu:
    """
    Represents a menu with a title and an optional description.
    
    Attributes:
        title (str): The title of the menu.
        description (str): An optional description of the menu.
    """
    def __init__(self, title: str, description: str = None):
        self.title = title
        self.description = description

class MenuItem:
    """
    Represents an item in a menu.
    
    Attributes:
        key (str): The key associated with the menu item.
        description (str): A description of the menu item.
        action (callable): The action to be executed when the item is selected.
        parent (Menu): The parent menu that contains this item.
    """
    def __init__(self, key: str, description: str, action: callable, parent: 'Menu'):
        self.key = key
        self.description = description
        self.action = action
        self.parent = parent