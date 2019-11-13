# https://docs.python.org/2/library/logging.html#thread-safety


import logging, threading, os, time


"""
The logging module is thread-safe. These notes are about using the built-in threading capabilities of the logging module. The documentation states
that any logger will implicitly 1) use 1 lock to serialize access to a module's shared underlying data and 2) each handler creates a lock in order
serialize access to underlying I/O. That means:
- If 1 handler is writing to a file from multiple threads, file access should be serialized (True)
- If two handlers are writing to the same file, access should be serialized??? (Have not tested this)
"""


def spawn_threads():
    lg = logging.getLogger('foo-logger')
    hdlr = logging.FileHandler(os.path.join(os.path.dirname(__file__), 'my-log.txt'), mode='w') # This particular line is what truncates the log file each time
    fmt = logging.Formatter('%(asctime)s: %(name)s: %(message)s')
    hdlr.setFormatter(fmt)
    lg.addHandler(hdlr)
    thread_names = ['Michael', 'Donna', 'Lindsy', 'Chuck', 'Nadar']
    for i in range(len(thread_names)):
        t = threading.Thread(name=thread_names[i], target=thread_write_value, args=(lg, i))
        t.start()


def thread_write_value(logger, value):
    """
    The output generated from the logger used in this function shows that:
    - The threads are not ordered in any way when accessing the file (expected)
    - Each thread logs its complete message without getting garbled by the other threads. This must be what the documentation means when it mentions
      'serialized' I/O access

    By contrast, when a regular old open() function is used, the writes to the log file get mixed up with each other. That's not
    thread-safe! Note that the size of the write needs to be big enough to force the default buffer to flush, otherwise its not so obvious that this
    is happening. Alternatively, set line buffering with buffering=1 to make the intermingling writes more apparent
    """
    # Thread-safe
    #logger.warning('{} wrote {}'.format(threading.current_thread().name, get_big_string(value)))

    # NOT thread-safe
    with open(os.path.join(os.path.dirname(__file__), 'my-log.txt'), 'a', buffering=0) as f:
        f.write('{} wrote {}'.format(threading.current_thread().name, get_big_string(value)))


def get_big_string(value):
    return str(value) * 100000


if __name__ == '__main__':
    spawn_threads()