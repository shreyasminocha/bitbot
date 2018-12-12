import typing

BITBOT_HOOKS_MAGIC = "__bitbot_hooks"
BITBOT_EXPORTS_MAGIC = "__bitbot_exports"

class IRCColor(object):
    def __init__(self, irc: int, ansi: int, color_bold: bool):
        self.irc = irc
        self.ansi = ansi
        self.color_bold = color_bold
    def ansi_background(self):
        return self.ansi+10

COLOR_NAMES = {}
COLOR_CODES = {}
def _color(name: str, irc: int, ansi: int, color_bold: bool):
    color = IRCColor(irc, ansi, color_bold)
    COLOR_NAMES[name] = color
    COLOR_CODES[irc] = color
    return color

WHITE       = _color("white",       0,  97, False)
BLACK       = _color("black",       1,  30, False)
BLUE        = _color("blue",        2,  34, False)
GREEN       = _color("green",       3,  32, False)
RED         = _color("red",         4,  91, False)
BROWN       = _color("brown",       5,  31, False)
PURPLE      = _color("purple",      6,  35, False)
ORANGE      = _color("orange",      7,  33, False)
YELLOW      = _color("yellow",      8,  93, False)
LIGHTGREEN  = _color("light green", 9,  92, False)
CYAN        = _color("cyan",        10, 36, False)
LIGHTCYAN   = _color("light cyan",  11, 96, False)
LIGHTBLUE   = _color("light blue",  12, 94, False)
PINK        = _color("pink",        13, 95, False)
GREY        = _color("grey",        14, 90, False)
LIGHTGREY   = _color("light grey",  15, 37, False)
TRANSPARENT = _color("transparent", 99, 39, False)

BOLD      = "\x02"
ITALIC    = "\x1D"
UNDERLINE = "\x1F"
INVERT    = "\x16"
COLOR     = "\x03"
RESET     = "\x0F"

ANSI_FORMAT           = "\033[%sm"
ANSI_RESET            = "\033[0m"
ANSI_FOREGROUND_RESET = "\033[39m"
ANSI_BACKGROUND_RESET = "\033[49m"
ANSI_BOLD             = "\033[1m"
ANSI_BOLD_RESET       = "\033[22m"
ANSI_UNDERLINE        = "\033[4m"
ANSI_UNDERLINE_RESET  = "\033[24m"
