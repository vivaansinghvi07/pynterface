"""
TODO: 
- Input for bounded integer
- Input for specific types
- Input for lists of numbers
- Input for 2-d arrays of numbers
"""
from typing import Any, Iterable

def __map_to_str(opt):
    if isinstance(opt, (bool, str, float, int)):
        return str(opt)
    try:
        return opt.__name__
    except:
        raise AssertionError("Option type unable to be converted to string using __name__.")


def bounded_int(lower: int, upper: int, prompt: str = None, 
                type_error: str = None, bounds_error: str = None) -> int:
    """
    Forces the user to return an integer between the two entered values.

    Arguments: A lower and an upper bound for the integers. An optional prompt.

    Raises: An AssertionError if the types of each the lower and upper bound are not integers, or is the upper bound si not greater than the lower

    Returns: The correct integer that the user inputs.
    """

    assert isinstance(lower, int), f"Lower bound must be an integer, not '{type(lower)}'."
    assert isinstance(upper, int), f"Upper bound must be an integer, not '{type(upper)}'."
    assert upper > lower, "Upper bound must be greater than lower bound."

    if not prompt:
        prompt = f"Please enter a number between {lower} and {upper}: "

    if not type_error:
        type_error = "You must enter an integer: "

    if not bounds_error:
        bounds_error = f"The number must be between {lower} and {upper}: "

    user_input = (lower - 1) / 1    # convert to float
    flag_type_error = False
    while not (lower <= user_input <= upper):
        try:
            if isinstance(user_input, float):       # get first input
                user_input = int(input(prompt))
            elif flag_type_error:
                user_input = int(input(type_error))     
                flag_type_error = False
            else:
                user_input = int(input(bounds_error))
        except:
            user_input = lower - 1      # reset to a set out of bounds value
            flag_type_error = True

    return user_input

def __list_print(prompt: str, spacing: int, str_options: list) -> None:
    """
    Prints menu options and beginning prompt.
    """

    if prompt:
        print(prompt)

    for index, opt in enumerate(str_options):
        print(f"{' '*spacing}{index+1}. {opt}")

def numbered_menu(options: Iterable[Any], beginning_prompt: str = None, 
                  end_prompt: str = None, spacing: int = 4) -> Any:

    """
    Creates a numbered menu, in the following format:
    ```
    '''
    <prompt>
        1. Option
        2. Option
        3. Option
    Please enter a number between {lower} and {upper}:
    '''
    ```
    Arguments: The list of options to enter, which can include things like classes, functions, or simple datatypes. An optional prompt, and an optional spacing value (how many spaces the options are intended by).

    Raises: An AssertionError for incompatible types.

    Returns: The choice selected by the user.
    """

    assert isinstance(options, Iterable), "Options must be iterable!"
    assert len(options) >= 2, "There should be at least two values to select from!"
    assert isinstance(spacing, int) and spacing >= 0, "Spacing must be a non-negative integer!"

    str_options = list(map(__map_to_str, options))

    __list_print(prompt=beginning_prompt, spacing=spacing, str_options=str_options)
    
    choice = bounded_int(1, len(str_options), prompt=end_prompt)

    return options[choice - 1]

def list_menu(options: Iterable[Any], beginning_prompt: str = None, 
              end_prompt: str = "Enter your choice: ",
              error_prompt: str = "Invalid chocie; enter a valid one: ",
              spacing: int = 4, selector: str = '-') -> Any:

    """
    Creates a numbered menu, in the following format:
    ```
    '''
    <prompt>
        - Option
        - Option
        - Option
    Please enter yor option:
    '''
    ```
    Arguments: The list of options to enter, which can include things like classes, functions, or simple datatypes. An optional prompt, and an optional spacing value (how many spaces the options are intended by).

    Raises: An AssertionError for incompatible types.

    Returns: The choice selected by the user.
    """
    
    assert isinstance(options, Iterable), "Options must be iterable!"
    assert len(options) >= 2, "There should be at least two values to select from!"
    assert isinstance(spacing, int) and spacing >= 0, "Spacing must be a non-negative integer!"
    assert isinstance(selector, str), "List element introducer must be a string!"

    str_options = list(map(__map_to_str, options))

    __list_print(prompt=beginning_prompt, spacing=spacing, str_options=str_options)

    choice = input(end_prompt)

    while choice.strip() not in str_options:
        choice = input(error_prompt)

    return options[str_options.index(choice)]

def two_dim_array(rows: int, cols: int, delimiter: str = " ") -> list[list[Any]]:
    pass
