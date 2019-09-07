# https://stackoverflow.com/questions/18249949/python-file-object-to-flasks-filestorage


import os, tempfile
from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename


"""The web server must NOT be started before any tests can be run."""


# Never ever use relative paths
# Don't do "./uploads or /uploads"
UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "uploads")
ALLOWED_EXTENSIONS = set(["png"])

app = Flask(__name__)
app.config["UPLOAD_DIR"] = UPLOAD_DIR

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/person")
def person():
    # protip: The return type must be a string, tuple, Response instance, or WSGI callable, but it was a dict.
    return (str({"name": "Goliath", "age": 99}), 200, {})

@app.route("/fileupload", methods=["POST"])
def file_upload():
    """
    The files inside of request.files are FileStorage instances. FileStorage is a Flask class. The documentation says that a FileStorage object acts
    like a File object, but with an extra method, save(). However, open() does not work with FileStorage objects. The usual workaround is to save the
    FileStorage object, and then open the regular file.

    The key inside of request.files seems to be "file", regardless of how the FileStorage object was created. I need the "filename" property of the
    FileStorage object, not the key in the request.files dictionary.
    """
    form_file_name = "cool_form_file_name"
    if form_file_name in request.files:
        fs = request.files.get(form_file_name)
        if allowed_file(fs.filename):
            filename = secure_filename(fs.filename)
            file_path = os.path.join(app.config.get("UPLOAD_DIR"), filename)
            fs.save(file_path)
            # This will return 404 if if doesn't find a matching file
            return send_from_directory(app.config.get("UPLOAD_DIR"), filename)    
        else:
            return ("Wrong format", 415, {})
    else:
        return ("No file POSTed", 400)

if __name__ == "__main__":
    app.run()
