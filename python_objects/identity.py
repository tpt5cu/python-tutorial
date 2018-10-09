def identify_object():
    """Every object is assigned a unique id during its lifetime when it is initialized. It can be found with the id()
    function.

    As soon as an object has no more references, it is eligible for garbage collection. This means the literals 1 and 2
    could have the same id, as long as the 1 literal is reclaimed before the 2 literal is initialized.
    In my case, the code below happens not to reuse the same id, but this is not guaranteed.
    """
    print("literal 1 has id: " + str(id(1)))
    print("literal 2 has id: " + str(id(2)))
    print("literal 3 has id: " + str(id(3)))

    n = 300
    m = 300
    """Often Python will make two variables point to the same object in memory as an optimization as shown below.
    However, this behavior is not guaranteed."""
    print("id(n): " + str(id(n)))
    print("id(m): " + str(id(m)))


if __name__ == "__main__":
    identify_object()


