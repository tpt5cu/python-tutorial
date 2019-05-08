import os, signal, multiprocessing, time


"""
Hard way:
1) Users submits a DELETE request.
2) I look up the PID.txt file in their directory, which contains the PID of their process
3) Pass that specific PID into a message to all worker Process
4) Worker processes will check to see if their PID matches the PID I want to kill
5) Worker with matching PID terminates itself, that PID is removed from the messages

Easy way:
1) Get the PID to kill
2) Use os.kill(<PID>, <signal>)
"""


def create_process(limit, wait, spaces):
    p = multiprocessing.Process(target=print_numbers, args=(limit, wait, spaces))
    p.start()
    return p.pid


def print_numbers(limit, wait, spaces):
    for x in range(limit):
        print(spaces + str(x))
        time.sleep(wait)


def spawn_processes():
    """ Attempting to kill a non-existant PID throws an OSError """
    pid1 = create_process(10, 1.0, " ")
    pid2 = create_process(10, 1.5, "    ")
    pid3 = create_process(10, 2, "        ")
    time.sleep(5)
    #os.kill(pid1, signal.SIGTERM)
    os.kill(pid2, signal.SIGTERM)
    #os.kill(99999999, signal.SIGTERM)


if __name__ == "__main__":
    spawn_processes()