# https://www.stefanjudis.com/today-i-learned/the-complicated-syntax-of-lookaheads-in-javascript-regular-expressions/
# https://docs.python.org/2/library/re.html


import re


def lookbehind():
    """
    Sometimes I want to match everything after a character, not including the character. A lookbehind will match <pattern1> only if it is preceeded by
    <pattern2>, e.g. (?<=<pattern2>)<pattern1>
    """
    string = "I am a string, isn't that weird?"
    pattern = re.compile("(?<=,).*$")
    mo = re.search(pattern, string)
    print(mo.group()) # " isn't that weird?"
    # sub (i.e. substituition) returns a new string where all occurances of <regex> (unless a count was specified) were replaced by the substitute.
    new_string = pattern.sub(" that's really cool!", string)
    print(new_string)


def lookahead():
    """
    A lookahead will match <pattern1> only if it is followed by <pattern2>, e.g. <pattern1>(?=<pattern2>) will ONLY mach <pattern1> if it is also
    followed by <pattern2>
    """


if __name__ == "__main__":
    lookbehind()