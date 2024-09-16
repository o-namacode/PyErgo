# Stub file to resolve circular imports

class Menu:
    def __init__(self, title: str, description: str = None):
        self.title = title
        self.description = description

class MenuItem:
    def __init__(self, key: str, description: str, action: callable, parent: 'Menu'):
        self.key = key
        self.description = description
        self.action = action
        self.parent = parent