import inspect, subprocess
from flask import Flask


app = Flask(__name__)


@app.route("/hello")
def hello():
    #for x in inspect.getmembers(app):
    #    print(x)
    return "hello world!"


if __name__ == "__main__":
    """ Run from this directory because gunicorn must be run as a module. Alternatively, use in conjunction with os.chdir() """
    # Don't do this because an entirely new process is created. If this is run in Docker, the Python process will terminate and the Docker container
    # will exit
    #subprocess.Popen(["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "--preload", "-k gevent", "app:app"])
    # This is different from Popen(). It makes the Python process wait for this new process to return, which it won't, so the Docker container will
    # stay alive
    subprocess.call(["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "--preload", "-k gevent", "app:app"])