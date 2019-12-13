# https://stackoverflow.com/questions/13646245/is-it-possible-to-make-abstract-classes-in-python


from numbers import Number
from abc import ABCMeta, abstractmethod

'''
An abstract class CAN be instantiated if it doesn't have any abstract methods. However, that's silly. Provided that an abstract method has at least
one abstract method, it cannot be instantiated
- An abstract class could be used to represent an interface, provided that all of its methods were abstract. However, this goes against the Python
  philosophy of duck typing
'''

class MyAbstractClass():

    __metaclass__ = ABCMeta

    @abstractmethod
    def perform_calculation(self, value):
        if not isinstance(value, Number):
            raise TypeError('Argument should be a number')

    @abstractmethod
    def say_hi(self):
        print('Hello!')


class MyConcreteClass(MyAbstractClass):

    def perform_calculation(self, value):
        super(MyConcreteClass, self).perform_calculation(value)
        return value / 2.0

    def say_hi(self, name):
        '''
        Method overriding in Java requires the method signature in the child to match the method signature in the parent. This is not a requirement
        for method overriding in Python
        '''
        #super(MyConcreteClass, self).say_hi()
        print('Hello, {}'.format(name))


def examine_classes():
    #ab = MyAbstractClass() # TypeError: cannot instantiate abstract class with abstract methods
    cc = MyConcreteClass()
    print(cc.perform_calculation(4)) # 2.0
    #cc.perform_calculation('yay') # TypeError: Argument should be a number
    cc.say_hi('Mark') # Hello, Mark


if __name__ == '__main__':
    examine_classes()