from color_print import color_print


def explain():
    color_print('blue', '[AND] [OR] [XOR] [NAND] [NOR]')
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
