# https://stackoverflow.com/questions/1748641/how-do-i-use-a-boolean-in-python


def two_boolean_literals():
    """There are only two boolean literals: True and False."""
    my_true = True
    my_false = False
    also_true = True
    also_false = False
    print(my_true is also_true) # True
    print(my_false is also_false) # True
    print(type(my_true)) # <type 'bool'>



def create_false_expression():
    """
    - Empty data structures are False
    - 0 is False
    - A non-empty data structure containing falsy values is True! If it seems like it's False, it's probably because I wrote an expression (e.g. (0))
      instead of a single element tuple (e.g. (0,))
    """
    print(bool("")) # False
    print(bool([])) # False
    print(bool({})) # False
    print(bool(())) # False
    print(bool(0)) # False because 0 is False
    print(bool((0))) # False because (0) is an expression that evaluates to 0 which is False
    print(bool((0,))) # True
    print(bool((0, 0, 0, False, 0))) # True
    print(bool(0.0)) # False
    print(bool(None)) # False


def create_true_expression():
    """
    - Non-empty data structures are True
    - Numbers other than 0 are True
    """
    print(bool("\n")) # True
    print(bool(1)) # True
    print(bool(2)) # True
    print(bool(-1)) # True
    print(bool([1])) # True
    print(bool({"a": 1})) # True
    print(bool((1,))) # True
    print(bool((0,))) # True, ironically


def booleans_are_integers():
    """
    Apparently 1 is special in that 1 == True is True, but for other "truthy" numbers (i.e. numbers that aren't 0), the result of <num> == True is
    False. See: https://stackoverflow.com/questions/2764017/is-false-0-and-true-1-in-python-an-implementation-detail-or-is-it-guarante. This is
    because booleans are a subclass of integers.
    """
    print(1 == True) # True
    print(1 is True) # False
    print(2 == True) # False
    print(0 == True) # False
    print(0 == False) # True
    # All of this is wild
    l = ["Some", "strings"]
    print(l[True]) # strings
    print(l[False]) # Some
    print(1 + True) # 2
    print(10 - True) # 9
    print(True * 77) # 77


if __name__ == "__main__":
    #two_boolean_literals()
    #create_false_expression()
    #create_true_expression()
    booleans_are_integers()