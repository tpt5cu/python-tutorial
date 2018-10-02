# https://realpython.com/python-string-formatting/


def string_interpolation():
    """Python has string interpolation, which allow me to use variables inside the string!"""
    num = 33
    name = "Allison"
    string = f"{name} is {num} years old today!"
    print(string)


if __name__ == "__main__":
    string_interpolation()