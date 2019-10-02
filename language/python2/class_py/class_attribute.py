# https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide


"""
- Class attributes are not visible in instance methods, class methods, nor static methods
- Class attributes are implicitly static. No 'static' keyword is needed
"""

some_var = 'foo!'

class Book(object):

    publisher = 'We Publish Books'
    editions = [1990, 1995]

    def __init__(self, title='The Best Book', author='Austin Chang'):
        self.title = title
        self.author = author

    def get_editions(self):
        """Class attributes are not visible in instance methods!!!"""
        #return some_var
        return editions # NameError: global name 'editions' is not defined

    @classmethod
    def get_editions_class(self):
        """Class attributes are not visible in class methods!!!"""
        return editions

    @staticmethod
    def get_editions_static():
        """Class attributes are not visible in static methods!!!"""
        return editions


def modify_mutable_class_attribute():
    """Modifying a mutable class attribute through an instance or class will mutate that attribute for all other instances"""
    hardcover = Book()
    print(hardcover.editions) # [1990, 1995]
    print(Book.editions) # [1990, 1995]
    hardcover.editions.append(2000)
    print(hardcover.editions) # [1990, 1995, 2000]
    print(Book.editions) # [1990, 1995, 2000]
    Book.editions.append(2005)
    print(hardcover.editions) # [1990, 1995, 2000, 2005]
    print(Book.editions) # [1990, 1995, 2000, 2005]
    softcover = Book()
    print(softcover.editions) # [1990, 1995, 2000, 2005]


def modify_immutable_class_attribute():
    """An immutable object cannot be modified, so this is impossible"""
    pass


def reassign_class_attribute():
    """
    Reassigning a class attribute through a class will change that attribute for all instances of the class. If I TRY to reassign a class attribute
    through a instance, what I'm actually doing is creating a new attribute on the instance that shadows the class attribute
    - Thus, if a class reassigns a class attribute, the new value of that attribute won't (easily) be displayed if it is being shadowed on a
      particular instance
    """
    hardcover = Book()
    print(hardcover.publisher) # We Publish Books
    print(Book.publisher) # We Publish Books
    hardcover.publisher = "New Publisher"
    print(hardcover.publisher) # New Publisher
    print(Book.publisher) # We Publish Books
    Book.publisher = "Newest Publisher"
    print(hardcover.publisher) # New Publisher
    print(Book.publisher) # Newest Publisher
    Book.editions = "Quack"
    print(hardcover.editions) # Quack
    print(Book.editions) # Quack
    print(hardcover.__class__.publisher) # Newest Publisher


if __name__ == '__main__':
    b = Book()
    #b.get_editions()
    #Book.get_editions_class()
    #Book.get_editions_static()
    #modify_mutable_class_attribute()
    reassign_class_attribute()
    