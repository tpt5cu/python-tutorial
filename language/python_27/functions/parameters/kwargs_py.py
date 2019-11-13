def unpack_dictionary(name, age):
    """The ** syntax is also used to unpack a dictionary into a function that is being invoked"""
    print(name)
    print(age)


"""If **kwags is used, it must be the last parameter. *args must come before **kwargs"""
#def use_kwargs(**kwargs, age):
#def use_kwargs(**kwargs, *args):
def use_kwargs(color, *args, **kwargs):
    """**<whatever> (commonly "**kwargs") is a regular old dictionary"""
    print('color: {}'.format(color))
    #print(type(kwargs)) # <type 'dict'>
    print(kwargs) # {'favorite': 'pie', 'name': 'Austin'}
    print(args)


if __name__ == '__main__':
    """
    Any keyword arguments that are passed to a function fall into two groups:
    - 1) Those with a keyword that is an explicit parameter. This kind of keyword argument will fill the corresponding parameter and will NOT be
         included in **kwargs
    - 2) Those with a keyword that is NOT an explicit parameter. This kind of keyword argument will be shuffled into **kwargs
    - The keyword argument 'color' correctly fills in its assigned parameter, and is not included in **kwargs
        - Even if the 'color' argument is out of order, it still works just fine
    - If a keyword argument and a positional argument both fill in the same parameter, a TypeError is raised. Great!
    - An empty dictionary can be unpacked in a function call with no ill effects
    """
    #use_kwargs(color='yellow', name='Austin', favorite='pie') # works fine
    #use_kwargs(name='Austin', favorite='pie', color='yellow') # Also works fine even though color is 'out of order'
    #use_kwargs('blue', color='yellow', name='Austin', favorite='pie') # TypeError
    use_kwargs('green', 'Bill', **{})
    #unpack_dictionary(**{'name': 'Austin', 'age': '5'})
    #unpack_dictionary(*['Austin', '5']) # This works too!