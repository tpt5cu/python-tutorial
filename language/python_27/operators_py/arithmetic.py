# http://python-history.blogspot.com/2010/08/why-pythons-integer-division-floors.html
# https://stackoverflow.com/questions/3950372/round-with-integer-division


def division():
    '''
    - Regular division with at least one float will result in a float
    - Regular division with only ints will result in an int that is the result of flooing a float
    - Floor division will maintain the type of the result as regular division
    '''
    print(5 / 2.6) # 1.9...
    print(type(5 / 2.6)) # <type 'float'>
    print(5 / 3) # 1.6... -> 1
    print(type(5 / 3)) # <type 'int'>
    print(5 // 2.6) # 1.0
    print(type(5 // 2.6)) # <type 'float'>
    print(5 // 3) # 1.6... -> 1
    print(type(5 // 3)) # <type 'int'>


def exponentiate():
    print(5 ** 2) # 25
    print(2 ** 5) # 32
    print(2.1 ** 5) # 40.84101


def cast_float_to_int():
    """
    A positive float is always floored downward when cast to a int. A negative float is always ceiling-d upward when cast to an int
    - Thus, casting an division have DIFFERENT behavior
    """
    f = 2.999
    i = int(f)
    print(i) # 2
    f = -4.999
    i = int(f)
    print(i) # -4


def integer_divison_floors():
    """
    The floor of a number is the largest integer that is LESS THAN or EQUAL TO the number. Python always floors the result of integer division. 
    - Flooring is not the same thing as rounding. -4.4 rounded to the 1's place is -4. -4.4 floored is -5. 
    """
    quotient = -22/float(5)
    print(quotient) # -4.4
    quotient = -22/5
    print(quotient) # -5


def mixed_type_operations():
    """
    Python is not JavaScript. There are only a few confusing cases:
    - The * operator when used with sequence types is a repetition operator, NOT a multiplication operator
    - bool objects can be used in arithmetic contexts. True is 1 and False is 0
    """
    #val = "yes" + 1 # TypeError. str and int cannot be concatenated
    val = "yes" * 2 # This is a sequence repetition operator, not an arithemtic multiplication operator
    print(val) # yesyes
    #val = "yes" / 2 # TypeError. / does not support str type
    #val = "yes" / "no" # TypeError. Same as above
    #val = "yes" ** 2 # TypeError. ** does not support str type
    #val = "yes" - 2 # TypeError. - does not support str type
    #val = "yes" - "no" # TypeError. Same as above
    val = 1 + True
    print(val) # 2
    val = True - 10
    print(val) # -9
    val = 1 + False
    print(val) # 1
    val = False - True
    print(val) # -1


if __name__ == "__main__":
    division()
    #exponentiate()
    #cast_float_to_int()
    #integer_divison_floors()
    #mixed_type_operations()