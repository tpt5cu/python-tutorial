# - If b.py is __main__, then this import causes no problems, regardless of what import style a.py is using
#   - This is an "unresolved_import", so "a" is already in the global symbol table of b when this statement is encountered again. Therefore, as far as
#     Python imports are concerned, this statement has been satisfied. It's almost like there are two execution stages of Python: the import stage and
#     the execution stage
# - If b.py is NOT __main__, then this line CAN cause an import cycle trap if a.py performed a resolved import of b.py AND the symbol(s) of the
#   resolved import are NOT resolved before this line is encountered
#   - In other words, if this import statement is moved below say_hello_from_b, there will be no ImportError
#       - Thus, it is NOT the case that simply using resolved import syntax in a cyle WILL cause an ImportError. It's more complicated than that.
#         Instead, a "resolved import" will cause an ImportError if and only if the symbol(s) that are being searched for are not resolved before THAT
#         importing module (i.e. a.py) is itself imported
#           - The proof of this is the fact that this is an unresolved_import AND it can cause an ImportError! It's the resolution of symbols that
#             matter, not whether the problematic recursive import is "resolved" or "unresolved" 
#           - This is further proved by the fact that if b.py imports c.py before the symbol is resolved, and c.py imports a.py, an ImportError
#             occurs!
from module_.import_.import_processing.resolved_import import a

# Don't even bother with this line. It's just the same problem mirrored a different way
#from module_.import_.import_processing.resolved_import.a import say_hello_from_a

# Test my theory that a.py -> b.py -> c.py -> a.py causes an ImportError when a.py uses a resolved import to get a symbol from b: It's true!!!!!!!
#import c


def say_hello_from_b():
    print('Hello from b.py')


if __name__ == '__main__':
    print('__main__ is b.py')
    say_hello_from_b()
    a.say_hello_from_a()