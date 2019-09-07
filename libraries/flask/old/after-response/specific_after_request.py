from flask import Flask, send_from_directory, after_this_request

"""
Sometimes, I want an after_request handler to only execute after a particular endpoint function. The first two view functions do the same thing in two
different ways.
"""

app = Flask(__name__)

@app.route("/firstroute")
def first_route():
    response = send_from_directory(app.static_folder, "myfile.1.txt")
    #print(type(response))
    response.headers["CustomHeader"] = "foo"
    return response

@app.route("/secondroute")
def second_route():
    @after_this_request
    def do_stuff(response):
        response.headers["CustomHeader"] = "foo"
        return response
    return send_from_directory(app.static_folder, "myfile.1.txt")

"""
This route exists to show that the CustomHeader won't be added on to this response
"""
@app.route("/thirdroute")
def third_route():
    return "Hello from /thirdroute"
