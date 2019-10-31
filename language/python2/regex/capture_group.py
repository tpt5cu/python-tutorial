# https://www.rexegg.com/regex-capture.html - this stuff is ridiculous
# https://www.rexegg.com/regex-lookarounds.html


import re


def quantified_capture_group():
    '''
    - There is 1 capture group for every set of capturing parentheses, regardless of whether or not there is a quantifier like + or *
        - There would be 1 capture group for (...). There would also be 1 capture group for (...)+ or (...)*
        - Since there is 1 capture group, what happens if the capture group finds multiple matches? The answer is that the LAST match is recorded as
          the value of the capture group. Any intermediate matches are lost
    '''
    # The single capture group records D_ because that was the last match found.
    # - search() returns the first location where the rgx produced a match. Normally, search() would stop, but the "+" quantifier made search() keep
    #   looking. 'A_' is the first location that produced a match, but search() kept looking just in case it could extend from that initial location.
    #   It found that it could, so the entire string ended up being included
    #   - Try adding a space between different [A-Z]_ pairs to verify this
    string = 'A_B_C_D_'
    mo = re.search(r'([A-Z]_)+', string)
    print(mo.group()) # A_B_C_D
    print(mo.group(1)) # D_
    # The single capture group records A_ because that was the first match found. There was no quantifier to make search() keep looking, so it stopped.
    string = 'A_B_C_D_'
    mo = re.search(r'([A-Z]_)', string)
    print(mo.group()) # A_
    print(mo.group(1)) # A_
    # The single capture group records A_ because that was the only match found. If a substring matches a capture group, it is captured as the string
    # is parsed. The only time a capture group wouldn't consume part of a string is if it were inside of a lookaround. But the concepts of lookarounds
    # and capture groups are orthogonal. Why doesn't this regex behave like the first one? It's because search() recognizes that it cannot extend from
    # 'A_'. That's the key. search() returns the FIRST location where a match was found. It could extend from that point depending on other factors,
    # but those factors are secondary to the main goal of search().
    string = 'A_ B_ C_ D_'
    mo = re.search(r'([A-Z]_)+', string)
    print(mo.group()) # A_
    print(mo.group(1)) # A_


def capture_group_with_lookaround_simple():
    '''
    https://www.rexegg.com/regex-lookarounds.html#overlapping
    In this example, each of the 4 tuples is found by the same parser logic:
    - Assert that from the current parser position, there is at least one succeeding alphanumeric character (it's a lookahead!)
    - If that is true, search for exactly one capital letter
    - Lookarounds do not consume characters on the string, so the lookaround can overlap with the actual matching characters
    '''
    string = 'ABCD'
    for mo in re.finditer(r'(?=(\w+))[A-Z]', string):
        #print(mo.group())
        #print(mo.group(1))
        pass
        # (A, ABCD)
        # (B, BCD)
        # (C, CD)
        # (D, D)
    # There is only one time in which 1) the capture group captures "ABCD" in the lookahead and 2) that capture group is matched. This proves that
    # capture groups CAN be used in a lookaround and referenced later on
    for mo in re.finditer(r'(?=(\w+))\1', string):
        print(mo.group())
        print(mo.group(1))
        # (ABCD, ABCD)


def capture_group_with_lookaround_complex_and_backreference():
    '''
    - Once a capture group is captured IT IS FULL. IT CANNOT BE RESET. This is a good thing and the only reason why the below example works.
    - A capture group is only captured IF THE ENGINE FINDS A MATCH FOR THE ENTIRE REGEX. This is the reason the capture group "B_" isn't ever printed
      out. Perhaps "B_" is captured, but I'll never know and don't care because if/when "B_" was captured, the engine did not find a match in the
      string with that particular capture group.
    - A trick is to wrap the capture group in a lookaround so as not to consume part of the string
    '''
    # This capture group is part of the entire regex, so it cannot be ignored after capturing it. But how many real-world examples would be
    # constructed like this? It makes using backreferences with capture groups difficult. Don't do this.
    string = 'A_ A_ likes apples.'
    mo = re.search(r'([A-Z]_) \1.*\.', string)
    print(mo.group()) # A_ A_ likes apples.
    print('')
    # I did it! This really works!
    string = 'A_B_C_D_. A_ likes apples. D_ likes durian. C_ likes pasta. '
    for mo in re.finditer(r'(?=([A-Z]_))\1 [\w ]+\.', string):
        print(mo.group())
        print(mo.group(1))
    print('')
    # Here is a similar example. I don't think its possible to capture every instance of a capture group. E.g. I don't think it's possible to get this
    # result, or something like it: "Austin likes to read history books. Austin likes to read history books."
    sentences = 'My name is Austin. Austin likes to read history books. David likes to read comic books. Austin likes cartoons. Austin likes to read history books.'
    rgx = re.compile(r'(?=((?<!^)[A-Z]\w+\b))\1 [\w ]+\.')
    #rgx = re.compile(r'(?=((?<!^)[A-Z]\w+\b))(\1 [\w ]+\.)+')
    for mo in re.finditer(rgx, sentences):
        print(mo.group())
        print(mo.group(1))


if __name__ == '__main__':
    #quantified_capture_group()
    #capture_group_with_lookaround_simple()
    capture_group_with_lookaround_complex_and_backreference()