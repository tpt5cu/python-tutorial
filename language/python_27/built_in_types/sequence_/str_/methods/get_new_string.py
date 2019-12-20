# https://docs.python.org/2/library/stdtypes.html#string-methods - built-in methods on str objects
# https://docs.python.org/2/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange - sequence-type methods that all sequence types (including strings) support
# https://docs.python.org/2/library/string.html - the string module (not same as built-in str)

def strip_():
    '''
    Use <string>.strip() to remove the specified characters from the leading and trailing ends of the string. CAUTION: ALL such specified characters
    will be removed!
    '''
    # The first 'o', the last 'd', and '.omd' will be removed
    string = 'oOoy, what a nice string you created.omd'.strip('.omd')
    print(string)


def rstrip_():
    '''print() automatically inserts a newline, so sometimes it's useful to strip off an existing newline'''
    line = 'This line has a newline\n'
    print(line.rstrip('\n'))
    print('no extra space above')
    

def replace_():
    '''replace() can also take a number specifying the number of time to replace a pattern, starting from the beginning of the string'''
    string = 'This is a cool file/name.txt'
    replacement = string.replace('/', ':')
    print(replacement)


def string_to_list():
    '''
    split() will create a list from a string based on the passed delimiter.
    For each pair of consecutive delimiters in the original string, an empty string is inserted as an element of the new list. 
    '''
    my_string = '1,,2'
    my_list = my_string.split(',')
    print(my_list) # ['1', '', '2']
    # This is a nice trick for ignoring empty strings that were the output of consecutive delimiters
    my_list = [x for x in my_string.split(',') if len(x) != 0]
    print(my_list) # ['1', '2']


def get_individual_lines():
    '''
    split_lines() returns a list of all the lines (deliniated by newlines) in a string literal. It accepts an optional boolean specifying whether or
    not to keep each newline as part of its string in the returned list.
    '''
    my_str = ("This is a string.\nIt has three lines.\nIsn't that cool?")
    str_list = my_str.splitlines()
    print(str_list)


def get_lowercase():
    '''<str>.lower() returns a new string with all capital letters converted into lowercase'''
    string = 'I am a Sentence with Capital letTers'
    print(string.lower())


if __name__ == '__main__':
    strip_()
    rstrip_()
    replace_()
    string_to_list()
    get_individual_lines()
    get_lowercase()