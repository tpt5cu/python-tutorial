from python_369.function.default_parameters import modify


def modify_external_function_default_parameters():
    '''This works!'''
    modify.do_stuff('baz') # foo bar baz boo
    modify.do_stuff.__defaults__ = ('new_foo', 'new_bar')
    print(modify.do_stuff.__defaults__) # ('foo', 'bar')
    modify.do_stuff('baz') # new_foo new_bar baz boo


if __name__ == '__main__':
    modify_external_function_default_parameters()
