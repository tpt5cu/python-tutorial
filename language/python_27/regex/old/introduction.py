# https://docs.python.org/2/library/re.html
# https://stackoverflow.com/questions/18493677/how-do-i-return-a-string-from-a-regex-match-in-python
# https://docs.python.org/2/library/re.html#module-contents - re flags

# https://regexone.com/references/python2 - excellent tutorial for Python 2


'''
Fun fact: the Python 2/3 re module is not fully PCRE (Perl Compatible Regular Expressions) compatible, but it gets pretty close.
'''


import re


"""
In regular string literals, backslash "\" is used to escape characters. By escape, I mean that it can either 1) make a special character not-special
(e.g. "\\" escapes the backslash so that the backslash isn't special) or 2) make a special meaning when combined with another character (e.g. "\n"
makes a newline). This is confusing enough, and if we combine regular expressions on top of that it gets really messy (e.g. the string used to match
one backslash is "\\\\" because "\\" is needed to create one backslash to escape the next backslash, and "\\" creates a literal backslash character).
Use raw strings to avoid this in regular expressions
"""


def examine_match_object():
    """
    - <MatchObject>.group() default to <MatchObject>.group(0) if no arguments are passed. The first group is the entire match. Additional groups are
      only present if 1) parenthesized matching was done (i.e. (...)) and 2) a match(es) was found for that parenthesized group
        - If an index is used that to access a nonexistent match, an IndexError is raised
    """
    string = 'cat\ndog\nfrogs\nfish\nmonkeys\nbat'
    mo = re.search(r'\b(\w)\w{3}\b', string) # re.search() only returns the FIRST match in the string. That's what it's supposed to do
    # The first found match for the pattern was 'fish'. The parenthesized group (\w) found a match at 'f'
    print(mo.group()) # fish
    print(mo.group(1)) # f
    #print(mo.group(2)) # IndexError


def string_to_list():
    """<regex>.split() will convert a string into a list, similar to how <string>.split() does the same thing without a regex"""
    data = """63838 20170101 0100 20161231 2000  2.422  -84.75   38.09     4.4     4.1     4.4     3.9     0.0      0 0      0 0      0 0 C     3.7 0     3.8 0     3.5 0    93 0   0.340   0.341   0.343   0.324   0.410     4.5     4.6     5.3     7.2     9.2
        63838 20170101 0200 20161231 2100  2.422  -84.75   38.09     4.8     4.6     4.9     4.4     0.0      0 0      0 0      0 0 C     4.0 0     4.2 0     3.8 0    92 0   0.342   0.341   0.340   0.326   0.427     4.5     4.7     5.3     7.2     9.2
        63838 20170101 0300 20161231 2200  2.422  -84.75   38.09     4.7     4.7     4.8     4.6     0.0      0 0      0 0      0 0 C     4.2 0     4.2 0     4.2 0    93 0   0.343   0.339   0.339   0.327   0.421     4.6     4.7     5.4     7.2     9.1"""
    lines = data.splitlines()
    #print(lines)
    #my_list = re.split("!^\s+", lines[1]) # ['        63838 20170101 0200 20161231 2100  2.422  -84.75   38.09     4.8     4.6     4.9     4.4     0.0      0 0      0 0      0 0 C     4.0 0     4.2 0     3.8 0    92 0   0.342   0.341   0.340   0.326   0.427     4.5     4.7     5.3     7.2     9.2']
    my_list = re.split("\s+", lines[1]) # ['', '63838', '20170101', '0200', '20161231', '2100', '2.422', '-84.75', '38.09', '4.8', '4.6', '4.9', '4.4', '0.0', '0', '0', '0', '0', '0', '0', 'C', '4.0', '0', '4.2', '0', '3.8', '0', '92', '0', '0.342', '0.341', '0.340', '0.326', '0.427', '4.5', '4.7', '5.3', '7.2', '9.2']
    print(my_list)
    print(len(my_list)) # 39


def get_numbers_from_string():
    """
    The string found by a regex can be returned from a MatchObject with the group() method.
    - With no arguments, group() returns the entire string that was matched by the regex. If there were no parenthesized groups (i.e. "(<regex>)"),
      then there will only ever be 1 group.

    Regexs are greedy.
    - \d will find exactly 1 digit since that's all it can do
    - \d will find as many consecutive digits as possible (greedy)
    """
    string = "Meter121XYZ333"
    # re.search() returns a MatchObject. re.search() only returns a MatchObject with the FIRST matching occurance to the regex
    mo = re.search("\d+", string)
    print(mo.group()) # 121
    #print(mo.group(1))
    #print(mo.group(2))


def match_vs_search():
    '''
    - re.match() only returns a MatchObject if the regex matched from the beginning of the string onwards.
        - A MatchObject returned from match() does NOT mean that the entire string matched the regex
        - Thus, match() seems more like a convenience function than anything. I suppose the function is useful in communicating intent
    - re.search() returns a MatchObject if there was a match anywhere in the string
    '''
    string = '9feeder1beads'
    rgx = re.compile(r'[a-z]+\d')
    # match() found a valid match that started from the beginning of the string
    mo = rgx.match(string) # MatchObject was None
    #print(mo.group()) 
    mo = rgx.search(string)
    print(mo.group()) # feeder1


def match_entire_string():
    good_string = 'feeder1'
    #bad = 'feeder1a'
    #entire_string = re.compile(r'^[a-z]+\d$')
    substring = re.compile(r'[a-z]+\d')
    mo = substring.search(good_string)
    print(mo.groups())


if __name__ == "__main__":
    #examine_match_object()
    #string_to_list()
    #get_numbers_from_string()
    match_entire_string()