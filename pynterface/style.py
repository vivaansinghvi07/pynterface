"""
All ANSI codes are adapted from w3schools's ANSI colors reference:
https://www.w3schools.blog/ansi-colors-java

This is my attempt to reproduce colorama's implementation!
"""

class __ResetMethod:

    @property
    def RESET_ALL(self):
        return "\033[0m"

class __TextClass(__ResetMethod):

    def __mod(func):
        def new_func(self):
            self._status = func(self)
            return "\033[" + func(self) + ";" + Color._status + ";" + Background._status + "m"
        return property(new_func)
    
    def __init__(self):
        self._status = "0"

    @__mod
    def RESET_STYLE(self): return "0"

    @__mod
    def UNDERLINE(self): return "4"

    @__mod
    def BOLD(self): return "1" 

    @__mod
    def STRIKETHROUGH(self): return "9"

class __BackGroundClass(__ResetMethod):
    def __mod(func):
        def new_func(self):
            self._status = func(self)
            return "\033[" + Text._status + ";" + Color._status + ";" + func(self) + "m"
        return property(new_func)
    
    def __init__(self):
        self._status = "49"

    @__mod
    def RESET_BACKGROUND(self): return "49"

    @__mod
    def BLACK(self): return "40"

    @__mod
    def RED(self): return "41"

    @__mod
    def GREEN(self): return "42"

    @__mod
    def YELLOW(self): return "43"

    @__mod
    def BLUE(self): return "44"

    @__mod
    def PURPLE(self): return "45"

    @__mod
    def CYAN(self): return "46"

    @__mod
    def WHITE(self): return "47"

    @__mod
    def BLACK_BRIGHT(self): return "100"

    @__mod
    def RED_BRIGHT(self): return "101"

    @__mod
    def GREEN_BRIGHT(self): return "102"

    @__mod
    def YELLOW_BRIGHT(self): return "103"

    @__mod
    def BLUE_BRIGHT(self): return "104"

    @__mod
    def PURPLE_BRIGHT(self): return "105"

    @__mod
    def CYAN_BRIGHT(self): return "106"

    @__mod
    def WHITE_BRIGHT(self): return "107"
    

class __ColorClass(__ResetMethod):
 
    def __mod(func):
        def new_func(self):
            self._status = func(self)
            return "\033[" + Text._status + ";" + func(self) + ";" + Background._status + "m"
        return property(new_func)

    def __init__(self):
        self._status = "39"

    @__mod
    def RESET_COLOR(self): return "39"

    @__mod
    def BLACK(self): return "30"
    
    @__mod
    def RED(self): return "31"
        
    @__mod
    def GREEN(self): return "32"
    
    @__mod
    def YELLOW(self): return "33"
    
    @__mod
    def BLUE(self): return "34"
    
    @__mod
    def PURPLE(self): return "35"
    
    @__mod
    def CYAN(self): return "36"
    
    @__mod
    def WHITE(self): return "37"

    @__mod
    def BLACK_BRIGHT(self): return "90"
    
    @__mod
    def RED_BRIGHT(self): return "91"
        
    @__mod
    def GREEN_BRIGHT(self): return "92"
    
    @__mod
    def YELLOW_BRIGHT(self): return "93"
    
    @__mod
    def BLUE_BRIGHT(self): return "94"
    
    @__mod
    def PURPLE_BRIGHT(self): return "95"
    
    @__mod
    def CYAN_BRIGHT(self): return "96"
    
    @__mod
    def WHITE_BRIGHT(self): return "97"



Color = __ColorClass()
Text = __TextClass()
Background = __BackGroundClass()

if __name__ == "__main__":

    print(f"{Text.BOLD}Colors:{Text.RESET_STYLE}")

    # demo code for colors
    for name in dir(Color):
        if name[0] != "_":
            color_modifier = getattr(Color, name)
            print(f"{color_modifier}{name}{Color.RESET_COLOR}")

    print(f"{Text.BOLD}Backgrounds:{Text.RESET_STYLE}")

    # demo code for styles
    for name in dir(Background):
        if name[0] != "_":
            text_modifier = getattr(Background, name)
            print(f"{text_modifier}{name}{Background.RESET_BACKGROUND}")

    print(f"{Text.BOLD}Text Styles:{Text.RESET_STYLE}")

    # demo code for styles
    for name in dir(Text):
        if name[0] != "_":
            text_modifier = getattr(Text, name)
            print(f"{text_modifier}{name}{Text.RESET_STYLE}")

    print(f"{Color.BLUE}{Text.BOLD}{Background.RED_BRIGHT}You can also have a combination of all!{Color.RESET_ALL}")