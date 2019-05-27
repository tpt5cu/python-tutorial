import os, signal


def kill_nonexistent_process():
    """ Killing a nonexistent process raises an OSError with errno == 3 """
    os.kill(99999999, signal.SIGTERM)


def remove_nonexistent_file():
    """ Removing a nonexistent file raises an OSError with errno == 2 """
    os.remove("./blahblah")


if __name__ == "__main__":
    #kill_nonexistent_process()
    remove_nonexistent_file()