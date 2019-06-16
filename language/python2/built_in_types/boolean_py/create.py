"""
https://stackoverflow.com/questions/1748641/how-do-i-use-a-boolean-in-python
"""


def boolean_literal():
    """ There are only two boolean literals: True and False """
    my_true = True
    my_false = False
    also_true = True
    also_false = False
    print(my_true is also_true) # True
    print(my_false is also_false) # True
    print(type(my_true)) # <type 'bool'>


def evaluate_expression():
    """
    The built-in bool() function evaluates an expression and returns True or False.
    - 0 is False, any other integer is True
    - empty string is False, any other string is True
    - None is False
    - empty data structures are False. If a data structure contains 1 or more elements, it's True
    """
    print(bool("")) # False
    print(bool("\n")) # True
    print(bool(0)) # False
    print(bool(0.0)) # False
    print(bool(1)) # True
    print(bool(-1)) # True
    print(bool(None)) # False
    print(bool([])) # False
    print(bool([1])) # True
    print(bool({})) # False
    print(bool({"a": 1})) # True
    print(bool(())) # False
    print(bool((1,))) # True
    print(bool((0,))) # True, ironically


if __name__ == "__main__":
    boolean_literal()
    #evaluate_expression()