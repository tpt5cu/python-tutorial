# https://docs.python.org/2.7/reference/datamodel.html#object.__lt__
# https://devinpractice.com/2016/11/29/python-objects-comparison/


'''
- I can implement any subset of rich comparison methods for a class that I want
    - That being said, I must implement the correct subset or I'll get weird results. For example, x == y does not (by default) imply that x != y. The
      best solution is to supply one of __lt__(), __le__(), __gt__(), __ge__() and an __eq__(), then use functools.total_ordering.
- Rich comparison operators are Python's way of providing operator overloading
'''


class Business(object):

    def __init__(self, asset_worth, debt):
        self.asset_worth = asset_worth
        self.debt = debt

    def __lt__(self, other):
        '''
        Typically, rich comparison methods return True or False, but they can return whatever I want. Remember, defining this method does not define
        an overloaded operator for any other comparision.
        '''
        # In Python 2, I'm relying on the implementation of __cmp__() behavior for ints to make this method work.
        return self.asset_worth - self.debt < other.asset_worth - other.debt 

    def __gt__(self, other):
        return True

    def __eq__(self, other):
        return 'Yes'

    def __ne__(self, other):
        return self.asset_worth - self.debt != other.asset_worth - other.debt


def compare_businesses():
    dog_groomer = Business(1000, 200)
    uber_driver = Business(3000, 1000)
    print(dog_groomer < uber_driver) # True
    print(dog_groomer > uber_driver) # True
    print(dog_groomer == uber_driver) # Yes
    print(dog_groomer != uber_driver) # True


if __name__ == '__main__':
    compare_businesses()