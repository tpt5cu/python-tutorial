import traceback

def inspect_print_exc():
    try:
        5/0
    except:
        '''
        As expected, print_exc() doesn't return anything
        - What I probably want it format_exc()
        '''
        ## Traceback (most recent call last):
        ## File "/Users/austinchang/tutorials/python/language/python_369/exceptions_/traceback_/introduction.py", line 5, in inspect_print_exc
        ##     5/0
        ## ZeroDivisionError: division by zero
        #val = traceback.print_exc()
        val = traceback.format_exc()
        print(type(val)) # <class 'str'>
        print(val) # None
        pass


if __name__ == '__main__':
    inspect_print_exc()
