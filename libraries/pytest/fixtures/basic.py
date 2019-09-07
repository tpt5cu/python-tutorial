# Need to import pytest to use fixtures
import pytest

""" 
Fixtures are an example of dependency injection. The fixture function is the injector, and the test functions are the consumers. Any function can use
any fixture. This is much more flexible then scoped beforeEach() and afterEach() calls.
- Decorate a function to turn it into a 'fixture function'. A fixture function will return a fixture object, which is simply a wrapper around whatever
  the function normally returns.
- Do scope="module" to create a fixture only once per module
- A fixture function is only called when a test needs it. So if 4/5 tests use a fixture, the fixture will only be called 4 times
"""
@pytest.fixture
#@pytest.fixture(scope="module")
def my_cool_fixture():
    # This function returns a dictionary. Now that it's a fixture function, it will return a fixture object that wraps the dictionary
    return {
        "name": "Gregory",
        "age": "33"
    }


"""
A test function can use a fixture by having the precise fixture function name as a parameter.
"""
def test_person(my_cool_fixture):
    # This is wrong on purpose
    assert my_cool_fixture.get("age") == 33
    assert my_cool_fixture.get("name") == "Gregory"

