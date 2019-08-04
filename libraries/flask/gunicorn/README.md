- http://docs.gunicorn.org/en/latest/run.html - introduction
- http://docs.gunicorn.org/en/latest/settings.html - basically an API reference
- https://www.sitepoint.com/python-web-applications-the-basics-of-wsgi/ - background on WSGI
- https://medium.com/building-the-system/gunicorn-3-means-of-concurrency-efbb547674b7
- https://stackoverflow.com/questions/45071875/memory-sharing-among-workers-in-gunicorn-using-preload
- https://github.com/benoitc/gunicorn/issues/1367
- https://stackoverflow.com/questions/46528360/why-gevent-needs-synchronization-since-it-is-in-a-single-threaded (gevent is single-threaded)

# Installation

- $ pip install gunicorn

# Introduction

- Each worker process created by gunicorn is running a completely separate instance of my Flask app.

# Flask.run()

- See /Users/austinchang/tutorials/python/libraries/flask/venv2/lib/python2.7/site-packages/flask/app.py
- This "runs the application on a local development server" and is NOT suitable for production use
- The "**options" parameter is forwarded to the underlying function werkzeug.serving.run_simple()
- The "port" argument defaults to 5000 if it isn't provided
- The "host" argument defaults to localhost (127.0.0.1) if it isn't provided

# Start gunicorn

- $ gunicorn [OPTIONS] <APP_MODULE>
    - E.g. $ gunicorn -w 4 app:app
        - I could run this command from any directory, but I would have to ensure all the subdirectories are also Python modules
    - APP_MODULE = <MODULE_NAME>:<VARIABLE_NAME>
        - MODULE_NAME: the path to the Python module that contains the application object
        - VARIABLE_NAME: the variable that holds a refernce to a WSGI callable that exists in the module
            - A WSGI callable is a Python callable (i.e. a function, class, or object with a \_\_call\_\_ method)
                - Regular Python functions are just objects with a \_\_call\_\_ method
                - In addition, the WSGI callable must take two arguments: a dict (environ) and a function (start_fn)
                - The app = Flask(\_\_name\_\_) object is already a WSGI callable. The source code proves it.
    - OPTIONS: There are lots of options
        - $ -b <HOST>:<PORT> 
            - E.g. gunicorn --bind 0.0.0.0:8000 app:app
            - Specify a server socket to bind
            - -b $(HOST) is also acceptable syntax
            - This must be the port the gunicorn is listening on. The underlying application's run() method is never called, so its port doesn't matter
        - $ -w <NUMBER>
            - E.g. $ -w 4
            - Specify the number of worker processes, which should be 2 - 4 per server core
        - $ -k <WORKER CLASS>
            - E.g. gunicorn -k gevent app:app
            - Specify the type of worker process to run. 
        - $ --preload
            - This option can load application code before workers are forked. It may help with performance.

# Sync vs async (gevent) workers

- An I/O bounded application gets best performance from using "pseudo-threads" (i.e. gevent)
    - gevent enables "concurrency" in Python, which means executing 2 or more tasks at the same time. This could mean that 1 task gets worked on while
      the others are paused.
        - However, I don't have an I/O bounded application. The file conversion operations run on the CPU and take forever. The CPU operations may
          take a long time, but they aren't asynchronous at all.
    - Gevent workers with the multiprocessing Python package don't work together at all.
- Just use sync workers with gunicorn

# Stop gunicorn

- Get the process id and kill it?
    - ps -ef | awk '/gunicorn/ {print $2}' | xargs kill

# gevent issues

- gevent replaces the stdlib socket with its own socket. The multiprocessing package extensively uses the stdlib socket, so it does not tolerate
  this switch in sockets. That's why multiprocessing and gevent (and thus gunicorn with gevent workers) don't work together at all.
- gevent has no built-in support for multiprocessing. This is because gevent is asynchronous. It has nothing to do with multiprocessing or
  multithreading since it is single-threaded.