# https://docs.pytest.org/en/latest/getting-started.html#group-multiple-tests-in-a-class


'''
A class is not instantiated before any of the tests (although it could be). The purpose of the class is thus solely to group related testing methods.
- Is using a class to group tests for organization worth the extra self argument?
'''

##########################################################
# These classes are all detected by pytest automatically #
##########################################################


class TestClass(object):

    def test_pass(self):
        assert 1 == 1


    def test_fail(self):
        assert 1 == 2

    # pytest will NOT automatically discover this test
    def x_test(self):
        assert 1 == 2


class Test_niceFunctionName(object):

    def test_pass(self):
        assert 1 == 1

    def test_fail(self):
        assert 1 == 2

class Test_CoolClass(object):

    def test_pass(self):
        assert 1 == 1
    
    def test_fail(self):
        assert 1 == 2


##############################################################
# These classes are all NOT detected by pytest automatically #
##############################################################


class test_class(object):

    def test_pass(self):
        assert 1 == 1

    def test_fail(self):
        assert 1 == 2


class CoolClass(object):

    def test_pass(self):
        assert 1 == 1
    
    def test_fail(self):
        assert 1 == 2


class AnimalTest(object):

    def test_pass(self):
        assert 1 == 1
    
    def test_fail(self):
        assert 1 == 2


class Animal_Test(object):

    def test_pass(self):
        assert 1 == 1
    
    def test_fail(self):
        assert 1 == 2
