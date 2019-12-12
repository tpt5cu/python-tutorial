# https://docs.python.org/2.7/library/functions.html#apply


def do_stuff(first, second, third, *args):
    print('Regular arguments: {}, {}, {}'.format(first, second, third))
    print('args arguments: {}'.format(args))


def invoke_function_with_args():
    '''
    apply() will invoke a function that uses *args with the sequence argument filling up all positional arguments and optionally overflowing into args
    - This function is redundant since argument unpacking was introduced
    '''
    l = ['hello', 'there', 'general', 'Kenobi', 'lightsaber']
    #do_stuff(l) # TypeError: do_stuff() takes at least 3 arguments (1 given)
    # Regular arguments: hello, there, general
    # args arguments: ('Kenobi', 'lightsaber')
    apply(do_stuff, l)
    l = l[0:2]
    # Regular arguments: hello, there, there
    # args arguments: ()
    apply(do_stuff, l, {'third': l[-1]})


def sequence_unpacking():
    '''The * syntax is much more concise than apply()'''
    # Regular arguments: hello, there, general
    # args arguments: ('Kenobi', 'lightsaber')
    l = ['hello', 'there', 'general', 'Kenobi', 'lightsaber']
    do_stuff(*l)


if __name__ == '__main__':
    #invoke_function_with_args()
    sequence_unpacking()