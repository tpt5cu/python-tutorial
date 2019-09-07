def different_base():
    print(int("r", 28)) # Create a base-28 number. "r" in base-28 is 27
    print(int("rr", 28)) # Create a base-28 number. (27 * 28) + 27 = 783


if __name__ == "__main__":
    different_base()