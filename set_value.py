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
