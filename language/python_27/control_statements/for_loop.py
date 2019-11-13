def reverse_iteration():
    """
    There isn't really reverse iteration in Python. I can iterate forwards over a list that is sorted in decreasing order. I could also use the
    reversed() function, which presumably reverses and returns a sequence
    """
    for i in range(10, 0, -1):
        print(i)
    print("")
    for i in reversed(range(10)):
        print(i)


if __name__ == "__main__":
    reverse_iteration()