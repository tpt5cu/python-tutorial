# https://docs.python.org/2/reference/datamodel.html#object.__contains__


class Name(object):

    def __init__(self, name):
        self._name = name

    def __contains__(self, item):
        '''
        The __contains__ special method defines behavior for the "in" operator
        - Return True if the item is contained within, else False
        '''
        for c in self._name:
            if c.lower() == item.lower():
                return True
        return False


def is_letter_in_name():
    n = Name('Bart')
    print('b' in n) # True
    print('A' in n) # True



class Vacation(object):
    '''
    If a class doesn't define __contains__, the "in" operator tries to see if the item is inside by 1) iterating via __iter__() or 2) using old-style
    iteration via __getitem__()
    '''

    def __init__(self, locations):
        self._locations = locations

    def __iter__(self):
        '''Vacation instances are now iterable'''
        return iter(self._locations)


def is_location_in_locations():
    v = Vacation(['Rome', 'China'])
    print('China' in v) # True


if __name__ == '__main__':
    is_letter_in_name()
    #is_location_in_locations()