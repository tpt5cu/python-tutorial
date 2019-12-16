# https://stackoverflow.com/questions/893333/multiple-variables-in-a-with-statement


import os


def read_files():
    '''
    It is possible to use multiple aliases within a with-statement. It's actually multiple context managers at once
    - It's equivalent to nesting multiple with-statements inside each other
    '''
    root = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(root, 'decorator_.py')) as d, open(os.path.join(root, 'return_within_context.py')) as w:
        print(d.read())
        print(w.read())


if __name__ == '__main__':
    read_files()