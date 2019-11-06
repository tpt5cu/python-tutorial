import re


def case_insensitive_matching():
    '''Case-insensitive matching can be done with compile() or not'''
    string = 'FeEderNamE1'
    rgx = re.compile(r'feedername', re.IGNORECASE)
    print(rgx.match(string).group()) # feederName
    print(re.search(r'feedername', string, re.IGNORECASE).group()) # feederName


if __name__ == '__main__':
    case_insensitive_matching()