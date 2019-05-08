import os, time

"""
https://unix.stackexchange.com/questions/24441/get-file-created-creation-time
https://stackoverflow.com/questions/25834356/flask-caching-result-of-data-load
"""

"""
Linux is only guaranteed to store last access time, last modification time, and last inode modification time. Anything else, like the time of a
file/directory's creation, is only present on certain file systems.

Maybe I can create a creation-time.json file and read from it on each request. Even better, I could cache the value from the file.
"""

def calculate_elapsed_time():
    """
    Sometime I want to see how long its been since a directory was modified. The following examples are explicitly about directories on macOS
    - mtime is when the contents of a directory were changed
        - Changes when a file is added to the directory
        - Changes when a file inside of the directory is changed
        - Changes when a file inside of the directory is deleted or moved from the directory
    - ctime is when some metadata of a directory, like permissions, were changed 
        - Changes when a file is added to the directory
        - Changes when a file inside of the directory is changed
        - Changes when a file inside of the directory is deleted or moved from the directory
    """
    elapsed_time = int((time.time() - os.path.getmtime("/Users/austinchang/Desktop/stuff")))
    print(elapsed_time)
    print("{:02}:{:02}:{:02}".format(elapsed_time // 3600, ((elapsed_time % 3600) // 60), elapsed_time % 60))
    print("{:02} hours:{:02} minutes:{:02} seconds".format(elapsed_time // 3600, ((elapsed_time % 3600) // 60), elapsed_time % 60))

def readable_time():
    """
    time.ctime() returns a human-readable string of the time (in seconds) that was passed as an argument
    """
    print(time.ctime(os.path.getmtime("/Users/austinchang/Desktop/stuff")))


if __name__ == "__main__":
    calculate_elapsed_time()
    #readable_time()