from flask import Flask

app = Flask(__name__)

"""
Restrict the parameter to a certain type. If the route parameter violates the constraint, the route isn't found.
"""
@app.route("/numroute/<int:num>")
def get_number(num):
    return "The number was " + str(num)

"""
If I define a route with a trailing slash and the URL is hit without the slash, it will be redirected.
"""
@app.route("/trailingslash/")
def trailing_slash():
    return "You could have been redirected"

"""
If I define a route without a trailing slash, then hitting the URL with a slash is a 404
"""
@app.route("/noslash")
def noslash():
    return "404 if you added the slash"

"""
A route only takes GET requests by default.
This route only takes POST requests. It will return 405 if a GET request is sent.
"""
@app.route("/postrequest", methods=["POST"])
def post_request():
    return "nice post"

"""
When a route parameter is defined to be a "path" type, Flask will accept the URL parameter with "/" characters.
Flask does not check to see whether or not the path exists on the server filesystem.
If there are subsequent route parameters after a "path" parameter, Flask will smartly parse the incoming URL so that each parameter is filled with a
value. If every parameter cannot be filled with a value, a 404 is returned because the URL didn't match the route.
"""
@app.route("/givemeapath/<path:some_dir>/<name>")
def get_path(some_dir, name):
    print("path: " + some_dir)
    print("name: " + name)
    return (str((some_dir.encode("utf-8"), name.encode("utf-8"))), {})

"""
If a URL path parameter argument IS an absolute path (e.g. /hello/goodbye), Flask will interpret the entire URL as /abspath//hello/goodbye and return
a 404. Even if I encode one of the slashes as %2F (e.g. /abspath/%2Fhello/goodbye), Flask still treats the escaped slash as a regular slash and
returns a 404. I cannot use absolute paths as URL path parameter arguments.
"""
@app.route("/abspath/<path:abs_path>")
def get_abs_path(abs_path):
    print(abs_path)
    return "path was: " + abs_path