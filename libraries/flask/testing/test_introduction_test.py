# https://realpython.com/python-web-applications-with-flask-part-iii/
# https://flask.palletsprojects.com/en/1.1.x/testing/


import pytest
from app import app
from flask import url_for, session


"""
The Flask test client, which is a wrapper around the Werkzeug test client, is pretty much exclusively for sending requests to the wrapped Flask
application as well as keeping that corresponding request context around.
- A Pytest fixture is only created when it is used by a test

I can start a Flask applicatin with pdb, but then the stdout and stdin change so that I can't work with the debugger anymore in the console. It
appears that I'll have to use pdb destructively with 'import pdb; pdb.set_trace()'
- At least it works!
- After the initial pause with this line of code, then I can use pdb in the terminal like normal
"""


def setup_module():
    pass


def teardown_module(): 
    pass


#@pytest.fixture(scope='module') # Don't want module level client
@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


def test_validUsernameAndPassword_LogsIn(client):
    with client as c:
        rv = c.post('/login', data={
            'username': 'user1',
            'password': 'user1'
        })
        assert rv.status_code == 302
        assert rv.headers.get("Location") == "http://localhost" + "/"


def test_invalidUsernameAndPassword_DoesNotLogIn(client):
    """The test_client is a context manager. I can access the request object and the like"""
    with client as c:
        rv = c.post('/login', data={
            'username': 'user',
            'password': 'test'
        })
        #print(type(rv)) # <class 'flask.wrappers.Response'>
        #print(rv.data) # HTML redirect page
        assert rv.status_code == 302 # redirected because it's an invalid login
        assert rv.headers.get("Location") == "http://localhost" + url_for('landing')


def test_loggedInUser_canViewContentPage(client):
    """This really works! The login is essential, but after that the client is logged in!"""
    #rv = client.get('/content')
    #assert rv.status_code == 200 # 401 as expected because the client is not logged in
    rv = client.post('/login', data={
        'username': 'user1',
        'password': 'user1'
    })
    # Client IS logged in after this. No context manager is necessary
    assert rv.status_code == 302
    assert rv.headers["Location"] == "http://localhost" + "/"
    #with client as c:
    rv = client.get('/content')
    assert rv.status_code == 200
    assert rv.data == "<h1>Welcome to the content page, user1</h1>"
        #print(session)
        #assert session.get("user_id") == "user1"


def test_noFixtureNeeded_doesNotUseFixture():
    assert 1 == 1