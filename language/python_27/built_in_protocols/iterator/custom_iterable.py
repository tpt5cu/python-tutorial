# https://stackoverflow.com/questions/9884132/what-exactly-are-iterator-iterable-and-iteration - __getitem__() can be used to implement an iterable
# https://stackoverflow.com/questions/926574/why-does-defining-getitem-on-a-class-make-it-iterable-in-python - official doc on why __getitem__() can
# be used to implement an iterable


'''
__getitem__() can be used to implement an iterable because that's how it was done before the iterator protocol existed, not because it's a good idea.
__getitem__() predates the iterator protocol. 
'''


class MyContainer(object):

    def __init__(self, *args):
        self.data = lambda x: None # Functions can be assigned arbitrary attributes, so use it as an object!
        count = 0
        for item in args:
            setattr(self.data, str(count), item)
            count += 1

    def __getitem__(self, idx):
        """Apparently if an object defines this method, it is iterable"""
        # Infinite iteration
        #pass 
        # Infinite iteration
        #return None 
        # This works and demonstrates how to create an iterable object that isn't using a built-in iterable type already, but it's really dumb
        try:
            return getattr(self.data, str(idx))
        except:
            raise IndexError


def iterate_over_my_container():
    obj = MyContainer(7, 8, 9, 10)
    #getattr(obj, "5") # AttributeError
    #obj[str(5)] # IndexError
    for x in obj:
        print(x)
    print("done")


if __name__ == "__main__":
    iterate_over_my_container()