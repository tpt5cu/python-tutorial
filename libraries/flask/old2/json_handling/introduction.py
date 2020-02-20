from flask import Flask, json


app = Flask(__name__)

'''
{
  "NoneType": null, 
  "dictionary": {
    "coolness": "10/10", 
    "name": "Austin"
  }, 
  "exists": true, 
  "list": [
    "1", 
    2, 
    3.0, 
    false
  ], 
  "sentence": "This is a string!", 
  "tuple": [
    "hello", 
    "there", 
    [
      1, 
      2, 
      3
    ]
  ]
}
'''
@app.route('/get-json')
def get_json():
    '''Make sure to set status to a string'''
    r = json.jsonify(
        exists=True,
        dictionary={"name": "Austin", "coolness": "10/10"},
        sentence="This is a string!",
        list=["1", 2, 3.0, False],
        tuple=("hello", "there", [1, 2, 3]),
        NoneType=None
    )
    #r.status = 202 # TypeError
    r.status = '202'
    return r
