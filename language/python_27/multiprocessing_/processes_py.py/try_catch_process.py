import multiprocessing, time


def print_numbers():
    for i in range(3):
        print(i)
        time.sleep(1.0)
    raise Exception('The process raised an exception')


def spawn_process():
    '''As expected, a child process cannot be try-excepted in a parent process'''
    p = multiprocessing.Process(target=print_numbers)
    try:
        p.start()
    except:
        print('Caught an exception!')


if __name__ == '__main__':
    spawn_process()
    print('Child process is running')