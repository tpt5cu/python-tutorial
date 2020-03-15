# https://realpython.com/python-descriptors/


'''
Here's a thought: should properties be declared as if they were private attributes? In summary, NO. NO NO NO. They should be declared as if they were
public attributes
- Argument: yes, properties should be declared as if they were private attributes
    - If a refactor turned a previous attribute (which should have been private) into a property, than the property would have to be declared as if it
      were a private attribute anyway
        - Counter-argument: if the attribute was previously private, no one should have accessed it as a public API in the first place and their code
          should break if they do
    - If I'm creating a new class, the standard OO paradigm is that attrbutes should be private as much as possible. Allowing attributes to be public
      (even if they are Python properties) will likely lead to confusing API design. E.g. I hate how NetworkX allows some instance object attributes
      to be treated as both Python attributes and Python methods (e.g. <Graph>.nodes and <Graph>.nodes()).
        - Counter-argument: the confusing NetworkX design has nothing to do with properties at all. If I examine the NodeView class, I see that is
          really a mapping object (e.g. dict-like) AND it defines a __call__() method. That's the reason for the confusing API
        - Counter-argument: Attributes can still be private (as they should) while properties are public. Properties should be accessed as public
          attributes. That's their purpose. They are a cleaner version of getters/setters.
            -  If the property design were ALSO abused to allow the property to be invoked as a method AND as a "Python property" (although I haven't
               actually seen this in the wild, and I had better not ever see it!!!), that would be orthoganal to the property being public
- Argument: no, properties should be declared as if they were public attributes
    - The point of being a property is to function as a getter and a setter for an attribute. In Java, get<Attribute>() and set<Attribute() are always
      public (if they are declared at all). A property is SUPPOSED to function as a public interface to a real, PRIVATE attribute. That's why a
      property like "name" would actually set the "_name" attribute on all of the instances it worked with
'''

# TOBE continued


class DecoratorPropertyUser:
    '''This class is NOT supposed to itself be a descriptor'''

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    # This is wrong. Don't do this
    #@property.setter
    @name.setter
    def name(self, value):
        if len(value) > 0 and isinstance(value, str):
            self._name = value
        else:
            raise ValueError


def use_decoratorpropertyuser():
    o = DecoratorPropertyUser('Frank')
    print(o.name) # Frank
    o.name = 'Mike'
    print(o.name) # Mike
    #o.name = '' # ValueError


if __name__ == '__main__':
    use_decoratorpropertyuser()
