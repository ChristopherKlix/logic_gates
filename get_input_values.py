def get_input_values():
    # define constants
    AMOUNT = 2
    # create a 0-valued list of size AMOUNT
    # i.e. input_values = [0, 0]
    input_values = [ 0 for i in range(AMOUNT) ]

    # prompt user for input
    for i in range(AMOUNT):
        while True:
            input_value = int(input(f'{chr(i + 97)}:   '))
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
    
    return input_values
