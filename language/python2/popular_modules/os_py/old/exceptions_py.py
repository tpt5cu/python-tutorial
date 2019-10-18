import os, signal, time, shutil, time
from multiprocessing import Process


def kill_nonexistent_process():
    """ Using os.kill() with a nonexistent process raises an OSError with errno == 3 """
    os.kill(99999999, signal.SIGTERM)


def kill_nonsense_value():
    """ Using os.kill() with a non-integer value creates a TypError. It actually has nothing to do with the os module """
    os.kill("working", signal.SIGTERM)


def kill_string():
    """ Attempting to use os.kill() with an integer string will throw a TypeError """
    p = Process(target=sleep_py)
    p.start()
    time.sleep(1)
    os.kill(str(p.pid), signal.SIGTERM)


def sleep_py():
    time.sleep(10)


def remove_nonexistent_file():
    """ Removing a nonexistent file raises an OSError with errno == 2 """
    os.remove("./blahblah")


def make_existing_sub_dir():
    """ Making directories recursively when some child directory(s) already exists raises an OSError with errno == 17 """
    dir_path = os.path.join(os.path.dirname(__file__), "parent/child")
    os.makedirs(dir_path)


def make_existing_dir():
    """ Attemping to make a directory that already exists raises an OSError with errno == 17 """
    dir_path = os.path.join(os.path.dirname(__file__), "somedir")
    os.mkdir(dir_path)


if __name__ == "__main__":
    #kill_nonexistent_process()
    #kill_nonsense_value()
    kill_string()
    #remove_nonexistent_file()
    #make_existing_sub_dir()
    #make_existing_dir()