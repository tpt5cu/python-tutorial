# https://docs.python.org/3.6/library/warnings.html


import warnings


'''Warnings are already built-in Python exceptions, but conceptually they belong to the warnings module'''


def adjust_warnings_filter():
    '''
    If an argument is omitted from filterwarnings(), it defaults to a value that matches everything
    '''
    # A warnings category was not specified, so all warnings will be ignored!
    #warnings.filterwarnings('ignore')
    # Warning is the base class of all warnings, so the net result is the same as above
    #warnings.filterwarnings('ignore', category=Warning)
    # A regular old warn() invocation has the UserWarning category, so such warnings will be ignored with this filter
    #warnings.filterwarnings('ignore', category=UserWarning)
    # A UserWarning is not a sublcass of RuntimeWarning, so only RuntimeWarnings will be ignored. All other warnings will be printed (by default)
    #warnings.filterwarnings('ignore', category=RuntimeWarning)
    pass


def create_warning():
    '''
    - Warnings are grouped into categories
        - 
    - There is a single filter that determines what happens when a warning is created. A warning can be 1) ignored, 2) displayed or 3) turned into an
      exception and raised
        - Every warning is matched against this filter to determine what happens
        - The default filter is created with specific options: DepreciationWarning, PendingDepreciationWarning, ImportWarning, BytesWarning, and
          ResourceWarning are all ignored (see source for specifics)

    '''
    # warn() doesn't return anything
    # Default arguments: warn(message, category=UserWarning, stacklevel=1, source=None)
    warnings.warn('This is your final warning!')
    warnings.warn('This is a RuntimeWarning', RuntimeWarning)


def reset_warnings_filter():
    '''
    The global warnings object can be inspected to see what filters already exist
    - Use warnings.resetfilters() to remove ALL existing filters
    '''
    # Show standard filters
    # - DepreciationWarning: ignored
    # - PendingDepreciationWarning: ignored
    # - ImportWarning: ignored
    # - BytesWarning: ignored
    # - ResourceWarning: ignored
    print(warnings.filters)
    print('')
    # Show that warnings state is global across modules
    # - FutureWarning: ignored (I added this in external.py)
    from python_369.popular_modules.warnings_ import external
    print(warnings.filters)
    print('')
    warnings.resetwarnings()
    # ALL warnings filters were removed
    print(warnings.filters)
    print('')


if __name__ == '__main__':
    #adjust_warnings_filter()
    #create_warning()
    reset_warnings_filter()
