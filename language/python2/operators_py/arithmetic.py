"""
http://python-history.blogspot.com/2010/08/why-pythons-integer-division-floors.html
https://stackoverflow.com/questions/3950372/round-with-integer-division
"""


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


def exponentiate():
    print(5 ** 2) # 25
    print(2 ** 5) # 32
    print(2.1 ** 5) # 40.84101


def float_to_int():
    """ A float is always towards its integer value when cast to an int """
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


if __name__ == "__main__":
    #divide()
    #exponentiate()
    #float_to_int()
    integer_divison_floors()