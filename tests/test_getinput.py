import pytest
from ..ioutils import getinput, IO__LEFT_PAD, NLBR
from unittest.mock import patch

@pytest.fixture
def mock_input():
    with patch('builtins.input', return_value='Test Input') as mock:
        yield mock

def test_getinput_default(mock_input):
    result = getinput()
    assert result == 'Test Input'

def test_getinput_custom_prompt(mock_input):
    result = getinput(prompt="Enter value:")
    assert result == 'Test Input'

def test_getinput_no_nl(mock_input):
    result = getinput(prompt="Enter:", nl=False)
    assert result == 'Test Input'

def test_getinput_custom_cursor(mock_input):
    result = getinput(cursor="=> ")
    assert result == 'Test Input'

def test_getinput_strip(mock_input):
    mock_input.return_value = '  Test Input  '
    result = getinput()
    assert result == 'Test Input'

def test_getinput_no_strip(mock_input):
    mock_input.return_value = '  Test Input  '
    result = getinput(strip=False)
    assert result == '  Test Input  '

def test_getinput_lower(mock_input):
    mock_input.return_value = 'Test Input'
    result = getinput(lower=True)
    assert result == 'test input'

def test_getinput_empty(mock_input):
    mock_input.return_value = ''
    result = getinput()
    assert result is None