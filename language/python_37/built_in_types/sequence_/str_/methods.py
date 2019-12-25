# https://docs.python.org/3.7/library/stdtypes.html#string-methods - built-in string methods


def mix_unicode_and_str():
    '''unicode and str objects cannot be concatenated'''
    s = b'hello' + u'world' # TypeError: can't concat str to bytes


def remove_characters():
    '''
    The old Python 2 str (bytes) object had a <str>.translate() method with a different signature than the old <unicode>.translate()
    - Basically, the method will turn all specified Unicode ordinals into other Unicode ordinals based on a provided mapping
    - This is THE way to remove all occurances of some character(s) from a string without using replace() in a loop
        - Using <str>.replace() is annoying because I have to iterate over the string for every character to remove b/c replace() works with substrings
    '''
    # Delete characters by mapping the Unicode ordinal (an integer) to None
    mapping = {
        ord('a'): None,
        ord('e'): None,
        ord('i'): None,
        ord('o'): None,
        ord('u'): None
    }
    str_ = 'reoooad theeeis shoaeiourt text aeiouz'
    new_str = str_.translate(mapping)
    print(new_str) # rd ths shrt txt z

    str_ = 'Nice\nstring\r\nyou got there\r.'
    print(str_) # Nice string .ou got there 
    str_ = str_.translate({
        ord('\r'): None,
        ord('\n'): None
    })
    print(str_) # Nicestringyou got there.


def strip_characters():
    '''
    - TLDR: <str>.strip() is NOT sufficient for replacing all instances of some character(s) in a string
    - None of these methods care about subdividing the string in half based on its length (thank goodness)
    - rstrip(): remove all trailing characters from the string
        - In the case of multiple non-whitespace characters, rstrip() will either:
            1) Do nothing if none of the non-whitespace characters matched the last character in the target string
            2) Delete the last character in the target string and every other matching character from the right until it encounters a character in the
               target string that does not match any of the specified characters
    - lstrip(): ditto but from the left
    - strip(): does NOT remove all matching characters from the string
        - Instead, it merely applies lstrip() and rstrip() together! Confusing!
    - Order of target characters doesn't matter
    - Repetition of target characters doesn't matter
    '''
    str_ = 'mississippi'
    # From the right, it found 'i' and 'p' characters until it found 's'. Once it found 's', it stopped
    print(str_.rstrip('ipz')) # mississ
    # It found neither 'i' or 'p' nor 'z', so it stopped at 'm' and did nothing
    print(str_.lstrip('ipz')) # mississippi
    # lstrip() followed by rstrip()
    print(str_.strip('ipz')) # mississ
    # There are 3 subsequences that include two 'a's and one 'd', but only two of those subsequences will be stripped
    str_ = 'aad' + 'bbb' + 'aad' + 'acc' + 'daa'
    print(str_)                 # aadbbbaadaccdaa
    print(str_.rstrip('ad'))    # aadbbbaadacc
    print(str_.lstrip('da'))    #    bbbaadaccdaa
    print(str_.strip('ddaa'))   #    bbbaadacc


if __name__ == '__main__':
    #mix_unicode_and_str()
    remove_characters()
    #strip_characters()