# https://docs.python.org/3.7/library/locale.html


import locale


def format_number():
    '''
    locale.format() will format a number argument according to the current LC_NUMERIC setting
    - Now I see why we set the locale in grip.py, but we still shouldn't be setting it inside of a function!
    - This method is depreciated
    '''
    formatted_val = locale.format('%.5d', 1.99)
    #formatted_val = locale.format('%d %f', (1.99, 2.99)) # ValueError: format() must be given exactly one %char format specifier
    print(formatted_val) # 00001


def format_numbers():
    '''format_string() is different from format() because it can take more than one %char format specifier (e.g. %d AND %f)'''
    formatted_val = locale.format_string('%d     %f', (1.99, 2.99))
    print(formatted_val) # 1     2.990000


if __name__ == '__main__':
    #format_number()
    format_numbers()