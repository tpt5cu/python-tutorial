# https://regexone.com/references/python2


import re


def examine_timestap():
    '''
    re.search() stops after it finds the first match in a string, so it is best suited for testing a string rather than extracting data
    '''
    rgx = re.compile(r'([a-zA-Z]+)\s*(\d+)\s*(\d+)')
    timestamp = 'May 5 1995'
    mo = rgx.search(timestamp)
    # MatchObjects always have a bool value of True
    if mo:
        # group(0) or group() is always the entire substring that was matched
        print(mo.group()) # May 5 1995
        # group(<num>) will return the substring that satisified the capturing group. There will only ever be as many elements in
        # group() as there were capturing groups in the regex
        print(mo.group(1)) # May
        print(mo.group(2)) # 5
        print(mo.group(3)) # 1995
        #print(mo.group(4)) # IndexError
    
    # This regex has no capturing groups, so anything other than group(0) is an IndexError
    mo = re.search(r'\w+', timestamp)
    print(mo.group()) # May
    #print(mo.group(1)) # IndexError


if __name__ == '__main__':
    examine_timestap()