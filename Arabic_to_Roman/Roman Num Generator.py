# This program allows users to input any Arabic numeral and automatically produce its equivalent in Roman numerals
# (e.g. 25 ---> XXV)


# asks user to input an Arabic numeral
def get_num():
    value = input('Type value to convert to Roman numeral:')
    while True:    # loops indefinitely until user types an integer
        try:
            value = int(value)    # converts input into an integer
            break
        except ValueError:
            value = input('Please type an integer:')
    return value


# converts Arabic numeral from the previous function into Roman numeral
def arab_to_roman():
    v = get_num()    # initializes variable to store the value returned by the previous function
    print('Calculating...')
    result = ''
    while v > 0:    # finds greatest Roman numeral that can fit into value, subtracts it from the value till zero
        if v < 4:
            result += 'I'
            v -= 1
        elif v < 5:
            result += 'IV'
            v -= 4
        elif v < 9:
            result += 'V'
            v -= 5
        elif v < 10:
            result += 'IX'
            v -= 9
        elif v < 40:
            result += 'X'
            v -= 10
        elif v < 50:
            result += 'XL'
            v -= 40
        elif v < 90:
            result += 'L'
            v -= 50
        elif v < 100:
            result += 'XC'
            v -= 90
        elif v < 400:
            result += 'C'
            v -= 100
        elif v < 500:
            result += 'CD'
            v -= 400
        elif v < 900:
            result += 'D'
            v -= 500
        elif v >= 900:
            result += 'CM'
            v -= 900
    print('Your number in Roman numerals:', result)


def main():
    arab_to_roman()


main()