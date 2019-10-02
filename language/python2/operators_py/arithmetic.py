# http://python-history.blogspot.com/2010/08/why-pythons-integer-division-floors.html
# https://stackoverflow.com/questions/3950372/round-with-integer-division


def divide():
    """
    - Division between ints is floor division, regardless of / or //
    - If // is used with at least 1 float, the quotient is floored
    - Division with at least one float is regular division
    - Floor division with at least one float will result in a float that is floored to the next integer value
    """
    print(5 / 4) # 1
    print(5.0 / 4) # 1.25
    print(5 / 4.0) # 1.25
    print(5 // 4) # 1
    print(5.0 // 4) # 1.0 the quotient was floored here. The actual result is 1.25
    print(7.0 // -2) # -4.0 the quotient was floored here. The actual result is -3.5


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
    #divide()
    #exponentiate()
    #cast_float_to_int()
    #integer_divison_floors()
    mixed_type_operations()