# https://www.rexegg.com/regex-disambiguation.html#noncap
# https://stackoverflow.com/questions/1687620/regex-match-everything-but-specific-pattern
# https://stackoverflow.com/questions/3548949/how-can-i-exclude-some-characters-from-a-class


import re


'''A non-capturing group is formed with (?:...)'''


def double_negative():
    '''I was struggling with this one for a while because the combination ".*" is dastardly. It's too strong'''
    string = 'A_ likes apples. D_ likes doritos. I like pie. A_ does not like bonfires. D_ likes cake.'
    # This is great! But I only want sentences that start with A_
    too_broad = re.compile(r'\b[A-Z]_[\w ]+\.')
    for mo in too_broad.finditer(string):
        print(mo.group())
    print('')
    # This is it! [^\W] means "anything that is not a non-alphanumeric character", which is a double negative for all alphanumeric characters. [^\WD]
    # means all alphanumeric characters and not "D", so it excludes "D" from the set of possible matching alphanumeric characters
    double_negative = re.compile(r'\b[^\WD]_[\w ]+\.')
    for mo in double_negative.finditer(string):
        print(mo.group())



if __name__ == '__main__':
    double_negative()