import os, signal


def kill_nonexistent_process():
    '''There is a new "ProcessLookupError for killing a nonexistent process. It's a subclass of OSError'''
    pid = 999999
    try:
        os.kill(int(pid), signal.SIGTERM)
    #except OSError as e:
    #    print(e.errno) # 3
    except ProcessLookupError as e:
        print(e.errno) # 3



if __name__ == "__main__":
    kill_nonexistent_process()