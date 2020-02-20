import subprocess
from pathlib import Path


def create_python_string():
    '''
    The -c option allows python to run a string as if it were a Python module
    - The directory of the entrypoint python command is used as the current working directory of the subprocess python command (this makes total
      sense)
    '''
    path = Path(__file__).parent / 'source.py'
    with open(path) as f:
        lines = f.readlines()
    print(lines)
    python_string = ''.join(lines)
    #print(python_string)
    p = subprocess.Popen(['python3', '-c', python_string], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    print(f'out: {out}')
    print(f'err: {err}')
    #p = subprocess.Popen(['python3', '-c', python_string])
    #p.wait()
    ## returncode is 1 if error, 0 if successful
    #print(p.returncode)


if __name__ == '__main__':
    create_python_string()
