import re


def match_newline():
    '''[\n] does indeed match a newline character'''
    exp = re.compile(r"[\n]*hi")
    mo = exp.search("""
hi""")
    print(mo) # <_sre.SRE_Match object; span=(0, 3), match='\nhi'>
    mo = exp.search('hi') 
    print(mo) # <_sre.SRE_Match object; span=(0, 2), match='hi'>


def match_newline_and_line_start():
    '''
    The ^ character apparently matches just after the newline, but doesn't include the newline
    '''
    exp = re.compile(r"[\n]*^hi")
    mo = exp.search("""
hi""")
    # My guess is that when the newline is greedily consumed, there is nothing left for ^ to match
    print(mo) # None
    exp = re.compile(r"[\^]*hi")
    mo = exp.search("""
hi""")
    # This works!
    print(mo) # <_sre.SRE_Match object; span=(1, 3), match='hi'>


if __name__ == '__main__':
    #match_newline()
    match_newline_and_line_start()
