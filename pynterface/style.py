"""
All ANSI codes are adapted from w3schools's ANSI colors reference:
https://www.w3schools.blog/ansi-colors-java

This is my attempt to reproduce colorama's implementation!
Combinations of styles (backgrounds, colors, and text styles) are possible.
This version includes the ability to modify RGB values of colors.
"""

class Text:

    """
    This class stores information about editing text styles.
    """

    RESET_ALL =     "\033[0m"
    RESET_STYLE =   "\033[22m"

    BOLD =          "\033[1m"
    DIM =           "\033[2m"
    ITALIC =        "\033[3m"
    UNDERLINE =     "\033[4m"
    BLINKING =      "\033[5m"
    INVERTED =      "\033[7m"
    STRIKETHROUGH = "\033[9m"

class Background:

    """
    This class stores information about modifying the background color.
    """

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

    def RGB(r: int, g: int, b: int) -> str:

        """
        Returns the ANSI escape code for a background color in RGB.
        """

        for var in [r, g, b]:
            assert isinstance (var, int) and 0 <= var <= 256, "Invalid RGB value!"
        return f"\033[48;2;{r};{g};{b}m"
    
class Color:

    """
    This class stores information about modifying the foreground color (color of text)
    """

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

    def RGB(r: int, g: int, b: int) -> str:

        """
        Returns the ANSI escape code for a text color in RGB.
        """

        for var in [r, g, b]:
            assert isinstance (var, int) and 0 <= var <= 256, "Invalid RGB value!"
        return f"\033[38;2;{r};{g};{b}m"

def demo():

    """
    A simple demonstration of the different colors supported.
    """

    # prints examples for each property of the color classes
    def printing_loop(var):
        for name in dir(var):
            if name[0] != "_" and "RESET" not in name and "RGB" not in name:
                modifier = getattr(var, name)
                print(f"{modifier}{name}{var.RESET_ALL}")

    # test cases for normal color properties
    print(f"{Text.BOLD}Colors:{Text.RESET_STYLE}")
    printing_loop(Color)
    print(f"{Text.BOLD}Backgrounds:{Text.RESET_STYLE}")
    printing_loop(Background)
    print(f"{Text.BOLD}Text Styles:{Text.RESET_STYLE}")
    printing_loop(Text)

    # test cases for rgb colors
    print(f"{Color.RGB(100, 150, 200)}Color.rgb_color(100, 150, 200){Text.RESET_ALL}")
    print(f"{Background.RGB(200, 100, 100)}Background.rgb_color(200, 100, 100)")

if __name__ == "__main__":
    demo()