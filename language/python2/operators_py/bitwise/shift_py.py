# https://docs.python.org/2.7/library/stdtypes.html#bitwise-operations-on-integer-types
# https://stackoverflow.com/questions/5832982/how-to-get-the-logical-right-binary-shift-in-python


"""
- Logical right shift always shifts in 0s from the left side
- Arithmetic right shift always copies the sign bit when shifting in from the left side
    - Think of it this way: if I was doing arithmetic with negative numbers, I would want to keep the sign bit right?
Python has no built-in logical right shift operator.
"""


def arithmetic_right_shift():
    val = 8 
    print(bin(val)) # 0b1000
    print(val >> 1) # 4


def my_logical_right_shift():
    pass


if __name__ == '__main__':
    arithmetic_right_shift()