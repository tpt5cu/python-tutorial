from flask import Flask


app = Flask(__name__)


@app.route('/get-inline-html')
def get_inline_html():
    '''This is how to return inline HTML. I should almost never do this, but it's cool'''
    return '''
        <div style="background:red">
            <p>Hello there!</p>
        </div>
    '''