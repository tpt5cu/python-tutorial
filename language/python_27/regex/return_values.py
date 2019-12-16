import re


def find_all_matches():
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


if __name__ == '__main__':
    find_all_matches()