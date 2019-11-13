# https://realpython.com/python-type-checking/
# https://stackoverflow.com/questions/1549801/what-are-the-differences-between-type-and-isinstance
# https://stackoverflow.com/questions/21024913/python-isinstance-vs-hasattr-vs-try-except-what-is-better


"""
Apparently the "Pythonic" way of type-checking is to use an argument as if it were the proper type in a try-except block, and to do something else if
the argument was not the expected type in the except-block. I'm also supposed to catch specific exceptions.
"""


def is_string():
    print(isinstance("hello", str)) # True
    print(isinstance(u'goodbye', basestring)) # True
    print(isinstance(True, str)) # False

def is_int():
    print(isinstance(4, int)) # True
    print(isinstance(4.0, int)) # False

def is_float():
    print(isinstance(2.0, float)) # True
    print(isinstance(2, float)) # False

def get_float():
    #tolerance = "5"
    tolerance = "5.s"
    try: 
        my_float = float(tolerance) 
    except: 
        my_float = None
    print(my_float) # 5.0, None

if __name__ == "__main__":
    is_string()
    #is_int()
    #is_float()
    #get_float()