import re


def match_entire_string():
    '''
    The way to ensure that an entire string matches a regex is to use the ^ and $ metacharacters
    - <re>.match() only cares if a match was found from the beginning of the string, not if the entire string matched the pattern
    '''
    good_string = 'feeder1'
    bad_string = 'feeder12'
    rgx = re.compile(r'^[a-z]+\d$')
    mo = rgx.search(good_string)
    print(mo.group()) # feeder1
    print(mo.groups()) # ()
    mo = rgx.search(bad_string)
    print(mo is None) # True


if __name__ == '__main__':
    match_entire_string()