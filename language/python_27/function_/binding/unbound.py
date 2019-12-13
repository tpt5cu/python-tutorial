def do_stuff():
    print('Doing stuff')


class Orange(object):
    family = 'Rutaceae'
    genus = 'Citrus'

    def __init__(self, species):
        self._species = species
    
    def peel(self):
        print('Peeled the {} orange'.format(self._species))

    do_things = do_stuff

    @classmethod
    def state_biological_classification(cls):
        print('The orange is in the family {} and the genus {}'.format(cls.family, cls.genus))


def unbound_method_type_checking():
    '''
    When a non-static, non-class function is accessed directly through a class object (i.e. not the __dict__ of the class object), it is transformed
    into an unbound method.
    - An unbound method will type check its first argument to ensure that it is the same type as the class to which it belongs
        - This is the most useful difference between an unbound method and a function
    '''
    print(Orange.peel) # <unbound method Orange.peel>
    print(Orange.__dict__['peel']) # <function peel at 0x10d9260d0>
    print(Orange.do_things) # <unbound method Orange.do_stuff>
    o = Orange('Florida')
    Orange.peel(o) # Peeled the Florida orange
    #Orange.peel({'foo': 'bar'}) # TypeError: unbound method peel() must be called with Orange instance as first argument (got dict instance instead)
    #Orange.__dict__['peel']({'foo': 'bar'}) # AttributeError: 'dict' object has no attribute '_species'


def unbound_method_class_awareness():
    '''
    Implicitly, an unbound method knows which class it is bound to in order to perform type checking
    - __class__: the class/type of the the object it was referenced from
    - im_class: the class of the instance (for bound methods) or the class that the method was referenced from (for unbound methods)
    '''
    ubm = Orange.peel 
    print(ubm) # <unbound method Orange.peel>
    # I suppose an unbound method is an instance method as well
    print(ubm.__class__) # <type 'instancemethod'>
    print(ubm.im_class) # <class '__main__.Orange'>
    f = Orange.__dict__['peel']
    print(f) # <function peel at ...>
    print(f.__class__) # <type 'function'>
    # Function objects of course have no associated class. This distinction between functions and unbound doesn't seem that useful. No wonder
    # unbound methods were removed in Python 3
    #print(f.im_class) # AttributeError


def examine_unbound_method_attributes():
    '''
    - im_self (i.e. __self__): None
    - im_class: the class which the method was created from
    - im_func: the original function object which is accessible a variety of ways
    '''
    m = Orange.peel
    #print(dir(m))
    print(m) # <unbound method Orange.peel>
    # The method is unbound, so by definition __self__ is None
    print(m.im_self) # None
    # True for compatibility reasons
    print(m.im_self is m.__self__) # True
    print(m.im_class) # <class '__main__.Orange'>
    print(m.im_func) # <function peel at 0x101692350>


if __name__ == '__main__':
    #unbound_method_type_checking()
    #unbound_method_class_awareness()
    examine_unbound_method_attributes()