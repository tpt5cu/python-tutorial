def divide():
    """
    - Division between ints is floor division, regardless of / or //
    - Division with at least one float is regular division
    - Floor division with at least one float will result in a float that is floored to the next integer value
    """
    print(5 / 4) # 1
    print(5.0 / 4) # 1.25
    print(5 / 4.0) # 1.25
    print(5 // 4) # 1
    print(5.0 // 4) # 1.0

def exponentiate():
    print(5 ** 2) # 25
    print(2 ** 5) # 32
    print(2.1 ** 5) # 40.84101

if __name__ == "__main__":
    #divide()
    exponentiate()
