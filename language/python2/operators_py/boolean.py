"""
https://www.programiz.com/python-programming/methods/built-in/bool
"""

"""
The boo() built-in function takes only 1 argument
These values are false:
- None
- False
- 0, 0.0, etc.
- Empty sequences: "", (), [], {} 

All other values are True
"""

def my_bool():
    """ Non-empty sequences are always True, regardless of their contents """
    b = bool((1 == 2, "Hello"))
    print(b)
    b = bool((1 == 2, 3 == 4))
    print(b)

if __name__ == "__main__":
    my_bool()