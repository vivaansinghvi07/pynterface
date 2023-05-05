"""
TODO: 
- Input for bounded integer
- Input for specific types
- Input for lists of numbers
- Input for 2-d arrays of numbers
"""

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
