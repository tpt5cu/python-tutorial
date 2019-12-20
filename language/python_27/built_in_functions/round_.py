# https://docs.python.org/2/library/functions.html#round


def round_to_ones():
    '''
    If no precision is specified, it defaults to 0 (i.e. round to the one's place)
    - Technically, a zero-precision number shouldn't have any zeros after the decimal point, but such a floating-point literal would look weird
    '''
    print(round(7.66)) # 8.0
    print(round(-7.5, 1)) # -7.5
    print(round(-7.5, 0)) # -8.0


def round_to_precision():
    '''The round() function rounds to a given precision, NOT a number of significant figures'''
    print(round(1111.54321, 3)) # 1111.543


def round_away_from_zero():
    '''For round(<val>, <precision>), if two multiples of 10^(-<precision>) are equally close to <val>, then rounding is done away from zero'''
    # 10^0 = 1, so 7.5 rounded to the one's place (away from zero) is 8.0
    print(round(7.5, 0)) # 8.0
    # 10^0 = 1, so -7.5 rounded to the one's place (away from zero) is -8.0
    print(round(-7.5, 0)) # -8.0


def inherent_float_representation_limitations():
    '''
    You would think that rounding 2.675 to the hundreth's place would yield 2.68 (according to the above function), but it doesn't. If our work ever
    becomes so important that utilities care about rounding errors, then this will actually be a problem.
    - Just like in base 10, in base 2 certain fractions can only be expressed as repeating decimals
    - A computer must use a finite number of bits to store a repeating decimal, so the actual binary decimal number always has a true value that is
      slightly LESS than the mantissa of a floating point number
    - When a floating-point number is rounded, Python is rounding the exact binary decimal number, not the approximate representation that is shown to
      humans
    - This inherent limitation is why doing operations with floating-point numbers can yield crazy-long decimals
    - Use the "decimal" module if I need more precise treatment of decimal fractions
    '''
    # 2.675 is stored as 2.67499999999999982236431605997495353221893310546875, which when rounded to the hundreth's place is 2.67, NOT 2.68
    print(round(2.675, 2)) # 2.67


def round_with_negative_precision():
    '''
    Rounding with a negative precision means to round to the ten's place or greater:
    - -1: round to ten's place (i.e. the ten's place IS the last position of precision)
    - -2: round to hundred's place (i.e. the hundred's place IS the last position of precision)
    - etc.
    '''
    print(round(1111, -1)) # 1110.0
    print(round(1111, -2)) # 1100.0
    # If you round to the ten's place, look at the digit to the right of the ten's place (e.g. 5), determine whether or not the ten's place should
    # change, then set everything after the ten's place to 0
    print(round(5.0, -1)) # 10.0
    # The hundred's place is 0, so look at the ten's place and see that the ten's place is also 0, therefore the hundred's place remains 0
    print(round(5.0, -2)) # 0.0


def round_int():
    '''Python doesn't show sig figs well, but ints can be rounded just as if they were floats'''
    # This should techically be 5.00 to indicate 3 sig figs
    print(round(5, 3)) # 5.0
    print(round(5, -2)) # 0.0


if __name__ == '__main__':
    round_to_ones()
    #round_to_precision()
    #round_away_from_zero()
    #inherent_float_representation_limitations()
    #round_with_negative_precision()
    #round_int()