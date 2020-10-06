from logic_gates import and_gate, or_gate, nand_gate, nor_gate, xor_gate
from set_value import set_value


def try_custom():
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

    output = xor_gate(a, b)
    print('XOR-gate: ', end=' ')
    print('on' if output else 'off')

    output = nand_gate(a, b)
    print('NAND-gate: ', end='')
    print('on' if output else 'off')

    output = nor_gate(a, b)
    print('NOR-gate: ', end=' ')
    print('on' if output else 'off')
