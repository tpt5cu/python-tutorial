# https://docs.python.org/3.7/library/secrets.html#module-secrets
# https://stackoverflow.com/questions/42190663/questions-about-python3-6-os-urandom-os-getrandom-secrets


import secrets, hashlib, random, time, os


'''
Come back to this if I have time
'''


def get_cryptographically_insecure_csrf_token_hex_string():
    '''This is the insecure way of doing it because random.random() is insecure'''
    str_ = hashlib.md5(str(random.random()).encode('utf-8') + str(time.time()).encode('utf-8'))
    print(str_) # <md5 HASH object @ 0x100a47030>
    print(str_.hexdigest()) # a93f7a995b0e523e3a4147a2db51b161


def get_cryptographically_secure_csrf_token_hex_string():
    '''x'''
    print(secrets.SystemRandom.random) # <function SystemRandom.random at 0x1034aa950>
    print(os.urandom) # <built-in function urandom>
    print(secrets.SystemRandom.random is os.urandom) # False
    #str_ = hashlib.md5(str(secrets.SystemRandom().random().encode('utf-8') + str(time.time()).encode('utf-8'))
    #s = secrets.SystemRandom()
    #print(s.random())
    #print(s)
    #print(dir(s))


if __name__ == '__main__':
    #get_cryptographically_insecure_csrf_token_hex_string()
    get_cryptographically_secure_csrf_token_hex_string()