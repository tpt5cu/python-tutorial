# https://stackoverflow.com/questions/11502268/how-does-pythons-comma-operator-works-during-assignment
# https://stackoverflow.com/questions/2535760/python-try-except-comma-vs-as-in-except


"""Normally, I see the "," character in lists, tuples, dictionaries, sets, etc. In those contexts, it's just a normal comma"""


def sequence_unpack():
    """Commas on the left-hand side indicate that values should be unpacked from a sequence"""
    my_list = [1, 2, 3, 4, 5]
    a, b, c, d, e = my_list
    print(e)
    a, b = "HI"
    print(b)


def make_tuple():
    """Commas on the right-hand side indicate that the right-hand value is a tuple"""
    thing = 1, 2, 3, 4
    print(type(thing))


def exception_alias():
    """The comma is used in versions of Python earlier than 2.6 instead of the 'as' keyword"""
    try:
        #result=1/0
        raise Exception
    except ZeroDivisionError, e:
        print("ZeroDivisionError")
        print(e.message if e.message != "" else 'no message')
    except Exception, e:
        print("Exception")
        print(type(e.message)) # <type 'str'>
        print(e.message if e.message != "" else 'no message')


if __name__ == "__main__":
    #sequence_unpack()
    #make_tuple()
    exception_alias()