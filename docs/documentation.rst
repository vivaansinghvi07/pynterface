Documentation
#############

Here is the documentation for Pynterface!

Text Styling and Coloring
+++++++++++++++++++++++++

This is simply an alternative to `colorama <https://github.com/tartley/colorama>`, which I attempted to replicate, for fun, with this part of the package! It includes the additional ability to set custom RGB values, or custom colors with custom RGB values.

You can import this module using:

.. code:: python

    import pynterface.style

    # import individual classes
    from pynterface.style import Color, Background, Text 

For a quick demonstration of the different presets supported, you can call the following:

.. code:: python

    from pynterface.style import demo
    demo()  # prints presets and the ways to call them

Preset Options
--------------

For the :code:`Text` class, which manages text styles, here are the preset values and their corresponding ANSI codes:

.. code:: python

    RESET_ALL =     "\033[0m"
    RESET_STYLE =   "\033[22m"

    BOLD =          "\033[1m"
    DIM =           "\033[2m"
    ITALIC =        "\033[3m"
    UNDERLINE =     "\033[4m"
    BLINKING =      "\033[5m"
    INVERTED =      "\033[7m"
    STRIKETHROUGH = "\033[9m"

    HIDE_CURSOR =   "\033[?25l"
    SHOW_CURSOR =   "\033[?25h"

For the :code:`Color` class, which manages the color of text, here are the preset values and their codes:

.. code:: python

    RESET_COLOR =   "\033[39m"
    RESET_ALL =     "\033[0m"

    BLACK =     "\033[30m"
    RED =       "\033[31m"
    GREEN =     "\033[32m"
    YELLOW =    "\033[33m"
    BLUE =      "\033[34m"
    PURPLE =    "\033[35m"
    CYAN =      "\033[36m"
    WHITE =     "\033[37m"

    BLACK_BRIGHT =     "\033[90m"
    RED_BRIGHT =       "\033[91m"
    GREEN_BRIGHT =     "\033[92m"
    YELLOW_BRIGHT =    "\033[93m"
    BLUE_BRIGHT =      "\033[94m"
    PURPLE_BRIGHT =    "\033[95m"
    CYAN_BRIGHT =      "\033[96m"
    WHITE_BRIGHT =     "\033[97m"

For the :code:`Background` class, which manages the background of the text, here are the supported presets and their codes:

.. code:: python

    RESET_BACKGROUND =  "\033[49m"
    RESET_ALL =         "\033[0m"

    BLACK =     "\033[40m"
    RED =       "\033[41m"
    GREEN =     "\033[42m"
    YELLOW =    "\033[43m"
    BLUE =      "\033[44m"
    PURPLE =    "\033[45m"
    CYAN =      "\033[46m"
    WHITE =     "\033[47m"

    BLACK_BRIGHT =     "\033[100m"
    RED_BRIGHT =       "\033[101m"
    GREEN_BRIGHT =     "\033[102m"
    YELLOW_BRIGHT =    "\033[103m"
    BLUE_BRIGHT =      "\033[104m"
    PURPLE_BRIGHT =    "\033[105m"
    CYAN_BRIGHT =      "\033[106m"
    WHITE_BRIGHT =     "\033[107m"

Text Styles
-----------

Here are what the different text styles look like, and how you call them:

.. image:: imgs/text-demo.png
    :width: 300

The :code:`Text.BLINKING`, which cannot be displayed in an image, produces blinking text.

You can also move the cursor up, down, left, and right, as follows:

.. code:: python

    Text.MOVE_CURSOR_UP(lines: int = 1)
    Text.MOVE_CURSOR_DOWN(lines: int = 1)
    Text.MOVE_CURSOR_LEFT(cols: int = 1)
    Text.MOVE_CURSOR_RIGHT(cols: int = 1)

Colors
------

Here are what the different colors look like and how you call them:

.. image:: imgs/colors-demo.png
    :width: 300

You can also call a custom RGB color, in the following format:

.. code:: python

    Color.RGB(rgb: tuple[int, int, int])

Or, you can set a color and call it later on,

.. code:: python

    Color.SET(name: str, rgb: tuple[int, int, int])

Here is an example:

.. image:: imgs/custom-colors-demo.png
    :width: 800
    
Backgrounds
-----------

Here are what the different background colors are, and how you call them:

.. image:: imgs/background-demo.png
    :width: 300

You can also call a custom RGB background, in the following format:

.. code:: python

    Background.RGB(rgb: tuple[int, int, int])

Or, you can set a color and call it later on,

.. code:: python

    Background.SET(name: str, rgb: tuple[int, int, int])

Here is an example:

.. image:: imgs/custom-background-demo.png
    :width: 800

Menu Templates
++++++++++++++

Import this subsection of the module using the following:

