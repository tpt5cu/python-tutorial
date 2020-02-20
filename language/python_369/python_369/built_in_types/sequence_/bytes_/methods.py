# https://docs.python.org/3/library/stdtypes.html#bytes-and-bytearray-operations
# https://stackoverflow.com/questions/42339876/error-unicodedecodeerror-utf-8-codec-cant-decode-byte-0xff-in-position-0-in/42340744 - invalid start byte


import base64


'''A bytes object is an immutable sequences of integers'''


def decode_bytes_to_str():
    '''
    - The decode() method default to UTF-8, which is sensible, but not always correct!
        - \xBC == 10111100 in raw binary (no encoding at all). Unfortunately, there is no code point in UTF-8 that STARTS with that exact sequence of
          bits, so UTF-8 can't decode this particular sequence of bytes. It's actually really useful that Python raises this error instead of
          corrupting data by outputing �
    - It's really cool how it just so happens I can decode this sequence of bytes via two different encodings!
    '''
    b = b'\xBC\xbd\xbe\xbf'
    # It turns out that UTF-8 has rules about what byte sequences are considered valid. I'm trying to decode this byte sequence (which I intended to
    # be decoded with ISO-8859-1) with UTF-8, and UTF-8 is complaining
    #s = b.decode() # UnicodeDecodeError
    s = b.decode(encoding='utf-16')
    print(type(s)) # <class 'str'>
    print(s) # 붼뾾
    s = b.decode(encoding='latin_1')
    print(type(s)) # <class 'str'>
    print(s) # ¼½¾¿®


def decode_readable_bytes_to_str():
    '''
    Sometimes all I need to do is get rid of the little 'b' prefix'
    - decode() defaults to using 'utf-8' which is ascii compatible, so it will usually be sufficient
    - This is especially needed for Base64-encoded PNGs, which need to be bytes objects in Python, but need to be actual strings for json.dump()
    '''
    b = b'Hello there'
    s = b.decode()
    print(type(s)) # <class 'str'>
    print(s) # Hello there


def encode_base64():
    '''The only way to do this is with the base64 module. There is no encode() method on bytes objects since that would be confusing'''
    bytes_ = b'Hello World'
    #bytes_ = bytes_.encode('base64') # AttributeError
    print(bytes_)


def decode_base64():
    '''
    Technically, this function should be in the base64 notes. I put it here because sometimes I need Base64 bytes -> UTF-8 bytes (or whatever) ->
    str or binary file
    - The point is, I can only Base64 decode a bytes object that was previously encoded in Base64
    '''
    bytes_ = b'Hello World!'
    #print(bytes_.decode('base64')) # LookupError: 'base64' is not a text encoding;
    #utf8_bytes = base64.standard_b64decode(bytes_) # binascii.Error: Incorrect padding
    bytes_ = base64.standard_b64encode(bytes_)
    print(bytes_) # b'SGVsbG8gV29ybGQh'
    utf8_bytes = base64.standard_b64decode(bytes_)
    print(utf8_bytes) # b'Hello World!'


def count():
    '''
    I can count the number of non-overlapping occurances of a byte with the specified value
    - Searching for b'5' searches for bytes that have a value of 53. 5 and \x35 are two such bytes
    - Searching for 5 searches for bytes that have a literal value of 5. \x05 is one such byte
    '''
    # The digit '5' has an ASCII code point of 53. Therefore, this bytes object is a sequence containing one byte with a value of 53: 00110101
    print(b'5'[0]) # 53
    b = b'5 \x05 \x35 4 \x05 \x05'
    count = b.count(b'5')
    print(count) # 2
    count = b.count(5)
    print(count) # 3


def bad_conversion():
    '''Just "casting" a bytes object to a str will give me a weird looking str which is never what I want'''
    bytes_ = b'USCRN station 45'
    str_ = str(bytes_)
    print(type(str_)) # <class 'str'>
    print(str_) # b'USCRN station 45'


def split_():
    '''
    str and bytes objects have (almost?) the same set of methods, but each respective method only accepts the same respective type as the calling
    object
    - E.g. <bytes>.split(<bytes>) and <str>.split(<str>)
    '''
    bytes_ = b'hello\r\nworld'
    split_bytes = bytes_.split(b'\r\n')
    print(split_bytes) # [b'hello', b'world']


if __name__ == '__main__':
    #decode_bytes_to_str()
    #decode_readable_bytes_to_str()
    #encode_base64()
    decode_base64()
    #count()
    #bad_conversion()
    #split_()
