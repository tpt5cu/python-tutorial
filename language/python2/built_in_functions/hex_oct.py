# https://stackoverflow.com/questions/11620151/what-do-numbers-starting-with-0-mean-in-python


def get_hexadecimal_representation():
    print(hex(17)) # 0x11


def get_octal_representation():
    """It's quirky but in Python 2 ONLY, oct() returns an old-style octal representation that is missing a 'o' or "O" after the 0"""
    print(oct(17)) # 021
    print(021 == 0o21) # True


if __name__ == '__main__':
    #get_hexadecimal_representation()
    get_octal_representation()