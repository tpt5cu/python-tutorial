# https://gavv.github.io/articles/file-locks/
# https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/flock.2.html


import os, fcntl, time
from multiprocessing import Process


"""
Review:
- On macOS and Linux, flock locks are ADVISTORY. This means that application-level code can check for and obey locks, but processes that don't check
  for locks will ignore flock locks entirely.

- An open() call returns a file descriptor (actually it returns a Python file object that presumably wraps a file descriptor). A file descriptor is
  just an integer. Therefore, every call to open() returns a DIFFERENT file descriptor, but that's trivial
- If open() is called twice with the same filepath, the corresponding file descriptors point to DIFFERENT file objects. A file object represents a
  file in user-space, NOT a filesystem object. Therefore, two different file objects can point to the SAME filesystem object.
    - filesystem objects are stored in the separate i-node table
- A BSD flock lock is associted with a file object. Independent file descriptors (e.g. two separate open() calls on the same file) don't share lock
  acquisition. Therefore, whether we are in a separate process or separate thread, a BSD flock lock cannot be acquired on an already-locked file, so
  long as the earlier lock was acquired with a DIFFERENT open() call. This is what I want.

- sleep() does NOT affect locks! It does not release a lock!
"""


def write_many_numbers(filepath):
    def write_file(f):
        for n in range(50000):
            f.write(str(n) + "\n")
            # Even if there was a sleep() call here, it would not affect the locks
    try:
        with open(filepath, 'r+') as f: # Safe, as far as I can tell
            fcntl.flock(f, fcntl.LOCK_EX)
            f.truncate() # Safe
            write_file(f)
            fcntl.flock(f, fcntl.LOCK_UN)
    except IOError as e:
        if e.errno == 2:
            with open(filepath, 'w') as f: # Unsafe, but necessary if the file doesn't exist
                fcntl.flock(f, fcntl.LOCK_EX)
                write_file(f)
                fcntl.flock(f, fcntl.LOCK_UN)
    



#def bad_open_file_in_separate_process(filepath):
#    """
#    - When I disable the lock checks entirely, the file is always corrupted or the string of text isn't written at all!
#    - When I enable the lock checks, the file is sometimes corrupted. It's almost like the OS is ignoring when I DO bother to check for locks
#        - Even with LOCK_EX | LOCK_NB, the file still can be corrupted sometimes! And the correct IOError IS raised, which indictes that the OS is
#          respecting the advistory flock lock
#          - The only cause I can think of for this corruption is the open() call in 'w' mode. THIS IS TRUE!
#    """
#    time.sleep(.001)
#    with open(filepath, 'w') as f:
#        fcntl.flock(f, fcntl.LOCK_EX)
#        f.write("Bad separate process write")
#        fcntl.flock(f, fcntl.LOCK_UN)


def good_open_file_in_separate_process(filepath):
    """
    Even with this approach, the file is STILL corrupted sometimes! And still appears with the string AND numbers sometimes. 
    - However, it succeeds more often than the bad version. Actually the bad version hardly ever succeeds, since the file is usually either 1)
      corrupted or 2) has the text string AND the numbers when it should just have the text string.
    - Maybe this is because there's no guarantee about which process starts first, and the other process calls open() with 'w' before getting the
      lock?
        - This is true. Even with this sleep() call of .001, I've seen the other process start after this one! However, regardless of which process
          starts first, it is the unchecked open() 'w' call that causes problems, not the order of the processes.
    - I have absolutely confirmed without a doubt that when the other process uses the unsafe open() call in 'w' mode, while THIS process uses the
      safe open() call with the "r+" mode, that the numbers.txt file can be corrupted. Although I don't know why.
        - When the other process ALSO uses the safe open call() in "r+" mode, I still see corruption, it's just less likely! And I don't know why...
          So I'll use the safer open method for both file descriptors, and wrap the initial one in a try-except to create the file if needed.
            - If the exception block runs (and uses open() with 'w'), the file can be corrupted but there's nothing I can do about that. I just have
              to hope that both processes use the "r+" mode all the time (which they should)
        - The corruption happens approximately 1/200 times, but I've even seen 1/50 times
    - There is a problem with using the "r+" open() mode for both processes. The file can NEVER be created because neither proceses uses the "w+"
      mode!
    """
    time.sleep(.001)
    with open(filepath, "r+") as f: # open the file for reading and writing, but don't truncate it
        fcntl.flock(f, fcntl.LOCK_EX)
        f.truncate() # Delete everything in the in-memory representation of the file AFTER the lock has been acquired
        f.write("Good separate process write")
        fcntl.flock(f, fcntl.LOCK_UN)


def double_write():
    """
    - When the main thread starts p2 after p1 has already finished, "numbers.txt" only has one line of text as expected
    - When the main thread starts p2 while p1 is in-progress, the file is sometimes corrupted.
        - I assume that this is because of an inopportune call to open() in 'w' mode that trunctes the file
    - When the main thread starts p2 while p1 is in-progress, the file is sometimes has the text string followed by numbers the numbers. The file
      should be just contain the text string by itself
        - I assume that this is because of some weird interaction with Python's IOBuffer? Yes. Think about it. 1) The original file is being written
          to 2) a new open() call in "w" mode occurs during the original write 3) the original write is truncated up to a certain point, then the
          original write continues 4) the original write finishes and releases the lock 5) the new write starts 6) I get the weird result at the end
          where the text string appears at the beginning instead of the end of the original, truncated write due to some weird property of Python's
          buffering
    """
    for x in range(100):
        filename = "numbers" + str(x) + ".txt"
        filepath = os.path.join(os.path.dirname(__file__), filename)
        p1 = Process(target=write_many_numbers, args=[filepath])
        p1.start()
        #p2 = Process(target=bad_open_file_in_separate_process, args=[filepath])
        p2 = Process(target=good_open_file_in_separate_process, args=[filepath])
        p2.start()
        p1.join()
        p2.join()


if __name__ == "__main__":
    double_write()