from logic_gates import and_gate, or_gate, nand_gate, nor_gate, xor_gate


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
