# https://docs.python.org/2.7/reference/datamodel.html#more-attribute-access-for-new-style-classes
# https://stackoverflow.com/questions/37912229/disable-descriptor-object-in-python - disable descriptors for fun, but it didn't work


'''
Try stepping through with the debugger to understand how the correct __getattribute__() is invoked every time there is a dot access
- TLDR: don't ever implement __getattribute__(), and don't try to completely disable the descriptor protocol
'''


'''
For class instances, object.__getattribute__() transforms b.x into type(b).__dict__['x'].__get__(b, type(b))
- First, the class dictproxy will be examined. If 'x' exists in the dictproxy and is a descriptor, then the descriptor will be invoked. Neat!
- What about when 'x' doesn't exist in the dictproxy? In that case, ... I don't know. I guess normal attribute look-up occurs?
- Overriding __getattribute__() in a class prevents automatic descriptor calls
    - However, the descriptor protocol will still work if object.__getattribute__() is called at some point (which it almost always will be)
'''


class Vehicle(object):

    def __init__(self, wheel_count):
        self._wheel_count = wheel_count

    def __getattribute__(self, name):
        '''
        - If this function returns None, then looking up any attribute on an instance of this class will show that the attribute contains a value of
          None. 
          - In fact, even attempting to get the __dict__ of the instance will return None! Now, is the __dict__ actually None? Is the desired
            attribute actually None? I don't think so, but I don't think there's any way to bypass the __getattribute__() invocation while inspecting
            the contents of the object. Maybe there is a way, but it's irrelevant because I should almost never be overriding this function anyway
        '''
        # This line was messing everything up. Why? Because this line makes the function returns None! So the vehicle will have a _wheel_count of
        # None!
        #object.__getattribute__(self, name)
        print(name) # _wheel_count
        val = object.__getattribute__(self, name) # 8
        return val


class AirbagCount(object):
    '''This is a data descriptor'''

    def __get__(self, instance, owner):
        return instance.__dict__['_airbag_count']

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__['_airbag_count'] = value
        else:
            print('The airbag count cannot be zero or less')


class Car(Vehicle):

    _airbag_count = AirbagCount()

    def __init__(self, wheel_count, airbag_count):
        super(Car, self).__init__(wheel_count)
        self._airbag_count = airbag_count

    def __getattribute__(self, name):
        '''
        - In order to avoid infinite recursion, this method should always call the base class method's __getattribute__()
        - This method is supposed to return the computed attribute value
        - The docs say that "overriding __getattribute__() prevents automatic descriptor calls," but no matter what I do the AirbagCount descriptor is
          still called
        '''
        # Infinite recursion
        #self.__getattribute__(self, name)
        # Infinite recursion
        #return getattr(self, name)
        # Infinite recursion
        #val = self.__dict__[name]
        # Doing this makes the descriptor protocol function normally
        val = Vehicle.__getattribute__(self, name)
        return val


def create_vehicle():
    v = Vehicle(8)
    print('The vehicle has {} wheels'.format(v._wheel_count)) # The vehicle has 8 wheels


def create_car():
    c = Car(4, 2)
    print('The car has {} wheels and {} airbags'.format(c._wheel_count, c._airbag_count)) # The car has 4 wheels and 2 airbags


if __name__ == '__main__':
    #create_vehicle()
    create_car()