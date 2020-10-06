from sys import argv
import re

# local dependencies bundled in import file for cleaner code
from imports import *


'''
If the script is run w/o additional flags (args) in
the command-line, then the main function acts as
a menu.

color_print() is simply a custom print() that allows for easy
colored print statements.

Un-comment the line below if you prefer the default
print color of your console.


help_custom() is called that way, bc help()
is a Python reserved keyword (like print()).

'''


def main():
    color_print('blue', '[run] [compare] [add] [subtract] [explain] [help]')
    # print('[run] [compare] [add] [subtract] [explain] [help]')
    
    program = input('program ')

    if re.search(r'^compare$', program):
        compare()
    elif re.search(r'^run$', program):
        run()
    elif re.search(r'^add$', program):
        out = add_numbers()
        print(f'out: {out}')
    elif re.search(r'^subtract$', program):
        out = subtract_numbers()
        print(f'out: {out}')
    elif re.search(r'^explain$', program):
        explain()
    elif re.search(r'^help$', program):
        help_custom()
        main()
    else:
        print('no such program')
        main()


def run():
    # set input values a and b
    a = set_value('a')
    b = set_value('b')

    # print corresponding state of logic gate
    # using 'ternary'
    output = and_gate(a, b)
    print('AND-gate: ', end=' ')
    print('on' if output else 'off')

    output = or_gate(a, b)
    print('OR-gate: ', end='  ')
    print('on' if output else 'off')

    output = nand_gate(a, b)
    print('NAND-gate: ', end='')
    print('on' if output else 'off')

    output = nor_gate(a, b)
    print('NOR-gate: ', end=' ')
    print('on' if output else 'off')

    output = xor_gate(a, b)
    print('XOR-gate: ', end=' ')
    print('on' if output else 'off')


if __name__ == "__main__":
    if len(argv) == 2:
        if re.search(r'^compare$', argv[1]):
            compare()
        elif re.search(r'^run$', argv[1]):
            run()
        elif re.search(r'^add$', argv[1]):
            out = add_numbers()
            print(f'out: {out}')
        elif re.search(r'^subtract$', argv[1]):
            out = subtract_numbers()
            print(f'out: {out}')
        else:
            print(f'no argument called [{argv[1]}].')

    elif len(argv) > 2:
        color_print('red', 'too many arguments parsed')
    
    else:
        main()
