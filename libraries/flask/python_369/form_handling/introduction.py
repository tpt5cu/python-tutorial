# https://flask.palletsprojects.com/en/1.1.x/api/ - Flask API


from flask import Flask, request, json


app = Flask(__name__)


@app.route('/get-form-value', methods=['POST'])
def get_form_value():
    '''All string objects in Flask are handled as unicode'''
    val = request.form.get('foo')
    print(type(val)) # <class 'str'>
    print(val) # bar
    return 'OK'


@app.route('/return-submitted-file', methods=['POST'])
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


@app.route('/original-filename', methods=['POST'])
def original_filename():
    '''Any bad request response is caused by submitting 'foo' with a regular form value instead of a file form value'''
    fs = request.files['foo'] # Possible KeyError
    return f'filename was: {fs.filename}' # filename was: EOB.pdf
