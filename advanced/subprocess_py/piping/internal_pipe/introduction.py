# https://lyceum-allotments.github.io/2017/03/python-and-pipes-part-5-subprocesses-and-pipes/


import subprocess, sys, os


def read_from_stdin_and_stdout():
    """
    subprocess.PIPE means that the Popen object ("proc" in this case) gets control of the relevant file descriptor of the subprocess
    - stdin, stdout, and stderr are only Python file objects when subprocess.PIPE was passed as the argument; otherwise they are None
    """
    proc = subprocess.Popen(["python", "say_my_name.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    proc.stdin.write("matthew\n")
    proc.stdin.write("mark\n")
    proc.stdin.write("luke\n")
    proc.stdin.close()
    # The stdout is available at any time, I just choose to read it once the child process has terminated in order to view all the input at once
    #print("The output was:*** " + proc.stdout.read() + " ***")
    # returncode will be None as long as the child process hasn't terminated. returncode can be set by poll(), wait, or (indirectly) communicate()
    while proc.returncode is None: 
        proc.poll() # poll the child process to see if it has terminated and set the returncode attribute if it has
    print("I got back from the program this:\n{0}".format(proc.stdout.read()))


def communicate():
    proc = subprocess.Popen(["python", "say_my_name.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    proc.stdin.write("matthew\n")
    (out, err) = proc.communicate() # wait for the process to terminate, then read its stdout and stderr
    print("out was: *** " + out + " ***")
    print("err was: *** " + ("None" if err is None else err) + " ***")
    # This raises ValueError: I/O operation on closed file. This happens because proc.communicate() waits for the child process to terminate
    #proc.stdin.write("matthew\n")


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    #read_from_stdin_and_stdout()
    communicate()