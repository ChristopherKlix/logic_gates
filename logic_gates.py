def and_gate(input_a, input_b):
    return 1 if input_a and input_b else 0


def or_gate(input_a, input_b):
    return 1 if input_a or input_b else 0


def nand_gate(input_a, input_b):
    return 0 if and_gate(input_a, input_b) else 1


def nor_gate(input_a, input_b):
    return 0 if or_gate(input_a, input_b) else 1


def xor_gate(input_a, input_b):
    return 1 if not input_a == input_b else 0
