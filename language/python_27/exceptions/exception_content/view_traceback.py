# https://docs.python.org/2.7/library/traceback.html


import sys, traceback


def inspect_python_traceback_composition():
    '''
    A "stack trace" is the general term for the message the Python interpreter prints to stderr when an exception is raised.
    - A traceback object is the highest level object. 
    - A traceback object contains a "frame" object with a bunch of attributes that I don't understand. This "frame" object is actually a stack frame
      object
    - How does the "stack frame" object relate to "stack trace entries?" I believe that the "stack frame" object is an intermediate abstraction that I
      don't need to care about most of the time.
    - In summary, traceback objects are easier to work with than individual "stack frame" objects, but it is possible to directly use "stack frame"
      objects for more granular examination of the entire stack trace

    - print_tb() prints out the list of stack trace entries contained inside of the traceback object in a nice format
    - extract_tb() returns a list of stack trace entries. Each item in the list is a 4-tuple. Each 4-tuple contains information about a stack trace
    - print_tb() and extract_tb() thus are both working with the exact same list of stack trace entries

    - print_stack() prints out a stack trace from its invocation point.
        - How do I specify an alternative stack frame to start? A stack frame must have an "f_lineno" attribute. One way to do it is to get the next
          outer frame as shown below
    - extract_stack() returns a list of stack trace entries. It has the same return value as extract_tb()
        - The list that is returned will contain only stack trace entries that go as deep as the provided stack frame argument
    '''
    try:
        raise_exception(10)
    except:
        tb = sys.exc_info()[2]
        print(type(tb)) # <type 'traceback'>
        print(type(tb.tb_frame)) # <type 'frame'>
        print(type(tb.tb_frame.f_back)) # <type 'frame'>
        print(type(tb.tb_frame.f_code)) # <type 'code'>
        # Extract all stack trace entries from the traceback object
        print(traceback.extract_tb(tb))
        # Print all stack trace entries from the traceback object
        traceback.print_tb(tb)
        # Print the stack trace from this invocation point
        traceback.print_stack()
        # Equivalent to above
        traceback.print_stack(tb.tb_frame)
        # Print the stack trace starting from the frame just outside of this frame
        traceback.print_stack(tb.tb_frame.f_back)
        # Get a list of stack trace entries that go as deep as whatever frame was specified as the ending point
        print(traceback.extract_stack(tb.tb_frame))


def raise_exception(n):
    n = n - 1
    if n == 0:
        y = 52 / n
        return y
    else:
        raise_exception(n)


def print_all_stack_trace_entries():
    '''
    traceback.print_tb() prints all of the individual stack trace entries, up to an optional limit.
    - The stack trace entries are ordered from outermost frame to innermost frame. Thus, the limit does not by itself allow me to only print the last
      (innermost) stack trace entry.
    '''
    try:
        val = raise_exception(10)
    except:
        print('~~~~')
        traceback.print_tb(sys.exc_info()[2])
        print('~~~~')


def view_last_stack_trace_entry():
    '''
    Slice the list of stack trace entries to get the ones I want
    - All format_tb() (and format_list()) are doing is transforming the stack trace entries into nice pretty strings with newlines for printing
    '''
    try:
        val = raise_exception(10)
    except:
        print('~~~~')
        # format_tb() is a shorthand for the line immediately below it. 
        print(traceback.format_tb(sys.exc_info()[2])[-1])
        # This line is equivalent to the line above
        print(traceback.format_list(traceback.extract_tb(sys.exc_info()[2]))[-1])
        print('~~~~')


def view_last_and_first_stack_trace_entries():
    '''Unfortunately, this output isn't as useful as I thought it would be. Just using the last frame seems more clear'''
    try:
        raise_exception(10)
    except:
        print traceback.format_tb(sys.exc_info()[2])[0], '...\n', traceback.format_tb(sys.exc_info()[2])[-1]


def print_arbitrary_stack_trace():
    '''
    traceback.print_stack() will immediately print a stack trace starting from its own invocation line.
    - There is no raised exception, just a stack trace! It can also take a "frame" object (i.e. a stack frame object) and print the stack trace that
      goes as deep as that frame
    '''
    traceback.print_stack()


def print_exception_and_traceback():
    '''
    print_exception() does a little more formatting than print_tb(). It can be used to print the exception information in addition to the traceback in
    a nice way. It can also be abused to print some arbitrary exception if I want.
    - The limit attribute has the exact same limitations as for print_tb()
    '''
    try:
        raise_exception(10)
    except:
        # This is abusing the functionality
        #traceback.print_exception(IOError, 'quack', sys.exc_info()[2], 2)
        # This is more correct 
        traceback.print_exception(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])


def pretty_print_innermost_stack_frame_entry():
    '''
    I think this is a good way to show some kind of exception context to a client without overwhelming them.
    - Would it be better to just give the client the entire stack trace?
    '''
    try:
        #raise_exception(10)
        def raise_ioerror():
            raise IOError
        raise_ioerror()
    except:
        entries = traceback.format_exception(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
        print(entries[-0])
        print(entries[-2])
        print(entries[-1])


if __name__ == '__main__':
    #inspect_python_traceback_composition()
    #print_all_stack_trace_entries()
    #view_last_stack_trace_entry()
    #view_last_and_first_stack_trace_entries()
    #print_arbitrary_stack_trace()
    #print_exception_and_traceback()
    pretty_print_innermost_stack_frame_entry()