.. code:: python

    import pynterface.menu
    
    # for individual menus
    from pynterface.menu import numbered_menu, list_menu
    from pynterface import numbered_menu, list_menu

Numbered Menu
-------------

.. code:: python

    >>> option = numbered_menu(['option_1', 'option_2', 'option_3'])
        1. option_1
        2. option_2
        3. option_3
    Please enter a number between 1 and 3: 2
    >>> print(option)
    option_2

You can call this with the following:

.. code:: python

    numbered_menu(options: Iterable[Any], 
                  beginning_prompt: str = None, 
                  selection_prompt: str = None, 
                  spacing: int = 4, 
                  return_number: bool = False) -> Any:

The options is an Iterable containing things that either have a :code:`__name__`` attribute or can be converted to strings. By default, values that are :code:`bool, str, float, int, object` are converted to strings using the :code:`str()` function; on anything else the :code:`__name__` method is attempted to be used. Therefore, these can be functions, classes, or even modules.

The beginning prompt is what gets displayed initially, before the menu is shown. By default, nothing is printed.

The selection prompt is what is printed to prompt the user to choose a number. By default, it is "Please enter a number between <lower> and <upper>".

The spacing is the indentation for each option. It is set to 4 by default.

If return_number is True, the returned value will be the chosen number, rather than the option. Otherwise, it will return the option that was chosen.

List Menu
---------

.. code:: python

    >>> option = list_menu([int, float, str])
        - int
        - float
        - str
    Enter your choice: float
    >>> print(option)
    <class 'float'>

You can call this using the following:

.. code:: python 

    list_menu(options: Iterable[Any], 
              beginning_prompt: str = None, 
              selection_prompt: str = "Enter your choice: ",
              error_prompt: str = "Invalid choice, enter a valid one: ",
              spacing: int = 4, 
              selector: str = '-') -> Any:

The options and beginning prompt are used in the same manner as they are in the numbered list just above.

The selection prompt is, again, what is displayed to obtain a choice. It is defaulted to "Enter your choice: ".

The error prompt is what is printed when an invalid name is entered.

The spacing is the margin of the list, defaulted to 4.

The selector is the thing that indicates each option, like bullets in a bulleted list.

Input Methods
+++++++++++++

Import this subsection of the module using the following:

.. code:: python

    import pynterface.input
    
    # for individual menus
    from pynterface.input import bounded_int, two_dim_array
    from pynterface import bounded_int, two_dim_array 

Bounded Integer
---------------

.. code:: python

    >>> option = bounded_int(lower=2, upper=9)
    Please enter a number between 2 and 9: 10
    The number must be between 2 and 9: no
    You must enter an integer: 7
    >>> option
    7

.. code:: python

    bounded_int(lower: int, 
                upper: int, 
                prompt: str = None, 
                type_error: str = None, 
                bounds_error: str = None) -> int

:code:`lower` and :code:`upper` are the lower and upper bounds for the integer, both inclusive.

The :code:`prompt` is what asks for the user input, and is defaulted to "Please enter a number between <lower> and <upper>: ".

The :code:`type_error` is what is printed when the number cannot eb converted to an integer. It is defaulted to "You must enter an integer: ".

The :code:`bounds_error` is what is printed when a number is out of bounds. It is defaulted to "The number must be between <lower> and <upper>: ".

Two-Dimensional Array
---------------------

.. code:: python

    >>> from pynterface import two_dim_array
    >>> arr = two_dim_array(rows=2, cols=3, item_type=int)
    3 5 1
    4 7 21
    >>> arr
    [[3, 5, 1], [4, 7, 21]]

.. code:: python

    two_dim_array(rows: int, 
                  cols: int = None, 
                  delimiter: str = " ", 
                  item_type: int = str) -> list[list[Any]]

:code:`rows` and :code:`cols` represent the rows and columns of the 2d array respectively. If you leave columns as blank, there will be no checking for accurately sized columns.

:code:`delimiter` is the thing that seperates each item in a row. You can enter :code:`''` as a delimeter if you want to seperate characters in a string. 

:code:`item_type` is the type of each element. You can pass in things like :code:`int` or :code:`float` to automatically convert each item.

Yes/No Input
------------

.. code:: python

    >>> ans = yes_no("Yes or no? ")
    Yes or no? Okay
    Invalid choice; enter a proper form of yes or no: Yes 
    >>> ans
    True

.. code:: python

    yes_no(prompt: str, 
           error_prompt: str = "Invalid choice; enter a proper form of yes or no: ") -> bool:

The supported options for yes and no respectively are shown below:

.. code:: python

    yes = ['yes', 'y', '1']
    no = ['no', 'n', '0']

:code:`prompt` is what you enter as the prompt for your input.

:code:`error_prompt` is what is printed when an invalid choice in entered, prompting the user for another choice.