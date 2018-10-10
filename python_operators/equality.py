# https://stackoverflow.com/questions/132988/is-there-a-difference-between-and-is-in-python


def is_operator():
    """This 'is' operator is ONLY used to check if two variables point to the same object. That's it"""
    a = ["list", "of", "things"]
    b = a
    c = ["list", "of", "things"]
    if b is a:
        print("a and b point to the same object")
    if c is a:
        print("a and c point to the same object")


def equals_operator():
    """== returns true ONLY if two objects are deeply equivalent in value. It just so happens that an object has a value
    equal to itself, so 'is' would always return true too.
    """
    a = ["list", "of", "things", {1: "foo"}]
    c = ["list", "of", "things", {1: "foo"}]
    if a == c:
        if a is not c:
            print("a and c are equal in value, but are not the same object.")


if __name__ == "__main__":
    # is_operator()
    equals_operator()