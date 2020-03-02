# https://www.quora.com/How-can-one-print-memory-usage-in-Python-program
# https://unix.stackexchange.com/questions/30940/getrusage-system-call-what-is-maximum-resident-set-size
# https://stackoverflow.com/questions/41105733/limit-ram-usage-to-python-program


import resource


def get_process_memory_usage():
    '''
    getrusage is a system call. It returns the "maximum resident set size used in bytes."
        - $ man getrusage
    - A process's resident set size is the amount of memory that belongs to the process and is currently in real RAM
    - The ru_maxrss is the peak RAM usage of the process (when using RUSAGE_SELF)
    '''
    # 7364608 B == 7.364608 MB
    # This process uses 7 MB
    print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) # 7364608


if __name__ == '__main__':
    get_process_memory_usage()
