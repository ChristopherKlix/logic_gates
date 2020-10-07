from logic_gates import and_gate, or_gate, nand_gate, nor_gate, xor_gate
from get_input_values import get_input_values
import re


def add_numbers():
    print_instructions('add')

    input_values = get_input_values()

    for i in range(len(input_values)):
        # convert to decimals to binary strings
        input_values[i] = f'{input_values[i]:04b}'
        # store individual bin int in list and reverses it
        # therefore list index 0 is base 2^0
        input_values[i] = list(input_values[i])[::-1]

        # convert string bin int to actual int
        for j in range(len(input_values[i])):
            input_values[i][j] = int(input_values[i][j])

    # initialize out_sum and carry
    out_sum = list()
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
        out_sum.append(out)

    if carry == 1:
        out_sum.append(carry)

    # convert binary out_sum to decimal integer
    out_sum = out_sum[::-1]
    bin_sum = '0b'
    for i in range(len(out_sum)):
        bin_sum = bin_sum + str(out_sum[i])
    
    return int(bin_sum, 2)


def subtract_numbers():
    print_instructions('subtract')

    input_values = get_input_values()

    for i in range(len(input_values)):
        # convert to decimals to binary strings
        input_values[i] = f'{input_values[i]:04b}'
        # store individual bin int in list and reverses it
        # therefore list index 0 is base 2^0
        input_values[i] = list(input_values[i])[::-1]

        # convert string bin int to actual int
        for j in range(len(input_values[i])):
            input_values[i][j] = int(input_values[i][j])

    out_difference = list()
    borrow = 0

    for i in range(4):
        out = xor_gate(input_values[0][i], input_values[1][i])
        
        new_borrow = and_gate(not input_values[0][i], input_values[1][i])
        new_borrow = or_gate(and_gate(not out, borrow), new_borrow)

        out = xor_gate(out, borrow)
        borrow = new_borrow

        out_difference.append(out)
    
    if borrow == 1:
        out_difference.append(borrow)
    
    # convert binary sum to decimal integer
    out_difference = out_difference[::-1]
    bin_difference = '0b'
    for i in range(len(out_difference)):
        bin_difference = bin_difference + str(out_difference[i])
    
    return int(bin_difference, 2)


def print_instructions(operation):
    if re.search(r'^add$', operation):
        print('\n  ' + '-' * 30)
        print('  add two numbers')
        print('  ' + '-' * 30)
        print('  this is a 4 bit \'full adder\'')
        print('  only 4 bit inputs allowed')
        print('  no negative numbers supported')
        print('\n  ----------\n  a - b = out', end='\n\n')
    elif re.search(r'^subtract$', operation):
        print('\n  ' + '-' * 30)
        print('  subtract two numbers')
        print('  ' + '-' * 30)
        print('  this is a 4 bit \'full subtractor\'')
        print('  only 4 bit inputs allowed')
        print('  no negative numbers supported')
        print('\n  ----------\n  a - b = out', end='\n\n')
