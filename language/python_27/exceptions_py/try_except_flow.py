# https://docs.python.org/2.7/tutorial/errors.html


def try_except_else_finally():
    """
    There can be 1 optional else-clause that can follow all except-clauses. The else-clause will execute after the try-clause if and only if the
    try-clause did not raise any exceptions
    - If a try-clause returns, an else clause will not execute
    - A finally-clause will always execute regardless of what happens elsewhere
        - If the try-clause returns, the finally-clause gets executed first
        - If an except clause does not handle an exception, the exception is re-raised after the finally-clause
    """
    try:
        # IOError
        #with open('made-up-file-hahah.txt') as f:
        #    print(f.read())
        # UnboundLocalError
        asdf = asdf 
        #x = 1
        #return x
    except IOError as e:
        print("There was an IOError!")
    # This else-clause is valid, but it makes any succeeding else or except clause invalid!
    #else:
    #    print("Invalid syntax")
    except ZeroDivisionError as e:
        print("There was a ZeroDivisionError!")
    else:
        print("Continuing to execute as normal")
    finally:
        print("This always executes no matter if the try-clause returns or an exception was raised")


if __name__ == "__main__":
    val = try_except_else_finally()
    print("val was: " + str(val))