# https://realpython.com/primer-on-python-decorators/ - I have read this entire document up until classes as decorators. There is SO much
# https://stackoverflow.com/questions/13931633/how-can-a-flask-decorator-have-arguments
# https://stackoverflow.com/questions/1166118/how-to-strip-decorators-from-a-function-in-python


import random
from functools import wraps


'''
Decorators are especially useful when I have some larger functionality that is common to a bunch of small functions. I can refactor those small
functions so that they only have their bare logic, then the decorator can use their return values.
'''
def my_decorator(func): # The decorator should always just take a function
    # @wraps updates special attributes like __name__ and __doc__ that are used for introspection. Without this decorator, any function decorated by
    # @my_decorator is referred to as "wrapper", which is technically correct as that is the inner function here. However, it is more useful to have
    # the function yes_or_no referred to as "yes_or_no" instead of "wrapper" for example.
    @wraps(func) 
    # The wrapper should always have *args and **kwargs so that all arguments passed into it can be seen by the wrapped function
    def wrapper(*args, **kwargs): 
        val = func(*args, **kwargs)
        return "The response was: " + val
    return wrapper

'''These two functions are very similar. Instead of writing their shared logic twice, I can wrap them in the same decorator.'''
@my_decorator
def yes_or_no(rand):
    return "yes" if rand > 0.5 else "no"


@my_decorator
def hi_or_low(rand):
    return "high" if rand > 0.5 else "low"


def red_or_blue(rand):
    return "red" if rand > 0.5 else "blue"


def use_my_decorator():
    for x in range(5):
        print(yes_or_no(random.random()))
        print(hi_or_low(random.random()))
        print(my_decorator(red_or_blue)(random.random())) # This is how to do it without nice pretty decorators


def use_plain_function():
    '''
    There is no easy built-in way to use the undecorated version of a function because technically the plain function doesn't exist anymore
    - In this example, yes_or_no() can no longer simply return "yes" or "no". It returns the full sentence because the decorator enforces that behavior
    '''
    print(yes_or_no(random.random()))


'''
Decorators can take arguments. This is not essential to use custom decorators in Flask. In order for the uppermost argument to be bound in a closure,
I need to use the same argument name.
'''
def repeat(num_times): # Use this to make a closure
    def decorator_repeat(func):
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times): # Here is the closure
                value = func(*args, **kwargs)
            # wrapper_repeat() returns a value ONCE. It also happens to use the wrapped function
            return "I am the return value that will be returned during run-time" 
        # decorator_repeat() returns a function. When THAT returned function is invoked, it will return a value once (but in this case it will also print x times)
        return wrapper_repeat 
    # repeat() returns a function. When THAT function is invoked, it EXPECTS a function as an argument AND it returns a function.
    return decorator_repeat 


# repeat() will RETURN a function. And guess what? THAT function can be used as a decorator! The arguments that were passed to repeat() are just bound
# in a closure. Thus, @repeat(num_times=4) == @decorator_repeat with a closure value of 4
@repeat(num_times=5)
def say_hello():
    print("Hello there!")


if __name__ == "__main__":
    #use_my_decorator()    
    #use_plain_function()
    print(say_hello())