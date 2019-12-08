# https://docs.python.org/2.7/library/functions.html#super
# https://realpython.com/python-super/#super-in-multiple-inheritance


'''
The realpython tutorial touches on some other important considerations when using super() such as:
- Forgetting to call super(<type>, <self>).__init__() inside of a subclass initializer will cause the subclass to not have the properties of the
  superclass!
    - This is legal, but is a terrible design
- Python 2 and 3 super() invocations can be syntactically different, but the underlying functionality is the same
- super(<type>, <type>/<instance>) doesn't always have to set <type> equal to the current class. I could set it to a higher-up ancestor or an entirely
  different class depending on how I wanted an attribute/method to be resolved.
  - Doing this can get confusing fast.
- Reordering base classes to achieve the desired __mro__ with multiple inheritance is an option
- Classes A and B should be designed cooperatively when using them in multiple inheritance (e.g. don't define two functions in A and B with the exact
  same signature)
'''

class LivingThing(object):

    def __init__(self, name):
        self.name = name

    def breath(self):
        print(self.name + ' is breathing!')


class Friend(object):

    def __init__(self, greeting):
        self.greeting = greeting

    def greet(self):
        print('This friend greets you with {}'.format(self.greeting))


class Animal(LivingThing, Friend):
    '''
    There is never an implicit call to super() for a method. That is demonstrated by the fact that any Animal won't have a name automatically.
    - However, if Animal did not define an __init__() method at all, THEN LivingThing.__init__() would be called, and consequently Animal would have
      to be initialized with a name argument
    - Friend.__init__() is NOT called, only LivingThing.__init__() is called. That's because due the __mro__, LivingThing.__init__() was found first
      and called. There was no need to search further back. If LivingThing ALSO did not define __init__(), then Friend.__init__() would implicitly be called
    '''
    #def __init__(self, birthday):
    #    self.birthday = birthday
    # Now the subclass is initialized propertly with regard to LivingThing
    def __init__(self, name, birthday):
        super(Animal, self).__init__(name)
        self.birthday = birthday

    def say_happy_birthday(self):
        print('Happy birthday to ' + self.name + '! Your birthday is on ' + self.birthday)


class Cat(Animal):

    #def __init__(self, name, species, birthday):
    '''
    Cat instances have access to the greet() function, but they can't use it effectively because instances lack the 'greeting' attribute.
    - Cat -> Animal -> LivingThing, Friend, so greet() is in the inheritance hierarchy of Cat
    '''
    #    super(Cat, self).__init__(name, birthday)
    #    self._species = species

    def __init__(self, name, species, birthday):
        '''
        Here, Cat is first initialized as an Animal. Next, it is initialized as a Friend.
        - This is because Python can tell that LivingThing and Friend are sibling classes. See the sibling classes notes.
            - This is not a great usage of sibling classes for a variety of reasons, but it demonstrates the functionality of super()
        '''
        super(Cat, self).__init__(name, birthday)
        super(LivingThing, self).__init__('Wasssup?')
        self._species = species

    def move(self):
        '''
        The functionality of superclass methods can be used and extended if desired. Here, I'm using a superclass method and then adding to it. I
        could use the return value of the superclass method too if I wanted
        '''
        super(Cat, self).move()
        print('Cats need to pounce too!')


def play_with_animals():
    # This is valid when Animal does not define an __init__() function because it uses LivingThing.__init__()
    #a = Animal('Chuck') 
    a = Animal('Boots', 'Monday')
    a.breath() # Boots is breathing!
    # a has access to Friend.greet(), but cannot use it effectively because of bad class design.
    a.greet() # AttributeError: 'Animal' object has no attribute 'handshake'


def play_with_cat():
    c = Cat('Ginger', 'Lion', 'Friday')
    c.greet() # This friend greets you with Wasssup?


if __name__ == '__main__':
    #play_with_animals()
    play_with_cat()