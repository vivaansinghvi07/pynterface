"""
TODO:
- Smooth print
- Rainbow text
- Align to center
- Hide cursor, show cursor
"""

import os
from typing import Any

def clear_window() -> None:
    """
    Clears the terminal window.
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def clear_print(message: Any, end: str = "\n") -> None:
    """
    Clears the terminal window and prints the prompt.
    """
    clear_window()
    print(message, end=end)
