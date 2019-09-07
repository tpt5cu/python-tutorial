# https://stackoverflow.com/questions/22403897/what-does-it-mean-by-the-super-object-returned-is-unbound-in-python - not too helpful
# https://www.artima.com/weblogs/viewpost.jsp?thread=236278 - unbound super is bad
# # https://rhettinger.wordpress.com/2011/05/26/super-considered-super/ - finer details of super() usage not in these notes


"""
super(<type>, [<instance>]): returns a proxy object that delegates method calls to a PARENT class or sibling class of <type>
- super(<type>) returns an unbound super object. Why would this ever be useful? I don't know
    - The search order is the same as getattr(), except that <type> itself is skipped. That's why an unbound super object can't directly call the
      superclass methods!
- An unbound super() proxy object is a design wart, NOT something to be used regulalry!!!
- 'super(C, c).method' returns a bound method. I get that
- 'super(C, C).method' returns an unbound method. I get that
- 'super(C).method' does NOT return an unbound method! What does it do?
    - Honestly not much. Consider an unbound super to be black magic that should never be used
    - It actually fails to look up 'method' entirely because of how look-ups on a super object are designed

A BOUND super object will ONLY look up attributes on the relevant class, never any instance object. The instance object argument is only good for getting
bound methods, that's it
"""


class Animal(object):

    cool_property = "I'm a class property"

    def __init__(self, name, species, birthday):
        self.name = name
        self.species = species
        self.birthday = birthday
        self.cool_property = "I'm an instance property"

    def say_happy_birthday(self):
        print("Happy birthday to " + self.name + "! Your birthday is on " + self.birthday)


class Cat(Animal):

    def __init__(self, name, species, birthday):
        #unbound_super = super(Cat)
        #unbound_super.say_happy_birthday() # AttributeError: 'super' object has no attribute 'say_happy_birthday'
        #unbound_super.__thisclass__.say_happy_birthday() # TypeError: unbound method say_happy_birthday() must be called with Cat instance as first argument (got nothing instead)
        # class_bound_super delegates to the class object
        #class_bound_super = super(Cat, Cat)
        #class_bound_super.say_happy_birthday() # TypeError: unbound method say_happy_birthday() must be called with Cat instance as first argument (got nothing instead)
        # instance_bound_super delegates to the object instance
        instance_bound_super = super(Cat, self)
        instance_bound_super.say_happy_birthday() # AttributeError: 'Cat' object has no attribute 'name'


    def meow(self):
        print(self.name + " says meow!")


def play_with_cat():
    cat = Cat("Flipper", "Tiger", "Wednesday")


class BetterCat(Animal):

    def __init__(self, name, species, birthday):
        """
        - If the super object is bound to a class, I can only look up class attributes (i.e. unbound methods, class properties, etc.)
        - If the super object is bound to an instance object, I can STILL only look up class attributes. It's just that instead of unbound methods I
          will get bound methods
        """
        # self hasn't been initialized yet, but that doesn't matter. super will never look up the instance object property 'cool_property'
        print(self.cool_property) # I'm a class property
        print(super(BetterCat, self).cool_property) # I'm a class property
        # __init__() doesn't return anything, it merely initializes the invoking object
        super(BetterCat, self).__init__(name, species, birthday)
        # This doesn't invovle the super object, so of course I can look up an instance object property
        print(self.cool_property) # I'm an instance property
        # This is still looking up the class property, and ONLY the class property
        print(super(BetterCat, self).cool_property) # I'm a class property.


def play_with_betterCat():
    bcat = BetterCat("Hugs", "Lion", "Thursday")


if __name__ == "__main__":
    #play_with_cat()
    play_with_betterCat()