# dependencies for run.py
# bundled in import file for cleaner code
from imports import *


'''
If the script is run w/o additional flags (args) in
the command-line, then the main function acts as
a menu.

color_print() is simply a custom print() that allows for easy
colored print statements.

Change the color to 'default' if you prefer the default
print color of your command-line. Or simply change
it to the default print() function.


help_custom() is called that way, bc help()
is a Python reserved keyword (like print()).

'''


def main():
    color_print('blue', '[try] [compare] [add] [subtract] [explain] [help] [quit]')
    
    program = input('program ')

    if re.search(r'^compare$', program):
        compare()
    elif re.search(r'^try$', program):
        try_custom()
    elif re.search(r'^add$', program):
        out = add_numbers()
        print(f'out: {out}', end='\n\n')
    elif re.search(r'^subtract$', program):
        out = subtract_numbers()
        print(f'out: {out}', end='\n\n')
    elif re.search(r'^explain$', program):
        explain()
    elif re.search(r'^help$', program):
        help_custom()
        main()
    elif re.search(r'^quit$', program):
        print('\n  Thanks for using logic_gates!', end='\n\n')
        exit(0)
    else:
        print('no such program')
        main()


if __name__ == "__main__":
    if len(argv) == 2:
        if re.search(r'^compare$', argv[1]):
            compare()
        elif re.search(r'^run$', argv[1]):
            try_custom()
        elif re.search(r'^add$', argv[1]):
            out = add_numbers()
            print(f'out: {out}', end='\n\n')
        elif re.search(r'^subtract$', argv[1]):
            out = subtract_numbers()
            print(f'out: {out}', end='\n\n')
        else:
            print(f'no argument called [{argv[1]}].')

    elif len(argv) > 2:
        color_print('red', 'too many arguments parsed')
    
    else:
        main()
