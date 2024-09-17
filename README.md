# Pyergo
Pyergo is a Python library designed to facilitate the creation of console-based applications with a focus on user interaction, menu management, and secure password handling. It provides a structured way to build menus, handle user input, and manage user accounts with encryption.

## Features
- **Menu System**: Create and manage complex menu structures with ease.
- **User Input Handling**: Customizable input functions to gather user data securely.
- **Password Management**: Secure password hashing and validation.
- **Encryption**: Built-in support for encrypting and decrypting sensitive data.
- **Testing Support**: Comprehensive test suite using `pytest`.
- **[ ONGOING UPDATES ]**

## Installation
To install Pyergo, you can use pip:

```bash
pip install git+https://github.com/o-namacode/PyErgo.git
```

## Usage Examples

### Creating a Menu

You can create a menu by instantiating the `Menu` class and adding `MenuItem` objects:

```python
from pyergo.console.menu import Menu, MenuItem

def sample_action():
    print("Action executed!")

menu = Menu(title="Main Menu", description="Select an option:")
menu.add(MenuItem(key="option1", description="Execute Sample Action", action=sample_action))

menu.display_menu()
```

### User Input
To get user input, you can use the `getinput` function:

```python
from pyergo.ioutils import getinput

user_response = getinput(prompt="Please enter your name:")
print(f"Hello, {user_response}!")
```

### Password Management
Pyergo provides a `PasswordManager` for hashing and verifying passwords:

```python
from pyergo.pwutils.pwman import PasswordManager

hashed_password = PasswordManager.HashPassword("my_secure_password")
is_valid = PasswordManager.VerifyPassword("my_secure_password", hashed_password)
```

## Testing
To run the tests, use the following command:

```bash
pytest
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Inspired by various console applications and user interaction libraries.
- Thanks to the open-source community for their contributions and support.
```
