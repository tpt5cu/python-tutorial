import multiprocessing, time

"""
https://stackoverflow.com/questions/32053618/how-to-to-terminate-process-using-pythons-multiprocessing
https://pymotw.com/2/multiprocessing/basics.html
"""

def slow_worker():
    print 'Starting worker'
    time.sleep(0.1)
    print 'Finished worker'


def terminate_and_join():
    """
    Immediately after terminate is called, this parent process still thinks that the child process is alive. Joining the child process to this parent
    process allows the process management code to understand that the child process has terminated
    """
    p = multiprocessing.Process(target=slow_worker)
    print 'BEFORE:', p, p.is_alive() # False
    
    p.start()
    print 'DURING:', p, p.is_alive() # True
    
    p.terminate()
    print 'TERMINATED:', p, p.is_alive() # True

    p.join()
    print 'JOINED:', p, p.is_alive() # False

def terminate_no_join():
    p = multiprocessing.Process(target=slow_worker)
    print 'BEFORE:', p, p.is_alive() # False
    
    p.start()
    print 'DURING:', p, p.is_alive() # True
    
    p.terminate()
    print 'TERMINATED:', p, p.is_alive() # True
    # This amount of sleep time is so short that sometimes the is_alive() result is True and sometimes it is False. Any greater amount of sleep time
    # will always result in is_alive() being False, which is what it should be. The point is that join() does not allow a teeny tiny amount of program
    # execution time to occur within which a child process has terminated, but the process management code doesn't think the child has terminated.
    time.sleep(0.00001)
    print 'Updated???:', p, p.is_alive() # True or False


if __name__ == "__main__":
    #terminate_and_join()
    terminate_no_join()