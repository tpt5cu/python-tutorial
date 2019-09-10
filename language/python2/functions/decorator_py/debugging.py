


"""
How do I debug a function that has been modified with a decorator?
- Putting a breakpoint at the invocation of the decorator (i.e @<say_hello>) just goes directly into the decorated function itself. It does not go into
  the decorator 'say_hello' like I wanted. In fact, everything in the wrapper before 'return func(...)' has already executed by this point!
    - This means that 1) 'say_hello' has already executed and returned the 'wrapper()' function 2) 'add_numbers()' is really invoking 'wrapper()', and
      'wrapper()' has already executed part of its code
- Putting a breakpoint inside of the decorator pauses execution before a breakpoint at the invocation of the decorator (i.e. @<say_hello>). This is
  what I want, but it means I have to find the source code where the decorator was defined and put a breakpoint there. How annoying!
- I need to put the breakpoint at the invocation of the decorated function itself (i.e. add_numbers(...)). Pausing execution here actually will allow
  me to step through the wrapper function itself like I wanted
"""


def say_hello(func):
    def wrapper(*args, **kwargs):
        print("I say hello!")
        return func(*args, **kwargs)
    return wrapper


@say_hello
def add_numbers(x, y):
    return x + y


if __name__ == "__main__":
    print(add_numbers(5, 6)) # Here is where the breakpoint should go in order to step through the 'wrapper()' function