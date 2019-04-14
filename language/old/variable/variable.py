"""These docstrings are not used correctly at all (same with docstrings in most of these modules).
I just like my explanations to easily span multiple lines and I like the green text color.
"""


def assign_variable():
    """Python is dynamically typed, so variables are 1) not declared with a type 2) can be reassigned to a value
    of any type.
    """
    number = 300
    number = "quack"
    print(number)
    """This is an example of chained assignment. Three different variables have been assigned the same value."""
    a = b = c = 4.2


def object_references():
    """A Python variable is a reference to an object which contains data (just like other languages).
    For example, creating a 500 number literal creates an object of the <class 'int'>. This is verified
    by using the built-in type() function.
    """
    print("Any literal is actually encapsulated by an object of a class: " + str(type(500)))


def reassign_variable():
    a = 5
    b = a
    print("When a variable is assigned to another variable, the assigned variable is merely made to point to the "
          "same object. 'b' does NOT point directly at 'a'. 'b' is: " + str(b))
    a = 100
    print("'a' was reassigned to a new object, but 'b' still points to the original object that 'a' previously pointed"
          " to: " + str(b))


def multivariable_assignment():
    a=b=c = None
    print(a, b, c)


if __name__ == "__main__":
    #assign_variable()
    #object_references()
    #reassign_variable()
    multivariable_assignment()
