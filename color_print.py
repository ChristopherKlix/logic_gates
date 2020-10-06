import re


r'''
If the input color string matches one of the pre-defined
colors, then the string is converted into a
ANSI colored string.

Format f'\033[XXm{string}\033[XXm'

\033 is an escape character (same as \e)
e.g. \010 is the escape character for newline (\n) or 'EOF'
This is why this doc-string starts with an 'r',
which indicates a 'raw' string without formatting.
Otherwise \n would literally print a new line if
this string would be printed.


When using \033 the next character is [ which indicates
the start of a 'command'

XXm is the command for a string format (such as color)
34m is defined as blue
32m is defined as green
1m is defined as blinking (such as a prompt) etc.

see https://misc.flogisoft.com/bash/tip_colors_and_formatting
for a detailed list.


If the re.search can't find a match, the parsed
string won't be altered.

Last, print() prints the string.

'''


def color_print(color, string):
    if re.search(r'^red$', color):
        colored_string = f'\033[31m{string}\033[00m'
    elif re.search(r'^green$', color):
        colored_string = f'\033[32m{string}\033[00m'
    elif re.search(r'^yellow$', color):
        colored_string = f'\033[33m{string}\033[00m'
    elif re.search(r'^blue$', color):
        colored_string = f'\033[34m{string}\033[00m'
    elif re.search(r'^magenta$', color):
        colored_string = f'\033[35m{string}\033[00m'
    elif re.search(r'^cyan$', color):
        colored_string = f'\033[36m{string}\033[00m'
    elif re.search(r'^light_gray$', color):
        colored_string = f'\033[37m{string}\033[00m'
    elif re.search(r'^dark_gray$', color):
        colored_string = f'\033[90m{string}\033[00m'
    elif re.search(r'^light_red$', color):
        colored_string = f'\033[91m{string}\033[00m'
    elif re.search(r'^light_green$', color):
        colored_string = f'\033[92m{string}\033[00m'
    elif re.search(r'^light_yellow$', color):
        colored_string = f'\033[93m{string}\033[00m'
    elif re.search(r'^light_blue$', color):
        colored_string = f'\033[94m{string}\033[00m'
    elif re.search(r'^light_magenta$', color):
        colored_string = f'\033[95m{string}\033[00m'
    elif re.search(r'^light_cyan$', color):
        colored_string = f'\033[96m{string}\033[00m'
    elif re.search(r'^white$', color):
        colored_string = f'\033[97m{string}\033[00m'
    
    print(colored_string)


def print_color_options():
    color_print('red', 'red')
    color_print('green', 'green')
    color_print('yellow', 'yellow')
    color_print('blue', 'blue')
    color_print('magenta', 'magenta')
    color_print('cyan', 'cyan')
    color_print('light_gray', 'light_gray')
    color_print('dark_gray', 'dark_gray')
    color_print('light_red', 'light_red')
    color_print('light_green', 'light_green')
    color_print('light_yellow', 'light_yellow')
    color_print('light_blue', 'light_blue')
    color_print('light_magenta', 'light_magenta')
    color_print('light_cyan', 'light_cyan')
    color_print('white', 'white')
