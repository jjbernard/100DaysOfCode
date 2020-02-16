from unittest.mock import patch
from . import ask_user_for_input

@patch("builtins.input", side_effect=['1950', '5', '3'])
def test_ask_user_for_input():
    assert ask_user_for_input() == (1950, 5, 3)