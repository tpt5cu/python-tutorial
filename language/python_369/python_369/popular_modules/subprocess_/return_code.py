# https://docs.python.org/3.6/library/subprocess.html


import subprocess
from subprocess import Popen


'''
- <Popen>.communicate() returns out, err
- <Popen>.wait() only sets the returncode attribute. It doesn't return anything else
    - A nonzero return code indicates a problem
'''


def run_process():
    '''Recall that any non-zero number is True'''
    p = Popen(
        #['python', '/Users/austinchang/tutorials/python/language/python_37/popular_modules/subprocess_/erroneous_module.py'],
        # - Ran for 1 minute successfully without sudo
        # - 
        #['python', '/Users/austinchang/pycharm/omf/omf/models/smartSwitching.py'], # Ran for 1 minute successfully, both with and without sudo

        # - This file ran successfully with/without sudo on Docker container in 1 minute
        # - runAllTests.py ran successfully with/without sudo on Docker container in 1 minute
        # - 
        ['python', '/home/omf/omf/models/smartSwitching.py'],
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    out, err = p.communicate()
    print('out: {}'.format(out))
    print('err: {}'.format(err))
    print('p.returncode: {}'.format(p.returncode))
    if 0:
        print('0 is True')
    if 1:
        print('1 is True') # True
    if 2:
        print('2 is True') # True
    if -1:
        print('1 is True') # True


if __name__ == '__main__':
    run_process()
