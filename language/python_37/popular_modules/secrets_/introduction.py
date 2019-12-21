# https://docs.python.org/3.7/library/secrets.html#module-secrets


import secrets, hashlib, random, time


def get_cryptographically_insecure_hex_string():
    '''Useful for signing cookies'''
    # This is the insecure way of doing it because random.random() is insecure
    str_ = hashlib.md5(str(random.random()).encode('utf-8') + str(time.time()).encode('utf-8')).hexdigest()
    print(str_) # 115bf3f97f73681660d5e1733a8075b5


def get_cryptographically_secure_hex_string():
    '''x'''
    s = secrets.SystemRandom()
    print(s.random())
    print(s)
    print(dir(s))


if __name__ == '__main__':
    #get_cryptographically_insecure_hex_string()
    get_cryptographically_secure_hex_string()