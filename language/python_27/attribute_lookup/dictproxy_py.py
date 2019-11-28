# https://codesachin.wordpress.com/2016/06/09/the-magic-behind-attribute-access-in-python/
# https://stackoverflow.com/questions/25440694/whats-the-purpose-of-dictproxy


'''
Neither an instance __dict__ nor a class dictproxy handle missing key references in a special way: they raise a KeyError just like a normal dictionary
'''

class Table(object):

    category_id = 5

    def __init__(self, length=4, width=6, height=10):
        self.length = length
        self.width = width
        self.height = height


def inspect_instance_dict():
    '''The __dict__ attribute of an instance object is just a regular old dictionary'''
    t = Table()
    print(t.__dict__) # {'width': 6, 'length': 4, 'height': 10}
    print(type(t.__dict__)) # <type 'dict'>
    #t.__dict__["thing"] # KeyError
    t.__dict__[False] = "nice job!"
    print(t.__dict__) # {False: 'nice job!', 'width': 6, 'length': 4, 'height': 10}


def inspect_class_dictproxy():
    """
    A dictproxy is itself read-only. However, class attributes are implicity added to it. There are restrictions on directly modify a dictproxy
    because its keys must be strings and it cannot be reassigned/deleted for the sake of interpeter stability. In short, it's an implementation detail
    that isn't too important for attribute lookup itself.
    """
    print(Table.__dict__) # {'module': ..., '__dict__': ..., 'category_id': 5, '__weakref__': ..., '__init__': ...}   
    print(type(Table.__dict__)) # <type 'dictproxy'>
    #Table.__dict__["cool"] = "bro" # TypeError
    # See how there's no way to put a bool key in a dictproxy? The keys of a dictproxy must be strings
    Table.whoa = "yeet"
    print(Table.__dict__) # {'module': ..., 'whoa': 'yeet', '__dict__': ..., 'category_id': 5, '__weakref__': ..., '__init__': ...}   


if __name__ == "__main__":
    inspect_instance_dict()
    #inspect_class_dictproxy()