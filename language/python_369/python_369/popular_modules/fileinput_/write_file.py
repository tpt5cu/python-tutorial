# https://docs.python.org/3.6/library/fileinput.html


import fileinput 
from pathlib import Path


def inplace_modification():
    '''
    inplace=True 1) creates a copy of the file with the ".backup" extension 2) redirects stdout (e.g. print()) to point to the original file. The
    back-up file is deleted once the output file is closed
    - Thus, this isn't "really" in-place modification, but it's close enough
    - Remember that if nothing is printed for a line, that line won't exist in the output file!
    - inplace and openhook can't be used together
    '''
    (Path(__file__).parent / 'modify.txt').write_text((Path(__file__).parent / 'modify-copy.txt').read_text())
    path = str((Path(__file__).parent / 'modify.txt').resolve())
    with fileinput.input(path, inplace=True) as f:
        for line in f:
            if '1' in line:
                print('FooBarBaz')
            else:
                print(line, end='')


def open_in_alternative_encoding():
    '''
    矇
    - https://stackoverflow.com/questions/54767506/ascii-codec-cant-encode-character-xc9-in-position-9-ordinal-not-in-range
        - This is the problem! Just set the locale and all problems below go away
        - Specifically, only LC_CTYPE needs to be set, but I should set all of them (see locale notes) 
    - There doesn't appear to be an easy way to inspect the default encoding of a fileinput object
        - It must just use the Python encoding
    - Both systems use utf-8 as the default encoding, so this is strange
    - On macOS, fileinput uses utf-8 by default
    - On Ubuntu, fileinput uses ascii is the default
        - These default encoding settings persist whether or not inplace == True
            - I ran THIS file in Ubuntu with a bind mount and this is true
              -$ docker run --rm -it --mount type=bind,src=/Users/austinchang/tutorials/python/language/python_369/python_369/popular_modules/fileinput_,dst=/home/stuff ubuntu:18.04
    '''
    import sys
    # Ubuntu: utf-8 
    #  macOS: utf-8
    print(sys.getdefaultencoding())
    path = str((Path(__file__).parent / 'unicode.txt').resolve())
    ## These errors were caused by using the ascii encoding in Python
    ## Ubuntu: UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 0: ordinal not in range(128)
    ##  macOS: UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 0: ordinal not in range(128)
    #with fileinput.input(path, openhook=fileinput.hook_encoded('ascii')) as f: 
    ## The rest of these errors were caused by incorrect locale settings on Ubuntu:
    ## Ubuntu: UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 0: ordinal not in range(128)
    #with fileinput.input(path) as f: 
    ## Ubuntu: UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 0: ordinal not in range(128)
    #with fileinput.input(path, inplace=True) as f:
    ## Ubunut: UnicodeEncodeError: 'ascii' codec can't encode character '\u77c7' in position 0: ordinal not in range(128) (this exception occurs at print())
    with fileinput.input(path, openhook=fileinput.hook_encoded('utf-8')) as f: 
        for line in f:
            print(line, end='')


if __name__ == '__main__':
    #inplace_modification()
    open_in_alternative_encoding()
