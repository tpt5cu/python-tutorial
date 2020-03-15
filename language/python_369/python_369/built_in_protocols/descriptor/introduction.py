# https://realpython.com/python-descriptors/


'''
Recall that:
- A descriptor is a Python class that implements __get__(), and optionally __set__() and/or __delete__()
- A descriptor object must be assigned as an attribute of a class that "owns" the descriptor in order for the object to function as a descriptor
- Read the old notes for details on precedence look-up order:
    1) Data descriptors (have __get__() and one/both of __set__(), __delete__())
    2) Regular instance attributes
    3) Non-data descriptors (only have __get__())
'''