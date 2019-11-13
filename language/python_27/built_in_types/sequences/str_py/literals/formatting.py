# https://pyformat.info/ - There is an insane amount of formatting customization


def pad_and_align_string():
    """
    - Use {:num} to set the length of a substring inside of a string.
    - Use {:<num} to explicitly align the substring to the left. (default)
    - Use {:>num} to explicitly align the substring to the right.
    - Use {:^num} to explicitly align the substring to the center. If there is an uneven amount of padding, the right side gets 1 extra character of
      padding
    - Use {:char<num} to select the character to be used for padding. The alignment specifier (e.g. '<') must be present.
    - Add the "0" character in front of the length specifier to zero-pad a string from the left

    If the length specifier is less than the actual substring, it is ignored.
    """
    val = "Austin"
    print("\"{:10}\"".format(val))
    print("\"{:<10}\"".format(val))
    print("\"{:>10}\"".format(val))
    print("\"{:^10}\"".format(val))
    print("\"{:_<10}\"".format(val))
    print("\"{:2}\"".format(val))
    print("{:010}".format(22))


def truncate_string():
    """
    - Use {:.num} to truncate a string to certain amount of characters
    """
    print("{:.8}".format("interesting"))
    print("interesting"[3:]) # This is just to show how to get the last 8 characters instead of the first 8
    print("{:_^10.8}".format("interesting")) # Combine truncation, padding, and alignment


def truncate_number():
    """
    Python formats numbers differently from strings.
    When a precision is specified:
    - For a string it means the number of characters not including "."
    - For a number it means the number of digits after the "." place
    """
    pie = 3.141592653
    print("{:.3}".format(pie)) # Apparently, Python ignores "." when calculating the precision for string types
    print("{:.3f}".format(pie))


def decimal_and_float():
    """
    - A floating point number cannot be formatted as a decimal. Cast the floating point number to a decimal instead.
    - A decimal number can be formatted as a floating point number. For some reason, 6 zeros are added to the decimal number.
    """
    #print("{:2d}".format(5.12345)) # illegal
    print("{:06.3f}".format(5.12345))
    print("{:f}".format(12))
    print("{:08.3f}".format(5.12345)) # A floating point number can be left-padded with 0s, but the specified length must be longer than the floating point number
    

def get_rid_of_scientific_notation():
    val = 1.56332825753e+12
    print(val) # Don't want this
    formatted_val = '%d' % val
    print(formatted_val) # This is great!


if __name__ == "__main__":
    #inserting_variables()
    #pad_and_align_string()
    #truncate_string()
    #truncate_number()
    #decimal_and_float()
    get_rid_of_scientific_notation()