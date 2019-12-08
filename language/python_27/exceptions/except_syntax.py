def bare_except_alias():
    '''
    - I cannot use an alias with a bare except statement. It is a SyntaxError.
    - If anything is except-ed, it must be an Exception object
    '''
    try:
        raise IOError("There was an IOError")
    #except as e: # SyntaxError: invalid syntax
    #except Error as e: # NameError: global name 'Error' is not defined
    except:
        pass
    print("Hello from bare_except_alias()")


if __name__ == '__main__':
    bare_except_alias()