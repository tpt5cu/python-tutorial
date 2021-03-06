# https://stackoverflow.com/questions/1549801/what-are-the-differences-between-type-and-isinstance


import numbers


'''
In Python, the preferred way of checking types is duck typing: try to use the object as if it is the expected type inside of a try-except block, and
if an exception is raised, deal with it. 
'''
class MyList(list):
    pass


def isinstance_vs_type():
    '''
    type(<obj>) returns the class object that created <obj>. Thus, it is unsuitable for inheritance. By contrast, isinstance(<obj>, <class>) will
    return True if <obj> is a subclass of <class>
    '''
    ml = MyList()
    print(type(ml) is MyList) # True
    print(type(ml) is list) # False
    print(isinstance(ml, MyList)) # True
    print(isinstance(ml, list)) # True


def number_hierarchy():
    '''int and float are subclasses of numbers.Number, not each other'''
    print(isinstance(4.0, int)) # False
    print(isinstance(4, float)) # False
    print(isinstance(4.0, numbers.Number)) # True
    print(isinstance(4, numbers.Number)) # True


if __name__ == '__main__':
    #isinstance_vs_type()
    number_hierarchy()