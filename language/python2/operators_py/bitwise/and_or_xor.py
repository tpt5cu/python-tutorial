

def str_and_bitwise():
    """
    Unfortunately, the str type cannot be used with any bitwise operators. How annoying. Therefore, use bitwise operators directly on integers, don't
    even convert to str
    """
    val = bin(9)
    print(type(val)) # <type 'str'>
    print(val) # 0b1001
    #print(val & 1) # TypeError
    print(9 & 1) # 1


if __name__ == '__main__':
    str_and_bitwise()
