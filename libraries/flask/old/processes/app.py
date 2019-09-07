from flask import Flask, request, abort, json, _request_ctx_stack
from multiprocessing import Process
import time, tempfile, os

app = Flask(__name__)

"""
I have to do some kind of pre-validation on the user's data. If I don't then I'll return 202 for every request. I'll only be able to tell the user why
their job failed through some kind of JSON response.
Validating with a try-except forces us to make everything synchronous. Ideally we would also validate on the client-side to save time, but we have no
client-side interface.
"""

@app.route("/firstroute", methods=["POST"])
def first_route():
    foo = request.form.get("foo")
    print("from first_route: " + foo) # I can get the value here just fine. No surprise
    print("is_multithread: " + str(request.is_multithread)) # True
    print("is_multiprocess: " + str(request.is_multiprocess)) # False
    try:
        json.loads(foo)
    except:
        abort(400)
    p = Process(target=long_operation, args=(3,))
    p.start()
    return "Process started"

def long_operation(start):
    print("from long_operation: " + request.form.get("foo")) # I can get the value here too!
    for x in range(start, start + 10):
        time.sleep(1)
        print(x)
        if x >= 10:
            #abort(400) # The client will never get this response because the response was returned long ago!
            pass

@app.route("/secondroute")
def second_route():
    temp_dir = tempfile.mkdtemp(dir=os.path.dirname(__file__))
    p = Process(target=write_after_sleep, args=(temp_dir,))
    p.start()
    return "Process started"

def write_after_sleep(temp_dir):
    try:
        time.sleep(10)
        str(x)
    except:
        with open(os.path.join(temp_dir, "error.txt"), 'w') as f:
            f.write("There was an error: " + time.ctime(time.time()))
        # If there is an exception in this block the uncaught exception is thrown on the server but Flask keeps going