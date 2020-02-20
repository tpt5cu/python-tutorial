import os
from flask import Flask, make_response, send_from_directory

app = Flask(__name__)

@app.route("/myroute")
def my_route():
    #return ("Hello from /myroute", 200, {})
    return send_from_directory(app.static_folder, "myfile.1.txt")

"""
Any function that has this decorator will be run after any view function returns, but before the response is sent to the client. This is in line with
Flasks's design in which a response object can be passed through numerous functions and modified before it is returned to the client.

However, deleting a file before the response is sent is okay. Presumably, Flask loads the file into the response when send_from_directory is called.
Keep in mind that the response won't be sent until all handlers have executed. If an after_request handler takes a long time, it will delay the response.
"""
@app.after_request
def execute_after_response(response):
    """
    This function must take 1 parameter: an instance of Flask's response class. It must also return an instance of Flask's response class. The
    returned instance can be new, or the same as the argument.
    """
    #print(response.response)
    #new_response = make_response("Hello from after_request handler")
    #return new_response
    os.remove(os.path.join(app.static_folder, "myfile.1.txt"))
    return response