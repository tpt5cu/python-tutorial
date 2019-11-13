# https://docs.python.org/2.7/library/re.html#match-objects


import re


def examine_group_attribute():
    '''
    - group() or group(0) return the entire substring that was matched
    - If no parenthesized 
    '''
    string = '1234 I declare a thumb war 5678'
    mo = re.search(r'(\w)+', string)
    print(mo.group()) # 1234
    print(mo.group(1)) # 4
    #print(mo.group(2)) # IndexError
    mo = re.search(r'\w+', string)
    print(mo.group()) # 1234
    #print(mo.group(1)) # IndexError


if __name__ == '__main__':
    examine_group_attribute()
