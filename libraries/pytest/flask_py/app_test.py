import pytest, io
#from werkzeug.datastructures import FileStorage
from app import app

"""
Print statements are useless here. The print() goes to the Flask application, not my stdout. Actually, pytest captures print() statements!
"""

@pytest.fixture
def client():
    # testing must be set to true on the Flask application
    app.config['TESTING'] = True
    # create a test client
    client = app.test_client()
    # The client should only be created once
    print("Client created")
    yield client
    # Could put teardown code here if needed

def test_app_response(client):
    response = client.get('/person')
    print(response.data)
    #assert response.data == "{'age': 99, 'name': 'Goliath'}"
    assert response.data == '{"name": "Goliath", "age": 99}'

"""
The entire point of this test is to be able to send a file to the server. How do I send a file with app.test_client()?
- All of the app.test_clients() HTTP methods take the same methods as an EnvironBuilder. Thus if I want to send a file, I have to send either
  1) a FileStorage object or 2) a tuple that has the same structure as a FileStorage object. I cannot just send a regular file.
- A FileStorage object expects a stream, so I can read a file into a BytesIO object and pass the BytesIO object into the FileStorage
"""
def test_file_upload(client):
    file_path = "/Users/austinchang/Desktop/ss.png" 
    #file_path = "/Users/austinchang/Desktop/coral.jpg"
    #file_path = "/Users/austinchang/tutorials/python/libraries/pytest_py/flask_py/README.md"
    with open(file_path) as f:
        b_io = io.BytesIO(f.read())
    data = {
        # The key "cool_file" is interpreted as the form file name in the route
        #"cool_form_file_name": FileStorage(b_io, "ss.png")
        "cool_form_file_name": (b_io, "ss.png")
    }
    response = client.post("/fileupload", data=data)
    # Assert that it returned the correct code
    assert response.status_code == 200
    # Assert that it returned the correct type of file!!!
    assert response.mimetype == "image/png"