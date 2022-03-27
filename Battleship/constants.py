import string


class bcolors:
    # RESET
    reset = f"\033[0;0m"
    # COLORS
    OKCYAN = '\033[96m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    OKGREEN = '\033[92m'
    BRIGHTRED = '\033[91m'
    OKGREY = '\033[90m'
    GREY = '\033[90m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    # STYLE
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    LIGHT = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    # BACKGROUND
    BBLACK = '\033[40m'
    BRED = '\033[41m'
    BGREEN = '\033[42m'
    BYELLOW = '\033[43m'
    BBLUE = '\033[44m'
    BPURPLE = '\033[45m'
    BCYAN = '\033[46m'
    BWHITE = '\033[47m'

# GLOBAl VARIABLES
BACKGROUND = bcolors.BBLACK
HEIGHT = 26
WIDTH = 26
MINSIZE = 2
MAXSIZE = 6
ALPHABET = string.ascii_uppercase
DISPLAYWIDTH = 50
TAB = " " * 50
DIVIDER = "-" * DISPLAYWIDTH
SPACERTOP = "=" * 50
SPACER = "=" * 55
SPACE = " " * 9
MAX_LABEL_SIZE = 9
WARNING = bcolors.RED
POSITIVE = bcolors.OKGREEN
CREDITS_1 = "Hello I'm Andrew, and I want to thank you for playing my Battleship game! This game has taken a ton of time and work to build, so sharing with someone or on social media would be a huge help to me as a creator. " 
CREDITS_2 = "If you're interested in how the game works feel free to look at the code that the main file imports. If you run into issues or have request, let me know via email. my email is andrewholmes011002@gamil.com or shoot me a dm on twitter: @AndrewNerdimo, Thanks again!"
EXIT = f"{TAB}|{SPACERTOP}|\n{TAB}|{WARNING}{'GAME QUIT'.center(DISPLAYWIDTH)}{bcolors.reset}|\n{TAB}|{SPACERTOP}|"
