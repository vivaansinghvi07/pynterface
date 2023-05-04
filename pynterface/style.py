"""
All ANSI codes are adapted from w3schools's ANSI colors reference:
https://www.w3schools.blog/ansi-colors-java
"""

class __ResetMethod:

    @property
    def RESET_ALL(self):
        return "\033[0m"

class __StyleClass(__ResetMethod):

    def __mod(func):
        def new_func(self):
            self.status = func(self)
            return "\033[" + func(self) + ";" + Color.color + "m"
        return property(new_func)
    
    def __init__(self):
        self.status = "0"

    @__mod
    def RESET_STYLE(self): return "0"

    @__mod
    def UNDERLINE(self): return "4"

    @__mod
    def BOLD(self): return "1" 

class __ColorClass(__ResetMethod):
 
    def __mod(func):
        def new_func(self):
            self.color = func(self)
            return "\033[" + Style.status + ";" + func(self) + "m"
        return property(new_func)

    def __init__(self):
        self.color = "0"

    @__mod
    def RESET_COLOR(self): return "0"

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
    def BLACK_BACKGROUND(self): return "40"

    @__mod
    def RED_BACKGROUND(self): return "41"

    @__mod
    def GREEN_BACKGROUND(self): return "42"

    @__mod
    def YELLOW_BACKGROUND(self): return "43"

    @__mod
    def BLUE_BACKGROUND(self): return "44"

    @__mod
    def PURPLE_BACKGROUND(self): return "45"

    @__mod
    def CYAN_BACKGROUND(self): return "46"

    @__mod
    def WHITE_BACKGROUND(self): return "47"

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

    @__mod
    def BLACK_BACKGROUND_BRIGHT(self): return "100"

    @__mod
    def RED_BACKGROUND_BRIGHT(self): return "101"

    @__mod
    def GREEN_BACKGROUND_BRIGHT(self): return "102"

    @__mod
    def YELLOW_BACKGROUND_BRIGHT(self): return "103"

    @__mod
    def BLUE_BACKGROUND_BRIGHT(self): return "104"

    @__mod
    def PURPLE_BACKGROUND_BRIGHT(self): return "105"

    @__mod
    def CYAN_BACKGROUND_BRIGHT(self): return "106"

    @__mod
    def WHITE_BACKGROUND_BRIGHT(self): return "107"


Color = __ColorClass()
Style = __StyleClass()