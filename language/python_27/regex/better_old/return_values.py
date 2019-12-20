import re


def get_list_of_matches():
    '''
    findall() does not return a MatchObject, it returns a list.
    - If there were parenthesized groups in the list, the function returns a list of groups
    '''
    string = 'cat\nzog\nfrogs\ndish\nmonkeys\nbat'
    # There is a group, so a list of groups is returned
    match_list = re.findall(r'\b(\w)\w{3}\b', string)
    print(len(match_list)) # 1
    print(match_list) # ['d']
    # There were no groups, so a list of non-overlapping matches of the pattern is returned
    match_list = re.findall(r'\b\w{3}\b', string)
    print(len(match_list)) # 3
    print(match_list) # ['cat', 'zog', 'bat']
    # This is another example of using groups. Why would this returned output ever be useful?
    match_list = re.findall(r'\b(\w)\w{1}(\w)\b', string)
    print(len(match_list)) # 3
    print(match_list) # [('c', 't'), ('z', 'g'), ('b', 't')]


def string_to_list():
    '''<regex>.split() will convert a string into a list, similar to how <string>.split() does the same thing without a regex'''
    data = """63838 20170101 0100 20161231 2000  2.422  -84.75   38.09     4.4     4.1     4.4     3.9     0.0      0 0      0 0      0 0 C     3.7 0     3.8 0     3.5 0    93 0   0.340   0.341   0.343   0.324   0.410     4.5     4.6     5.3     7.2     9.2
        63838 20170101 0200 20161231 2100  2.422  -84.75   38.09     4.8     4.6     4.9     4.4     0.0      0 0      0 0      0 0 C     4.0 0     4.2 0     3.8 0    92 0   0.342   0.341   0.340   0.326   0.427     4.5     4.7     5.3     7.2     9.2
        63838 20170101 0300 20161231 2200  2.422  -84.75   38.09     4.7     4.7     4.8     4.6     0.0      0 0      0 0      0 0 C     4.2 0     4.2 0     4.2 0    93 0   0.343   0.339   0.339   0.327   0.421     4.6     4.7     5.4     7.2     9.1"""
    lines = data.splitlines()
    #print(lines)
    #my_list = re.split("!^\s+", lines[1]) # ['        63838 20170101 0200 20161231 2100  2.422  -84.75   38.09     4.8     4.6     4.9     4.4     0.0      0 0      0 0      0 0 C     4.0 0     4.2 0     3.8 0    92 0   0.342   0.341   0.340   0.326   0.427     4.5     4.7     5.3     7.2     9.2']
    my_list = re.split("\s+", lines[1]) # ['', '63838', '20170101', '0200', '20161231', '2100', '2.422', '-84.75', '38.09', '4.8', '4.6', '4.9', '4.4', '0.0', '0', '0', '0', '0', '0', '0', 'C', '4.0', '0', '4.2', '0', '3.8', '0', '92', '0', '0.342', '0.341', '0.340', '0.326', '0.427', '4.5', '4.7', '5.3', '7.2', '9.2']
    print(my_list)
    print(len(my_list)) # 39


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
    mo = rgx.match(string) 
    #print(mo.group()) # AttributeError: MatchObject was None
    mo = rgx.search(string)
    print(mo.group()) # feeder1


def group_vs_groups():
    '''
    - <MatchObject>.group() default to <MatchObject>.group(0) if no arguments are passed. The first group is the entire match. Additional groups are
      only present if 1) parenthesized matching was done (i.e. (...)) and 2) a match(es) was found for that parenthesized group
        - If an index is used to access a nonexistent match, an IndexError is raised
    '''
    string = 'cat\ndog\nfrogs\nfish\nmonkeys\nbat'
    mo = re.search(r'\b(\w)\w{3}\b', string) # re.search() only returns the FIRST match in the string. That's what it's supposed to do
    # The first found match for the pattern was 'fish'. The parenthesized group (\w) found a match at 'f'
    print(mo.group()) # fish
    print(mo.group(1)) # f
    #print(mo.group(2)) # IndexError


if __name__ == '__main__':
    get_list_of_matches()
    #string_to_list()
    #match_vs_search()
    #group_vs_groups()