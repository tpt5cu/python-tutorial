# https://docs.python.org/2/library/threading.html
# https://realpython.com/intro-to-python-threading/
# https://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread


import threading, time


def print_numbers(start):
    for x in range(start, start + 5):
        print(x)
        time.sleep(1)


def run_two_threads():
    """Pretty straightforward."""
    t = threading.Thread(target=print_numbers, args=(7,))
    t.start()
    time.sleep(0.5)
    print_numbers(0)


if __name__ == "__main__":
    run_two_threads()