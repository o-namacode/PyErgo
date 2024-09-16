import pytest
from unittest.mock import Mock

from pyergo.console.menu import Menu, MenuItem
from pyergo.exceptions.err_commmand_not_found import CommandNotFoundError

@pytest.fixture
def menu():
    return Menu(title="Main Menu", description="This is the main menu.")

def test_menu_initialization(menu):
    assert menu.title == "Main Menu"
    assert menu.description == "This is the main menu."
    assert menu.menu_items == []

def test_add_menu_item(menu):
    action = Mock()
    item = MenuItem(key="item1", description="First item", action=action, parent=menu)
    menu.add(item)
    assert len(menu.menu_items) == 1
    assert menu.menu_items[0] == item

def test_add_menu_item_by_key(menu):
    action = Mock()
    menu.add(key="item2", description="Second item", action=action)
    assert len(menu.menu_items) == 1
    assert menu.menu_items[0].key == "item2"

def test_remove_menu_item(menu):
    action = Mock()
    item = MenuItem(key="item1", description="First item", action=action, parent=menu)
    menu.add(item)
    menu.remove(item)
    assert len(menu.menu_items) == 0

def test_remove_menu_item_by_key(menu):
    action = Mock()
    item = MenuItem(key="item1", description="First item", action=action, parent=menu)
    menu.add(item)
    menu.remove("item1")
    assert len(menu.menu_items) == 0

def test_execute_menu_item(menu):
    action = Mock()
    item = MenuItem(key="item1", description="First item", action=action, parent=menu)
    menu.add(item)
    menu.execute("item1")
    action.assert_called_once()

def test_execute_nonexistent_item(menu):
    with pytest.raises(CommandNotFoundError, match="Command `nonexistent` Not Found."):
        menu.execute("nonexistent")

def test_commands_property(menu):
    action = Mock()
    item1 = MenuItem(key="item1", description="First item", action=action, parent=menu)
    item2 = MenuItem(key="item2", description="Second item", action=action, parent=menu)
    menu.add(item1)
    menu.add(item2)
    assert menu.commands == ["item1", "item2"]

def test_display_menu(menu, capsys):
    action = Mock()
    item = MenuItem(key="item1", description="First item", action=action, parent=menu)
    menu.add(item)
    menu.display_menu()
    captured = capsys.readouterr()
    assert "Command" in captured.out
    assert "Description" in captured.out
    assert "item1" in captured.out
    assert "First item" in captured.out