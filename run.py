from sys import argv
from logic_gates import and_gate, or_gate, nand_gate, nor_gate, xor_gate


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


class Option:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.out_and = self.out_or = 0
        self.out_nand = self.out_nor = 0
        self.out_xor = 0


def compare():
    options = [
        Option(0, 0),
        Option(1 ,0),
        Option(0, 1),
        Option(1, 1)
    ]

    for option in options:
        option.out_and = and_gate(option.a, option.b)
        option.out_or = or_gate(option.a, option.b)
        option.out_nand = nand_gate(option.a, option.b)
        option.out_nor = nor_gate(option.a, option.b)
        option.out_xor = xor_gate(option.a, option.b)
    
    print('\n      | and | or  | nand| nor | xor |')

    for option in options:
        print(' ', option.a, option.b, '|', end='')

        print(' ', option.out_and, ' |', end='')
        print(' ', option.out_or, ' |', end='')
        print(' ', option.out_nand, ' |', end='')
        print(' ', option.out_nor, ' |', end='')
        print(' ', option.out_xor, ' |')

    print()


def explain():
    print('[AND] [OR] [NAND] [NOR] [XOR]')
    input_gate = input('gate ')
    if input_gate == 'and':
        print('\n' + '-' * 12)
        print('  AND-gate')
        print('-' * 12)
        print('The AND-gate returns 1 only if both inputs are 1')
        print('        ______                   ')
        print('  A ---|      \           0 0 | 0')
        print('       |  AND  )--- OUT   1 0 | 0')
        print('  B ---|______/           0 1 | 0')
        print('                          1 1 | 1')
        print()
    elif input_gate == 'or':
        print('\n' + '-' * 12)
        print('  OR-gate')
        print('-' * 12)
        print('The OR-gate returns 1 if one OR both inputs are 1')
        print('        ______                   ')
        print('  A ---\      \           0 0 | 0')
        print('        ) OR   )--- OUT   1 0 | 1')
        print('  B ---/______/           0 1 | 1')
        print('                          1 1 | 1')
        print()
    elif input_gate == 'nand':
        print('\n' + '-' * 12)
        print('  NAND-gate')
        print('-' * 12)
        print('The NAND-gate returns the inverse of an AND-gate.')
        print('1 only if both inputs are 1')
        print('        ______                   ')
        print('  A ---\      \           0 0 | 0')
        print('        ) NAND )--- OUT   1 0 | 1')
        print('  B ---/______/           0 1 | 1')
        print('                          1 1 | 1')
        print()
    else:
        print('\n# TODO', end='\n\n')


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


def add_numbers():
    # define constants
    AMOUNT_ADDENDS = 2
    # create a 0-valued list of size AMOUNT_ADDENDS
    # i.e. input_values = [0, 0]
    input_values = [ 0 for i in range(AMOUNT_ADDENDS) ]

    # prompt user for input
    for i in range(AMOUNT_ADDENDS):
        while True:
            input_value = int(input(f'{chr(i + 97)}: '))
            # check if input value is positive
            if input_value < 0:
                print(f'[{input_value}] Found negative integer.')
                print('Only positive inputs are allowed.', end='\n\n')
            # check if input value is 4 bit
            elif len(bin(input_value).lstrip('-0b')) > 4:
                print(f'[{input_value}] Found 5 bit integer.')
                print('Only 4 bit inputs are allowed.', end='\n\n')
            else:
                input_values[i] = input_value
                break

    print(f'decimal values: {input_values}')
    for i in range(AMOUNT_ADDENDS):
        # convert to decimals to binary strings
        input_values[i] = f'{input_values[i]:04b}'
        # store individual bin int in list and reverses it
        # therefore list index 0 is base 2^0
        input_values[i] = list(input_values[i])[::-1]

        # convert string bin int to actual int
        for j in range(len(input_values[i])):
            input_values[i][j] = int(input_values[i][j])
    
    print(f'binary values (reversed): {input_values}')
    # initialize sum and carry
    sum = list()
    carry = 0

    for i in range(4):
        out = xor_gate(input_values[0][i], input_values[1][i])
        out_for_carry = out
        out = xor_gate(out, carry)
        new_carry = and_gate(input_values[0][i], input_values[1][i])
        out_for_carry = and_gate(out_for_carry, carry)
        new_carry = or_gate(new_carry, out_for_carry)

        # reassign carry
        carry = new_carry
        # store calculate out
        sum.append(out)
        print(f'{i} -- a: {input_values[0][i]} b: {input_values[1][i]} out: {out} carry: {carry}')

    if carry == 1:
        sum.append(carry)

    # convert binary sum to decimal integer
    sum = sum[::-1]
    print(sum)
    bin_sum = '0b'
    for i in range(len(sum)):
        bin_sum = bin_sum + str(sum[i])
    print(int(bin_sum, 2))


if __name__ == "__main__":
    if 'compare' in argv:
        compare()
    elif 'run' in argv:
        run()
    elif 'add' in argv:
        add_numbers()
    else:
        main()
