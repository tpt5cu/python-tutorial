# https://docs.python.org/2/library/subprocess.html


import subprocess


def call_py():
    """
    - subprocess.call() runs the command in a child process and waits for it to complete before returning
    - All of the subprocess convenience functions, like call(), use the underlying Popen interface. Popen can take arguments in the form of 1) a
      string or 2) a Python sequence of program arguments
        - The sequence form is preferred. It makes it easier for Python to perform any necessary escaping on the arguments (e.g. a filename with
          spaces)
        - If the alternative string form is used, "shell=True" must be set or the string can only specifcy an executable with NO arguments
    """
    #subprocess.call(["ls", "-li"])
    subprocess.call("ls -li", shell=True)


def take_control_of_subprocess_file_descriptors() {
    """
    When subprocess.PIPE is passed as an argument to the stdin, stdout, or stderr of the child process, it means that the Popen object gets to control
    the respective file descriptor of the child process through a pipe.
    """
    subprocess.Popen("")
}


if __name__ == "__main__":
    call_py()
