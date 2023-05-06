"""
All ANSI codes are adapted from w3schools's ANSI colors reference:
https://www.w3schools.blog/ansi-colors-java

This is my attempt to reproduce colorama's implementation!
Combinations of styles (backgrounds, colors, and text styles) can be combined.
"""

class _BaseClass:

    def _modify(func):
        def new_func(self):
            return "\033[" + func(self) + "m"
        return property(new_func)

    @property
    def RESET_ALL(self):
        Color.__init__()
        Background.__init__()
        Text.__init__()
        return "\033[0m"

class __TextClass(_BaseClass):
    
    def __init__(self):
        self._status = "0"

    @_BaseClass._modify
    def RESET_STYLE(self): return "0"

    @_BaseClass._modify
    def BOLD(self): return "1" 

    @_BaseClass._modify
    def DIM(self): return "2"

    @_BaseClass._modify
    def ITALIC(self): return "3"

    @_BaseClass._modify
    def UNDERLINE(self): return "4"

    @_BaseClass._modify
    def BLINKING(self): return "5"

    @_BaseClass._modify
    def INVERTED(self): return "7"

    @_BaseClass._modify
    def STRIKETHROUGH(self): return "9"

class __BackGroundClass(_BaseClass):
    
    def __init__(self):
        self._status = "49"

    @_BaseClass._modify
    def RESET_BACKGROUND(self): return "49"

    @_BaseClass._modify
    def BLACK(self): return "40"

    @_BaseClass._modify
    def RED(self): return "41"

    @_BaseClass._modify
    def GREEN(self): return "42"

    @_BaseClass._modify
    def YELLOW(self): return "43"

    @_BaseClass._modify
    def BLUE(self): return "44"

    @_BaseClass._modify
    def PURPLE(self): return "45"

    @_BaseClass._modify
    def CYAN(self): return "46"

    @_BaseClass._modify
    def WHITE(self): return "47"

    @_BaseClass._modify
    def BLACK_BRIGHT(self): return "100"

    @_BaseClass._modify
    def RED_BRIGHT(self): return "101"

    @_BaseClass._modify
    def GREEN_BRIGHT(self): return "102"

    @_BaseClass._modify
    def YELLOW_BRIGHT(self): return "103"

    @_BaseClass._modify
    def BLUE_BRIGHT(self): return "104"

    @_BaseClass._modify
    def PURPLE_BRIGHT(self): return "105"

    @_BaseClass._modify
    def CYAN_BRIGHT(self): return "106"

    @_BaseClass._modify
    def WHITE_BRIGHT(self): return "107"

    def rgb_color(self, r, g, b):
        for var in [r, g, b]:
            assert isinstance (var, int) and 0 <= var <= 256, "Invalid RGB value!"
        return f"\033[48;2;{r};{g};{b}m"

class __ColorClass(_BaseClass):

    def __init__(self):
        self._status = "39"

    @_BaseClass._modify
    def RESET_COLOR(self): return "39"

    @_BaseClass._modify
    def BLACK(self): return "30"
    
    @_BaseClass._modify
    def RED(self): return "31"
        
    @_BaseClass._modify
    def GREEN(self): return "32"
    
    @_BaseClass._modify
    def YELLOW(self): return "33"
    
    @_BaseClass._modify
    def BLUE(self): return "34"
    
    @_BaseClass._modify
    def PURPLE(self): return "35"
    
    @_BaseClass._modify
    def CYAN(self): return "36"
    
    @_BaseClass._modify
    def WHITE(self): return "37"

    @_BaseClass._modify
    def BLACK_BRIGHT(self): return "90"
    
    @_BaseClass._modify
    def RED_BRIGHT(self): return "91"
        
    @_BaseClass._modify
    def GREEN_BRIGHT(self): return "92"
    
    @_BaseClass._modify
    def YELLOW_BRIGHT(self): return "93"
    
    @_BaseClass._modify
    def BLUE_BRIGHT(self): return "94"
    
    @_BaseClass._modify
    def PURPLE_BRIGHT(self): return "95"
    
    @_BaseClass._modify
    def CYAN_BRIGHT(self): return "96"
    
    @_BaseClass._modify
    def WHITE_BRIGHT(self): return "97"

    def rgb_color(self, r, g, b):
        for var in [r, g, b]:
            assert isinstance (var, int) and 0 <= var <= 256, "Invalid RGB value!"
        return f"\033[38;2;{r};{g};{b}m"

Color = __ColorClass()
Text = __TextClass()
Background = __BackGroundClass()

if __name__ == "__main__":

    # prints examples for each property of the color classes
    def printing_loop(var):
        for name in dir(var):
            if name[0] != "_" and "RESET" not in name and "rgb" not in name:
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
    print(f"{Color.rgb_color(100, 150, 200)}Color.rgb_color(100, 150, 200){Text.RESET_ALL}")
    print(f"{Background.rgb_color(200, 100, 100)}Background.rgb_color(200, 100, 100)")