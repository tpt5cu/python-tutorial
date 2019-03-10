# https://www.programiz.com/python-programming/methods/string


def ends_with():
    """Self explanatory."""
    string = "I am a cool string/test"
    print(string.endswith("/test"))
    print(string.endswith("/testz"))


def find():
    """<str>.find() returns -1 if the substring doesn't exist, else the starting index of the substring.
    There is no <str>.contains() method, so this is the next best thing.
    """
    string = "IsTheNameOfTheGameDistribution?"
    print("find() is case sensitive: " + str(string.find("distribution")))
    print(string.find("Distribution"))


if __name__ == "__main__":
    #ends_with()
    find()