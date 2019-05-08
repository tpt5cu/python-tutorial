import os
from flask import Flask, make_response, send_from_directory

app = Flask(__name__)

"""
This is a very simple way of deleting a file after it is sent to the client.
"""

@app.route("/myroute")
def my_route():
    response = send_from_directory(app.static_folder, "myfile.1.txt")
    os.remove(os.path.join(app.static_folder, "myfile.1.txt"))
    return response