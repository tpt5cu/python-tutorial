# https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide


'''Class attributes are implicitly static. No 'static' keyword is needed'''


class Book(object):

    publisher = 'We Publish Books'
    editions = [1990, 1995]

    def __init__(self, title='The Best Book', author='Austin Chang' ):
        self.title = title
        self.author = author

    def view_editions(self):
        '''Class attributes are absolutely visible inside of instance methods'''
        print(self.__class__.editions) # [1990, 1995]

    @classmethod
    def view_editions_class(cls):
        '''Class attributes are visible in class methods'''
        print(cls.editions) # [1990, 1995]

    @staticmethod
    def view_editions_static():
        '''Class attributes are visible in static methods'''
        print(globals()['Book'].editions) # [1990, 1995]


def test_class_attribute_visibility():
    '''Instances have access to class attributes, so of course they are visible!'''
    b = Book()
    print(b.editions)


def modify_mutable_class_attribute():
    '''Modifying a mutable class attribute through an instance or class will mutate that attribute for all other instances'''
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
    '''An immutable object cannot be modified, so this is impossible'''
    pass


def reassign_class_attribute():
    '''
    Reassigning a class attribute through a class will change that attribute for all instances of the class. If I TRY to reassign a class attribute
    through a instance, what I'm actually doing is creating a new attribute on the instance that shadows the class attribute
    - Thus, if a class reassigns a class attribute, the new value of that attribute won't (easily) be displayed if it is being shadowed on a
      particular instance
    '''
    hardcover = Book()
    print(hardcover.publisher) # We Publish Books
    print(Book.publisher) # We Publish Books
    hardcover.publisher = 'New Publisher'
    print(hardcover.publisher) # New Publisher
    print(Book.publisher) # We Publish Books
    Book.publisher = 'Newest Publisher'
    print(hardcover.publisher) # New Publisher
    print(Book.publisher) # Newest Publisher
    Book.editions = 'Quack'
    print(hardcover.editions) # Quack
    print(Book.editions) # Quack
    print(hardcover.__class__.publisher) # Newest Publisher


if __name__ == '__main__':
    #test_class_attribute_visibility()
    b = Book()
    b.view_editions()
    Book.view_editions_class()
    Book.view_editions_static()
    #modify_mutable_class_attribute()
    #reassign_class_attribute()