# https://flask.palletsprojects.com/en/1.1.x/errorhandling/ - tutorial
# https://werkzeug.palletsprojects.com/en/0.16.x/exceptions/ - built-in werkzeug exceptions
# https://jsonapi.org/examples/#error-objects - JSON error response example


import json
from werkzeug.exceptions import BadRequestKeyError
from flask import Flask, request, send_from_directory, send_file


app = Flask(__name__)


@app.route('/missing-form-key')
def missing_form_key():
    '''
    - A regular dictionary KeyError will return 500 in production mode
    - A request.form or request.files KeyError will actually raise a werkzeug.exceptions.BadRequestKeyError, which returns 400 in production mode
        - This is a very special case. Most unhandled errors will simple return 500
    '''
    #val = request.form['nonexistent']
    val = request.files['nothing']
    #d = dict()
    #d['whatever']
    return 'OK'


@app.route('/missing-file')
def missing_file():
    '''
    - send_from_directory() implicitly raises 404 for a nonexistent file
        - It will serve files from anywhere in the filesystem
        - It is more secure than send_file() because it will remove dangerous path components that could exist in the filename argument (if it was
          provided by a malicious user)
    - send_file() raises 500 for a nonexistent file
        - Never use send_file(). It does not protect against malicious filenames
    '''
    #return send_from_directory('.', 'introduction.py') # Returns 200 and file as expected
    #return send_from_directory('.', 'blahblah.txt') # Returns 404 
    # This is not a flaw. There is nothing dangerous about the filename argument itself
    #return send_from_directory('..', 'introduction.md') # Returns 200
    # This show security in action
    #return send_from_directory('.', '../introduction.md') # Returns 404
    # This is a security flaw. send_file() does not remove potentially dangerous path components from the filename
    return send_file('../introduction.md') # Returns 200
    #return send_file('./blahblah.txt') # Returns 500



@app.route('/bad-json')
def bad_json():
    '''An invalid JSON decoding will return 500 production mode, just like any other error normal error'''
    val = json.loads('blahblahblah')
    return 'OK'


@app.route('/raise-400')
def raise_400():
    '''As expected, werkzeug exceptions can be manually raised with expected behavior'''
    raise BadRequestKeyError('This is a custom message')
    return 'OK'


#@app.errorhandler(404)
def return_404_page(e):
    '''
    Flask is really neat. <app>.errorhandler() can register a code or an exception. In this case, any 404 that is raised anywhere in the application
    will be handled by this view function
    - The argument to an error handling function (not the decorator) is always a werkzeug exception. There's quite a bit of data associated with a
      werkzeug exception
    '''
    print(type(e)) # <class 'werkzeug.exceptions.NotFound'>
    #print(dir(e))
    print(e.get_body())
    #<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    #<title>404 Not Found</title>
    #<h1>Not Found</h1>
    #<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
    print(e.get_response()) # <Response 233 bytes [404 NOT FOUND]>
    print(e.get_description()) # <p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
    print('Message was: ' + e.message) # <empty string>
    print(e.get_headers()) # [('Content-Type', 'text/html')]
    return '''
    <div style="background:blue; text-align:center">
        <p>Not found! Keep looking!</p>
    </div>
    '''


@app.errorhandler(BadRequestKeyError)
def deal_with_badrequestkeyerror(e):
    '''Any custom error message that a werkzeug error was created with is available in the "message" attribute'''
    print(type(e)) # <class 'werkzeug.exceptions.BadRequestKeyError'>
    #print(dir(e))
    print(e.get_headers()) # [('Content-Type', 'text/html')]
    print(e.get_body())
    #<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    #<title>400 Bad Request</title>
    #<h1>Bad Request</h1>
    #<p>The browser (or proxy) sent a request that this server could not understand.</p>
    print(e.get_description()) # <p>The browser (or proxy) sent a request that this server could not understand.</p>
    print('Message was: ' + e.message) # This is a custom message
    print(e.get_response()) # <Response 192 bytes [400 BAD REQUEST]>
    return 'You were missing a form key-value pair entirely!!!\n', 400