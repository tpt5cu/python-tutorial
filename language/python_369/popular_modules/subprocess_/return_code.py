import subprocess
from subprocess import Popen


def run_process():
    '''Recall that any non-zero number is True'''
    p = Popen(
        ['python', '/Users/austinchang/tutorials/python/language/python_37/popular_modules/subprocess_/erroneous_module.py'],
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
