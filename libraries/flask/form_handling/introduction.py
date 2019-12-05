from flask import Flask, request, json


app = Flask(__name__)


@app.route('/get-form-value', methods=["POST"])
def get_form_value():
    '''All string objects in Flask are handled as unicode'''
    val = request.form.get('foo')
    print(type(val)) # <type 'unicode'>
    print(val) # bar
    return 'OK'


@app.route('/return-submitted-file', methods=["POST"])
def return_submitted_file():
    '''
    It turns out I cannot just return a Flask FileStorage object in JSON at all
    - Returning the FileStorage object itself also does not work
    '''
    # TypeError: <FileStorage: u'introduction.py' ('application/octet-stream')> is not JSON serializable
    return json.jsonify({ 
        'foo': 'bar',
        'file': request.files['foo']
    })
    # TypeError: 'FileStorage' object is not callable
    # The view function did not return a valid response. The return type must be a string, tuple, Response instance, or WSGI callable, but it was a FileStorage.
    return request.files['foo']