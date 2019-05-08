import inspect, subprocess
from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    #for x in inspect.getmembers(app):
    #    print(x)
    return "hello world!"

if __name__ == "__main__":
    # Run from this directory because gunicorn must be run as a module. Alternatively, os.chdir()
    subprocess.Popen(["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "--preload", "-k gevent", "app:app"])