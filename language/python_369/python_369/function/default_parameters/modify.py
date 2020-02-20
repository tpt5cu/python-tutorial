# https://stackoverflow.com/questions/17625695/is-it-possible-to-change-a-functions-default-parameters-in-python


# Non-default parameters cannot come after default parameters
#def do_stuff(foo='foo', bar='bar', baz):
def do_stuff(baz, foo='foo', bar='bar', *, boo='boo'):
    print(foo, bar, baz, boo)


def change_do_stuff():
    '''
    Given that non-default parameters cannot come after default parameters, if the __defaults__ attribute is modified, then the new default parameter
    values are matched by counting right to left from the leftmost *, *args, or **kwargs.
    '''
    #print(type(do_stuff.__defaults__)) # <class 'tuple'>
    # Here, I get a reference to do_stuff.__defaults__. Since do_stuff.__defaults__ is immutable, when I reassign it, I create a new tuple object and
    # make do_stuff.__defaults__ point to the new tuple
    do_stuff.__defaults__ = ('new_foo', 'new_bar')


if __name__ == '__main__':
    do_stuff('baz') # foo bar baz boo
    change_do_stuff()
    do_stuff('baz') # new_foo new_bar baz boo
