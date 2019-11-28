# https://docs.pytest.org/en/latest/getting-started.html#group-multiple-tests-in-a-class


"""
This is a class. The class is not instantiated before any of the tests (although it could be). The purpose of the class is thus solely to group
related testing methods.
- Is using a class to group tests for organization worth the extra self argument?
"""
class TestClass(object):

    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')
    
    # pytest will NOT automatically discover this test
    #def three_test(self):
    #    assert 5 == 4

# pytest will NOT automatically discover this class
class CoolClass(object):

    def test_number(self):
        assert 3 == 2

# pytest will discover this class
"""
class Test_CoolClass(object):

    def test_number(self):
        assert 3 == 2
"""

# pytest will NOT automatically discover these classes
class AnimalTest(object):
#class Animal_Test(object):

    def test_is_cat(self):
        assert "cat" == "dog"