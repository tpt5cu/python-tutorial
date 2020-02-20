# This line CAN cause an ImportError for that exact same reason as the mirror line in b.py. But don't think about it too hard. Just always treat a.py
# as the entry point and this whole problem will be easier to understand
#from module_.import_.import_processing.complete_imports import b

# If 
# 1) a.py is __main__ and
# 2) b.py performs either style of import of a.py BEFORE the symbol(s) that a.py needs from b.py are resolved
# Then this line causes an ImportError
from module_.import_.import_processing.resolved_import.b import say_hello_from_b


'''
Summary: "resolved imports" can cause ImportErrors. A true resolved import only occurs when symbols from an actual MODULE need to be resolved, not
when a module of a package needs to be resolved.
'''


'''
Why does this ImportError situation occur? Let's review
1) Python sees that it cannot simply add "b" to the global symbol table of "a". When the "resolved import" syntax is used like this, b never enters
   into the symbol table of a. The only thing that should be added to the symbol table of a is "say_hello_from_b", so Python dives into b to tries and
   find that symbol. Python needs to create a reference to "say_hello_from_b" inside of a.py. As soon as it finds that symbol (if it can), control
   will return to a.py
2) Python searches in b to find "say_hello_from_b". An import error can occur or not (see notes)
'''


def say_hello_from_a():
    print('Hello from a.py')


if __name__ == '__main__':
    print('__main__ is a.py')
    say_hello_from_a()
    b.say_hello_from_b()
    