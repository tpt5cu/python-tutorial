def rounding():
    """Python rounds floating point values <= x.5 downwards, and values > x.5 upwards."""
    num1 = round(4.1)
    num2 = round(4.5)
    num3 = round(4.51)
    print(str(num1) + " " + str(num2) + " " + str(num3))


if __name__ == "__main__":
    rounding()