# https://stackoverflow.com/questions/27954695/what-is-a-sibling-class-in-python - kinda confusing lmao, but the main points are good enough
# https://rhettinger.wordpress.com/2011/05/26/super-considered-super/ - how the functionality of super() can be used (along with other techniques) to
# tweak inheritance hierarchies (no notes here on this)


class ClassA(object):

    def say_hello(self):
        print "say_hello from ClassA instance"


class ClassB(ClassA):

    def say_hello(self):
        print('About to call super from ClassB')
        print "say_hello from ClassB instance"


class ClassC(ClassA):

    def say_hello(self):
        '''
        The result of this method call depends on how this method was invoked
        - If it was invoked directly on a ClassC instance, then the super() call goes straight to ClassA. This is because ClassC is not by itself
            aware that it has a sibling class
        - If it was invoked from a ClassD instance, then the super() call first goes to ClassB. This is because Python is now aware that ClassC has
            a sibling class because of how 1) ClassD inherits from ClassC and ClassB and 2) ClassC and ClassB both inherit from ClassA
            - This is an example of Diamond inheritance in action. Diamon inheritance is required in order to define sibling classes. This is proven
              by the fact that ClassDPrime never has ClassB in its look-up hierarchy
        '''
        print('About to call super from ClassC')
        super(ClassC, self).say_hello()


class ClassD(ClassC, ClassB):

    def say_hello(self):
        '''
        Class B and class C both inherit from class A. Class B is a sibling of class C, and class C is a sibilng of class B.
        - ClassD has no sibling class.
        - The look-up of the method say_hello() is ClassC -> ClassB. Why? 
            - Apparently sibling classes take precedence over parent classes, so ClassB comes before classA in the look-up process
            - If ClassB were itself to call super().say_hello(), then next ClassA().say_hello() would be called. Thus, sibling classes take
              precedence over parent classes, but parent classes are by no means ignored
        '''
        # About to call super from ClassC
        # About to call super from ClassB
        # say_hello from ClassB instance
        super(ClassD, self).say_hello() 


class ClassDPrime(ClassC):
    '''
    ClassC might have ClassB as a sibling class conceptually, but from the standpoint of ClassDPrime, ClassB doesn't exist so ClassC doesn't have a
    sibling class
    '''

    def say_hello(self):
        super(ClassDPrime, self).say_hello() 



def inspect_method_delegation():
    #ClassC().say_hello() # say_hello from ClassA instance
    #ClassD().say_hello() # say_hello from ClassB instance
    ClassDPrime().say_hello() # say_hello from ClassA instance


if __name__ == '__main__':
    inspect_method_delegation()