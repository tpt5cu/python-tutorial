https://stackoverflow.com/questions/35616639/python-multiprocessing-in-flask
https://stackoverflow.com/questions/14814201/can-i-serve-multiple-clients-using-just-flask-app-run-as-standalone
https://www.reddit.com/r/Python/comments/4s40ge/understanding_uwsgi_threads_processes_and_gil/
https://opensource.com/article/17/4/grok-gil - detailed explanation of the GIL

# Multiprocessing directly in Flask

- Using the multiprocessing module in the Flask development server to start new processes works as expected. I can access the request and application
  context in spawned processes. But, is this the way I SHOULD be doing this?
    - No. I should be using a task queue to coordinate between separate web servers and background-process servers. But for a simple prototyping,
      multiprocessing is fine.
- Since a long-running process occurs in a function which has access to the request context, does that means Flask doesn't release the request context
  until the long-running process finishes?
  - I don't know. Probably.

# Nature of requests in Flask

- By default, Flask is multi-threaded. That means there are multiple threads to handle all incoming requests. However, because of the GIL of CPython
  (which is the version of Python I use), only one thread ever runs at a time in a Python interpreter. Threads cannot execute concurrently (without hacks).
- I can enable multiple processes too, but that is not a substitute for a real web server
  - See the first link