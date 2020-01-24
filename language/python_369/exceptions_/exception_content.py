def examine_exception_content():
    '''
    Python 3 exceptions lack the "message" attribute entirely. Instead, everything should be looked up inside of the "args" attribute
    - This is good because the value of the "message" attribute was unreliable in Python 2, so this removes ambiguity
    - 
    '''
    # This is typically how exceptions are created.
    e = Exception('hello world')
    print(e.args) # ('hello world',)
    print(e.args[0]) # hello world
    #print(e.message) # AttributeError
    # Exceptions can also be created with a variable number of arguments.
    e = Exception('foo', 'bar', 'baz')
    print(e.args) # ('foo', 'bar', 'baz')
    print(type(e.args)) # <class 'tuple'>
    #print(e.message) # AttributeError


def examine_empty_exception():
    '''The only way to safely deal with exceptions is to check the length of args'''
    e = Exception()
    print(len(e.args)) # 0
    #print(e.args[0]) # IndexError
    msg = e.args[0] if len(e.args) > 0 else 'nothing'
    print(msg)


if __name__ == '__main__':
    #examine_exception_content()
    examine_empty_exception()
