# https://flask-login.readthedocs.io/en/latest/


import os, json
import flask_login
from flask import Flask, request, redirect, render_template, render_template_string


"""
There's a minor issue of hitting logout again and getting an unauthorized request response. I don't know why.
"""


app = Flask(__name__, template_folder=os.path.dirname(__file__))
### The app MUST have a secrete key to use sessions
app.secret_key = "1234"
### Set up flask_login
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


class User(flask_login.UserMixin):
    """The 'User' class object is required by flask_login (it doesn't have to be named 'User' thought)"""
    def __init__(self, username):
        self.id = username


@login_manager.user_loader
def load_user(username):
    """Mandatory function for flask_login. Return the corresponding User object or None if the user doesn't exist"""
    with open(os.path.join(os.path.dirname(__file__), "users.json")) as f:
        all_users = json.load(f)
    password = all_users.get(username)
    if password is None:
        return None
    return User(username)


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    with open(os.path.join(os.path.dirname(__file__), "users.json")) as f:
        all_users = json.load(f)
    if all_users.get(username) is not None and all_users.get(username) == password:
        user = User(username)
        flask_login.login_user(user)
        #return redirect(request.args.get('next') or "/")
        return redirect("/")
    return redirect('/landing')


@app.route("/content")
@flask_login.login_required
def content():
        return render_template_string("<h1>Welcome to the content page, {{current_user.id}}</h1>", current_user=flask_login.current_user)


@app.route("/landing")
def landing():
    return render_template("login.html")


@app.route("/")
@flask_login.login_required
def home():
    return render_template_string("<h1>Welcome to the home page, {{current_user.id}}</h1>", current_user=flask_login.current_user)


@app.route("/logout")
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return redirect('/landing')


if __name__ == "__main__":
    app.run(debug=True)    