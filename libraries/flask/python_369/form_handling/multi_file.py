# https://flask.palletsprojects.com/en/1.1.x/api/ - Flask API


from flask import Flask, request


app = Flask(__name__)


@app.route('/multiple-files-same-form-name', methods=['POST'])
def multiple_files_same_form_name():
    length = len(request.files.getlist('glm'))
    return f'There were {length} files sent with the "glm" key' # There were 3 files sent with the "glm" key
