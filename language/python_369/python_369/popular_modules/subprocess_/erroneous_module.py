'''
In summary, as long as an except-block catches the exception, no matter how, the process returns with a code of 0
'''


def do_bad_thing():
    x = 5/0


def swallow_all_exceptions(func):
    try:
        func()
    except:
        #return True # returncode 0
        #return False # returncode 0
        pass # returncode: 0


def swallow_only_exception_subclasses(func):
    try:
        func()
    except Exception as e:
        #return True # returncode 0
        #return False # returncode 0
        pass # returncode 0


def dont_swallow_exception(func):
    try:
        func()
    except IOError as e:
        pass # returncode: 1


if __name__ == '__main__':
    #swallow_all_exceptions(do_bad_thing)
    #swallow_only_exception_subclasses(do_bad_thing)
    dont_swallow_exception(do_bad_thing)