"""
TODO:
- Smooth print
- Rainbow text
- Align to center
- Hide cursor, show cursor
"""

import os
import re
from typing import Any
from time import sleep

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

def smooth_print(message: Any, delay: int = 25, end: str = "\n") -> None:
    """
    Prints a message, smoothly.

    Arguments: A message, and delay (in milliseconds), and an optional end. 
    """

    # splits into ascii
    chars = __split_esc_chars(str(message))

    # prints each character with a delay
    for char in chars:
        print(char, end="")
        sleep(delay/1000)

    # prints the end (optional)
    print(end, end="")

def __split_esc_chars(message: str) -> list[str]:
    """
    Splits a message up into characters and escape codes.
    """

    """
    Note: "between" represents characters that are between the ANSI codes.
    """

    char_list = []

    # \033[ followed by a combo of numbers and ; ended with a single letter
    ansi_pattern = "\033\[[0-9|;]*[a-z|A-Z]"

    # get codes and normal things in between
    ansi_codes = re.finditer(ansi_pattern, message)
    matches = [(match.start(), match.end(), match.group()) for match in ansi_codes]

    i = 0
    while i < len(message):

        # check if start is an ansi value
        if len(matches) > 0 and i == matches[0][0]:
            char_list.append(matches[0][2])     # add match
            i = matches[0][1]                   # move index to end of match
            matches.pop(0)                      # get rid of it
        else:
            char_list.append(message[i])        # otherwise add normal char
            i += 1
        
    return char_list