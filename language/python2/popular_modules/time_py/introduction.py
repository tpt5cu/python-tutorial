import time


def get_local_time_string():
    t = time.time()
    print(t) # floating point number
    lt = time.localtime(t)
    print(lt) # struct_time
    #st = time.strftime("%a", t) # TypeError
    st = time.strftime("%a", lt) # Day of week
    st = time.strftime("%d %H %M %S") # Day of month, hour (24 hr), minute, second
    st = time.strftime("%a %I:%M:%S") # Day of week, hour (12 hr), minute, second
    print(st)


if __name__ == "__main__":
    get_local_time_string()