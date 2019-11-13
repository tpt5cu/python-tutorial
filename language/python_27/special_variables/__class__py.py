"""
The __class__ attribute of an object is a refernce to the class object that created the instance.
"""

class CoolClass(object):
    pass


def examine_class():
    cc = CoolClass()
    print(cc.__class__ is CoolClass) # True


if __name__ == "__main__":
    examine_class()