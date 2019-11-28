from flask import Flask, request


app = Flask(__name__)


@app.route('/get-form-value', methods=["POST"])
def get_form_value():
    '''All string objects in Flask are handled as unicode'''
    val = request.form.get('foo')
    print(type(val)) # <type 'unicode'>
    print(val) # bar
    return 'OK'