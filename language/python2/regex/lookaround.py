# https://www.rexegg.com/regex-disambiguation.html#lookarounds


import re


'''
The most important thing to remember is: a lookaround does not move the parser
- lookarounds in Python must be fixed width. PYTHON re DOES NOT ALLOW VARIABLE WIDTH LOOKAROUNDS!!!
- (?=foo): lookahead
- (?!foo): negative lookahead
- (?<=foo): lookbehind
- (?<!foo): negative lookbehind
'''


def succeeding_lookahead():
    '''Match the first 3 digits, then look ahead from the third digit to confirm that the characters " dollars" follow the match'''
    string = '100 dollars'
    mo = re.search(r'\d+(?= dollars)', string)
    print(mo.group()) # 100


def preceeding_lookahead():
    '''
    Assert that at the current position in the string (the very beginning before the first character), what follows is some number of digits and "
    dollars". Provided that is true, the engine then matches the digits with \d+.
    - This is less efficient than the succeeding_lookahead because \d+ is matched twice
    '''
    string = '100 dollars'
    mo = re.search(r'(?=\d+ dollars)\d+', string)
    print(mo.group()) # 100


def preceeding_lookbehind():
    '''
    At the current position in the string, assert that the characters "USD" come beforehand, then try to match 3 digits 
    - Note that the parser has to move forward a little bit before it succeeds in finding a match, but that's fine
    '''
    string = 'USD100'
    mo = re.search(r'(?<=USD)\d{3}', string)
    print(mo.group()) # 100


def succeeding_lookbehind():
    '''
    Find 3 digits. Then from that position, assert that the 6 earlier characters were "USD\d{3}"
    - This is less efficient than the preceeding_lookbehind because \d{3} is matched twice
    '''
    string = 'USD100'
    mo = re.search(r'\d{3}(?<=USD\d{3})', string)
    print(mo.group()) # 100


def match_everything_but_foo():
    '''
    Remember: the as the parser moves along the string from left to right, it will try to find a match from each starting position. Normally, I would
    only see the first match with search(), but finditer() reveals all of the possible matches.
    '''
    string = 'I like food. Food is great.'
    # This is a good solution
    # Why isn't "ood." matched? Because the \b character class requires all matches to start with a word boundary. Since \b doesn't consume any
    # character, these regular expressions are equivalent to the one below: '\b\b\b\b\b\b\b(?!foo)\S+', '(?!foo)\b\b\b\b\b\S+', '\b\b\b(?!foo)\b\b\S+'
    # - Fun fact: "." is matched because "d." has a \b in the middle and "." is a non-whitespace character (\S)
    no_foo = re.compile(r'\b(?!foo)\S+')
    # This is a completely different regex
    # - "." is not matched like above because \b is the boundary between a \w character and a \W character. "." and " " BOTH belong to the \W
    #   character class, so there is no \b between them! Tricky!
    #no_foo = re.compile(r'\b(?!foo)\S+\b')
    for mo in no_foo.finditer(string):
        print(mo.group())


if __name__ == '__main__':
    #succeeding_lookahead()
    #preceeding_lookahead()
    #preceeding_lookbehind()
    #succeeding_lookbehind()
    match_everything_but_foo()