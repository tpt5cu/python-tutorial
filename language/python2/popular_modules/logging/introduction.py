# https://realpython.com/python-logging/
# https://docs.python.org/2.7/library/logging.html#logrecord-attributes


import logging, os, time


"""
The default Python logger has 5 levels of severity: DEBUG, INFO, WARNING, ERROR, CRITICAL
- Basically, basicConfig() can only be called once per process (see notes and source)
"""


filepath = os.path.join(os.path.dirname(__file__), "my-log.txt")


def log_to_console():
    """
    - The logging module gives the name 'root' to the default logger. By default, the logging module only logs messages at WARNING level or above. The
      level at which the logger actually logs something can be configured.
    - basicConfig(): creates a StreamHandler with a default Formatter and adds it to the root logger
        - By default, an instance of StreamHandler uses sys.stderr for the stream
        - If no handlers are already defined for the root logger, any of the convenience functions (debug(), info(), warning(), error(), critical())
          will make an initial call to basicConfig() on their own
        - basicConfig() does nothing if the root logger already has a handler configured for it
    """
    logging.basicConfig(level=logging.DEBUG) # This must be called first to attach a configured handler that I want
    logging.debug("Debug message") # Only shows up in console stderr because I configured it so
    logging.warning("This is a warning!")
    #logging.basicConfig(level=logging.DEBUG) # Does nothing because there was an earlier logging.debug() call
    logging.debug("This debug message shows up")


def log_to_file():
    """
    Opening in 'w' mode means that each time basicConfig() is called, the file will be truncated. It would be useless if every time a message was
    logged the whole log file was truncated!
    """
    logging.basicConfig(filename=filepath, filemode='w')
    for x in range(10):
        t = time.strftime("%a %I:%M:%S: ", time.localtime(time.time()))
        logging.warning(t + "This is a huge warning")
        time.sleep(0.1)
    logging.warning("Here's some more info!")


def format_output():
    """
    It turns out that the LogRecord class has a TON of pre-built attributes that I can use in my log messages! I won't even try to list them all here
    """
    #format_string = "%(filename)s %(funcName)s %(levelname)s (%process)d %(message)s" # Does not work. Process ID not available?
    format_string = "%(filename)s %(funcName)s %(levelname)s %(message)s %(asctime)s" # This works
    logging.basicConfig(filename=filepath, filemode='w', format=format_string)
    logging.error("There was a big bad error!")


if __name__ == "__main__":
    #log_to_console()
    #log_to_file()
    format_output()