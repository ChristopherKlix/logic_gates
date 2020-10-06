from logic_gates import and_gate, or_gate, nand_gate, nor_gate, xor_gate


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
    
    return int(bin_sum, 2)


def subtract_numbers(input_a, input_b):
    input_values = [input_a, input_b]

    for i in range(len(input_values)):
        # convert to decimals to binary strings
        input_values[i] = f'{input_values[i]:04b}'
        # store individual bin int in list and reverses it
        # therefore list index 0 is base 2^0
        input_values[i] = list(input_values[i])[::-1]

        # convert string bin int to actual int
        for j in range(len(input_values[i])):
            input_values[i][j] = int(input_values[i][j])

    sum = list()
    borrow = 0

    for i in range(4):
        out = xor_gate(input_values[0][i], input_values[1][i])
        
        new_borrow = and_gate(not input_values[0][i], input_values[1][i])
        new_borrow = or_gate(and_gate(not out, borrow), new_borrow)

        out = xor_gate(out, borrow)
        borrow = new_borrow

        print(f'out: {out}, borrow: {new_borrow}')
        sum.append(out)
    
    if borrow == 1:
        sum.append(borrow)
    
    # convert binary sum to decimal integer
    sum = sum[::-1]
    print(sum)
    bin_sum = '0b'
    for i in range(len(sum)):
        bin_sum = bin_sum + str(sum[i])
    print(int(bin_sum, 2))
    
    return int(bin_sum, 2)
