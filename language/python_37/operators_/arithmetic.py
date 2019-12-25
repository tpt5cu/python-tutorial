# http://python-history.blogspot.com/2010/08/why-pythons-integer-division-floors.html
# https://stackoverflow.com/questions/3950372/round-with-integer-division


def division():
    '''
    - Different from Python 2:
        - Regular divison will always result in a float
    - Same as Python 2:
        - Floor division will floor the result, but the type of the result depends on the operands
    '''
    print(5 / 2.6) # 1.923076923076923
    print(type(5 / 2.6)) # <class 'float'>
    print(4/2) # 2.0
    print(5 / 3) # 1.6666666666666667
    print(type(5 / 3)) # <class 'float'>
    print(5 // 2.6) # 1.0
    print(type(5 // 2.6)) # <class 'float'>
    print(5 // 3) # 1
    print(type(5 // 3)) # <type 'int'>


def exponentiate():
    '''Python 3 has greater floating-point precision across the board'''
    print(5 ** 2) # 25
    print(2 ** 5) # 32
    print(2.1 ** 5) # 40.84101000000001


def cast_float_to_int():
    '''
    Same as Python 2:
    - A positive float is always floored downward when cast to a int.
    - A negative float is always ceiling-d upward when cast to an int
    - Thus, "casting" and floor division have DIFFERENT behavior, since floor divison always floors downward
    '''
    # 7 / 4 = 1.75
    print(int(1.75)) # 1
    print(int(-1.75)) # -1
    print(7 // 4) # 1
    print(-7 // 4) # -2


def mixed_type_operations():
    '''Same as Python 2, except that error messages can be different'''
    val = 'yes' * 2 # This is a sequence repetition operator, not an arithemtic multiplication operator
    print(val) # yesyes
    print(1 + True) # 2
    print(True - 10) # -9
    print(1 + False) # 1
    print(False - True) # -1
    # This is the only one that is different
    val = 'yes' + 1 # TypeError: can only concatenate str (not "int") to str


if __name__ == '__main__':
    division()
    #exponentiate()
    #cast_float_to_int()
    #integer_divison_floors()
    #mixed_type_operations()