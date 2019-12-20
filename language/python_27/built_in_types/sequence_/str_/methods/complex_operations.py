# -*- coding: UTF-8 -*-

# https://stackoverflow.com/questions/1207457/convert-a-unicode-string-to-a-string-in-python-containing-extra-symbols - unicode to str
# https://docs.python.org/2.7/library/itertools.html#itertools.permutations


import re, math, itertools


def reverse_sentence_order():
    '''The delimieter that will be used to join the iterable is defined by the invoking string literal. It's very strange, but that's how it works.'''
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


def mix_unicode_and_str():
    '''unicode and str objects can be concatenated to form a unicode object'''
    s = b'hello' + u'world'
    print(type(s)) # <type 'unicode'>
    print(s) # helloworld


def show_permutations(string):
    '''
    Shifting is not sufficient because some letters will always be next to each other
    - Python slicing syntax is very forgiving. Slicing out of bounds or slicing nothing returns ''
    '''
    def create_permutations(str_):
        length = len(str_)
        if length == 1:
            return str_
        permutations = []
        for i in range(length):
            p_subset = [str_[i] + p for p in create_permutations(str_[0:i] + str_[i + 1:])]
            permutations.extend(p_subset)
        return permutations

    permutations = create_permutations(string)
    assert len(permutations) == math.factorial(len(string))
    print(permutations) # ['cat', 'cta', 'act', 'atc', 'tca', 'tac']


def better_show_permutations(string):
    '''The itertools module is incredibly powerful and I should learn it'''
    permutations = [''.join(x) for x in itertools.permutations(string)]
    assert len(permutations) == math.factorial(len(string))
    print(permutations)
        

if __name__ == '__main__':
    #reverse_sentence_order()
    #unicode_to_str()
    #mix_unicode_and_str()
    #get_permutations()
    #show_permutations('cars')
    better_show_permutations('cars')