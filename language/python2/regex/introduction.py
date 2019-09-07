# https://docs.python.org/2/library/re.html
# https://stackoverflow.com/questions/18493677/how-do-i-return-a-string-from-a-regex-match-in-python


import re


"""
In regular string literals, backslash "\" is used to escape characters. By escape, I mean that it can either 1) make a special character not-special
(e.g. "\\" escapes the backslash so that the backslash isn't special) or 2) make a special meaning when combined with another character (e.g. "\n"
makes a newline). This is confusing enough, and if we combine regular expressions on top of that it gets really messy (e.g. the string used to match
two backslashes is "\\\\"). Use raw strings to avoid this when needed.
"""


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


if __name__ == "__main__":
    #string_to_list()
    get_numbers_from_string()