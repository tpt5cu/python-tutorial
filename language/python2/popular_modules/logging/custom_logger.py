# https://docs.python.org/2/library/logging.html
# https://realpython.com/python-logging/
# https://docs.python.org/2/library/logging.handlers.html#module-logging.handlers - available handlers
# https://docs.python.org/2.7/library/logging.html#logrecord-objects - actual log record attributes


"""
Python Loggers are complex objects that delegate responsibility to several internal components including:
- Handler: determines where a log is output to and how that is performed
    - Don't attach a handler to more than one logger because it will result in duplicate messages. I COULD do it, but I shouldn't unless I can think
      of a really good reason
- Formatter: determines how to transform an internal LogRecord object into (usually) a human-readable string
    - A formatter is only allowed to be attached to a handler, not a logger
- Filter: provides more granular filtering than could be accomplished with log levels
    - Can be attached to a logger or handler
"""


import logging


def create_custom_logger():
    """
    The only way to get a custom logger is with the logging.getLogger() factory function. I'm never supposed to directly instantiate a Logger object
    myself.
    - Calling this factory function with the same string will return the same logger (as long as I'm in the same process, I'm assuming)
    - The recommend way to invoke the factory function is 'getLogger(__name__)'
    - A logger can use periods in its name to make itself a child of another logger (e.g. 'foo.bar' is a descendent of the 'foo' logger)
    """
    lg = logging.getLogger(__name__)


def propagate_message_to_ancestor():
    """
    If <Logger>.propagate is True (which it is by default), then events on a child logger will be propagated to the parent logger and any other
    ancestors. What does it mean for the messages to be propagated? It means that the propagated messages go directly to any ancestor loggers'
    handlers. Neither the filters nor configured output levels of an ancestor logger are considered.
    - The workflow here, which shows specifying a handler and a formatter and attaching them, is the basic workflow for creating a custom logger. None
      of it is superfluous
    - StreamHandler() uses sys.stderr by default
    """
    parent = logging.getLogger('foo')
    hdlr = logging.StreamHandler()
    fmt = logging.Formatter(fmt='%(name)s: %(asctime)s: %(message)s') 
    hdlr.setFormatter(fmt)
    parent.addHandler(hdlr)

    # This is a REAL child logger. Any ancestors will emit the child logger's message EXACTLY as it originally was written to their respective
    # handlers. For example, the 'name' of the logger will still be the child logger even though the parent logger handler is emitting the message
    child = logging.getLogger('foo.bar')

    # If the parent logger does not have a handler, then a warning message is shown and this message is never emitted. That's because there is no
    # handler anywhere in the logging hierarchy. If the parent logger DOES have a handler, then this message is only output to stderr once by the
    # parent's handler and no warning message is shown
    child.warning('premature warning')

    # This is NOT a child logger.
    #child = logging.getLogger('food.bar')

    hdlr = logging.StreamHandler()
    fmt = logging.Formatter(fmt='%(name)s: %(asctime)s: %(message)s') 
    hdlr.setFormatter(fmt)
    child.addHandler(hdlr)
    child.warning('The child logger logged a warning!') # The parent logger (so long as it has at least one handler) will also emit a message


def use_base_filter():
    """
    A filter can be attached to a handler or a logger (or both I supposed). The base implemented filter will filter based on a logger's name
    - If it is attached to a handler, the filter is only used before the handler is about to emit the message
    - If it is attached to a logger, the filter is used when a message is logged with 'debug()', 'info()' etc. BEFORE any handler sees the message
    """
    lg = logging.getLogger('foo.bar') # passes through filter
    #lg = logging.getLogger('food') # rejected
    hdlr = logging.StreamHandler()
    fmt = logging.Formatter(fmt='%(name)s: %(message)s')
    hdlr.setFormatter(fmt)
    fltr = logging.Filter('foo') # This will allow loggers named 'foo', 'foo.*' to emit their messages
    hdlr.addFilter(fltr)
    lg.addHandler(hdlr)
    lg.warning('this is a warning!')


def use_custom_filter():
    """
    I'm not required to subclass logging.Filter. Duck typing means that a class which implements a filter() method with the same semantics can be
    passed in place of a Filter instance
    """
    class MyFilter(object):
        def filter(self, log_record):
            """Filter based on whether or not the message has an exclamation point!"""
            return 0 if log_record.msg.find('!') == -1 else 1

    lg = logging.getLogger('Tim')
    hdlr = logging.StreamHandler()
    fltr = MyFilter()
    hdlr.addFilter(fltr)
    lg.addHandler(hdlr)
    lg.warning('Hello there!') # emitted
    lg.warning('Goodbye...') # not emitted
    lg.warning('What?!?!?!?!') # emitted


if __name__ == '__main__':
    #propagate_message_to_ancestor()
    #use_base_filter()
    use_custom_filter()