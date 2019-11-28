class PermanentName(object):
    '''This is a data descriptor'''

    def __get__(self, instance, owner):
        #print('Invoked PermanentName __get__()')
        return instance.__dict__['_name']
    
    def __set__(self, instance, value):
        '''
        A data descriptor must set the attribute on the instance itself, otherwise it will never be set because the data descriptor intercepts every
        access of that specific attribute!
        '''
        #print('Invoked PermanentName __set__')
        if instance.__dict__.get('_name') is None:
            instance.__dict__['_name'] = value
        else:
            print('The name is read-only!')

    #def __delete__(self, instance):
    #    '''This is called in order to delete the attribute on the instance'''
    #    pass


class DoWork(object):
    '''This is a nondata descriptor'''

    def __get__(self, instance, owner):
        return 'Non-data descriptor did some work'


class Foo(object):
    '''A data descriptor's variable name must match the instance attribute that it wants to shadow '''

    _name = PermanentName()
    do_work = DoWork()

    def __init__(self, name):
        self._name = name
    
    def __getattr__(self, attribute):
        return "Here's a default value"

    def say_name(self):
        '''A method is actually a non-data descriptor!'''
        print('My name is {}'.format(self._name))
    

def delete_data_descriptor():
    '''
    - In order to delete a data descriptor itself, I must delete it off of the class object
        - Attempting to delete the data descriptor off of the instance will trigger Python to invoke the __delete__() method of the descriptor
    '''
    f = Foo('Maurice')
    print(f._name) # Maurice
    f._name = 'Joseph'
    print(f._name) # Maurice
    # This raises an AttributeError because the data descriptor does not implement __delete__()
    #del f._name # AttributeError: __delete__
    # Here I remove the data descriptor. If I were to instead set Foo._name = None, that would not be correct. There would now be a class attribute
    # called "_name" with a value of None
    del Foo._name
    f._name = 'Ziggy'
    print(f._name) # Ziggy
    del f._name
    print(f._name) # Here's a default value
    #del f._name # AttributeError: _name


def delete_nondata_descriptor():
    '''
    - In order to delete a non-data descriptor itself, I must delete it off of the class object
        - Attempting to delete the non-data descriptor off of the instance will fail.
            - I don't know why, because I thought that dot access (which is cleary able to find the non-data descriptor) would be completed before the
              del statement executed, but whatever
    '''
    f = Foo('Taft')
    print(f.do_work) # Non-data descriptor did some work
    f.do_work = 'something new'
    print(f.do_work) # something new
    del f.do_work
    print(f.do_work) # Non-data descriptor did some work
    #del f.do_work # AttributeError: do_work
    del Foo.do_work
    print(f.do_work) # Here's a default value


if __name__ == '__main__':
    #delete_data_descriptor()
    delete_nondata_descriptor()