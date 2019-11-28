# https://realpython.com/primer-on-python-decorators/ - See "Both Please, But Never Mind the Bread"


from introduction import repeat


def optional_introduction(_func=None, introduction=None):
    def cool_decorator(func):
        def wrapper(*args, **kwargs):
            if introduction:
                print(introduction)
            func(*args, **kwargs)
            return 'Irrelevant return value'
        return wrapper
    if _func is None:
        # In this case, optional_introduction() was called with keyword arguments (and none of those keyword arguments was _func; this is an
        # unfortuante invocation requirement to make this work). Thus, I need to return the un-invoked cool_decorator() so that it can later be
        # invoked by the implicit @cool_decorator call, which translates to cool_decorator(say_name)(name='Billy Strings')
        # - Keep in mind that cool_decorator() was already modified by the closure which set the value of the "introduction" variable
        return cool_decorator 
    else:
        # In this case, optional_introduction() was called without arguments, so immediately apply cool_decorator() to the def function. It's like
        # cool_decorator() had always existed as the outermost scope and that optional_introduction() was never even there. No further Python
        # interpreter processing will occur because optional_introduction was invoked as @optional_introduction
        return cool_decorator(_func)


# What if I want a decorator that can take entirely optional arguments? repeat() as it is written is not able to do this.
# In this case, say_aloha fills in the num_times argument. Then, decorator_repeat() is invoked but it doesn't get any arguments!
#@repeat # TypeError: decorator_repeat() takes exactly 1 argument (0 given)
# In this case, num_times argument is entirely absent
#@repeat() # TypeError: repeat() takes exactly 1 argument (0 given)
# In this case, 'Sup' fills in the _func argument
#@optional_introduction('Sup') # TypeError: 'str' object is not callable
def say_aloha():
    print('Aloha!')


# This is invoking optional_introduction() so that it returns a modified version of cool_decorator(). Think of it this way:
# 1) option_introduction(introduction='Welcome everyone!'): create a closure and return a modified, un-invoked version of cool_decorator()
# 2) @option_introduction: invoke the modified version of cool_decorator()
# - It's a 2-step process that works from right to left
# - The non-function arguments MUST MUST MUST be passed by keyword, or they will take up the place of _func!
#   - It's too bad that the "*" syntax (keyword-only arguments) is only available in Python 3
@optional_introduction(introduction='Welcome everyone!')
def say_name(name):
    print('Hello my name is {}!'.format(name))


if __name__ == '__main__':
    say_aloha() # Aloha!
    say_name('Billy Strings') # Welcome everyone! Hello my name is Billy Strings!