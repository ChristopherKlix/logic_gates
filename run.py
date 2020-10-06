from sys import argv
import re
# dependencies bundled in import file for cleaner code
from imports import *


def main():
    print('[run] [compare] [add] [subtract] [explain] [help]')
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


def set_value(value_name):
    while True:
        value_string = input(f'{value_name}: ')

        # try to convert to int with exception catch
        try:
            value = int(value_string)
            if value in (0, 1):
                break
            else:
                print('Enter a value of [0, 1]')
        except:
            print('Enter valid integer')

    return value


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
    else:
        main()
