import logging, threading
 
def get_logger():
    """ 
    Printing to stdout is a real mess with threads. Use logging instead.
    """
    # Create a logger which is identified with the name. All getLogger() calls with the same name return the same logger.
    logger = logging.getLogger("threading_example")
    logger.setLevel(logging.DEBUG)
    # There is no logging.FileHandler() function. Actually, FileHandler is a class that is defined inside of the logging module, it's just
    # documented elsewhere
    fh = logging.FileHandler("threading.log")
    fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
 
 
def doubler(number, logger):
    """
    The logger should be passed into the function. If I were to create the logger inside of the function, my log file would have a lot of duplicate
    entries in it. I honestly don't know why.
    """
    logger.debug('doubler function executing')
    result = number * 2
    logger.debug('doubler function ended with: {}'.format(
        result))
 
 
if __name__ == '__main__':
    logger = get_logger()
    thread_names = ['Mike', 'George', 'Wanda', 'Dingbat', 'Nina']
    for i in range(5):
        # The ',' in the 'args' parameter is required
        my_thread = threading.Thread(target=doubler, name=thread_names[i], args=(i,logger))
        my_thread.start()