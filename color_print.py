import re

# pypi dependency for colored console output
from clint.textui import puts, colored


def color_print(color, string):
    if re.search(r'^blue$', color):
        clint_color = colored.blue(string)
    elif re.search(r'^red$', color):
        clint_color = colored.red(string)
    else:
        return
    puts(clint_color)
