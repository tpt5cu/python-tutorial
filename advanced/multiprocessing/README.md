- https://bencane.com/2014/04/01/understanding-the-kill-command-and-how-to-terminate-processes-in-linux/
- https://stackoverflow.com/questions/17856928/how-to-terminate-process-from-python-using-pid
- https://unix.stackexchange.com/questions/8916/when-should-i-not-kill-9-a-process
- https://major.io/2010/03/18/sigterm-vs-sigkill/

# Multiprocessing vs subprocess

- The multiprocessing module is for managing multiple processes that are all written in Python.
- The subprocess module is for managing programs that are not written in Python.

# Bad side effects of os.kill(<PID>, signal.SIGKILL)

- Using SIGKILL does not allow an operation to close files, close database connections, or shutdown nicely in other ways. This can cause issues in the
  long run
    - What are these issues? Corrupted files or other leftover state may be left around that cannot be interpreted. In the worst case, SIGKILL could corrupt
      an important production database.