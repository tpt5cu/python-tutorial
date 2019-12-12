# http://python-history.blogspot.com/2010/08/why-pythons-integer-division-floors.html
# https://stackoverflow.com/questions/3950372/round-with-integer-division


def division():
    '''
    - Regular division with at least one float will result in a float
    - Regular division with only ints will result in an int that is the result of flooring a float
    - Floor division will floor the result, but the type of the result depends on the operands
    '''
    print(5 / 2.6) # 1.92307692308
    print(type(5 / 2.6)) # <type 'float'>
    print(5 / 3) # 1.6667 -> 1
    print(type(5 / 3)) # <type 'int'>
    print(5 // 2.6) # 1.9230769231 -> 1.0
    print(type(5 // 2.6)) # <type 'float'>
    print(5 // 3) # 1.6667 -> 1
    print(type(5 // 3)) # <type 'int'>


def exponentiate():
    print(5 ** 2) # 25
    print(2 ** 5) # 32
    print(2.1 ** 5) # 40.84101


def cast_float_to_int():
    '''
    - A positive float is always floored downward when cast to a int.
    - A negative float is always ceiling-d upward when cast to an int
    - Thus, "casting" and (floor) division have DIFFERENT behavior, since (floor) divison always floors downward
    '''
    # 7 / 4 = 1.75
    print(int(1.75)) # 1
    print(int(-1.75)) # -1
    print(7 / 4) # 1
    print(-7 / 4) # -2


def integer_divison_floors():
    '''
    The floor of a number is the largest integer that is LESS THAN or EQUAL TO the number. Python always floors the result of integer division. 
    - Flooring is not the same thing as rounding. -4.4 rounded to the 1's place is -4. -4.4 floored is -5. 
    '''
    # -22 / 5 = -4.4
    print(-22 / 5) # -5


def mixed_type_operations():
    '''
    Python is not JavaScript. There are only a few confusing cases:
    - The * operator when used with sequence types is a repetition operator, NOT a multiplication operator
    - bool objects can be used in arithmetic contexts. True is 1 and False is 0
    '''
    val = 'yes' * 2 # This is a sequence repetition operator, not an arithemtic multiplication operator
    print(val) # yesyes
    print(1 + True) # 2
    print(True - 10) # -9
    print(1 + False) # 1
    print(False - True) # -1
    #val = 'yes' + 1 # TypeError: cannot concatenate 'str' and 'int' objects
    #val = 'yes' / 2 # TypeError: unsupported operand type(s) for /: 'str' and 'int'
    #val = 'yes' / 'no' # TypeError: unsupported operand type(s) for /: 'str' and 'str' 
    #val = 'yes' ** 2 # TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
    #val = 'yes' - 2 # TypeError: unsupported operand type(s) for -: 'str' and 'int'
    #val = 'yes' - 'no' # unsupported operand type(s) for -: 'str' and 'str'


if __name__ == '__main__':
    #division()
    #exponentiate()
    #cast_float_to_int()
    #integer_divison_floors()
    mixed_type_operations()