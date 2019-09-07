import os
from flask import Flask, url_for, request, make_response, redirect, abort, json
from werkzeug.utils import secure_filename

"""This is the simplest way to create a Flask instance. I could also create the instance in a factory function and configure it as shown in the tutorial"""
app = Flask(__name__)


@app.route('/<int:num>')
def hello_world(num):
    return "Hello, World!: " + str(num)


""" 
The url_for() function doesn't redirect me anywhere, it takes a function (and optional arguments) that is bound to a route, looks up the url of that
route, and returns the route.
"""
@app.route("/reverseurl")
def reverse_url():
    # Return "/"
    #return url_for("hello_world") # This will throw an exception because I didn't provide a URL parametere
    #return url_for("hello_world", num=7) # This returns /7 because that is the URL! url_for() is not the same as redirect()!
    return redirect(url_for("hello_world", num=7))


"""Flask provides access to all the information in a request via the global "request" object. The request object must be imported."""
@app.route("/requestcontext")
def request_context():
    string = """ The method was: {method}
    The url was: {url}
    The host was: {host}""".format(method=request.method, url=request.url, host=request.host)
    return string


"""
Uploaded files can be accessed via the request object. The keys in request.files are the names that were assigned to the files when the form was
submitted. These form-defined names are NOT nececessarily the same as the actual file names of the files.
"""
@app.route("/file", methods=["POST"])
def file():
    #request.files is a dictionary of <key, file> entries. 'key' is a string and 'file' is a modified Python file object.
    file_names = []
    for key in request.files:
        print(key)
        file_names.append(key)
        # I need to filter the client-provided file name because the client could 1) overwrite an important system file 2) include invalid characters # (such as weird unicode characters)
        path = os.path.join(os.path.dirname(__file__), "./uploads", secure_filename(key))
        # This is an insecure file name and a security risk. I can overwrite app.pyc (or anything else)
        #path = os.path.join(os.path.dirname(__file__), "./files", key)
        request.files.get(key).save(path)
    return "The names of the saved files were: " + str(file_names)


""" 
Flask will create a default response object for me if I return a string. The default response object has code 200 and a best-guess mimetype. If I want
a little more customization, I can return a tuple. Returning a tuple is the middle ground of customization between returning a plain string (which is
converted into a default response object) and creating my own response with make_response()

https://flask.palletsprojects.com/en/1.1.x/quickstart/#about-responses
If a tuple is returned the items in the tuple can provide extra information. Such tuples have to be in the form (response, status), (response,
headers), or (response, status, headers). The status value will override the status code and headers can be a list or dictionary of additional header
values.
"""
@app.route("/tupleresponse")
def tuple_response():
    # A 202 is wrong, but I do it just to demonstrate setting a custom status code
    # The last tuple element (headers) must be a dictionary
    # Throws an error if I'm not running the web server
    print("Request method: " + str(request.method))
    return ("<h1>Tuple Response</h1>", 202, {"mycustomheader": "cool"})


""" 
Flask normally converts whatever I return from a route function into a response object for me, but I can explicity create a response object if I want.
A response object is composed of: response (i.e. entity-body), status, headers. In reality, this is identical to returning a tuple, but the syntax
might be easier to work with in some cases.

I NEED to use make_response() if I want to edit something like the mimetype of the response.
"""
@app.route("/customresponse/<int:num>")
def custom_response(num):
    code = {
        0: 200,
        # Using a 301 instead of a 302 makes the client cache the redirect url
        3: 302 
    }.get(num, 200)
    resp = make_response("I could render a template here if I wanted", code)
    # Header keys cannot contain spaces!
    resp.headers["Another-custom-header"] = "whoa there"
    resp.mimetype="igPa atinLa"
    if num == 3:
        resp.headers["Location"] = "/"
    return resp


"""Flask provides the redirect() function to redirect requests. It uses a 302 by default, but this can be changed"""
@app.route("/my_redirect")
def my_redirect():
    return redirect(url_for("hello_world"))


"""
Flask provides the abort() function to return some kind of 4xx response to the client. Apparently, Flask will intentionally raise the correct
exception that would have been thrown if the 4xx code had occurred unintentionally.
"""
@app.route("/abort!abort!")
def my_abort():
    # No return statement necessary
    abort(418)


"""
{
  "NoneType": null, 
  "dictionary": {
    "coolness": "10/10", 
    "name": "Austin"
  }, 
  "exists": true, 
  "list": [
    "1", 
    2, 
    3.0, 
    false
  ], 
  "sentence": "This is a string!", 
  "tuple": [
    "hello", 
    "there", 
    [
      1, 
      2, 
      3
    ]
  ]
}
"""
@app.route("/somejson")
def some_json():
    return json.jsonify(
        exists=True,
        dictionary={"name": "Austin", "coolness": "10/10"},
        sentence="This is a string!",
        list=["1", 2, 3.0, False],
        tuple=("hello", "there", [1, 2, 3]),
        NoneType=None
    )


if __name__ == "__main__":
  """
  I can use the undecorated versions of view functions in Flask. This is NOT standard to Python. However, keep in mind that Flask will throw an
  exception if I attempt to use Flask objects inside of the undecorated view function.
  """
  print(tuple_response())