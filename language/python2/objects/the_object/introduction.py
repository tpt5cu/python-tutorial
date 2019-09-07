# https://docs.python.org/2.7/reference/datamodel.html#objects-values-and-types
# https://stackoverflow.com/questions/865911/is-everything-an-object-in-python-like-ruby
# https://stackoverflow.com/questions/1529002/cant-set-attributes-of-object-class

"""
Pretty much everything in Python inherits from the base class Object. But why is that important? It doesn't seem to be that important. Much of the
functionality in Python is defined across many built-in functions and built-in types. It's not like the object() constructor contains all of that code.


The built-in object constructor returns a featureless object with serveral attributes. 
- Included attributes: __class__, __doc__, ...
- NOT included attributes: __dict__
"""