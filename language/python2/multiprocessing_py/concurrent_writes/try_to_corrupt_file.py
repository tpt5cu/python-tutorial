import fcntl, os, time
from multiprocessing import Process


"""
- All of these tests use proper locking. That's the point
- Using r+ mode with 'truncate()' DOES create corrupted files for about 1/100 files
    - Using r+ mode with 'truncate(0)' DOES create corrupted files with about the same probability
    - Doing the same tests but adding a time.sleep(.1) call to separate the starting time of the processes resulted in no corrupt files. Thus, for the
      purposes of the omf web appliation, r+ mode with truncate() calls is good enough to prevent file corruption
- Using 'w' mode corrupts files with a probability that is MUCH higher
    - When the same time.sleep(.1) call is used, surprisingly the 'w' mode does not corrupt files either
"""


def write_many_numbers(filepath):
    def write_file(f):
        for n in range(50000):
            f.write(str(n) + "\n")
            # Even if there was a sleep() call here, it would not affect the locks
    try:
        #with open(filepath, 'r+') as f: # Safe, as far as I can tell
        with open(filepath, 'w') as f: # Unsafe
            fcntl.flock(f, fcntl.LOCK_EX)
            #f.truncate()
            #f.truncate(0) # Safe
            write_file(f)
            fcntl.flock(f, fcntl.LOCK_UN)
    except IOError as e:
        if e.errno == 2:
            with open(filepath, 'w') as f: # Unsafe, but necessary if the file doesn't exist
                fcntl.flock(f, fcntl.LOCK_EX)
                write_file(f)
                fcntl.flock(f, fcntl.LOCK_UN)


def write_a_string(filepath):
    #with open(filepath, "r+") as f: # open the file for reading and writing, but don't truncate it
    with open(filepath, "w") as f: # Unsafe
        fcntl.flock(f, fcntl.LOCK_EX)
        #f.truncate()
        #f.truncate(0) # Delete everything in the in-memory representation of the file AFTER the lock has been acquired
        f.write("Good separate process write")
        fcntl.flock(f, fcntl.LOCK_UN)


if __name__ == "__main__":
    for x in range(200):
        filename = "numbers" + str(x) + ".txt"
        filepath = os.path.join(os.path.dirname(__file__), "files", filename)
        p1 = Process(target=write_many_numbers, args=[filepath])
        p2 = Process(target=write_a_string, args=[filepath])
        p1.start()
        #time.sleep(.1)
        p2.start()
        p1.join()
        p2.join()