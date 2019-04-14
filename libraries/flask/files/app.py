import os, tempfile, shutil
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from contextlib import contextmanager

"""
Flask stores uploaded FileStorage objects in memory if they are small. Otherwise, it internally uses tempfile.gettempdir() which returns the globally
configured temporary directory that tempfile is using.

WARNING: Flask accepts an unlimited file size unless I limit it

Flask encourages the use of <FileStorage>.save() to save uploaded files on the server. Afterwards, I can interact with the files normally. There does
not appear to be an easy way to directly interact with a FileStorage object with such functions as open()
"""

#UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
# Limit the file size fo 16 MB
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
# I want each user to have their own upload folder
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

"""
Upload a text file and the server will process the file by writing a single line to it and returning the modified file. The temporary directory where
the file was saved (and modified) is deleted at the end of the request. It works exactly as expected! Try stepping through it.
"""
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        f = request.files['file']
        # if the user does not select file, browser should also submit an empty part without filename
        if f.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if f and allowed_file(f.filename):
            """ 
            This code is fine because 'with' acts like a finally block. The context manager will always exit (unless the program abnormally
            terminates), even if an exception is thrown or return is called within the 'with' block. Thus, I can send the processed file to the
            client and then the entire directory will be deleted.
            """
            filename = secure_filename(f.filename)
            with TemporaryDirectory() as temp_dir:
                print("temp_dir was: " + temp_dir)
                path = os.path.join(temp_dir, filename)
                f.save(path)
                #f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                with open(path, "r+") as my_file:
                    my_file.write("The server wrote this line.\n")
                return send_from_directory(temp_dir, filename)
        #return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

# Send the uploaded file right back to the user as an example. I don't do this because I process the file and spit it back to the user
"""
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
"""


# Create a context manager to deal with automatically deleting the temporary directory when the 'with' statement exists
@contextmanager
def TemporaryDirectory():
    name = tempfile.mkdtemp()
    try:
        yield name
    finally:
        shutil.rmtree(name)