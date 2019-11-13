def assign_with_ternary():
    """Assignment can be done with the ternary operator. It's intuitive syntax"""
    var = 'first' if 1 == 1 else 'second'
    print(var) # first
    var = 'hello' if 2 == 1 else 'goodbye'
    print(var) # goodbye
    var = 'yes' if (1 == 3 or 2 == 2.0) else 'no'
    print(var) # yes


if __name__ == "__main__":
    assign_with_ternary()