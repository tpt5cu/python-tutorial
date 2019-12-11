import os, subprocess, time


'''See advanced threading notes for how locks are used as context managers'''


filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.txt')


class RuntimeContextValue(object):

    def __init__(self, filepath, mode='r'):
        self.filepath = filepath
        self.mode = mode

    def __enter__(self):
        '''
        This method returns either self (this object) or a different object related to the run-time context. The returned value is bound to the
        identifier of the 'as' clause (when also used with the 'with' statement, which is a prerequisite for using a context manager anyway). 
        '''
        # We need a reference to the file object (it's NOT a file descriptor!) in order to close it later on in __exit__()
        self.fo = open(self.filepath, self.mode) 
        return self.fo


    # Use the *args object to emphasize that the exception attributes aren't important, but are still accounted for
    def __exit__(self, *args):
        self.fo.close()
        return False


def create_file():
    with open(filepath, 'w') as f:
        f.write('I am a test file!')


def inspect_runtime_context():
    with RuntimeContextValue(filepath) as f:
        data = f.read()
        # remove the file after reading it to raise an exception in __exit__(). Actually, os.remove() is written to not actually deallocate the
        # storage space used by the file until it is no longer in use, so this won't raise an exception
        #os.remove(filepath) 
        # This doesn't work either
        #proc = subprocess.Popen(['rm', filepath])
        #proc.communicate()
    print(data)


if __name__ == '__main__':
    create_file()
    inspect_runtime_context()