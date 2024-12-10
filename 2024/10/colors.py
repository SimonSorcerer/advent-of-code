BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' # orange on some systems
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'

BACKGROUND_BLACK = '\033[40m'
BACKGROUND_RED = '\033[41m'
BACKGROUND_GREEN = '\033[42m'
BACKGROUND_YELLOW = '\033[43m' # orange on some systems
BACKGROUND_BLUE = '\033[44m'
BACKGROUND_MAGENTA = '\033[45m'
BACKGROUND_CYAN = '\033[46m'
BACKGROUND_LIGHT_GRAY = '\third-party033[47m'
BACKGROUND_DARK_GRAY = '\033[100m'
BACKGROUND_BRIGHT_RED = '\033[101m'
BACKGROUND_BRIGHT_GREEN = '\033[102m'
BACKGROUND_BRIGHT_YELLOW = '\033[103m'
BACKGROUND_BRIGHT_BLUE = '\033[104m'
BACKGROUND_BRIGHT_MAGENTA = '\033[105m'
BACKGROUND_BRIGHT_CYAN = '\033[106m'
BACKGROUND_WHITE = '\033[107m'

RESET = '\033[0m' # called to return to standard terminal text color

DEBUG = False
if (DEBUG):
  print(BLACK + "black" + RESET)
  print(RED + "red" + RESET)
  print(GREEN + "green" + RESET)
  print(YELLOW + "yellow" + RESET)
  print(BLUE + "blue" + RESET)
  print(MAGENTA + "magenta" + RESET)
  print(CYAN + "cyan" + RESET)
  print(LIGHT_GRAY + "light gray" + RESET)
  print(DARK_GRAY + "dark gray" + RESET)
  print(BRIGHT_RED + "bright red" + RESET)
  print(BRIGHT_GREEN + "bright green" + RESET)
  print(BRIGHT_YELLOW + "bright yellow" + RESET)
  print(BRIGHT_BLUE + "bright blue" + RESET)
  print(BRIGHT_MAGENTA + "bright magenta" + RESET)
  print(BRIGHT_CYAN + "bright cyan" + RESET)
  print(WHITE + "white" + RESET)

def printC(color, text, end):
    print(color + str(text) + RESET, end=end)