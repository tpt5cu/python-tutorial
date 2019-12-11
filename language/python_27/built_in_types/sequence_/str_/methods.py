# -*- coding: UTF-8 -*-

# https://docs.python.org/2/library/stdtypes.html#string-methods - built-in methods on str objects
# https://docs.python.org/2/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange - sequence-type methods that all sequence types (including strings) support
# https://docs.python.org/2/library/string.html - the string module (not same as built-in str)
# https://stackoverflow.com/questions/1207457/convert-a-unicode-string-to-a-string-in-python-containing-extra-symbols - unicode to str


import re


def strip_py():
    '''
    Use <string>.strip() to remove the specified characters from the leading and trailing ends of the string. CAUTION: ALL such specified characters
    will be removed!
    '''
    # The first 'o', the last 'd', and '.omd' will be removed
    string = 'oOoy, what a nice string you created.omd'.strip('.omd')
    print(string)


def rstrip_py():
    '''print() automatically inserts a newline, so sometimes it's useful to strip off an existing newline'''
    line = 'This line has a newline\n'
    print(line.rstrip('\n'))
    print('no extra space above')
    

def replace_py():
    '''replace() can also take a number specifying the number of time to replace a pattern, starting from the beginning of the string'''
    string = 'This is a cool file/name.txt'
    replacement = string.replace('/', ':')
    print(replacement)


def find_py():
    '''find() returns the index of the substring, or -1 if it isn't found'''
    string = 'Hi there'
    print(string.find('z'))


def equals():
    '''Just use == to compare strings'''
    my_str = 'hello there'
    print(my_str == 'hello there\n') # False
    print(my_str.startswith('hello there\n')) # False
    print(my_str.startswith('hello there')) # True
    print(my_str == 'hello there') # True


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


def check_beginning_and_end():
    '''startswith() and endswith() are neat convenience methods'''
    string = 'I think that coconuts are cool.'
    print(string.startswith('I t')) # True
    print(string.endswith('cool')) # False


def get_lowercase():
    '''<str>.lower() returns a new string with all capital letters converted into lowercase'''
    string = 'I am a Sentence with Capital letTers'
    print(string.lower())


def reverse_sentence_order():
    '''
    The delimieter that will be used to join the iterable is defined by the invoking string literal. It's very strange, but that's how it works.
    '''
    sentence = 'cats like catnip and rubs.'
    my_list = list(reversed(sentence.split(' ')))
    print(my_list) # ['rubs.', 'and', 'catnip', 'like', 'cats']
    reversed_sentence = ' '.join(my_list)
    print(reversed_sentence) # 'rubs. and catnip like cats'

    my_list = list(reversed(re.split(r'\W*', sentence)))
    print(my_list) # ['', 'rubs', 'and', 'catnip', 'like', 'cats']
    reversed_sentence = ' '.join(my_list)
    print(reversed_sentence) # ' rubs and catnip like cats'


def unicode_to_str():
    '''
    There are many ways of doing this. Check the source. Note that regardless of the approach, one of two things must happen to convert a unicode
    object to a str object: 1) drop the unicode characters that cannot be encoded in extended ascii 2) replace those characters with something else
    '''
    a = u'aaaàçççñññ'
    print(type(a)) # <type 'unicode'>
    print(a) # aaaàçççñññ
    print(len(a)) # 10
    b = a.encode('ascii', 'replace')
    print(type(b)) # <type 'unicode'>
    print(b) # aaa???????
    print(len(b)) # 10
    print(ord(b[9])) # 63 is question mark in extended ascii, so the characters really are replaced


if __name__ == '__main__':
    #strip_py()
    #rstrip_py()
    #replace_py()
    #find_py()
    #regex_find()
    #equals()
    #split_py()
    #string_to_list()
    #get_individual_lines()
    #check_beginning_and_end()
    get_lowercase()
    #reverse_sentence_order()
    #unicode_to_str()