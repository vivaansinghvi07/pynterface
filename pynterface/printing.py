"""
TODO:
- Smooth print
- Rainbow text
- Align to center
- Hide cursor, show cursor
- Gradient
"""

import os
import re
from copy import deepcopy as copy
from typing import Any, Iterable
from time import sleep

# \033[ followed by a combo of numbers and ; ended with a single letter
__ANSI_PATTERN = "\033\[[0-9|;]*[a-z|A-Z]"
__CENTERED_FORBIDDEN_CHARS = "[\t]"
__UNIQUE_CHAR_LENGTHS = {
    "\b": -1
}

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
        if re.search(__ANSI_PATTERN, message) == None:    # delay only if ansi
            sleep(delay/1000)       
        print(char, end="")
        
    # prints the end (optional)
    print(end, end="")

def centered(messages: list[str], margin: int = 2) -> str:
    """
    Centers several lines of text.
    """
    
    assert isinstance(messages, Iterable), "Messages must be iterable."
    assert isinstance(margin, int), "Margin must be an integer."

    msgs = copy(messages)

    # preprocessing to split newlines into two and remove forbidden characters
    for i in range(len(msgs)-1, -1, -1):
        line = re.sub(__CENTERED_FORBIDDEN_CHARS, '', msgs[i]).strip()  # remove forbidden characters and strip whitespace
        if "\n" in line:
            msgs = msgs[0:i] + line.split('\n') + msgs[i+1:]
        else:
            msgs[i] = line  # different kinds of line replacement

    # calculate the lengths of each segment
    lens = [sum([1 if c in __UNIQUE_CHAR_LENGTHS else __UNIQUE_CHAR_LENGTHS[c] for c in line]) for line in msgs]
    max_len = max(lens)

    # prints lines and adds whitespace
    for line, ln in zip(msgs, lens):
        print((margin + ln//max_len)*" " + line)


def __split_esc_chars(message: str) -> list[str]:
    """
    Splits a message up into characters and escape codes.
    """

    """
    Note: "between" represents characters that are between the ANSI codes.
    """

    char_list = []

    # get codes and normal things in between
    ansi_codes = re.finditer(__ANSI_PATTERN, message)
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