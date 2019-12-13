# https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects
# https://docs.python.org/3/library/io.html - This is the actual documentation I'm interested in
# https://docs.python.org/3/library/functions.html#open - shows documentation for open() and modes

# https://docs.python.org/3/library/functions.html#open-newline-parameter - what's the deal with "newline"


import io, os, locale


'''
newline

- The "newline" parameter only applies if a file is opend in text mode
- It can be:
    - None (default): universal newlines are enabled. A line that is read can end with '\n', '\r', or '\r\n', but that ending will always be returned
      inside Python as '\n'
    - '': universal newlines are enabled. A line can end with any of the above BUT will not be translated into '\n'
    - '\n', '\r', '\r\n: a newline is only delineated by the respective pattern. The respective line ending will also be returned without translation
- 
'''


'''
The old Python built-in open() function would read a file into a bytes object (so decoding wasn't relevant), then when a textual representation was
required it would decode using US-ASCII
- Since most of the time I was working with str objects in Python 2 anyway, when a str object was written to a file, it would just be encoded as US-ASCII
'''


def compare_open():
    '''The built-in open function is identical to the io.open function in Python 3'''
    print(io.open is open) # True


def open_py():
    '''
    - By default, reading a file returns a "str" object, which IS a unicode object in Python 3
        - Use 'b' mode to read a file into a bytes object
    - The "file" object is no longer a <type 'file'>
    '''
    try:
        file = open(os.path.join(os.path.dirname(__file__), '../../../../.gitignore'), 'r')
        print(type(file)) # <class '_io.TextIOWrapper'>
        # read() without an argument reads the entire file into a unicode-string object
        s = file.read()
        print(type(s)) # <type 'str'>
        print(s)
    finally:
        file.close()


def open_with_encoding():
    '''
    io.open() accepts an "encoding" argument, which defaults to None. However, that doesn't mean that no encoding scheme is used
    - For files that are opened in text-mode (i.e. without 'b'), the file is decoded transparently with "locale.getpreferredencoding(False)"
        - This is UTF-8 in Python 3 and US-ASCII in Python 2
    - Recommended practice is to use the encoding parameter whenever possible
    '''
    print(locale.getpreferredencoding(False)) # UTF-8
    def write_utf_16_encoded_file():
        with open(__file__, encoding='utf-8') as f:
            text = f.read()
        path = os.path.join(os.path.dirname(__file__), 'files', 'utf-16-text.txt')
        with open(path, 'w', encoding='utf-16') as f:
            f.write(text)
        # The file is encoded in UTF-16, so of course decoding UTF-8 will raise an exception
        #with open(path) as f:
        #    print(f.read()) # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
        with open(path, encoding='utf-16') as f:
            print(f.read())
    write_utf_16_encoded_file()


def invalid_filename():
    '''An OSError is thrown (good), but in this case would my code crash or handle the exception properly?'''
    #with open(b'bad-\xFF-filename', 'wb') as f: # OSError: [Errno 92] Illegal byte sequence: b'bad-\xff-filename'
    # This looks code weird, but is valid in Python 3
    filename = 'é ñ ü Đ ř ů Å ß ç ı İ.txt'
    with open(os.path.join(os.path.dirname(__file__), 'files', filename), 'wb') as f:
        f.write(b'binary-\xFF-data')


if __name__ == '__main__':
    #compare_open()
    #open_py()
    #open_with_encoding()
    invalid_filename()