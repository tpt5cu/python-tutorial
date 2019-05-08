from flask import Flask, current_app, g, request

app = Flask(__name__)

""" app.config is a special dictionary. I can treat it like a regular dictionary, but it has extra functionality like being able to load configuration from files easily. """
app.config["CONFIG_VAR"] = "cool config var!!!"

@app.route("/firstroute")
def first_route():
    """ current_app appears to basically be equivalent to app. """
    print(app.config["CONFIG_VAR"])
    print(current_app.config["CONFIG_VAR"])
    print(current_app is app)
    print(current_app._get_current_object() is app)
    return "Hello from /firstroute"

@app.route("/secondroute")
def second_route():
    # This throws an exception because g does not have an attribute "config"
    #print(g.config["CONFIG_VAR"])
    # This throws an exception because the global request object does not support assignment
    #request["foo"] = "bar"
    return "Hello from /secondroute"

@app.teardown_request
def pre_request_pop(e):
    """
    Any @app.teardown_request() function must take 1 argument which will either be None or an exception. The return value of the function is ignored.
    This function will be called after a request ends, but before the request context and application context are popped. That means that current_app
    and g should be available, as well as request.
    """
    print("Hello from request context: " + request.method)

@app.teardown_appcontext
def post_request_pop(e):
    """
    This function will be called after the request context has been popped, but before the application context has been popped. 
    """
    # This throws an error because I'm working outside of the request context.
    #print(request.method)
    print("Hello from application context: " + current_app.config["CONFIG_VAR"])