# https://stackoverflow.com/questions/27138440/how-to-create-a-traceback-object - TLDR: I cannot create my own traceback objects


import sys


def use_discontinued_syntax():
    '''In Python 2, raise can be written as: raise <Exception class>, <message>, <traceback>'''
    raise Exception, 'Some message', sys.exc_info()[2]


def except_exception():
    try:
        use_discontinued_syntax()
    except Exception as e:
        print(e.args)
        print(e) # Some message


if __name__ == '__main__':
    except_exception()