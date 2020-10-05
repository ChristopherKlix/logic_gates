from sys import argv
import re
from logic_gates import and_gate, or_gate, nand_gate, nor_gate, xor_gate
from logic_gate_calculator import add_numbers
from compare import compare
from explain import explain


def main():
    print('[run] [compare] [explain]')
    program = input('program ')
    if 'compare' in program:
        compare()
    elif 'run' in program:
        run()
    elif 'explain' in program:
        explain()


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
            add_numbers()
        else:
            print(f'no argument called [{argv[1]}].')
    else:
        main()
