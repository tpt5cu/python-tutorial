
def unpack_dictionary(name, age):
    """The ** syntax is also used to unpack a dictionary into a function that is being invoked"""
    print(name)
    print(age)


"""If **kwags is used, it must be the last parameter. *args must come before **kwargs"""
#def use_kwargs(**kwargs, age):
#def use_kwargs(**kwargs, *args):
def use_kwargs(*args, **kwargs):
    """**<whatever> (commonly "**kwargs") is a regular old dictionary"""
    print(type(kwargs)) # <type 'dict'>
    print(kwargs) # {'name': 'Austin'}
    print(args)


if __name__ == "__main__":
    #use_kwargs(5, name="Austin")
    unpack_dictionary(**{"name": "Austin", "age": "5"})
    unpack_dictionary(*["Austin", "5"]) # This works too!