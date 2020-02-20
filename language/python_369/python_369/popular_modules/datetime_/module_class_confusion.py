# https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior - format string quick reference


import datetime


def class_strftime():
    '''
    <datetime>.stftime() is supposed to return a string OF a datetime that already exists. What happens when this method is called on the datetime
    class instead of an instance?
    - Recall that when what is SUPPOSED to be a method is called as a class function, the first argument MUST be a instance of the class! The
      subsequent arguments are the "normal" arguments for the METHOD
    - The "normal method" is a 'builtin_function_or_method' while an "improperly used method" is a 'method_descriptor'
    - A normal class function is also a 'builtin_function_or_method'
    '''
    format_string = '%Y-%m-%d %H:%M:%S'
    str_ = datetime.datetime.strftime( # Invoke the method as a function (bad practice)
        datetime.datetime.strptime('May 05 1995', '%B %d %Y'), # return a datetime INSTANCE here
        format_string # supply the expected format string
    )
    print(str_) # 1995-05-05 00:00:00
    print(type(datetime.datetime.strftime)) # <class 'method_descriptor'>
    dt = datetime.datetime(1, 1, 1)
    print(type(dt.strftime)) # <class 'builtin_function_or_method'>
    print(type(datetime.datetime.strptime)) # <class 'builtin_function_or_method'>


if __name__ == '__main__':
    class_strftime()