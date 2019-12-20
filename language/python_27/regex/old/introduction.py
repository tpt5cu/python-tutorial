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


if __name__ == "__main__":
    #examine_match_object()
    #string_to_list()
    #get_numbers_from_string()